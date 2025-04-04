import pandas as pd
import numpy as np
import pickle as pk
import matplotlib.pyplot as plt


df = pd.read_csv("loan_prediction.csv")

# this deletes the values in the "Loan_ID" column
df.drop(['Loan_ID'], axis=1, inplace=True)

# this fills up the null or empty columns in the dataset with the mean or mode of the 
# specified dataset column
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Years_of_Establishment'].fillna(df['Years_of_Establishment'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)

# this converts categorical field or non-numeric column values into numeric integer values
from sklearn.preprocessing import OrdinalEncoder
ord_encoder = OrdinalEncoder()
df[['Gender','Married','Years_of_Establishment','Education','Self_Employed','Property_Area',
    'Loan_Status']] = ord_encoder.fit_transform(df[['Gender','Married','Years_of_Establishment',
                                                    'Education','Self_Employed','Property_Area',
                                                    'Loan_Status']]).astype('int')

# this prepares the X and y datasets
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# This split the selected dataset columns X and y into train and test group. test_size = 0.2 
# means the "test" group should only be 20% of the selected datasets. random_state = 0 means
# the selected train and test dataset should be the same across different execution of the program.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=10000,C=1)
model.fit(X_train, y_train)

#save the above model as "trained_prediction_model.pkl" using the pickle (pk) module
pk.dump(model, open('trained_prediction_model.pkl', 'wb'))
