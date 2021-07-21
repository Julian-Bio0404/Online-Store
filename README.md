# Online-store
Tienda Online de productos lácteos.
----
### Features
- Home que describe la web page
- Tienda: expone los productos disponibles y permite agregar al carrito
- Carrito: widget que expone los productos agragados por el usuario, permite agregar o eliminar cantidad, sumar los precios por productos y exponer un gran total.
- Servicios: expone los servicios disponibles
- Blog: expone los posts publicados. Estos están asociados a un usuario y categoria
- Contacto: Es la via de comunicacion entre un cliente y la empresa; llenando el fromulario cuyos campos son: nombre, email y contenido
----

### Skills  
- Python
- Django
- HTML
----

### Documentación 
#### Para correr el proyecto:
- Clone este proyecto
- Cree un ambiente virtual donde alojará el proyecto
- Diríjase a la raíz del proyecto e instale los requerimientos con: pip install -r requirements.txt
- Dentro del proyecto cree un archivo .env llenando las variables expuestas en .env_example
- Corra: py manage.py migrate 
- Corra: py manage.py create superuser
- Corra: py manage.py runserver 
- diríjase a: http://localhost:8000/admin/ inicie sesion como superusuario y juegue creando servicios, posts y productos con sus respectivas categorias