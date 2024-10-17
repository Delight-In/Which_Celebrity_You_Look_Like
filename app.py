import pandas as pd  # Importing pandas for data manipulation
import streamlit as st  # Importing Streamlit for web app interface
from src.cloud_io.cloud import MongoIO  # Importing MongoIO for cloud storage functionality
from src.constants import SESSION_PRODUCT_KEY  # Importing session key constant
from src.scrappers.scrape import ScrapeReviews  # Importing ScrapeReviews for scraping functionality

# Set the configuration for the Streamlit page
st.set_page_config(
    "Myntra-Review-Scrapper"  # Title of the Streamlit app
)

# Title of the app displayed in the main section
st.title("Myntra Review Scrapper")  
st.session_state["data"] = False  # Initialize session state for data storage

def form_input():  # Function to create the input form
    product = st.text_input("Search Products")  # Text input for product search
    st.session_state[SESSION_PRODUCT_KEY] = product  # Store the product name in session state
    no_of_products = st.number_input("No of products to search",  # Number input for quantity of products
                                     step=1,
                                     min_value=1)  # Minimum value set to 1

    # Button to trigger the review scraping process
    if st.button("Scrape Reviews"):  
        scrapper = ScrapeReviews(  # Create an instance of the ScrapeReviews class
            product_name=product,  # Pass the product name
            no_of_products=int(no_of_products)  # Pass the number of products to search
        )

        scrapped_data = scrapper.get_review_data()  # Call method to scrape review data
        if scrapped_data is not None:  # Check if data was successfully scraped
            st.session_state["data"] = True  # Update session state to indicate data availability
            mongoio = MongoIO()  # Create an instance of MongoIO for data storage
            mongoio.store_reviews(product_name=product,  # Store reviews in MongoDB
                                  reviews=scrapped_data)  # Pass the scraped reviews
            print("Stored Data into mongodb")  # Print confirmation of data storage

        st.dataframe(scrapped_data)  # Display the scraped data in a dataframe

if __name__ == "__main__":  # Check if the script is run directly
    data = form_input()  # Call the form_input function to execute the app logic
