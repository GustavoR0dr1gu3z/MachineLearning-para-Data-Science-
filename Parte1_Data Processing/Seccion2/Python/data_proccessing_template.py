#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:24:35 2020

@author: gustavo
"""

# Plantilla de Pre Procesado
#-----------------------------------------IMPORTAR LIBRERÍAS-------------------
# ¿Cómo importar las librerías?

import numpy as np
import matplotlib as plt
import pandas as pd
# Libreria para carga y manipulacion de datos "Pandas"
#-----------------------------------------IMPORTAR DATASETS--------------------
# Importar el dataset
dataset = pd.read_csv('Data.csv')

# Variable X = Variables independientes 
# Variable Y = Variables dependientes

# iloc = Localizar elementos filas y columnas de un dataset por posicion
# Todas las columnas excepto la última
X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 3].values

#-----------------------------------------TRATAMIENTO DE NA--------------------
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose=0) 
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])


#-----------------------------------------CODIFICAR DATOS CATEGORICOS----------
# Codificar datos categóricos
# Convertir string a int
#OneHotEncoder libreria para variables Dummyu
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
le_X = preprocessing.LabelEncoder()
#Codifica esas columnas

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'),[0])],
    remainder ="passthrough"
    )
X = np.array(ct.fit_transform(X), dtype = np.float)


label_encoder_y = preprocessing.LabelEncoder()
y = label_encoder_y.fit_transform(y)

#-----------------------------------------DIVIDIR DATASET EN CONJUNTOS---------
from sklearn.model_selection import train_test_split
#train_test_split <---> divide el dataset
#20% para validar, para el test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 0)

#-------------------------------------------ESCALADO DE VARIABLES--------------
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

















 

