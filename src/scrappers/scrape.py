from flask import request
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from src.exceptions import customExceptions
from bs4 import BeautifulSoup as bs
import pandas as pd
import os, sys
import time
from selenium.webdriver.chrome.options import Options 
from urllib.parse import quote

class ScrapeReviews:
    # Initialize the scraper with product name and number of products to scrape
    def __init__(self, product_name:str, no_of_products:int):
        options = Options()  # Set options for the Chrome driver
        self.driver = webdriver.Chrome(options=options)  # Create a new Chrome driver instance
        self.product_name = product_name  # Store product name
        self.no_of_products = no_of_products  # Store number of products to scrape

    # Method to scrape product URLs based on the product name
    def scrape_product_urls(self, product_name):
        try:
            search_string = product_name.replace(" ","-")  # Format the product name for URL
            encoded_query = quote(search_string)  # URL-encode the search string
            self.driver.get(
                f"https://www.myntra.com/{search_string}?rawQuery={encoded_query}"  # Navigate to the product page
            )
            myntra_text = self.driver.page_source  # Get the page source
            myntra_html = bs(myntra_text, "html.parser")  # Parse the HTML
            pclass = myntra_html.findAll("ul", {"class": "results-base"})  # Find product results

            product_urls = []  # Initialize list to hold product URLs
            for i in pclass:
                href = i.find_all("a", href=True)  # Find all anchor tags with href

                for product_no in range(len(href)):
                    t = href[product_no]["href"]  # Extract the product link
                    product_urls.append(t)  # Append link to the list

            return product_urls  # Return the list of product URLs
        
        except Exception as e:
            raise customExceptions(e, sys)  # Handle exceptions

    # Method to extract reviews from a product link
    def extract_reviews(self, product_link):
        try:
            productLink = "https://www.myntra.com/" + product_link  # Construct the full product URL
            self.driver.get(productLink)  # Navigate to the product page
            prodRes = self.driver.page_source  # Get the page source
            prodRes_html = bs(prodRes, "html.parser")  # Parse the HTML
            title_h = prodRes_html.findAll("title")  # Get the product title

            self.product_title = title_h[0].text  # Store the product title

            overallRating = prodRes_html.findAll(
                "div", {"class": "index-overallRating"}  # Find the overall rating
            )
            for i in overallRating:
                self.product_rating_value = i.find("div").text  # Store the rating value

            price = prodRes_html.findAll("span", {"class": "pdp-price"})  # Find the product price
            for i in price:
                self.product_price = i.text  # Store the price

            product_reviews = prodRes_html.find(
                "a", {"class": "detailed-reviews-allReviews"}  # Find the link to detailed reviews
            )

            if not product_reviews:
                return None  # Return None if no reviews are found
            return product_reviews  # Return the reviews link
        except Exception as e:
            raise customExceptions(e, sys)  # Handle exceptions

    # Method to scroll down the page to load reviews
    def scroll_to_load_reviews(self):
        # Change the window size to load more data
        self.driver.set_window_size(1920, 1080)  # Set window size to a standard dimension

        # Get the initial height of the page
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        # Scroll in smaller increments, waiting between scrolls
        while True:
            # Scroll down by a small amount
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(3)  # Wait for new content to load
            
            # Calculate the new height after scrolling
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # Break the loop if no new content is loaded after scrolling
            if new_height == last_height:
                break
            
            # Update the last height for the next iteration
            last_height = new_height

    # Method to extract detailed reviews from the review link
    def extract_products(self, product_reviews: list):
        try:
            t2 = product_reviews["href"]  # Get the href from the reviews link
            Review_link = "https://www.myntra.com" + t2  # Construct the full review URL
            self.driver.get(Review_link)  # Navigate to the review page
            
            self.scroll_to_load_reviews()  # Scroll to load more reviews            
            review_page = self.driver.page_source  # Get the page source

            review_html = bs(review_page, "html.parser")  # Parse the HTML
            review = review_html.findAll(
                "div", {"class": "detailed-reviews-userReviewsContainer"}  # Find user reviews container
            )

            # Initialize lists to hold extracted information
            reviews = []
            for i in review:
                user_rating = i.findAll(
                    "div", {"class": "user-review-main user-review-showRating"}  # Extract user ratings
                )
                user_comment = i.findAll(
                    "div", {"class": "user-review-reviewTextWrapper"}  # Extract user comments
                )
                user_name = i.findAll("div", {"class": "user-review-left"})  # Extract user names

            # Process each review and collect data
            for i in range(len(user_rating)):
                try:
                    rating = (
                        user_rating[i]
                        .find("span", class_="user-review-starRating")
                        .get_text()
                        .strip()  # Extract and clean the rating text
                    )
                except:
                    rating = "No rating Given"  # Default if no rating found
                try:
                    comment = user_comment[i].text  # Extract comment text
                except:
                    comment = "No comment Given"  # Default if no comment found
                try:
                    name = user_name[i].find("span").text  # Extract user name
                except:
                    name = "No Name given"  # Default if no name found
                try:
                    date = user_name[i].find_all("span")[1].text  # Extract review date
                except:
                    date = "No Date given"  # Default if no date found

                # Create a dictionary for the review data
                mydict = {
                    "Product Name": self.product_title,
                    "Over_All_Rating": self.product_rating_value,
                    "Price": self.product_price,
                    "Date": date,
                    "Rating": rating,
                    "Name": name,
                    "Comment": comment,
                }
                reviews.append(mydict)  # Append review dictionary to the list

            # Convert the list of reviews to a DataFrame
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

            return review_data  # Return the DataFrame containing reviews

        except Exception as e:
            raise customExceptions(e, sys)  # Handle exceptions
        
    
    # Method to skip certain products based on index
    def skip_products(self, search_string, no_of_products, skip_index):
        product_urls: list = self.scrape_product_urls(search_string, no_of_products + 1)  # Scrape more URLs

        product_urls.pop(skip_index)  # Remove the URL at the skip index

    # Method to get review data and return as a DataFrame
    def get_review_data(self) -> pd.DataFrame:
        try:
            product_urls = self.scrape_product_urls(product_name=self.product_name)  # Scrape product URLs
            product_details = []  # Initialize list for product details

            review_len = 0  # Initialize review count
            while review_len < self.no_of_products:
                product_url = product_urls[review_len]  # Get the current product URL
                review = self.extract_reviews(product_url)  # Extract reviews

                if review:
                    product_detail = self.extract_products(review)  # Extract detailed reviews
                    product_details.append(product_detail)  # Add to details list

                    review_len += 1  # Increment the review count
                else:
                    product_urls.pop(review_len)  # Remove the URL if no reviews found

            self.driver.quit()  # Close the browser
            data = pd.concat(product_details, axis=0)  # Combine all product details into a single DataFrame
            data.to_csv("fetched_data.csv", index=False)  # Save the data to a CSV file            
            return data  # Return the collected review data

        except Exception as e:
            raise customExceptions(e, sys)  # Handle exceptions
