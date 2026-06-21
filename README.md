## Demo

🚀 [Ver aplicación en producción](http://coffee-shop-production.eba-mmycmmbq.us-east-2.elasticbeanstalk.com)

# ☕ Coffee Shop Django

Aplicación web de gestión de pedidos para una cafetería, desarrollada con Django y Django REST Framework.

## Tecnologías

- Python 3.12
- Django 6.0
- Django REST Framework
- PostgreSQL
- Tailwind CSS

## Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/danderi/django-coffee-shop
```

2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno — copiar `.env.example` a `.env` y completar los valores
```bash
DJANGO_DB_URL=postgres://usuario:password@host:port/nombre_db
```

5. Correr migraciones
```bash
python manage.py migrate
```

6. Crear superusuario
```bash
python manage.py createsuperuser
```

7. Correr el servidor
```bash
python manage.py runserver
```

## Aplicaciones

- **products** — gestión del catálogo de productos
- **orders** — gestión de pedidos por usuario
- **users** — registro y autenticación de usuarios

## API Endpoints

- `GET /api/` — lista de productos
- `POST /api/create/` — crear producto
- `POST /orders/api/create/` — crear orden