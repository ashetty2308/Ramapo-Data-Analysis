"""
    - RCNJ Data Analytics Internship Project 1
    - Professor Osei Tweneboah
    - Adit Shetty
    - Due: July 30th, 2021
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the Salaries.csv file using pandas
salaryData = pd.read_csv('Salaries.csv')
#print(salaryData)

'''
    1ai) What is the dimension of the dataset?
        - Answer: 78 rows x 6 columns. This value was returned when I read the data frame.        
'''

'''
    1aii) How many categorical and numerical variables are there in the data set? There are 
        - There are 3 categorical variables (Rank, Discipline, Sex) --> These are "yes/no" variables, so it is categorical
        - There are 3 numerical variables (PhD, Service, Salary) --> These answers have variation with numbers, so it is numerical. 
'''

# Seeing the number of null/empty values in the df
#print(salaryData.isnull().sum())
'''
    1bi) Tells me that there are 2 missing values in the 'rank' column, and 1 missing value in the 'salary' column
'''

#1bii)
salaryData['rank'].fillna('AsstProf',inplace=True)
salaryData['salary'].fillna(88000,inplace=True)

#confirming no more missing values
#print(salaryData.isnull().sum())

#creating a new CSV to just double check the values are present
salaryData.to_csv('newCsvSalary.csv')

#1biii)

#print(salaryData.nlargest(5,['salary']))
'''
    rank discipline  phd  service     sex    salary
0   Prof          B   56       49    Male  186960.0
13  Prof          B   35       33    Male  162200.0
72  Prof          B   24       15  Female  161101.0
27  Prof          A   45       43    Male  155865.0
31  Prof          B   22       21    Male  155750.0
'''

maleCombinedSalary = salaryData.loc[salaryData['sex'] == "Male", "salary"].sum()
femaleCombinedSalary = salaryData.loc[salaryData['sex'] == "Female", "salary"].sum()

professorsCombinedSalary = salaryData.loc[salaryData['rank'] == "Prof", "salary"].sum()
associateProfessorsCombinedSalary = salaryData.loc[salaryData['rank'] == "AssocProf", "salary"].sum()
assistantProfessorCombinedSalary = salaryData.loc[salaryData['rank'] == "AsstProf", "salary"].sum()

#print("male: ", maleCombinedSalary)
#print("female: ", femaleCombinedSalary)

#print("prof: ", professorsCombinedSalary)
#print("assistant prof: ", assistantProfessorCombinedSalary)
#print("associate prof: ", associateProfessorsCombinedSalary)

#2
'''
gender = ['Male','Female']
salary = [maleCombinedSalary,femaleCombinedSalary]
plt.bar(gender,salary)
plt.show()
'''

#3
'''
typeOfProfessor = ['Professor','Assistant','Associate']
salary = [professorsCombinedSalary,assistantProfessorCombinedSalary, associateProfessorsCombinedSalary]
plt.bar(typeOfProfessor, salary)
plt.show()
'''

#4

#Plotting each professor type with each sex (e.g; Male Asst. Prof vs Female Asst. Prof) to see differences

femaleProfessor = salaryData.loc[(salaryData["sex"] == "Female") & (salaryData["rank"] == "Prof"), "salary"].sum()
maleProfessor = salaryData.loc[(salaryData["sex"] == "Male") & (salaryData["rank"] == "Prof"), "salary"].sum()

femaleAsstProf = salaryData.loc[(salaryData["sex"] == "Female") & (salaryData["rank"] == "AsstProf"), "salary"].sum()
maleAsstProf = salaryData.loc[(salaryData["sex"] == "Male") & (salaryData["rank"] == "AsstProf"), "salary"].sum()

femaleAssocProf = salaryData.loc[(salaryData["sex"] == "Female") & (salaryData["rank"] == "AssocProf"), "salary"].sum()
maleAssocProf = salaryData.loc[(salaryData["sex"] == "Male") & (salaryData["rank"] == "AssocProf"), "salary"].sum()


categories = ["Professors", "Asst. Professors", "Assoc. Professors"]
femaleSalaries = [femaleProfessor, femaleAsstProf, femaleAssocProf]
maleSalaries = [maleProfessor, maleAsstProf, maleAssocProf]\


#print(femaleSalaries)
#print(maleSalaries)

b1 = np.arange(len(categories))
b2 = [i+0.3 for i in b1]

plt.bar(b1, femaleSalaries, 0.3, label="Female")
plt.bar(b2, maleSalaries, 0.3, label="Male")

plt.xlabel("Professor Type & Gender")
plt.ylabel("Salary")
plt.title("Professor Type vs Sex")
plt.xticks(b1, categories)
plt.legend()
plt.show()
plt.plot()