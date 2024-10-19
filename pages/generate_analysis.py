import pandas as pd
import streamlit as st 
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.utils import fetch_product_names_from_cloud
from src.data_report.generate_data_report import DashboardGenerator

# Initialize MongoIO instance for database operations
mongo_con = MongoIO()

def create_analysis_page(review_data: pd.DataFrame):
    # Check if the review data is not None
    if review_data is not None:
        # Display the review data in a Streamlit dataframe
        st.dataframe(review_data)
        
        # Button to generate analysis
        if st.button("Generate Analysis"):
            # Create an instance of DashboardGenerator with the review data
            dashboard = DashboardGenerator(review_data)

            # Display general information about the reviews
            dashboard.display_general_info()

            # Display product-specific sections with detailed reviews
            dashboard.display_product_sections()

try:
    # Check if review data is available in the session state
    if st.session_state.data:
        # Fetch reviews from the database using the product name stored in the session state
        data = mongo_con.get_reviews(product_name=st.session_state[SESSION_PRODUCT_KEY])
        # Create analysis page with the fetched review data
        create_analysis_page(data)

    else:
        # If no data is available, show a message in the sidebar
        with st.sidebar:
            st.markdown("""
            No Data Available for analysis. Please go to the search page to collect data.
            """)
except AttributeError as e:
    # Handle the case where 'data' attribute might not be set in the session state
    product_name = None
    st.markdown(""" # No Data Available for analysis.""")
    # Optionally log the error for debugging
    st.error(f"Error fetching data: {str(e)}")

except Exception as e:
    # Handle any other exceptions that might occur
    st.error(f"An unexpected error occurred: {str(e)}")
