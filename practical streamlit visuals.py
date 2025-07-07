import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# Load and preprocess the dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\USER\Desktop\Mini Project\imdb_movies_2024_list.csv")
    df['Genre'] = df['Genre'].apply(lambda x: str(x).split(',')[0] if pd.notnull(x) else x)
    df['Duration'] = df['Duration'].astype(str).str.extract(r'(\d+)').astype(float)
    df['Votes'] = df['Votes'].astype(str).str.replace(",", "").str.extract(r'(\d+)').astype(float)
    return df.dropna(subset=['Rating', 'Votes', 'Genre', 'Duration'])

df = load_data()

st.title("🎬 Movie Data Analysis Dashboard")

# -------------------------- SIDEBAR FILTERS --------------------------
st.sidebar.header("🔎 Filter Movies")

# Duration Filter
duration_filter = st.sidebar.selectbox(
    "Select Duration (Hours)",
    options=["All", "< 2 hrs", "2–3 hrs", "> 3 hrs"]
)

# Rating Filter
min_rating = st.sidebar.slider("Minimum IMDb Rating", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# Votes Filter
min_votes = st.sidebar.number_input("Minimum Votes", min_value=0, value=0, step=1000)

# Genre Filter
all_genres = sorted(df["Genre"].dropna().unique())
selected_genres = st.sidebar.multiselect("Select Genre(s)", options=all_genres, default=all_genres)

# Apply Duration Filter
def filter_by_duration(duration_col, option):
    if option == "< 2 hrs":
        return duration_col < 120
    elif option == "2–3 hrs":
        return duration_col.between(120, 180)
    elif option == "> 3 hrs":
        return duration_col > 180
    else:
        return pd.Series([True] * len(duration_col))  # No filter

duration_mask = filter_by_duration(df["Duration"], duration_filter)
rating_mask = df["Rating"] >= min_rating
votes_mask = df["Votes"] >= min_votes
genre_mask = df["Genre"].isin(selected_genres)

# Combine Filters
combined_mask = duration_mask & rating_mask & votes_mask & genre_mask
filtered_df = df[combined_mask]

# -------------------------- FILTERED DATA --------------------------
st.header("🧠 Filtered Movies Based on Your Selection")
st.write(f"Total Movies Matching Filters: {len(filtered_df)}")
st.dataframe(filtered_df[["Title", "Genre", "Rating", "Votes", "Duration"]])

# -------------------------- ANALYSIS --------------------------

# 1. Top 10 Movies by Rating and Votes
st.header("🔝 Top 10 Movies by Rating and Voting Counts")
top_movies = filtered_df.sort_values(['Rating', 'Votes'], ascending=[False, False]).head(10)
st.dataframe(top_movies[['Title', 'Rating', 'Votes']])

# 2. Genre Distribution
st.header("📊 Genre Distribution")
genre_counts = filtered_df['Genre'].value_counts()
fig, ax = plt.subplots()
genre_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_xlabel("Genre")
ax.set_ylabel("Number of Movies")
st.pyplot(fig)

# 3. Average Duration by Genre
st.header("⏱️ Average Duration by Genre")
avg_duration = filtered_df.groupby('Genre')['Duration'].mean().sort_values()
fig, ax = plt.subplots()
avg_duration.plot(kind='barh', ax=ax, color='lightgreen')
ax.set_xlabel("Average Duration (minutes)")
st.pyplot(fig)

# 4. Voting Trends by Genre
st.header("🗳️ Average Voting Counts by Genre")
avg_votes = filtered_df.groupby('Genre')['Votes'].mean().sort_values(ascending=False)
fig, ax = plt.subplots()
avg_votes.plot(kind='bar', ax=ax, color='coral')
ax.set_ylabel("Average Votes")
st.pyplot(fig)

# 5. Rating Distribution
st.header("⭐ Rating Distribution")
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(filtered_df['Rating'], bins=10, ax=ax[0], kde=True)
ax[0].set_title("Histogram of Ratings")
sns.boxplot(y=filtered_df['Rating'], ax=ax[1])
ax[1].set_title("Boxplot of Ratings")
st.pyplot(fig)

# 6. Genre-Based Rating Leaders
st.header("🏆 Top-Rated Movie per Genre")
top_per_genre = filtered_df.loc[filtered_df.groupby('Genre')['Rating'].idxmax()]
st.dataframe(top_per_genre[['Genre', 'Title', 'Rating']].reset_index(drop=True))

# 7. Most Popular Genres by Voting (Pie Chart)
st.header("🥧 Most Popular Genres by Total Voting Counts")
votes_by_genre = filtered_df.groupby('Genre')['Votes'].sum().sort_values(ascending=False)
fig, ax = plt.subplots()
votes_by_genre.plot.pie(ax=ax, autopct='%1.1f%%', startangle=90, figsize=(6, 6))
ax.set_ylabel("")
st.pyplot(fig)

# 8. Duration Extremes
st.header("🎬 Shortest and Longest Movies")
if not filtered_df.empty:
    shortest = filtered_df.loc[filtered_df['Duration'].idxmin()][['Title', 'Duration']]
    longest = filtered_df.loc[filtered_df['Duration'].idxmax()][['Title', 'Duration']]
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Shortest Movie", shortest['Title'], f"{shortest['Duration']} min")
    with col2:
        st.metric("Longest Movie", longest['Title'], f"{longest['Duration']} min")
else:
    st.info("No movies available for duration extremes in the current filter.")

# 9. Heatmap of Ratings by Genre
st.header("🌡️ Average Ratings by Genre (Heatmap)")
if not filtered_df.empty:
    heat_data = filtered_df.groupby('Genre')['Rating'].mean().to_frame().T
    fig, ax = plt.subplots()
    sns.heatmap(heat_data, annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)
else:
    st.info("Not enough data to render heatmap.")

# 10. Correlation Analysis: Rating vs Votes
st.header("🔗 Correlation: Rating vs. Voting Counts")
if not filtered_df.empty:
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_df, x='Votes', y='Rating', hue='Genre', palette='tab10', ax=ax)
    ax.set_xscale('log')
    st.pyplot(fig)
else:
    st.info("Not enough data for correlation plot.")

st.markdown("---")
st.caption("📈 Built with Streamlit and ❤️ by KyKan Data Horizon")
