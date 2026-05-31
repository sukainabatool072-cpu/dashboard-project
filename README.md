# WTA 2016 Tennis Dashboard

## What is this project?
This is a data visualization dashboard built using Python and Streamlit. 
It analyzes match data from the 2016 WTA (Women's Tennis Association) season 
including 2900 matches across different surfaces, tournaments and players.

## How to run it

Step 1 - Install the required libraries:
pip install pandas numpy matplotlib seaborn streamlit

Step 2 - Run the dashboard:
python -m streamlit run app.py

Step 3 - It will open automatically in your browser.

## Dataset
File name: wta_matches_2016.csv
Total matches: 2900
Columns used: surface, winner_name, loser_name, winner_age, loser_age, 
winner_rank, loser_rank, tourney_name, tourney_date

## Key Insights
1. Hard court is the most common surface with over 65% of all matches played on it.
2. Most winners are between the ages of 22 and 28.
3. Higher ranked players tend to win more consistently across all surfaces.
4. Match activity peaks between July and September during the US Open series.
5. Angelique Kerber and Serena Williams had the most wins in the 2016 season.