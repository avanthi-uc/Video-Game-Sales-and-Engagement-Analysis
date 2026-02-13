import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🎮 Video Game Analytics",
    layout="wide",
    page_icon="🎮"
)

st.markdown("""
<h1 style='text-align: center; color: white;'>
🎮 Video Game Sales & Engagement Dashboard
</h1>
<p style='text-align: center; color: lightgray;'>
Interactive insights into game popularity, platforms, and ratings
</p>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0f172a;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */
.stButton>button {
    border-radius: 12px;
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    font-weight: bold;
    border: none;
    padding: 0.5em 1em;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

/* Headers */
h1, h2, h3 {
    font-weight: 600;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* Sidebar title */
section[data-testid="stSidebar"] h1 {
    color: #00c6ff;
    text-align: center;
}

/* Radio buttons */
div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
    transition: 0.3s ease;
}

div[role="radiogroup"] > label:hover {
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    transform: translateX(5px);
}

</style>
""", unsafe_allow_html=True)





# Page settings
st.set_page_config(page_title="Video Game Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["Introduction", "View Tables","Insights"])




if page == "Introduction":
    st.title(" Video Game Sales Analysis")
    df = pd.read_csv("sales_cleaned.csv")   

    st.markdown("""
    🎮 Introduction

The Video Game Sales and Engagement Analysis Project aims to explore and visualize trends in game popularity, user behavior, and platform performance by integrating sales and engagement datasets. The project combines two major datasets — game engagement data and regional sales data — to uncover meaningful insights into how game features such as genre, rating, platform, developer, and wishlist activity influence global sales performance.

In today’s competitive gaming industry, understanding player preferences and market trends is crucial for game developers, publishers, and marketers. This project addresses that need by merging structured sales data with user engagement metrics to analyze:

The relationship between user ratings and global sales

The impact of wishlists and backlogs on commercial success

The performance of different genres and platforms

Regional sales trends and market evolution over time

🎯 Project Objective

The primary objective of this project is to build a structured SQL database and develop interactive dashboards using Power BI / Streamlit to:

Identify high-performing genres and platforms

Analyze user engagement patterns

Forecast potential sales trends

Support strategic decision-making in marketing and product development

🛠 Technical Approach

The project follows a systematic workflow:

Data Cleaning & Preprocessing

Removal of duplicates and null values

Standardization of genre, platform, and publisher names

Formatting of dates and categorical fields

SQL Database Design

Creation of structured relational tables

Enforcement of foreign keys to maintain data integrity

Data Visualization & Dashboarding

Interactive bar charts, line charts, heatmaps, and scatter plots

KPI indicators such as average rating, total sales, and top-performing genres

Drill-down analysis for regional and platform-level insights

Exploratory Data Analysis (EDA)

Examination of ratings, wishlists, plays, and backlog trends

Identification of success factors for high-selling games

Analysis of genre-platform combinations

📊 Business Value

This project supports:

🎯 Marketing Strategy Optimization

🎮 Data-driven Product Development

📈 Sales Forecasting and Trend Analysis

💰 Efficient Resource Allocation

By the end of the analysis, the dashboard provides clear insights into consumer behavior, genre success patterns, and platform dominance, enabling smarter strategic decisions within the gaming industry.
    """)


elif page == "View Tables":

    sales_df = pd.read_csv("sales_cleaned.csv")
    games_df = pd.read_csv("games_cleaned.csv")

    st.title("📊 Datasets Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💰 Sales Dataset")
        st.dataframe(sales_df)

        st.write("### Filter Sales by Platform")
        platform = st.selectbox(
            "Select Platform",
            sales_df["Platform"].unique(),
            key="sales_platform"
        )

        filtered_sales = sales_df[sales_df["Platform"] == platform]
        st.dataframe(filtered_sales)

    with col2:
        st.subheader("🎮 Games Dataset")
        st.dataframe(games_df)

        st.write("### Filter by Title")

        # Filter by Title
        title = st.selectbox(
            "Filter by Title",
            games_df["Title"].unique(),
            key="games_title"
        )

        filtered_games = games_df[games_df["Title"] == title]

        st.dataframe(filtered_games)

    st.subheader("🔗 Merged Dataset (Inner Join)")

    merged_df = pd.merge(
        sales_df,
        games_df,
        left_on="Title",     # from sales dataset
        right_on="Title",   # from games dataset
        how="inner"
    )

    st.dataframe(merged_df)

    
    st.subheader("🎯 Filter Merged Data by Game Name")

    game_name = st.selectbox(
        "Select Game",
        sorted(merged_df["Title"].unique())
    )

    filtered_merged = merged_df[merged_df["Title"] == game_name]

    st.dataframe(filtered_merged)

elif page == "Insights":

    st.title("📊 Key Insights & Analysis")

    # Load datasets
    sales_df = pd.read_csv("sales_cleaned.csv")
    games_df = pd.read_csv("games_cleaned.csv")

    # Clean for merge
    sales_df["Title"] = sales_df["Title"].str.strip().str.lower()
    games_df["Title"] = games_df["Title"].str.strip().str.lower()

    merged_df = pd.merge(
        sales_df,
        games_df,
        left_on="Title",
        right_on="Title",
        how="inner"
    )

    st.subheader(" Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Global Sales", round(sales_df["Global_Sales"].sum(), 2))

    with col2:
        st.metric("Average Game Rating", round(games_df["Rating"].mean(), 2))

    with col3:
        st.metric("Total Wishlist Count", int(games_df["Wishlist"].sum()))

    st.markdown("---")

    # ---------------- TOP GENRES ----------------
    st.subheader("🎮 Top Genres by Global Sales")

    top_genres = (
        sales_df.groupby("Genre")["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(top_genres)

    # ---------------- REGIONAL SALES ----------------
    st.subheader("🌍 Regional Sales Distribution")

    regional_sales = sales_df[
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    ].sum()

    st.bar_chart(regional_sales)

    # ---------------- SALES TREND ----------------
    st.subheader("📈 Global Sales Trend Over Years")

    yearly_sales = (
    sales_df[sales_df["Year"] > 1600]   
        .groupby("Year")["Global_Sales"]
        .sum()
        .sort_index()
)


    st.line_chart(yearly_sales)

  
    # ---------------- WISHLIST VS SALES ----------------
    st.subheader("Wishlist vs Global Sales")

    st.scatter_chart(
        merged_df[["Wishlist", "Global_Sales"]]
    )

    correlation_wishlist = merged_df["Wishlist"].corr(merged_df["Global_Sales"])

    st.write(f"Correlation between Wishlist and Sales: {round(correlation_wishlist,2)}")

    st.markdown("---")

    # ---------------- FINAL BUSINESS INSIGHTS ----------------
    st.subheader("📌 Business Conclusions")

    st.markdown("""
    - Action and high-engagement genres dominate global revenue.
    - North America contributes the largest portion of sales.
    - Wishlist count shows a strong relationship with global sales performance.
    - Higher ratings positively influence commercial success.
    - Certain platform and genre combinations consistently outperform others.
    """)
