# IMDB 2024 Data Scraping and Visualizations


Business Use Cases:
Top-Rated Movies: Identify the top 10 movies with the highest ratings and voting counts.
Genre Analysis: Explore the distribution of genres in the 2024 movie list.
Duration Insights: Analyze the average duration of movies across genres.
Voting Patterns: Discover genres with the highest average voting counts.
Popular Genres: Identify the genres that dominate IMDb's 2024 list based on movie count.
Rating Distribution: Analyze the distribution of ratings across all movies.
Genre vs. Ratings: Compare the average ratings for each genre.
Duration Extremes: Identify the shortest and longest movies in 2024.
Top-Voted Movies: Find the top 10 movies with the highest voting counts.
Interactive Filtering: Allow users to filter movies by ratings, duration, votes, and genre and view the results in a tabular DataFrame format.






Approach:
1. Data Scraping and Storage
Data Source: IMDb 2024 Movies page (link).
Scraping Method: Use Selenium to extract the following fields:
Movie Name
Genre
Ratings
Voting Counts
Duration
Genre-wise Storage: Save extracted data as individual CSV files for each genre.
Combine Data: Merge all genre-wise CSVs into a single DataFrame.
SQL Storage: Store the merged dataset into an SQL database for querying and future analysis.



2. Data Analysis, Visualization, and Filtration
Interactive Visualizations
Using Python and Streamlit, create dynamic visualizations for:
Top 10 Movies by Rating and Voting Counts: Identify movies with the highest ratings and significant voting engagement.
Genre Distribution: Plot the count of movies for each genre in a bar chart.
Average Duration by Genre: Show the average movie duration per genre in a horizontal bar chart.
Voting Trends by Genre: Visualize average voting counts across different genres.
Rating Distribution: Display a histogram or boxplot of movie ratings.
Genre-Based Rating Leaders: Highlight the top-rated movie for each genre in a table.
Most Popular Genres by Voting: Identify genres with the highest total voting counts in a pie chart.
Duration Extremes: Use a table or card display to show the shortest and longest movies.
Ratings by Genre: Use a heatmap to compare average ratings across genres.
Correlation Analysis: Analyze the relationship between ratings and voting counts using a scatter plot.
Interactive Filtering Functionality
Allow users to filter the dataset based on the following criteria:
Duration (Hrs): Filter movies based on their runtime (e.g., < 2 hrs, 2–3 hrs, > 3 hrs).
Ratings: Filter movies based on IMDb ratings (e.g., > 8.0).
Voting Counts: Filter based on the number of votes received (e.g., > 10,000 votes).
Genre: Filter movies within specific genres (e.g., Action, Drama).
Display the filtered results in a dynamic DataFrame within the Streamlit app.
Combine filtering options so users can apply multiple filters simultaneously for customized insights.
Example Use Case:
Users can filter for Action Movies with ratings above 8.0, duration between 2-3 hours, and voting counts greater than 50,000, and the results will be displayed dynamically as a table.
Dataset
Scraped IMDb data for 2024 movies, organized genre-wise.
Columns:
Movie Name
Genre
Ratings
Voting Counts
Duration



Technical Tags
Languages: Python
Database: MySQL/PostgreSQL
Visualization Tools: Streamlit
Libraries: Pandas, Selenium, Matplotlib, SQLAlchemy, Seaborn

Project Deliverables
SQL Database: Contains the complete movie dataset.
Python Scripts: For data scraping, cleaning, merging, and database interaction.
Streamlit Application: Interactive dashboard showcasing visualizations, insights, and filtering functionality.
CSV Files: Genre-wise datasets for each genre in the IMDb list.
Streamlit Application: Interactive dashboard for real-time analysis.
