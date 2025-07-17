import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\harsh\Downloads\shopping_trends.csv")
df.head()
df.describe()
df.info()

df.dtypes

sns.displot(x=df.Age, kde=True, bins=28)

def agegrp(data):
    if data < 20:
        return "below 20"
    elif (data >= 20) & (data < 30):
        return "20-30"
    elif (data >= 30) & (data < 40):
        return "30-40"
    elif (data >= 40) & (data < 50):
        return "40-50"
    elif (data >= 50) & (data < 60):
        return "50-60"
    elif (data >= 60) & (data <= 70):
        return "60-70"
    else:
        return np.nan

d1 = df.copy()
d1["age group"] = d1.Age.apply(agegrp)
d1

sns.barplot(x=d1["age group"], y=d1.index)

sns.countplot(x=d1.Gender)

plt.figure(figsize=(10, 6))
sns.countplot(x=d1.Location)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x=d1.Category, hue=d1.Gender)

meanprice = d1.groupby("Category")["Purchase Amount (USD)"].mean()
meanprice

totalpurchase = d1.groupby("Category")["Purchase Amount (USD)"].sum()
totalpurchase

sns.countplot(x=d1["Frequency of Purchases"])
plt.xticks(rotation=35)
plt.show()

sns.countplot(x=d1["Payment Method"])
plt.xticks(rotation=35)
plt.show()

productcount = d1["Item Purchased"].value_counts()
productcount

sns.countplot(x=d1.Size)

sns.countplot(x=d1.Color)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x=d1.Season)

d1["Frequency of Purchases"].unique().tolist()

fortnight = d1[d1["Frequency of Purchases"] == "Fortnightly"]
weekly = d1[d1["Frequency of Purchases"] == "Weekly"]
annually = d1[d1["Frequency of Purchases"] == "Annually"]
quarterly = d1[d1["Frequency of Purchases"] == "Quarterly"]
week2 = d1[d1["Frequency of Purchases"] == "Bi-Weekly"]
monthly = d1[d1["Frequency of Purchases"] == "Monthly"]
month3 = d1[d1["Frequency of Purchases"] == "Every 3 Months"]

def revrating(data):
    if data <= 2:
        return "below 2"
    elif (data > 2) & (data <= 3):
        return "2-3"
    elif (data > 3) & (data <= 4):
        return "3-4"
    elif (data > 4) & (data <= 5):
        return "4-5"
    else:
        return np.nan

d1["rating group"] = d1["Review Rating"].apply(revrating)

subscribed = d1[d1["Subscription Status"] == "Yes"]

sns.countplot(x=subscribed.Gender)

sns.countplot(x=subscribed["Item Purchased"])
plt.xticks(rotation=90)
plt.show()

sns.countplot(x=subscribed["Payment Method"])
plt.xticks(rotation=45)
plt.show()

sns.countplot(x=subscribed["Discount Applied"])

sns.countplot(x=subscribed["Promo Code Used"])

sns.countplot(x=subscribed["age group"])

sns.countplot(x=subscribed["rating group"])

sns.displot(x=d1["Review Rating"])

revcount = d1.groupby("rating group")["Category"].value_counts().reset_index(name="Count")
revcount

revcount = d1.groupby("Category")["Review Rating"].mean()
revcount.sort_values()

discount_impact = d1.groupby("Discount Applied")["Purchase Amount (USD)"].mean()
discount_impact

promo_impact = d1.groupby("Promo Code Used")["Purchase Amount (USD)"].mean()
promo_impact

def discountencode(data):
    if data == "Yes":
        return 1
    else:
        return 0

d1["discount"] = d1["Discount Applied"].apply(discountencode)

mapping = {
    "Weekly": 4,
    "Fortnightly": 2,
    "Monthly": 1,
    "Quarterly": 0.25,
    "Annually": 0.083
}

d1["Frequency"] = d1["Frequency of Purchases"].map(mapping)
d1

correlation = d1[["discount", "Frequency"]].corr()
correlation

sns.heatmap(correlation, annot=True)

sns.countplot(x=d1["Shipping Type"])
plt.xticks(rotation=45)
plt.show()

shipping_cat = d1.groupby(["Category", "Shipping Type"]).size()
shipping_cat.sort_values()

ship_rate = d1.groupby("Shipping Type")["Review Rating"].mean()
ship_rate.sort_values()

seasonal_behavior = d1.groupby("Season")["Purchase Amount (USD)"].mean()
seasonal_behavior

season_cat = d1.groupby(["Season", "Category"]).size()
season_cat.sort_values()

numerical_data = d1[["Age", "Purchase Amount (USD)", "Review Rating", "Previous Purchases"]]
correlation_matrix = numerical_data.corr()
correlation_matrix

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.xticks(rotation=15)
plt.show()
