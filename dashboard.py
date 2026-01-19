import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("Walmart_Sales.csv")

# Convert Date column (day-first format)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Dashboard title
st.title("Walmart Sales Dashboard")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Total sales by store
if 'Store' in df.columns and 'Weekly_Sales' in df.columns:
    st.subheader("Total Weekly Sales by Store")
    sales_by_store = df.groupby('Store')['Weekly_Sales'].sum()
    st.bar_chart(sales_by_store)

# Filter by store
if 'Store' in df.columns and 'Weekly_Sales' in df.columns:
    store = st.selectbox("Select Store", df['Store'].unique())
    filtered_df = df[df['Store'] == store]

    st.subheader(f"Weekly Sales Over Time for Store {store}")
    if 'Date' in df.columns:
        filtered_df = filtered_df.sort_values('Date')
        st.line_chart(filtered_df[['Date', 'Weekly_Sales']].set_index('Date'))
    else:
        st.line_chart(filtered_df[['Weekly_Sales']])
