import streamlit as st
from filters import load_data, apply_filters
from charts import (
    plot_pie_surface,
    plot_histogram_age,
    plot_line_matches_over_time,
    plot_bar_top_winners,
    plot_scatter_ranks,
    plot_box_ages,
    plot_heatmap_correlation,
    plot_area_cumulative,
    plot_count_tournaments,
    plot_violin_age_surface
)

st.set_page_config(page_title="WTA 2016 Dashboard", layout="wide")  

st.markdown("""
<style>
    
    [data-testid="stAppViewContainer"] {
        background-color: #ffe4f0;
    }
    
    [data-testid="stSidebar"] {
        background-color: #ffb6d9;
    }
    
    
    h1, h2, h3, h4, h5, h6 {
        color: #c2185b !important;
    }
    
    
    p, label, .stMarkdown {
        color: #880e4f  !important;
    }
    
    
    [data-testid="stMetric"] {
        background-color: #ffb6d9;
        border-radius: 10px;
        padding: 10px;
    }
    

    .stButton > button {
        background-color: #e91e8c;
        color: white;
        border-radius: 8px;
        border: none;
    } 
            /* Dropdown select box */
    [data-testid="stSelectbox"] > div > div {
        background-color: #ffb6d9;
        color: #880e4f;
    }
    
    /* Dropdown options list */
    [data-testid="stSelectbox"] div[role="listbox"] {
        background-color: #ffb6d9;
        color: #880e4f;
    }
    
    /* Text input box */
    [data-testid="stTextInput"] > div > div > input {
        background-color: #ffb6d9;
        color: #880e4f;
    }
    
    /* Multiselect box */
    [data-testid="stMultiSelect"] > div {
        background-color: #ffb6d9;
        color: #880e4f;
    }

    /* Slider */
    [data-testid="stSlider"] > div {
        color: ##c2185b;
    }
</style>
""", unsafe_allow_html=True)

# --- Load Data ---
@st.cache_data
def get_data():
    return load_data()

df = get_data()

# --- Sidebar Filters ---
with st.sidebar:
    st.header("Filters")

    # Surface dropdown
    surface = st.selectbox("Surface", ["All"] + sorted(df["surface"].dropna().unique().tolist()))

    # Round dropdown
    round_sel = st.selectbox("Round", ["All", "R128", "R64", "R32", "R16", "QF", "SF", "F", "RR"])

    # Tournament Level dropdown
    tourney_level = st.selectbox("Tournament Level", ["All"] + sorted(df["tourney_level_label"].dropna().unique().tolist()))

    # Winner Rank range slider
    rank_range = st.slider("Winner Rank Range", 1, 500, (1, 500))

    # Player name search
    search_text = st.text_input("Search Player Name")

    # Multi-select tournaments
    selected_tournaments = st.multiselect(
        "Select Tournaments (empty = all)",
        sorted(df["tourney_name"].dropna().unique().tolist())
    )

    # Reset button
    if st.button("Reset Filters"):
        st.rerun()

# Apply Filters 
filtered_df = apply_filters(df, surface, round_sel, rank_range, search_text, tourney_level)

if selected_tournaments:
    filtered_df = filtered_df[filtered_df["tourney_name"].isin(selected_tournaments)]

# Title and Description
st.title("WTA 2016 Season Dashboard")
st.markdown("Explore match statistics from the 2016 Women's Tennis Association season.")

# --- KPI Cards ---
st.subheader("Key Metrics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Matches", len(filtered_df))
c2.metric("Avg Duration", f"{filtered_df['minutes'].mean():.0f} min")
c3.metric("Unique Winners", filtered_df["winner_name"].nunique())
c4.metric("Most Wins", filtered_df["winner_name"].value_counts().idxmax())

st.markdown("---")

# --- Section 1: Surface Analysis ---
st.subheader("Surface Analysis")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_pie_surface(filtered_df))
with col2:
    st.pyplot(plot_count_tournaments(filtered_df))

st.markdown("---")

# --- Section 2: Player Performance ---
st.subheader("Player Performance")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_bar_top_winners(filtered_df))
with col2:
    st.pyplot(plot_scatter_ranks(filtered_df))

st.markdown("---")

# --- Section 3: Age Analysis ---
st.subheader("Age Analysis")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_histogram_age(filtered_df))
with col2:
    st.pyplot(plot_box_ages(filtered_df))

st.markdown("---")

# --- Section 4: Season Trends ---
st.subheader("Season Trends")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_line_matches_over_time(filtered_df))
with col2:
    st.pyplot(plot_area_cumulative(filtered_df))

st.markdown("---")

# --- Section 5: Statistics ---
st.subheader("Statistics")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_violin_age_surface(filtered_df))
with col2:
    st.pyplot(plot_heatmap_correlation(filtered_df))
