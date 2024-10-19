from flask import request
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from src.exception import CustomException
from bs4 import BeautifulSoup as bs
import pandas as pd
import sys
import time
from selenium.webdriver.chrome.options import Options 
from urllib.parse import quote

class ScrapeReviews:
    def __init__(self, product_name: str, no_of_products: int):
        # Set up options for the Chrome WebDriver
        options = Options()
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(options=options)
        # Store the product name and number of products to scrape
        self.product_name = product_name
        self.no_of_products = no_of_products

    def scrape_product_urls(self, product_name):
        try:
            # Format the search string by replacing spaces with hyphens
            search_string = product_name.replace(" ", "-")
            # Encode the search string for URL usage
            encoded_query = quote(search_string)
            # Navigate to the product search page
            self.driver.get(f"https://www.myntra.com/{search_string}?rawQuery={encoded_query}")
            # Get the page source
            myntra_text = self.driver.page_source
            # Parse the HTML content using BeautifulSoup
            myntra_html = bs(myntra_text, "html.parser")
            # Find all relevant product listings
            pclass = myntra_html.findAll("ul", {"class": "results-base"})

            product_urls = []
            for i in pclass:
                # Extract all anchor tags with href attributes
                href = i.find_all("a", href=True)
                for product_no in range(len(href)):
                    # Append each product URL to the list
                    t = href[product_no]["href"]
                    product_urls.append(t)

            return product_urls
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)

    def extract_reviews(self, product_link):
        try:
            # Construct the full product link
            productLink = "https://www.myntra.com/" + product_link
            # Navigate to the product page
            self.driver.get(productLink)
            # Get the page source
            prodRes = self.driver.page_source
            # Parse the HTML content
            prodRes_html = bs(prodRes, "html.parser")
            # Extract the product title
            title_h = prodRes_html.findAll("title")
            self.product_title = title_h[0].text

            # Extract the overall rating
            overallRating = prodRes_html.findAll("div", {"class": "index-overallRating"})
            for i in overallRating:
                self.product_rating_value = i.find("div").text
            
            # Extract the product price
            price = prodRes_html.findAll("span", {"class": "pdp-price"})
            for i in price:
                self.product_price = i.text

            # Find the link to detailed reviews
            product_reviews = prodRes_html.find("a", {"class": "detailed-reviews-allReviews"})
            if not product_reviews:
                return None
            return product_reviews
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)

    def scroll_to_load_reviews(self):
        # Set the window size to ensure all content loads properly
        self.driver.set_window_size(1920, 1080)
        # Get the initial height of the page
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down by a fixed amount
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(3)  # Wait for new content to load
            # Calculate the new height of the page
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # Break the loop if no new content is loaded
            if new_height == last_height:
                break
            last_height = new_height

    def extract_products(self, product_reviews: list):
        try:
            # Extract the href for the detailed reviews
            t2 = product_reviews["href"]
            Review_link = "https://www.myntra.com" + t2
            # Navigate to the reviews page
            self.driver.get(Review_link)
            # Scroll to load all reviews
            self.scroll_to_load_reviews()
            review_page = self.driver.page_source
            review_html = bs(review_page, "html.parser")
            # Find all review containers
            review = review_html.findAll("div", {"class": "detailed-reviews-userReviewsContainer"})
            reviews = []

            for i in review:
                # Extract user rating, comment, and name
                user_rating = i.findAll("div", {"class": "user-review-main user-review-showRating"})
                user_comment = i.findAll("div", {"class": "user-review-reviewTextWrapper"})
                user_name = i.findAll("div", {"class": "user-review-left"})

                for idx in range(len(user_rating)):
                    try:
                        # Extract the user rating
                        rating = user_rating[idx].find("span", class_="user-review-starRating").get_text().strip()
                    except:
                        rating = "No rating Given"
                    try:
                        # Extract the user comment
                        comment = user_comment[idx].text
                    except:
                        comment = "No comment Given"
                    try:
                        # Extract the user's name
                        name = user_name[idx].find("span").text
                    except:
                        name = "No Name given"
                    try:
                        # Extract the review date
                        date = user_name[idx].find_all("span")[1].text
                    except:
                        date = "No Date given"

                    # Create a dictionary to store the review details
                    mydict = {
                        "Product Name": self.product_title,
                        "Over_All_Rating": self.product_rating_value,
                        "Price": self.product_price,
                        "Date": date,
                        "Rating": rating,
                        "Name": name,
                        "Comment": comment,
                    }
                    reviews.append(mydict)

            # Convert the reviews list to a DataFrame
            review_data = pd.DataFrame(
                reviews,
                columns=[
                    "Product Name",
                    "Over_All_Rating",
                    "Price",
                    "Date",
                    "Rating",
                    "Name",
                    "Comment",
                ],
            )

            return review_data
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)

    def skip_products(self, search_string, no_of_products, skip_index):
        # Scrape product URLs and remove the one at the specified index
        product_urls = self.scrape_product_urls(search_string, no_of_products + 1)
        product_urls.pop(skip_index)

    def get_review_data(self) -> pd.DataFrame:
        try:
            # Scrape product URLs based on the product name
            product_urls = self.scrape_product_urls(product_name=self.product_name)
            product_details = []
            review_len = 0

            # Loop until the specified number of reviews has been scraped
            while review_len < self.no_of_products:
                product_url = product_urls[review_len]
                review = self.extract_reviews(product_url)

                if review:
                    # Extract product details and append to the list
                    product_detail = self.extract_products(review)
                    product_details.append(product_detail)
                    review_len += 1
                else:
                    # Remove the URL if no reviews were found
                    product_urls.pop(review_len)

            # Close the WebDriver
            self.driver.quit()
            # Concatenate all product details into a single DataFrame
            data = pd.concat(product_details, axis=0)
            # Save the DataFrame to a CSV file
            data.to_csv("data.csv", index=False)
            return data
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)
