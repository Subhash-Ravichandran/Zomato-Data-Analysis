# Zomato Data Analysis and Dashboard Development

## Problem Statement

Zomato is a popular restaurant discovery and food delivery service. Analyzing Zomato's data can provide insights into customer preferences and behavior, and identify trends in the restaurant industry. By leveraging various methodologies such as Data Exploration, Data Cleaning, Feature Selection, and Deployment, we can extract valuable insights. Data visualization techniques like bar charts, line charts, and scatter plots will help in effectively communicating these insights to stakeholders, including restaurants, food industry players, and investors.

## Approach

We will be using the Zomato dataset and the country ISO code for all the countries in the dataset. The datasets can be accessed from the following URLs:

- [Zomato Dataset](https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv)
- [Country Code Dataset](https://github.com/nethajinirmal13/Training-datasets/blob/main/zomato/Country-Code.xlsx)

### Task 1: Data Engineering

1. **Add a Column with Rupees as the Currency:**
   - Convert all monetary values in the dataset to Indian Rupees (INR) using appropriate conversion rates.
   
2. **Plot Comparing Indian Currency with Other Countries' Currencies:**
   - Create a visualization that compares the value of the Indian Rupee against other currencies present in the dataset.

### Task 2: Dashboard Development

Using Plotly or Streamlit, develop an interactive dashboard with the following features:

1. **Country-Specific Data Dropdown:**
   - A dropdown menu allowing users to select and view data specific to a chosen country.
   
2. **Custom Charts:**
   - Any two charts of your choice, such as:
     - Count of restaurants
     - Total sales
     - Favorite cuisines

3. **Costly Cuisines in India:**
   - Identify and display which cuisines are the most expensive in India.

4. **City-Based Filtering:**
   - Allow users to filter data based on city.

5. **Famous Cuisine in the City:**
   - Determine and display the most popular cuisine in each city.

6. **Costlier Cuisine:**
   - Identify and display which cuisines are costlier in each city.

7. **Rating Count in the City:**
   - Display a count of restaurant ratings in each city.

8. **Pie Chart: Online Delivery vs Dine-In:**
   - Show a pie chart comparing the proportion of online delivery orders versus dine-in orders.

9. **Comparison Between Cities in India:**
   - Generate a custom report comparing various metrics between different cities in India.

10. **Online Delivery Spending by Region:**
    - Identify and display which parts of India spend more on online delivery.

11. **Dine-In Spending by Region:**
    - Identify and display which parts of India spend more on dine-in services.

12. **High vs Low Living Cost Areas:**
    - Determine and display which parts of India have a higher cost of living compared to others.

### Task 3: Dashboard Deployment

- Host and deploy the developed dashboard on a web app server. Ensure the dashboard is accessible and user-friendly, providing valuable insights to improve Zomato's business operations.

## Results

Develop a Plotly Dashboard that effectively helps in analyzing and improving Zomato's business by providing detailed insights into customer preferences, restaurant performance, and industry trends. The dashboard should be intuitive and interactive, allowing users to explore the data through various filters and visualizations.
