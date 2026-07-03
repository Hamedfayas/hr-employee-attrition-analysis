import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Raw_HR-Employee-Attrition.csv")
print(df.head(10))
df.info()
print(df.shape)
print(df.describe())
print(df.isnull().sum())
df.columns = [c.strip() for c in df.columns]
print(df.duplicated().sum())
df=df.drop(columns=['EmployeeCount','Over18','StandardHours'],errors='ignore')

print(df["Attrition"])
df["Attritionflag"]=df["Attrition"].map({"Yes":1,"No":0})
print(df["Attritionflag"])
print(df["OverTime"])
df["OverTimeflag"] = df["OverTime"].map({"Yes":1,"No":0})
print(df["OverTimeflag"])
df["Manager_tenure_gap"] = df["YearsAtCompany"] - df["YearsWithCurrManager"].clip(lower=0)
print(df.head(10))
print(df.isnull().sum().sort_values(ascending=False).head(10))
print(df.head())

summary=pd.DataFrame({
    "metrics":[
        "row",
        "columns",
        "attrition_rate_pct",
        "avg_age",
        "avg_monthly_income",
        "avg_years_at_company"
    ],
    "values":[
        len(df),
        df.shape[1],
        round(df["Attritionflag"].mean()*100, 2),
        round(df["Age"].mean(),2),
        round(df["MonthlyIncome"].mean(),2),
        round(df["YearsAtCompany"].mean(),2)
    ]
})
print(summary)

df.to_csv("Hr_Employ_attrition_cleaned.csv",index=False)

plt.figure(figsize=(7,5))
sns.boxplot(data=df,x="Attrition",y="MonthlyIncome",order=["No","Yes"])
plt.title("Monthly income by attrition")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
department_attrition = df.groupby("Department", as_index=False)["Attritionflag"].mean()
sns.barplot(data=department_attrition, x="Department", y="Attritionflag")
plt.title("Attrition Rate by Department")
plt.ylabel("Attrition Rate")
plt.tight_layout()
plt.show()
print(df["OverTimeflag"].sum())
