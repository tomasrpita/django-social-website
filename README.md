# Django Social Website

Este es el segundo proyecto del libro *Django 5 By Example: Build powerful and reliable Python web applications from scratch (English Edition)*. Este proyecto abarca los siguientes capítulos y alcances:

## Capítulos del Libro

### Capítulo 4: Construyendo un Sitio Web Social
Explica cómo construir un sitio web social. Aprenderás a implementar vistas de autenticación de usuarios y a utilizar el marco de autenticación de Django. Implementarás el registro de usuarios y extenderás el modelo de usuario con un modelo de perfil personalizado.

### Capítulo 5: Implementando Autenticación Social
Cubre la implementación de la autenticación social y el uso del marco de mensajes. Crearás un backend de autenticación personalizado e integrarás la autenticación social con Google, utilizando OAuth 2. Aprenderás a usar `django-extensions` para ejecutar el servidor de desarrollo a través de HTTPS y a personalizar el pipeline de autenticación social para automatizar la creación de perfiles de usuario.

### Capítulo 6: Compartiendo Contenido en tu Sitio Web 
Te enseñará cómo transformar tu aplicación social en un sitio web de marcadores de imágenes. Definirás relaciones de muchos a muchos para los modelos y crearás un bookmarklet de JavaScript que se integrará en tu proyecto. El capítulo te mostrará cómo generar miniaturas de imágenes. También aprenderás a implementar solicitudes HTTP asíncronas utilizando JavaScript y Django, e implementarás paginación de desplazamiento infinito.

### Capítulo 7: Rastreando Acciones de los Usuarios
Te mostrará cómo construir un sistema de seguidores para los usuarios. Completarás tu sitio web de marcadores de imágenes creando una aplicación de flujo de actividad de usuarios. Aprenderás a crear relaciones genéricas entre modelos y a optimizar QuerySets.

Trabajarás con señales e implementarás desnormalización. Utilizarás Django Debug Toolbar para obtener información de depuración relevante. Finalmente, integrarás Redis en tu proyecto para contar las visualizaciones de imágenes y crearás un ranking de las imágenes más vistas con Redis.

## Puesta en Marcha

### Prerrequisitos

Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

### Instalación de Dependencias

1. **Clonar el repositorio:**

    ```sh
    git clone https://github.com/tomasrpita/django-social-website.git tu-repositorio
    cd tu-repositorio
    ```

2. **Crear un entorno virtual e instalar las dependencias de Python:** 

    ```sh
    python3 -m venv .venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Crear el archivo `.env` a partir del archivo de plantilla `env.template`:**

    ```sh
    cp .env.template .env
    ```

4. **Rellenar las variables de entorno en el archivo `.env`:**

    ```plaintext
    GOOGLE_OAUTH2_KEY=your-google-oauth2-key
    GOOGLE_OAUTH2_SECRET=your-google-oauth2-secret

    REDIS_HOST=localhost
    REDIS_PORT=6379
    REDIS_DB=0
    ```

### Configuración de la Aplicación Django

### Configuración de Docker

1. **Iniciar los servicios con Docker Compose:**

    ```sh
    docker-compose up -d
    ```

1. **Ejecutar las migraciones de la base de datos:**

    ```sh
    python ./bookmarks/manage.py migrate
    ```

2. **Crear un superusuario:**
    
    ```sh
    python ./bookmarks/manage.py createsuperuser
    ```

3. **Cargar datos iniciales (si aplica):**
    
    ```sh
    python ./bookmarks/manage.py loaddata fixtures/initial_data.json
    ```

### Iniciar el Servidor de Desarrollo

1. **Configure el archivo de hosts para simular un entorno real:**

    + En Linux o macOS, edite el archivo /etc/hosts.
    + En Windows, edite el archivo C:\Windows\System32\Drivers\etc\hosts.

    Agregue la siguiente línea al archivo:
    
    ```plaintext
    127.0.0.1 mysite.com
    ```

2. **Iniciar el servidor de desarrollo de Django con SSL/TLS:**

    ```sh
    python ./bookmarks/manage.py runserver_plus --cert-file cert.crt
    ```

### Acceso a la Aplicación

- La aplicación estará disponible en `http://mysite.com:8000/account`.
- La interfaz de administración de Django estará en `http://localhost:8000/admin`.
