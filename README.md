## 🛵 Fast Delivery API

### Nombre: Jimena Montaño Claros

Este es un proyecto de backend desarrollado con **Django** y **Django Rest Framework (DRF)** que simula el funcionamiento de una plataforma de delivery. 

## 🚀 Requisitos:
- ✅ **Arquitectura:** Proyecto Django con la aplicación `pedidos`.
- ✅ **Base de Datos:** 4 Modelos (`Restaurante`, `Producto`, `Repartidor`, `Pedido`).
- ✅ **Validaciones:** 2 Validaciones personalizadas (Precio positivo y longitud de nombre).
- ✅ **Administrador:** Modelos `Restaurante` y `Pedido` registrados.
- ✅ **API REST:** 3 ModelViewSets (CRUD completo) y 1 Custom API View.
- ✅ **Dependencias:** Archivo `requirements.txt` incluido.

---

## 🛠️ Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto localmente:

### 1. Clonar y preparar el entorno
- #### Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  
- #### En Windows: venv\Scripts\activate
- #### Instalar dependencias
pip install -r requirements.txt
### 2. Configurar la Base de Datos
python manage.py makemigrations

python manage.py migrate
### 3. Crear un superusuario (Para el Admin)
python manage.py createsuperuser
### 4. Iniciar el servidor
python manage.py runserver
