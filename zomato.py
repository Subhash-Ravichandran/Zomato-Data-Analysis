import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")
from PIL import Image

st.set_page_config(layout= "wide")
st.markdown("""
    <h1 style='text-align: center;'>Zomato Data Analysis</h1>
    """, unsafe_allow_html=True)
st.write("")

st.markdown(f""" <style>.stApp {{
                        background:url("https://cdn.dribbble.com/users/1830537/screenshots/6651824/ezgif.com-video-to-gif.gif");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)
#Uploading CSV files
df_1= pd.read_csv("/content/Q1")
df_2= pd.read_csv("/content/Q2")
india_cities= pd.read_csv("/content/Indian_cities")

select = option_menu(
    menu_title = None,
    options = ["Home","Explore Data"],
    icons =["house","bar-chart"],orientation="horizontal")

if select == "Home":
  text_content = """
    <h2 style='text-align: center; color: black;'>Welcome to my Zomato Data Analysis Project</h2>
    <p style='font-size: 18px; text-align: center;'>Zomato is a popular restaurant discovery and food delivery service. Data analysis on the platform's data could be used to gain insights into customer preferences and behavior, as well as identify trends in the restaurant industry. To perform the analysis various methodologies such as Data Exploration, Data Cleaning, Feature Selection And Deployment can be used. Additionally, various data visualization techniques like bar charts, line charts, scatter plots, etc. could be employed to help communicate the insights gained from the analysis.Overall, data visualization can be used to effectively communicate the insights from Zomato data analysis to a wide range of stakeholders, including restaurants, food industry players, and investors.</p>
        """

  # Display the text using markdown function
  st.markdown(text_content, unsafe_allow_html=True)

if select == "Explore Data":

  option = st.radio(
    "Select any category for Analysis",
    ('Currency Comparision', 'Country Specific Data', 'Costliest Cuisines', 'City wise Data', 'Comparing Cities',), horizontal=True)

  st.write("You selected:", option)
  if option == 'Currency Comparision':
    # Creating the table
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_1.columns),
                fill_color='black',  # Table background color
                font=dict(color='red'),  # Header text color
                align='center'),
    cells=dict(values=[df_1['Country'], df_1['Currency'], df_1['Amount_in_INR'], df_1['Average_Cost_for_two']],
               fill_color='white',  # Table background color
               font=dict(color='red'),  # Cells text color
               align='center'))
    ])

    # Display the table in Streamlit
    st.plotly_chart(fig, use_container_width=True)

  if option == 'Country Specific Data':
    option = st.selectbox(
    "Select any country to explore",
    ('India', 'Australia', 'Brazil', 'Canada', 'Indonesia',
            'New Zealand', 'Phillipines', 'Qatar', 'Singapore', 'South Africa',
            'Sri Lanka', 'Turkey', 'UAE', 'United Kingdom', 'United States'))

    filtered_df = df_2[df_2['Country'] == option]
    fig = px.bar(filtered_df, x='Cuisines', y='Reviews', title='Favourite Cuisines')
    # Display the table in Streamlit
    st.plotly_chart(fig,use_container_width=True)

  if option == 'Costliest Cuisines':
    df_3 = india_cities.groupby(['Cuisines']).agg({'Amount_in_INR': 'max'}).sort_values('Amount_in_INR', ascending=False).reset_index()
    fig = px.bar(df_3, x='Cuisines', y='Amount_in_INR', title='Costliest Cuisine in India')
    st.plotly_chart(fig,use_container_width=True)

  if option == 'City wise Data':
    df_4 = india_cities.groupby(['Cuisines','City']).agg({'Votes':'max','Reviews': 'count',"Rating":'count','Amount_in_INR':'max','Booking_Availability':'count','Online_delivery':'count'}).sort_values('Amount_in_INR', ascending=False).reset_index()
    fig = px.sunburst(df_4, path=['City','Cuisines'], values='Votes',
                    title='Famous cuisines')
    st.plotly_chart(fig,use_container_width=True)

    #Costliest Cousine
    df_4['Amount_Rank'] = df_4.groupby('City')['Amount_in_INR'].rank(method='first', ascending=False)

    df_4_costlier_cuisine = df_4[df_4['Amount_Rank'] == 1].drop(columns=['Amount_Rank', 'Votes', 'Online_delivery', 'Booking_Availability', 'Rating', 'Reviews'])

    fig = px.bar(df_4_costlier_cuisine, x='City', y='Amount_in_INR', color='Cuisines', 
             title='Costliest Cuisines in Each City by Amount in INR',
             labels={'Amount_in_INR': 'Amount in INR'},
             hover_data=['Cuisines'])
    st.plotly_chart(fig,use_container_width=True)

    #Rating Count
    df_4_rating_count = india_cities.groupby(['City','Rating_color']).agg({'Rating':'count'}).sort_values('Rating', ascending=False).reset_index()
    fig = px.sunburst(df_4_rating_count, path=['City', 'Rating_color'], values='Rating',
                    title='city wise Rating count')
    st.plotly_chart(fig,use_container_width=True)

    #Online Delivery vs Dine in
    df_4_delivery_availability = india_cities.groupby(['Booking_Availability','Online_delivery']).agg({'Rating':'count'}).sort_values('Rating', ascending=False).reset_index()
    fig = px.bar(df_4_delivery_availability, x='Booking_Availability', y='Rating', color='Online_delivery', 
             title='Costliest Cuisines in Each City by Amount in INR',
             labels={'Rating': 'Rating'},
             hover_data=['Rating'])

    
    st.plotly_chart(fig,use_container_width=True)

  if option == 'Comparing Cities':
    df_5_online_delivery = india_cities.groupby(['City']).agg({'Online_delivery':'count'}).sort_values('Online_delivery', ascending=False).reset_index()
    fig = px.bar(df_5_online_delivery, x='City', y='Online_delivery', color='Online_delivery', 
            title='Maximum online Deliveries',
            labels={'Online_delivery': 'Online_delivery'},
            hover_data=['Online_delivery'])
    st.plotly_chart(fig,use_container_width=True)

    df_5_dinein = india_cities.groupby(['City']).agg({'Booking_Availability':'count'}).sort_values('Booking_Availability', ascending=False).reset_index()
    fig = px.bar(df_5_dinein, x='City', y='Booking_Availability', color='Booking_Availability', 
            title='Maximum Dinein',
            labels={'Booking_Availability': 'Booking_Availability'},
            hover_data=['Booking_Availability'])
    st.plotly_chart(fig,use_container_width=True)

    df_5_living_cost = india_cities.groupby(['City']).agg({'Amount_in_INR':'max'}).sort_values('Amount_in_INR', ascending=False).reset_index()
    fig = px.bar(df_5_living_cost, x='City', y='Amount_in_INR', color='Amount_in_INR', 
            title='Cost of living',
            labels={'Amount_in_INR': 'Amount_in_INR'},
            hover_data=['Amount_in_INR'])
    st.plotly_chart(fig,use_container_width=True)






