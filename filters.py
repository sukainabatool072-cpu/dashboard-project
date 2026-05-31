import pandas as pd

def load_data():
    df = pd.read_csv("wta_matches_2016.csv")
    
    # Convert tourney_date from integer like 20160104 to a real date
    df['tourney_date'] = pd.to_datetime(df['tourney_date'].astype(str), format='%Y%m%d')
    
    # Fill missing text columns
    df['surface'] = df['surface'].fillna('Unknown')
    df['winner_hand'] = df['winner_hand'].fillna('Unknown')
    df['loser_hand'] = df['loser_hand'].fillna('Unknown')
    
    # Fill missing numbers with the median of each column
    num_cols = ['minutes', 'winner_rank', 'loser_rank', 'winner_age', 'loser_age',
                'w_ace', 'w_df', 'l_ace', 'l_df', 'w_svpt', 'l_svpt']
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    
    # Make tourney_level human-readable
    level_map = {'I': 'International', 'G': 'Grand Slam', 'P': 'Premier', 'D': 'Fed Cup'}
    df['tourney_level_label'] = df['tourney_level'].map(level_map).fillna(df['tourney_level'])
    
    return df


def apply_filters(df, surface, round_sel, rank_range, search_text, tourney_level):
    filtered = df.copy()
    
    if surface != "All":
        filtered = filtered[filtered['surface'] == surface]
    
    if round_sel != "All":
        filtered = filtered[filtered['round'] == round_sel]
    
    if tourney_level != "All":
        filtered = filtered[filtered['tourney_level_label'] == tourney_level]
    
    min_rank, max_rank = rank_range
    filtered = filtered[(filtered['winner_rank'] >= min_rank) & (filtered['winner_rank'] <= max_rank)]
    
    if search_text.strip():
        mask = (filtered['winner_name'].str.contains(search_text, case=False, na=False) |
                filtered['loser_name'].str.contains(search_text, case=False, na=False))
        filtered = filtered[mask]
    
    return filtered