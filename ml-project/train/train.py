# Importar las bibliotecas necesarias
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import joblib

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()  # Cargar el conjunto de datos Iris
X = iris.data  # Características (características de las flores)
y = iris.target  # Etiquetas (clases de flores)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)  # Dividir los datos en conjuntos de entrenamiento (75%) y prueba (25%)

# Elegir un modelo multiclase
model = linear_model.LogisticRegression(multi_class="multinomial")  # Crear un modelo de regresión logística multinomial

# Entrenar el modelo
model.fit(X_train, y_train)  # Entrenar el modelo con los datos de entrenamiento

# Guardar el modelo usando joblib
joblib.dump(model, 'iris_model.joblib')  # Guardar el modelo entrenado en un archivo
print("El modelo se guardó correctamente")