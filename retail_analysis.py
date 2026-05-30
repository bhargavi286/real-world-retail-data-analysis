import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("SampleSuperstore.csv")


print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nStatistical Summary:")
print(df.describe())


print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())


plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.show()


plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Profit", data=df)
plt.title("Profit by Category")
plt.show()


plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Sales", data=df)
plt.title("Sales by Region")
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(
    df[['Sales', 'Quantity', 'Discount', 'Profit']].corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()