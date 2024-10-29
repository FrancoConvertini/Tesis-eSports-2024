import cv2
import mediapipe as mp 
import csv
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Cargar datos
df = pd.read_csv('coords.csv')
X = df.drop('class', axis=1) # features
y = df['class'] # target value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# Definir pipelines
pipelines = {
    'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
}

# Entrenar y evaluar modelos
fit_models = {}
for algo, pipeline in pipelines.items():
    model = pipeline.fit(X_train, y_train)
    fit_models[algo] = model
    # Validación cruzada
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"{algo} Cross-Validation Scores: {cv_scores}")
    print(f"{algo} Average CV Score: {np.mean(cv_scores)}")

# Evaluar modelos en el conjunto de prueba
for algo, model in fit_models.items():
    yhat = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, yhat)}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, yhat))
    print("Classification Report:")
    print(classification_report(y_test, yhat))

