# ML-proyecto-individual

## Sistema de recomendacion de videojuegos para Steam.

Este proyecto ilustra las responsabilidades de un Ingeniero MLOps, integrando las competencias tanto de un Ingeniero de Datos como de un Científico de Datos, en el ámbito de la plataforma de videojuegos multinacional Steam. El propósito es crear un Producto Mínimo Viable (MVP) que contemple una API alojada en la nube y la implementación de un modelo de Machine Learning destinado a ofrecer recomendaciones de juegos.

# Introduccion.

El proyecto se fundamenta en un conjunto de datos en formato JSON relacionados con la plataforma de videojuegos Steam, sirviendo como base para el desarrollo de un Producto Mínimo Viable (MVP). Los archivos de datos incluyen:

steam_games: Contiene información sobre los juegos en la plataforma Steam, como el nombre, género, fecha de lanzamiento y otros detalles.
user_reviews: Proporciona detalles sobre las reseñas realizadas por los usuarios de Steam.
user_items: Ofrece información sobre la actividad de los usuarios en la plataforma Steam.


## Descripcion del proyecto

### 1. Ingeniería de Datos y Desarrollo de API
ETL: Se realizó la limpieza inicial y el formateo del conjunto de datos para asegurar su correcta lectura. Se implementó un análisis de sentimiento utilizando NLP para crear la columna 'opinion', lo que optimiza el rendimiento de la API y el entrenamiento de los modelos de machine learning.

API con FastAPI: Se propuso y desarrolló una API utilizando FastAPI que permite realizar diversas consultas sobre los datos disponibles, ofreciendo información sobre desarrolladores, usuarios, géneros y juegos.

Despliegue: La API está desplegada y accesible para ser consumida desde la web, utilizando el servicio Render, siguiendo el tutorial disponible en el repositorio.

### 2. Análisis Exploratorio de Datos (EDA) y Modelos de Machine Learning
Análisis Exploratorio: Se llevó a cabo un análisis exploratorio de los datos para comprender mejor las relaciones entre las variables del conjunto de datos, identificando outliers, anomalías y patrones interesantes para análisis posteriores.

Modelos de Recomendación: Se implementó al menos uno de los dos tipos de sistemas de recomendación: ítem-ítem y usuario-ítem. Estos modelos permiten sugerir juegos similares basados en la similitud entre ítems o usuarios.

# Funcionalidades Principales de la API

## La API ofrece las siguientes funcionalidades:

**developer** : Proporciona la cantidad de ítems y el porcentaje de contenido gratuito por año según la empresa desarrolladora.
**userdata** : Devuelve el dinero gastado por un usuario, el porcentaje de recomendación basado en reseñas y la cantidad de ítems.
**UserForGenre** : Retorna el usuario con más horas jugadas en un género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
**best_developer_year** : Devuelve el top 3 de desarrolladores con más juegos recomendados por usuarios en un año dado.
**developer_reviews_analysis** : Proporciona un análisis de reseñas de usuarios, categorizadas como positivas o negativas, para un desarrollador específico.
**recomendacion_juego** : Recibe el ID de un juego y devuelve una lista con 5 juegos recomendados similares.


Modelo de Machine Learning
El modelo de Machine Learning utilizado se basa en la similitud del coseno, estableciendo una relación ítem-ítem para recomendar juegos similares. Adicionalmente, se aplica un filtro usuario-juego para recomendar ítems basados en la similitud entre usuarios.

Despliegue
Para el despliegue de la API se utilizó la plataforma Render. Puedes acceder al funcionamiento de la API desplegada a través del siguiente enlace:  
https://ml-proyecto-individual.onrender.com/docs
