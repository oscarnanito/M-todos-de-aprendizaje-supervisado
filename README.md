# M-todos-de-aprendizaje-supervisado

## Descripción

Este proyecto forma parte de una actividad académica de inteligencia artificial aplicada al transporte público, esto con el docente Joaquin Sanchez

En una fase anterior, se desarrolló un sistema de ruteo utilizando el algoritmo A* para encontrar la mejor ruta entre estaciones de un sistema de transporte masivo.

En esta nueva etapa, se implementa un modelo de aprendizaje supervisado con el objetivo de predecir el tiempo de viaje entre estaciones, considerando diferentes variables operativas.

---

## Objetivo

Desarrollar un modelo de aprendizaje supervisado que permita estimar el tiempo de viaje entre estaciones, utilizando variables como distancia, tráfico, clima y cantidad de pasajeros.

---

##  Dataset

Se construyó un dataset sintético basado en las conexiones entre estaciones del sistema de transporte.

Cada registro representa un viaje entre dos estaciones.

### Variables utilizadas:

- `origen`: estación de salida  
- `destino`: estación de llegada  
- `distancia_m`: distancia aproximada entre estaciones  
- `hora_pico`: indica si es hora pico (0 o 1)  
- `trafico`: nivel de tráfico (1 bajo, 2 medio, 3 alto)  
- `lluvia`: presencia de lluvia (0 o 1)  
- `pasajeros`: número de pasajeros  
- `tiempo_viaje_min`: tiempo de viaje en minutos (variable objetivo)

---

## Modelo de Aprendizaje Supervisado

Se utilizó un modelo de regresión lineal para aprender la relación entre las variables de entrada y el tiempo de viaje.

El modelo fue entrenado con datos generados artificialmente mediante una fórmula determinística.

---

## Resultados

El modelo obtuvo los siguientes resultados:

- Error: 0.0  
- R²: 1.0  

Esto se debe a que el dataset fue generado sin ruido, lo que permitió al modelo aprender perfectamente la relación entre las variables.

En un entorno real, los resultados no serían perfectos debido a la variabilidad de los datos.

---

## Relación con el algoritmo A*

El modelo desarrollado puede complementar el sistema de ruteo basado en A*.

En lugar de utilizar costos fijos entre estaciones, se podrían usar los tiempos de viaje predichos por el modelo, permitiendo calcular rutas más realistas.

---

## Tecnologías utilizadas

- Python 3
- pandas
- scikit-learn

---

## ▶️ Ejecución del proyecto

1. Ejecutar el modelo:

```bash
python3 Aprendizaje Supervisado.py
