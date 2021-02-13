#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:52:50 2020

@author: gustavo
"""
import numpy as np
import matplotlib as plt
import pandas as pd
# Libreria para carga y manipulacion de datos "Pandas"
#-----------------------------------------IMPORTAR DATASETS--------------------
# Importar el dataset
dataset = pd.read_csv('Salary_Data.csv')

# Variable X = Variables independientes 
# Variable Y = Variables dependientes

# iloc = Localizar elementos filas y columnas de un dataset por posicion
# Todas las columnas excepto la última
X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 1].values


#-----------------------------------------DIVIDIR DATASET EN CONJUNTOS---------
from sklearn.model_selection import train_test_split
#train_test_split <---> divide el dataset
#20% para validar, para el test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, 
                                                    random_state = 0)

#-------------------------------------------ESCALADO DE VARIABLES--------------
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

# Crear modelo de regresion lineal simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression


regression = LinearRegression()
regression.fit(X_train, y_train)
  

# -----------------------------------------Predecdir el conjunto de Test 

# Vector de datos
y_pred = regression.predict(X_test)


# ----------------------------Visualizar los resultados de entrenamiento
# EjeX, ejeY
plt.scatter(X_train, y_train, color ="red")

# Recta de regresion
plt.plot(X_train, regression.predict(X_train), color = "blue")













