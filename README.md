```markdown
# Myntra Products Review Scraper and Dashboard

## Overview
This project is a web application that scrapes product reviews from Myntra, a popular online fashion retailer. The application enables users to search for products,
scrape their reviews, and analyze the data visually through interactive dashboards built using Streamlit.

## Features
- **Product Review Scraping**: Automatically fetches reviews, ratings, and pricing information from Myntra.
- **Data Storage**: Stores the scraped review data in a MongoDB database for persistent access.
- **Interactive Dashboard**: Provides visual analytics of the scraped data, including average ratings and price comparisons.
- **User-Friendly Interface**: Built with Streamlit for a seamless user experience.

## Installation
To set up this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/myntra-review-scraper.git
   cd myntra-review-scraper
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB**:
   - Ensure you have a MongoDB instance running.
   - Update your environment variables or configuration files to include your MongoDB URL.

## Usage
1. **Run the Application**:
   Use Streamlit to run the web application:
   ```bash
   streamlit run app.py
   ```

2. **Scrape Reviews**:
   - Enter the product name in the search bar.
   - Specify the number of products to scrape.
   - Click the "Scrape Reviews" button to begin the process.

3. **View Analysis**:
   - Once the data is scraped, you can generate an analysis.
   - The dashboard displays general information, average ratings, price comparisons, and detailed product reviews.

## Code Structure
### Key Components
- **ScrapeReviews Class**: Handles web scraping using Selenium and BeautifulSoup, extracting product URLs and reviews.
- **MongoIO Class**: Manages database operations, including storing and retrieving reviews from MongoDB.
- **DashboardGenerator Class**: Responsible for generating visual reports and insights from the scraped data using Plotly and Streamlit.
- **Error Handling**: Custom exceptions are implemented to manage errors gracefully throughout the application.

### Sample Code Snippets
#### Scraping Product Reviews
```python
def scrape_product_urls(self, product_name):
    try:
        search_string = product_name.replace(" ", "-")
        encoded_query = quote(search_string)
        self.driver.get(f"https://www.myntra.com/{search_string}?rawQuery={encoded_query}")
        # Code to extract product URLs...
    except Exception as e:
        raise CustomException(e, sys)
```

#### Generating the Dashboard
```python
def display_general_info(self):
    st.header('General Information')
    try:
        # Convert and visualize data...
    except Exception as e:
        raise CustomException(f"An error occurred in display_general_info: {str(e)}")
```

## Error Handling
The application includes robust error handling using a custom `CustomException` class, ensuring that issues during scraping or data processing are caught and logged appropriately.

```
