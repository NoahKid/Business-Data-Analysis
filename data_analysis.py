import sqlite3
import pandas as pd


conn = sqlite3.connect("business.db")


df = pd.read_sql_query("SELECT * FROM sales_data", conn)
conn.close()


print(df.head())


print("Total Revenue:", df["revenue"].sum())
print("Average Quantity Sold:", df["quantity"].mean())
print("Most Sold Category:", df.groupby("category")["quantity"].sum().idxmax())
