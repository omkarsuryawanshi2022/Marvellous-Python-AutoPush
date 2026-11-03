#---------------------------------------
#  Deep learning pipline
#---------------------------------------
#1  Read the data from csv
#2  Data Anylysis()EDA
#3  preprocessing
#4  train test split
#5  feature Scalling
#6  FNN Model Training
# 7 model Evoluation
# 8  grapical reepresentaion ghari karne ahe
# 9 model preserve
# 10   model loading and preserve
# 11 Test unseen data
# ------------------------------------------

import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


#-------------------------
# Step 1  Read the data from csv
#------------------------

print("Step 1 Read the data from csv")

data = pd.read_csv("placement_data.csv")

print("Complete dataset:")

print(data)

#-------------------------
# Step 2  Data Anylysis(EDA)
#------------------------

print("Data Anylysis(EDA)")

print("Fisrt 5 rows")

print(data.head())

print("Columns names:")
print(data.columns)

print("Shape of dataset:")
print(data.shape)

print("stattistical summery:")
print(data.describe())

#-------------------------
# Step 3  preprocessing
#------------------------

print(" step 3 preprocessing")

X =  data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y =  data['Placed']

print("input features:")
print(X.head())

print("Target :")
print(Y.head())

#-------------------------
# Step 4  train test split
#------------------------

print(" Step 4 train test split")

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42
)

print("Training input Shape:",X_train.shape)
print("Testing input Shape:",X_test.shape)
print("Training output Shape:",Y_train.shape)
print("Testing output Shape:",Y_test.shape)

#-------------------------
# Step 5  feature Scalling
#------------------------

print("Step 5  feature Scalling")
scalar = StandardScaler()

X_train_scalled = scalar.fit_transform(X_train)
X_test_scaled =  scalar.fit_transform(X_test)

print("Scalled training data:")

print(X_train_scalled[:5])

#-------------------------
# Step 6  FNN Model Training
#------------------------

print(" step 6 FNN Model Training")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42

)

print(model)

print("Train the model")

model.fit(X_train_scalled,Y_train)

print("Model training completed")

#-------------------------
# Step 7  model Evoluation
#------------------------

print("Step 7  model Evoluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)

print("Acccuracy is :",accuracy)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusation matrix :",cm)

print("Predict the probabilaty:")

Y_probaility = model.predict_proba(X_test_scaled)

print(Y_probaility[:5])

joblib.dump(model,'placement_fnn_model.pkl')

joblib.dump(scalar,"placement_scalar.pkl")

print("Model and scalar gets dump Sucessfully")



#-------------------------
# Step 8  grapical reepresentaion ghari karne ahe
#------------------------

#-------------------------
# Step 9  model preserve
#------------------------

print("step 9 model preserve")

#-------------------------
# Step 10 loading and preserve
#------------------------

print("Step 10 loading and preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_scalar.pkl")

print("model gets loaded sucessfully")


#-------------------------
# Step 11 Test unseen data
# applitute  :    70
# coding      :   75
# communication : 80
# acadamic :    : 85
# internship    : 1
#------------------------

new_student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probability = loaded_model.predict_proba(new_student_scaled)

print("New student data:")

print(new_student)

print("Prediction probability:",new_probability)

if new_prediction[0] == 1:
    print("prediction : placed")
else:
    print("prediction : not placed")












