# Group Assingment 1

# YAP JIA CONG 276882
# LOH MAN PIN s287504



# Clearing the Screen
import os
os.system('cls')

# Import pandas and matpotlib
import pandas as pd
import matplotlib.pyplot as plt


# Retrieve data from https://www.bnm.gov.my/publications/mhs
# Monthly Highlights & Statistics October 2023
# 4.7.14 General Insurance: Earned Premium Income
url = r"C:\Users\yapji\OneDrive\Documents\GitHub\SQIT-3073\Group_Assignment_1\4.7.14_cleaning.xlsx"

# Read data from the first sheet
df_1 = pd.read_excel(url, sheet_name=0)
print(df_1)

# Read data from the second sheet
df_2 = pd.read_excel(url, sheet_name=1)
print(df_2)

# Read data from the third sheet
df_3 = pd.read_excel(url, sheet_name=2)
print(df_3)



# Create a bar chart for the first sheet (df_1)
# Customize this based on your data and requirements

plt.figure(1,figsize=(10,6))
plt.plot(df_1['Period'],df_1['Marine, Aviation and Transit'])
plt.plot(df_1['Period'],df_1['Contractors All Risk and Engineering '])
plt.plot(df_1['Period'],df_1['Fire'])
plt.plot(df_1['Period'],df_1['Medical and Health, and Personal Accident'])
plt.plot(df_1['Period'],df_1['Motor'])
plt.plot(df_1['Period'],df_1['Liability'])
plt.plot(df_1['Period'],df_1['Workmens Compensation and Employers Liability'])
plt.plot(df_1['Period'],df_1['Miscellaneous'])

# Customize the plot
plt.xlabel('Period',color = 'black')
plt.ylabel('RM million',color = 'black')
plt.title('General Insurance: Earned Premium Income(Business within Malaysia)',color = 'blue')
line_1 = plt.plot(df_1['Period'],df_1['Marine, Aviation and Transit'],label ='Marine, Aviation and Transit',color='red',marker ='*')
line_2 = plt.plot(df_1['Period'],df_1['Contractors All Risk and Engineering '],label ='Contractors All Risk and Engineering',color='blue',marker ='*')
line_3 = plt.plot(df_1['Period'],df_1['Fire'],label ='Fire',color='green',marker ='*')
line_4 = plt.plot(df_1['Period'],df_1['Medical and Health, and Personal Accident'],label ='Medical and Health, and Personal Accident',color='orange',marker ='*')
line_5 = plt.plot(df_1['Period'],df_1['Motor'],label ='Motor',color='purple',marker ='*')
line_6 = plt.plot(df_1['Period'],df_1['Liability'],label ='Liability',color='pink',marker ='*')
line_7 = plt.plot(df_1['Period'],df_1['Workmens Compensation and Employers Liability'],label ='Workmens Compensation and Employers Liability',color='yellow',marker ='*')
line_8 = plt.plot(df_1['Period'],df_1['Miscellaneous'],label ='Miscellaneous',color='brown',marker ='*')
plt.legend()


# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Show the plot
plt.grid()
plt.show()


# Create a bar chart for the second sheet (df_2)
# Customize this based on your data and requirements

plt.figure(2,figsize=(10,6))
plt.plot(df_2['Period'],df_2['Marine, Aviation and Transit'])
plt.plot(df_2['Period'],df_2['Contractors All Risk and Engineering '])
plt.plot(df_2['Period'],df_2['Fire '])
plt.plot(df_2['Period'],df_2['Medical and Health, and Personal Accident'])
plt.plot(df_2['Period'],df_2['Motor'])
plt.plot(df_2['Period'],df_2['Liability'])
plt.plot(df_2['Period'],df_2['Workmens Compensation and Employers Liability'])
plt.plot(df_2['Period'],df_2['Miscellaneous'])

# Customize the plot
plt.xlabel('Period',color = 'black')
plt.ylabel('RM million',color = 'black')
plt.title('General Insurance: Earned Premium Income(Global Business)',color = 'blue')
line_1 = plt.plot(df_2['Period'],df_2['Marine, Aviation and Transit'],label ='Marine, Aviation and Transit',color='red',marker ='*')
line_2 = plt.plot(df_2['Period'],df_2['Contractors All Risk and Engineering '],label ='Contractors All Risk and Engineering',color='blue',marker ='*')
line_3 = plt.plot(df_2['Period'],df_2['Fire '],label ='Fire',color='green',marker ='*')
line_4 = plt.plot(df_2['Period'],df_2['Medical and Health, and Personal Accident'],label ='Medical and Health, and Personal Accident',color='orange',marker ='*')
line_5 = plt.plot(df_2['Period'],df_2['Motor'],label ='Motor',color='purple',marker ='*')
line_6 = plt.plot(df_2['Period'],df_2['Liability'],label ='Liability',color='pink',marker ='*')
line_7 = plt.plot(df_2['Period'],df_2['Workmens Compensation and Employers Liability'],label ='Workmens Compensation and Employers Liability',color='yellow',marker ='*')
line_8 = plt.plot(df_2['Period'],df_2['Miscellaneous'],label ='Miscellaneous',color='brown',marker ='*')
plt.legend()


# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Show the plot
plt.grid()
plt.show()


# Create a bar chart for the third sheet (df_3)
# Customize this based on your data and requirements

plt.figure(3,figsize=(10,6))
plt.plot(df_3['Period'],df_3['Marine, Aviation and Transit'])
plt.plot(df_3['Period'],df_3['Contractors All Risk and Engineering '])
plt.plot(df_3['Period'],df_3['Fire'])
plt.plot(df_3['Period'],df_3['Medical and Health, and Personal Accident'])
plt.plot(df_3['Period'],df_3['Motor'])
plt.plot(df_3['Period'],df_3['Liability'])
plt.plot(df_3['Period'],df_3['Workmens Compensation and Employers Liability'])
plt.plot(df_3['Period'],df_3['Miscellaneous'])

# Customize the plot
plt.xlabel('Period',color = 'black')
plt.ylabel('RM million',color = 'black')
plt.title('General Insurance: Earned Premium Income(Total Business)',color = 'blue')
line_1 = plt.plot(df_3['Period'],df_3['Marine, Aviation and Transit'],label ='Marine, Aviation and Transit',color='red',marker ='*')
line_2 = plt.plot(df_3['Period'],df_3['Contractors All Risk and Engineering '],label ='Contractors All Risk and Engineering',color='blue',marker ='*')
line_3 = plt.plot(df_3['Period'],df_3['Fire'],label ='Fire',color='green',marker ='*')
line_4 = plt.plot(df_3['Period'],df_3['Medical and Health, and Personal Accident'],label ='Medical and Health, and Personal Accident',color='orange',marker ='*')
line_5 = plt.plot(df_3['Period'],df_3['Motor'],label ='Motor',color='purple',marker ='*')
line_6 = plt.plot(df_3['Period'],df_3['Liability'],label ='Liability',color='pink',marker ='*')
line_7 = plt.plot(df_3['Period'],df_3['Workmens Compensation and Employers Liability'],label ='Workmens Compensation and Employers Liability',color='yellow',marker ='*')
line_8 = plt.plot(df_3['Period'],df_3['Miscellaneous'],label ='Miscellaneous',color='brown',marker ='*')
plt.legend()


# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Show the plot
plt.grid()
plt.show()