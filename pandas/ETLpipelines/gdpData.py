#1. This task helps you in understanding the ETL operation in a simple way.
    #a. Extract (Python/Pandas):
        #i. Read a CSV file to read Nepal’s GDP data
    #b. Transform (Pandas/Apply/Melt):
        #i. Select data for Nepal only
        #ii. Unpivot the data
        #iii. Format the yearly GDP data with 2 decimal places
        #iv. Prepare the data ready to load into database
    #c. Load (Python/PostgreSQL):
        #i. Load the clean data to database with suitable table name and
            #column names. Prepare a schema diagram (ER diagram) for the
            #data structure of your choice.
    #d. Visualize (Matplotlib):
        #i. Prepare a line-chart to visualize the GDP trend of Nepal.

import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

#reading the csv files
gdp_datewise = pd.read_csv("/home/subodh/workingDirectory/internship/pandas/ETLpipelines/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_76261.csv", skiprows=4)
metadata_income_groups = pd.read_csv("/home/subodh/workingDirectory/internship/pandas/ETLpipelines/Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_76261.csv")
metadata_indicator_name = pd.read_csv("/home/subodh/workingDirectory/internship/pandas/ETLpipelines/Metadata_Indicator_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_76261.csv")

#select the data for nepal only
nepal_data = gdp_datewise[gdp_datewise["Country Code"] == "NPL"]
nepal_data = nepal_data.drop(columns=["Unnamed: 68"])

#unpivot the data
nepal_data_melted = nepal_data.melt(id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"], var_name = "Year", value_name="GDP (current US$)")
nepal_data_melted["Year"] = nepal_data_melted["Year"].astype(int)
nepal_data_melted["Year"] = nepal_data_melted["Year"].apply(lambda x: round(x,2) if pd.notnull(x) else None)

#formatting the yearly gdp data with 2 decimal places
nepal_data_melted["GDP (current US$)"] = nepal_data_melted["GDP (current US$)"].apply(lambda x: "{:.2f}".format(x) if pd.notnull(x) else None)

#connecting to the database
engine = create_engine('postgresql+psycopg2://subodh:password@localhost:5432/gdp_data')

connection = psycopg2.connect(
    dbname="gdp_data",
    user="subodh",
    password="password",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM nepal_gdp LIMIT 5")
result = cursor.fetchall()
cursor.close()
connection.close()

# plotting the data in matplotlib
nepal_data_melted["GDP (current US$)"] = pd.to_numeric(nepal_data_melted["GDP (current US$)"])

nepal_data_melted = nepal_data_melted.dropna(subset=["GDP (current US$)"])

plt.figure(figsize=(10,6))  # Use a valid figure size (width, height)
plt.plot(nepal_data_melted['Year'], nepal_data_melted['GDP (current US$)'], marker='o', color='b', label='GDP (current US$)')

plt.title("GDP trend of Nepal", fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel("GDP (current US$)", fontsize=12)

plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
