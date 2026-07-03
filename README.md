HR Employee Attrition Analysis

# About the Project

I built this project to practice data cleaning, analysis, and dashboard creation using Python and Power BI. The main objective was to understand why employees leave a company and present those insights in a simple, interactive dashboard.

The project starts with cleaning the raw HR dataset in Python, followed by creating a Power BI dashboard that highlights important HR metrics and trends.

# Tools Used:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Power BI

# Project Files


HR-Employee-Attrition-Analysis/
│
├── data/
│   ├── Raw_HR-Employee-Attrition.csv
│   └── Hr_Employ_attrition_cleaned.csv
│
├── scripts/
│   └── hr-employ-attrition.py
│
├── dashboard/
│   └── Hr_Employee_attrition_Dashboard.pbix
│
├── images/
├── README.md
└── requirements.txt


# What I Did

* Cleaned the raw dataset.
* Removed unnecessary columns.
* Checked for missing values and duplicates.
* Created new columns such as Attrition Flag, OverTime Flag, and Manager Tenure Gap.
* Performed basic exploratory data analysis using Python.
* Built an interactive dashboard in Power BI.

# Dashboard

The dashboard includes:

* Total Employees
* Attrition Count
* Attrition Rate
* Average Age
* Average Monthly Income
* Average Years at Company
* Department-wise Attrition
* Job Role Analysis
* Gender Distribution
* Overtime Analysis


# What I Learned

Working on this project helped me improve my understanding of:

* Data cleaning with Pandas
* Feature engineering
* Exploratory data analysis
* Creating meaningful KPIs
* Building interactive dashboards in Power BI
* Organizing a complete analytics project for GitHub

# How to Run

1. Clone this repository.
2. Install the required Python libraries.


pip install -r requirements.txt


3. Run the preprocessing script.


python scripts/hr-employ-attrition.py


4. Open the .pbix file in Power BI Desktop to explore the dashboard.

# Dataset

This project uses the IBM HR Analytics Employee Attrition dataset, which is commonly used for learning HR analytics and employee attrition analysis.

# Author

Hamed Fayas M

BCA Graduate specializing in AI, Machine Learning, Robotics & IoT. I'm passionate about Data Analytics, Python, SQL, Power BI, and Machine Learning, and I'm building projects to strengthen my portfolio and prepare for a career in data analytics.
