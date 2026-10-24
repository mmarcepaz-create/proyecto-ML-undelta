**Glosario ML Proyecto  “Entrenando-2-modelos”**

Un glosario técnico al final del informe o presentación es una excelente estrategia académica: demuestra dominio del lenguaje formal de Machine Learning y ayuda a clarificar conceptos complejos ante la cátedra.

A continuación tienes el **Glosario Técnico de Machine Learning**, organizado alfabéticamente y enriquecido con términos clave de tu lista y conceptos adicionales altamente relevantes para su trabajo.

### **Glosario de Términos Técnicos (TP Machine Learning)**

* **Adam (*Adaptive Moment Estimation*):** Algoritmo optimizador basado en el descenso de gradiente estocástico. Ajusta la tasa de aprendizaje para cada parámetro de forma adaptativa, logrando un entrenamiento más eficiente en redes neuronales.  
* **Capa (*Layer*):** Estructura fundamental de una red neuronal organizada por grupos de neuronas. Se dividen en capas de entrada (*input layer*), capas ocultas (*hidden layers*) y capas de salida (*output layer*).  
* **Capa Oculta (*Hidden Layer*):** Capas intermedias ubicadas entre la entrada y la salida de la red. Se encargan de transformar las características de entrada mediante combinaciones lineales y funciones de activación no lineales.  
* **Convergencia de la Función de Pérdida (*Loss Function Convergence*):** Estado en el cual el error global del modelo (*Cross-Entropy* en clasificación) deja de disminuir significativamente, indicando que la optimización ha alcanzado una solución óptima o local.  
* **Convergencia Fluida y Estable:** Comportamiento ideal durante el entrenamiento donde la pérdida disminuye de manera progresiva y sostenida sin oscilaciones bruscas o desvíos numéricos.  
* **Desvanecimiento del Gradiente (*Vanishing Gradient*):** Problema numérico que ocurre durante la retropropagación (*backpropagation*) cuando las derivadas del error se vuelven extremadamente pequeñas hacia las primeras capas, congelando el aprendizaje. Ocurre frecuentemente al usar funciones como la Sigmoide o Tanh.  
* **Ensamble de Árboles de Decisión:** Técnica de Machine Learning (*como Random Forest*) que combina las predicciones de múltiples árboles entrenados de manera independiente para obtener un resultado final más robusto y reducir el varianza (*overfitting*).  
* **Esquema de Embudo (*Funnel Architecture*):** Diseño de red neuronal donde el número de neuronas por capa oculta disminuye gradualmente (ej. $784\rightarrow 128\rightarrow 64\rightarrow 10$), forzando a la red a condensar la información y extraer abstracciones de mayor nivel.  
* **Estimadores (*Estimators / n\_estimators*):** Número de árboles de decisión individuales creados dentro del ensamble de Random Forest.  
* **Función de Activación (ReLU, Sigmoide, Tanh):** Operación matemática no lineal aplicada a la salida de cada neurona:  
  * **ReLU (*Rectified Linear Unit*):** Devuelve $0$ si la entrada es negativa y la misma entrada si es positiva. Previene el desvanecimiento del gradiente y es computacionalmente muy rápida.  
  * **Sigmoide:** Comprime las salidas al rango $(0,1)$, ideal para probabilidades binarias.  
  * **Tanh (*Tangente Hiperbólica*):** Comprime las salidas al rango $(-1,1)$, centrada en cero.  
* **Garantizar Reproducibilidad:** Práctica que asegura que al volver a ejecutar el código con los mismos datos y parámetros se obtengan exactamente los mismos resultados.  
* **Paralelización Multihilo (n\_jobs=-1):** Capacidad del sistema para distribuir las tareas de entrenamiento en todos los núcleos lógicos disponibles del procesador CPU, reduciendo el tiempo de ejecución.  
* **PCA (*Principal Component Analysis* / Análisis de Componentes Principales):** Técnica de reducción de dimensionalidad no supervisada que transforma un conjunto de variables correlacionadas (como 784 píxeles) en un número menor de variables no correlacionadas llamadas componentes principales, preservando la mayor varianza posible.  
* **Precisión Marginal:** Ganancia decreciente de rendimiento al aumentar la complejidad del modelo (por ejemplo, agregar más árboles o neuronas aporta mejoras insignificantes al *accuracy* mientras aumenta el costo de cómputo).  
* **Red Neuronal Densa (*Fully Connected / Dense Network*):** Arquitectura donde cada neurona de una capa está conectada a absolutamente todas las neuronas de la capa anterior.  
* **Semilla Aleatoria (*Random State / Seed*):** Número fijado como referencia para inicializar el generador de números pseudoaleatorios del sistema, asegurando que la división de datos o inicialización de pesos sea siempre idéntica.  
* **Tolerancia de Parada Rápida (tol):** Criterio de parada (*stopping criteria*) que finaliza el entrenamiento prematuramente si la mejora en la función de pérdida entre épocas consecutivas es menor al valor umbral fijado, evitando ejecuciones infinitas.


### **Términos adicionales recomendados para sumar:**

1. **Overfitting (Sobreajuste):** Ocurre cuando el modelo memoriza el conjunto de entrenamiento y pierde capacidad de generalizar con datos nuevos de testeo.  
2. **Underfitting (Subajuste):** Ocurre cuando el modelo es demasiado simple (como una regresión logística en datos complejos) y no logra capturar los patrones ni en entrenamiento ni en prueba.  
3. **Mini-batch:** Subconjunto pequeño de muestras cargadas secuencialmente en memoria para actualizar los pesos de la red neuronal en cada paso de gradiente.

