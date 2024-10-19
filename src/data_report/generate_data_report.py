import streamlit as st
import pandas as pd
import plotly.express as px
from src.exception import CustomException

class DashboardGenerator:
    def __init__(self, data):
        # Initialize the dashboard generator with the provided data
        self.data = data

    def display_general_info(self):
        # Display a header for the general information section
        st.header('General Information')

        try:
            # Convert 'Over_All_Rating' and 'Price' columns to numeric types for analysis
            self.data['Over_All_Rating'] = pd.to_numeric(self.data['Over_All_Rating'], errors='coerce')
            self.data['Price'] = pd.to_numeric(
                self.data['Price'].apply(lambda x: x.replace("₹", "")),  # Remove currency symbol
                errors='coerce'
            )

            self.data["Rating"] = pd.to_numeric(self.data['Rating'], errors='coerce')

            # Create a summary pie chart of average ratings by product
            product_ratings = self.data.groupby('Product Name', as_index=False)['Over_All_Rating'].mean().dropna()

            fig_pie = px.pie(product_ratings, values='Over_All_Rating', names='Product Name',
                             title='Average Ratings by Product')
            st.plotly_chart(fig_pie)  # Display the pie chart

            # Create a bar chart comparing average prices of different products
            avg_prices = self.data.groupby('Product Name', as_index=False)['Price'].mean().dropna()
            fig_bar = px.bar(avg_prices, x='Product Name', y='Price', color='Product Name',
                             title='Average Price Comparison Between Products',
                             color_discrete_sequence=px.colors.qualitative.Bold)
            fig_bar.update_xaxes(title='Product Name')  # Update X-axis title
            fig_bar.update_yaxes(title='Average Price')  # Update Y-axis title
            st.plotly_chart(fig_bar)  # Display the bar chart

        except Exception as e:
            # Raise a custom exception if an error occurs during the display
            raise CustomException(f"An error occurred in display_general_info: {str(e)}")

    def display_product_sections(self):
        # Display a header for the product sections
        st.header('Product Sections')

        try:
            # Get unique product names for display
            product_names = self.data['Product Name'].unique()
            columns = st.columns(len(product_names))  # Create columns for each product

            for i, product_name in enumerate(product_names):
                # Filter data for the current product
                product_data = self.data[self.data['Product Name'] == product_name]

                with columns[i]:
                    st.subheader(f'{product_name}')  # Display product name

                    # Calculate and display average price with an emoji
                    avg_price = product_data['Price'].mean()
                    st.markdown(f"💰 Average Price: ₹{avg_price:.2f}")

                    # Calculate and display average rating
                    avg_rating = product_data['Over_All_Rating'].mean()
                    st.markdown(f"⭐ Average Rating: {avg_rating:.2f}")

                    # Display top positive reviews with ratings >= 4.5
                    positive_reviews = product_data[product_data['Rating'] >= 4.5].nlargest(5, 'Rating')
                    st.subheader('Positive Reviews')
                    for index, row in positive_reviews.iterrows():
                        st.markdown(f"✨ Rating: {row['Rating']} - {row['Comment']}")

                    # Display top negative reviews with ratings <= 2
                    negative_reviews = product_data[product_data['Rating'] <= 2].nsmallest(5, 'Rating')
                    st.subheader('Negative Reviews')
                    for index, row in negative_reviews.iterrows():
                        st.markdown(f"💢 Rating: {row['Rating']} - {row['Comment']}")

                    # Display count of ratings in different categories
                    st.subheader('Rating Counts')
                    rating_counts = product_data['Rating'].value_counts().sort_index(ascending=False)
                    for rating, count in rating_counts.items():
                        st.write(f"🔹 Rating {rating} count: {count}")

        except Exception as e:
            # Raise a custom exception if an error occurs during the display
            raise CustomException(f"An error occurred in display_product_sections: {str(e)}")
