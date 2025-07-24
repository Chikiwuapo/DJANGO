🛒 Proyecto Django - Inventario de Productos y Categorías
Este proyecto es una aplicación web desarrollada con Python y Django que permite gestionar productos y categorías mediante un sistema CRUD (crear, leer, actualizar, eliminar). Está diseñado como una solución básica para administrar inventarios de forma organizada y eficiente dentro de una empresa o negocio.

👥 Integrantes y Roles
Christian Cárdenas – 💻 Desarrollador Backend (Django)

favio vives ruidiaz – 🎨 Maquetador / Frontend

Adriel vergaray  – 🧪 Tester / QA

Daniel muñoz – 📂 Encargado de Documentación

⚙️ Instalación del Proyecto

🔽 Clonar el repositorio
bash
Copiar-Editar
git clone https://github.com/Chikiuwapo/DJANGO.git
cd DJANGO

🐍 Crear entorno virtual
bash
Copiar
Editar
python -m venv env

▶️ Activar el entorno virtual

En Windows:
env\Scripts\activate

En macOS/Linux:
source env/bin/activate

📦 Instalar dependencias
nginx
pip install -r requirements.txt
🛠️ Ejecutar migraciones

nginx
Copiar
Editar
python manage.py makemigrations
python manage.py migrate

🚀 Iniciar el servidor
nginx
python manage.py runserver

🌐 Ingresar al sistema

Abre tu navegador y entra a:
cpp
http://127.0.0.1:8000/

📖 Historias de Usuario Principales

📖 Historias de Usuario Principales

Como usuario, quiero visualizar una lista de productos para conocer el stock disponible. Como administrador, quiero registrar nuevos productos para mantener actualizado el inventario, así como editar la información de los productos existentes para corregir o actualizar datos, y también eliminar aquellos productos que ya no se encuentren disponibles o en uso. Además, como usuario, deseo acceder a la lista de categorías para explorar los productos según su tipo. Finalmente, como administrador, quiero poder gestionar las categorías, es decir, crear, editar y eliminar, con el fin de organizar eficientemente los productos dentro del sistema.

🧩 Tecnologías Utilizadas

🐍 Python
🌐 Django
🗃️ SQLite3
🖼️ HTML5 y (opcionalmente) Bootstra
🖥️ Visual Studio Code

🗂️ Estructura del Proyecto

inventario/ – Configuración principal del proyecto.

productos/ – App encargada de gestionar productos y categorías (CRUD).

db.sqlite3 – Base de datos local del proyecto.

requirements.txt – Lista de dependencias necesarias.

