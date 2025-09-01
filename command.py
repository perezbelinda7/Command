import streamlit as st
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Juice Type': ['Chilled', 'Frozen', 'Shelf Stable', 'Fresh', 'Chilled', 'Frozen'],
    'Sales': [1200, 800, 950, 1100, 1300, 900]
})

# Sidebar filter
selected = st.sidebar.multiselect("Select Juice Types", df['Juice Type'].unique(), default=df['Juice Type'].unique())

# Filter data
filtered_df = df[df['Juice Type'].isin(selected)]

# Display
st.title("Orange Juice Dashboard")
st.bar_chart(filtered_df.groupby('Juice Type')['Sales'].sum())

