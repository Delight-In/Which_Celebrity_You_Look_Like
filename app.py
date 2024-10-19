import streamlit as st 
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.scrapper.scrape import ScrapeReviews

# Set the title and configuration for the Streamlit page
st.set_page_config("myntra-review-scrapper")

st.title("Myntra Review Scrapper")
# Initialize session state to track whether data has been scrapped
st.session_state["data"] = False

def form_input():
    # Input field for the user to search for products
    product = st.text_input("Search Products")
    # Store the product name in session state for later use
    st.session_state[SESSION_PRODUCT_KEY] = product
    
    # Input for the number of products to scrape, with validation
    no_of_products = st.number_input("No of products to search",
                                     step=1,
                                     min_value=1)

    # Button to trigger the review scraping process
    if st.button("Scrape Reviews"):
        # Create an instance of ScrapeReviews with the provided product name and count
        scrapper = ScrapeReviews(
            product_name=product,
            no_of_products=int(no_of_products)
        )

        # Call the method to scrape reviews and store the data
        scrapped_data = scrapper.get_review_data()
        
        if scrapped_data is not None:
            # Update session state to indicate that data has been scrapped
            st.session_state["data"] = True
            
            # Initialize MongoIO to store the scrapped reviews in the database
            mongoio = MongoIO()
            mongoio.store_reviews(product_name=product,
                                  reviews=scrapped_data)
            print("Stored Data into MongoDB")

        # Display the scrapped data in a dataframe format
        st.dataframe(scrapped_data)

if __name__ == "__main__":
    # Run the form_input function when the script is executed
    data = form_input()
