# Plantilla para el Pre Procesado de Datos

# Importar el dataset

dataset = read.csv('Data.csv')


#-------------------------------------Tratamiento de los valores NA
#evaluar si el valor es o no es NA
#condicion, si lo es, si no lo es
#ave 
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

#-------------------------------Codificar las variables categoricas

dataset$Country = factor(dataset$Country, 
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased, 
                         levels = c("No", "Yes"),
                         labels = c(0,1))
str(dataset)
#-------------------------------------DIVIDOR CONJUNTOS DEL DATASET
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set  = subset(dataset, split == FALSE)

#-----------------------------------------------ESCALADO DE VALORES
training_set[,2:3] =scale(training_set[,2:3])
testing_Set[,2:3] = scale(testing_set[,2:3]