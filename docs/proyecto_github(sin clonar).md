📁 Pasos para futuros proyectos en GitHub
Este documento describe paso a paso cómo configurar un nuevo proyecto en GitHub, incluyendo la creación del entorno, inicialización de Git y conexión con el repositorio remoto.

Pasos para futuros proyectos github. 

** 1. Crear carpeta:

mkdir nombre-proyecto
cd nombre-proyecto

** 2. Inicializar git:

git init

** 3. Crea el entorno virtual y actívalo 

uv venv
.venv\Scripts\activate
code .

** 4. Inicia el entorno e Instala los paquetes que necesites 

uv init
uv add ...

** 5. Commit inicial 

git add . 
git commit -m "Initial commit" (Importante comillas dobles) 

** 6. Crear el repo en GitHub (sin README)

** 7. Agregar el remote:

git remote add origin https://github.com/tu-usuario/tu-repo.git

** 8. Forzar rama main:

git branch -M main

** 9. PUSH PUSH PUSH PUSH 

git push -u origin main






