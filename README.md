# Chatbot con LLM y arquitectura RAG

## Descripción

Este proyecto consiste en el desarrollo de un chatbot basado en un **Large Language Model (LLM)**, implementando una arquitectura **Retrieval-Augmented Generation (RAG)** para permitir que el modelo genere respuestas utilizando información proveniente de documentos externos.

La aplicación utiliza **Google Gemini** como modelo generativo y **ChromaDB** como base de datos vectorial para almacenar y recuperar información relevante de los documentos proporcionados.

El objetivo principal es explorar e implementar conceptos de Inteligencia Artificial Generativa, procesamiento de documentos, embeddings, búsqueda semántica y recuperación de información mediante Python.

## Tecnologías utilizadas

- **Python:** lenguaje principal para el desarrollo de la aplicación.
- **Google Gemini:** modelo de lenguaje utilizado para la generación de respuestas.
- **Google GenAI SDK:** integración y comunicación con los modelos de Google.
- **ChromaDB:** almacenamiento y recuperación de vectores.
- **Embeddings:** representación vectorial del contenido para realizar búsquedas semánticas.
- **Pydantic:** estructuración y validación de datos.
- **SQLite:** soporte de almacenamiento local.
- **Python-dotenv:** gestión de variables de entorno y configuración.

## Arquitectura

El proyecto implementa una arquitectura RAG, que combina la capacidad generativa de un LLM con un mecanismo de recuperación de información externa.

El funcionamiento se divide principalmente en dos procesos:

### 1. Procesamiento e indexación de documentos

1. Se cargan documentos PDF mediante un módulo de extracción de texto.
2. El contenido se divide en fragmentos (*chunks*) para facilitar su procesamiento.
3. Se generan embeddings para representar los fragmentos mediante vectores numéricos.
4. Los vectores y su información asociada se almacenan en ChromaDB.

### 2. Recuperación de información y generación de respuestas

1. El usuario realiza una pregunta al chatbot.
2. Se recuperan los fragmentos de información más relevantes mediante búsqueda semántica.
3. Se construye un contexto con la información recuperada.
4. Se genera un prompt que integra la pregunta, el contexto y la memoria conversacional.
5. Gemini utiliza esta información para generar una respuesta contextualizada.
6. Se gestiona el historial de conversación para mantener continuidad entre las interacciones.

## Estructura del proyecto

El código está organizado en módulos independientes, buscando separar responsabilidades y facilitar el mantenimiento y la ampliación de la aplicación.

```text
app/
│
├── chat/          # Gestión de memoria conversacional
├── chunkers/      # División de documentos en fragmentos
├── config/        # Configuración de la aplicación
├── embeddings/    # Generación de embeddings
├── llm/           # Cliente de comunicación con Gemini
├── loaders/       # Carga y extracción de documentos PDF
├── models/        # Modelos y estructuras de datos
├── prompt/        # Construcción de prompts
├── retrievers/    # Recuperación de información relevante
├── services/      # Lógica y coordinación de servicios
├── vectorstores/  # Gestión de la base de datos vectorial
│
└── data/
    ├── chroma/    # Almacenamiento vectorial
    ├── documents/ # Documentos de entrada
    └── sqlite/    # Almacenamiento local
```

## Propósito y aprendizajes

Este proyecto tiene como propósito aplicar conocimientos de Inteligencia Artificial Generativa y desarrollo de software mediante la construcción de una aplicación funcional basada en LLMs.

Durante su desarrollo se trabajaron conceptos como:

- Integración de modelos de lenguaje mediante APIs.
- Generación y utilización de embeddings.
- Búsqueda semántica y bases de datos vectoriales.
- Arquitectura RAG (*Retrieval-Augmented Generation*).
- Procesamiento y fragmentación de documentos.
- Ingeniería de prompts (*Prompt Engineering*).
- Gestión de memoria conversacional.
- Organización modular y separación de responsabilidades en Python.

## Posibles mejoras

- Incorporar soporte para diferentes formatos de documentos.
- Implementar una interfaz gráfica para interactuar con el chatbot.
- Mejorar la persistencia de la memoria conversacional.
- Incorporar mecanismos de evaluación de la calidad de recuperación y generación de respuestas.

---

**Proyecto desarrollado con Python y Google Gemini como práctica de implementación de arquitecturas RAG y aplicaciones basadas en modelos de lenguaje.**              
