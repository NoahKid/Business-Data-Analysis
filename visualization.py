import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


conn = sqlite3.connect("business.db")
df = pd.read_sql_query("SELECT * FROM sales_data", conn)
conn.close()


df["date"] = pd.to_datetime(df["date"])


plt.figure(figsize=(10, 5))
sns.lineplot(x="date", y="revenue", data=df, marker="o")
plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()
