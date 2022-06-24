# CoderHouse_Python_Blog

Trabajo Final

Equipo de trabajo:
- Romina Garcia Rojas
- Romina Quispe Real

Trabajo: Web Educación - La navegación de la web permite visualizar blogs con información de diversos temas. Poder completar un formulario con consultas. Registración 
a la web, el cual permitirá dar de alta nuevos blogs, eliminar o actualizarlos. Se podrá elegir los blogs que serán públicos para ser visualizados.

El proyecto contiene:
 - Vistas 
 - Urls
 - Statics Files
 - Formularios
 - Modelos
 - Templates

Herramienta de desarrollo y requeridas para el funcionamiento:

Archivo requirements.txt

asgiref==3.5.1
beautifulsoup4==4.11.1
Django==4.0.4
django-bootstrap-v5==1.0.11
gunicorn==20.1.0
Pillow==9.1.1
soupsieve==2.3.2.post1
sqlparse==0.4.2
tzdata==2022.1
whitenoise==6.2.0
psycopg2==2.6.2
dj_database_url==0.5.0

Ingreso admin: http://localhost:8000/admin/login/?next=/admin/

Mapa web:

  1- Ingreso sin logueo

    Home 

      Url Acceso: http://localhost:8000/blog/index/
      Descripción funcionalidad: Página de inicio, presentación de la web.

    Blogs

      Url Acceso: http://localhost:8000/blog/blogs/
      Descripción funcionalidad: Página donde se lista todos los blogs creados por usuarios registrados. Blogs que el dueño eligió sean públicos, es decir
      ser visualizados por cualquier persona que acceda a la aplicación web.

    Acerca De

      Url Acceso: http://localhost:8000/blog/about/
      Descripción funcionalidad: Página donde se describe la tarea que se realiza sobre educación y da una idea de los temas e información que podrá publicarse.

    Equipo

      Url Acceso: http://localhost:8000/blog/team/
      Descripción funcionalidad: Página donde se describen los miembros del equipo de desarrollo, con acceso al GitHub de cada miembro.

    Contacto

      Url Acceso: http://localhost:8000/blog/contact/
      Descripción funcionalidad: Página la cual contiene un formulario, el cual podrá ser completado y enviado, solicitando información o quejas.


    Ingresar

      Url Acceso: http://localhost:8000/blog/entrar/
      Descripción funcionalidad: Página que me permitirá registrarme en caso que así lo desee o si ya poseo usuario y contraseña poder loguearme.

          Crear Cuenta
              Url Acceso: http://localhost:8000/blogger/crear/
              Funcionalidad: Registración con usuario y contraseña (se aplican validaciones de logueo standard provistas por Django)

          Logueo  

              Url Acceso: http://localhost:8000/blog/entrar/
              Funcionalidad: Ingreso (logueo) al perfil de usuario creado, el cual nos habilitara al ABM de Blogs.

 2- Ingreso usuario Logueado
  
    Blogs
    
      Url Acceso: http://localhost:8000/blog/lista/
      Descripción funcionalidad: Página donde se lista solo los blogs creados por el usuario que se logueo con usuario y contraseña. Se visualizaran todos
      sus blogs, públicos y privados. Se le dará el acceso a borrar y actualizar los blog que dio de alta previamente.
      
          Borrar
          
              Url Acceso: http://localhost:8000/blog/borrar/<pk>/
              Funcionalidad: Acceso a eliminar el blog seleccionado.
          
          Actualizar
          
              Url Acceso: http://localhost:8000/blog/editar/<pk>/
              Funcionalidad: Acceso al formulario de Blog, permitiendo su actualización.
    
    Perfil
    
      Url Acceso: http://localhost:8000/blogger/profile/<pk>/
      Descripción funcionalidad: Página que me permite visualizar los datos del perfil, más la imagen o avatar seleccionado.
      
          Editar Perfil
          
              Url Acceso: http://localhost:8000/blogger/editar/<pk>/
              Funcionalidad: Acceso a página que permitirá la modificación del perfil del usuario.
          
          Añadir Imagen
          
              Url Acceso: http://localhost:8000/blogger/imagen/<pk>/
              Funcionalidad: Acceso a página que permitirá añadir una imagen al perfil del usuario logueado.
    
    Salir
    
      Url Acceso: http://localhost:8000/blog/salir/
      Descripción funcionalidad: Salir de la registración, redirecciona a una página de agradecimiento, habilitando el menú detallado anteriormente (Ingreso sin logueo).
    
    Nuevo Blog
    
      Url Acceso: http://localhost:8000/blog/crear/
      Descripción funcionalidad: Página que habilita el formulario para el ingreso de nuevos blogs del usuario logueado. 
    


