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

Python 3.9.5
Django 4.0.4
Bootstrap5
CSS
HTML
SQlite 3

Mapa web:

  1- Ingreso sin logueo

    Home 

      Url Acceso: http://127.0.0.1:8000/blog/index/
      Descripción funcionalidad: Página de inicio, presentacion de la web.

    Blogs

      Url Acceso: http://127.0.0.1:8000/blog/blogs/
      Descripción funcionalidad: Página donde se lista todos los blogs crados por usuarios registrados. Blogs que el dueño eligió sean publicos, es decir
      ser visualizados por cualquier persona que acceda a la aplicación web.

    Acerca De

      Url Acceso: http://127.0.0.1:8000/blog/about/
      Descripción funcionalidad: Página donde se describe la tarea que se realiza sobre la educación y da una idea de los temas e información que podra publicarse.

    Equipo

      Url Acceso: http://127.0.0.1:8000/blog/team/
      Descripción funcionalidad: Página donde se dscriben los miembros del equipo de desarrollo, con acceso al GitHub de cada miembro.

    Contacto

      Url Acceso: http://127.0.0.1:8000/blog/contact/
      Descripción funcionalidad: Página la cual contiene un formulario, el cual podra ser completado y enviado, solicitando información o quejas.


    Ingresar

      Url Acceso: http://127.0.0.1:8000/blog/entrar/
      Descripción funcionalidad: Página que me permitira registrarme en caso que asi lo desee o si ya poseo usuario y contraseña poder loguearme.

          Crear Cuenta
              Url Acceso: http://127.0.0.1:8000/blogger/crear/
              Funcionalidad: Registracion con usuario y contraseña (se aplican validaciones de logueo standard provistas por Django)

          Logueo  

              Url Acceso: http://127.0.0.1:8000/blog/entrar/
              Funcionalidad: Ingreso (logueo) al perfil de usuario creado, el cual nos habilitara al ABM de Blogs.

 2- Ingreso usuario Logueado
  
    Blogs
    
      Url Acceso: http://127.0.0.1:8000/blog/lista/
      Descripción funcionalidad: Página donde se lista solo los blogs crados por el usuario que se logueo con usuario y contraseña. Se visualizaran todos
      sus blogs, publicos y privados. Se le dara el acceso a borrar y actualizar los blog que dio de alta previamente.
      
          Borrar
          
              Url Acceso: http://127.0.0.1:8000/blog/borrar/<pk>/
              Funcionalidad: Acceso a eliminar el blog seleccionado.
          
          Actualizar
          
              Url Acceso: http://127.0.0.1:8000/blog/editar/<pk>/
              Funcionalidad: Acceso al formulario de Blog, permitiendo su actualización.
    
    Perfil
    
      Url Acceso: http://127.0.0.1:8000/blogger/profile/<pk>/
      Descripción funcionalidad: Página que me permite visualizar los datos del perfil, mas la imagen o avatar seleccionado.
      
          Editar Perfil
          
              Url Acceso: http://127.0.0.1:8000/blogger/editar/<pk>/
              Funcionalidad: Acceso a página que permitira la modificación del perfil del usuario.
          
          Añadir Imagen
          
              Url Acceso: http://127.0.0.1:8000/blogger/imagen/<pk>/
              Funcionalidad: Acceso a página que permitira añadir una imagen al perfil del usuario logueado.
    
    Salir
    
      Url Acceso: http://127.0.0.1:8000/blog/salir/
      Descripción funcionalidad: Salir de la registración, redirecciona a una pagina de agradecimiento, habilitando el menu detallado anteriormente (Ingreso sin logueo).
    
    Nuevo Blog
    
      Url Acceso: http://127.0.0.1:8000/blog/crear/
      Descripción funcionalidad: Página que habilita el formulario para el ingreso de nuevos blogs del usuario logueado. 
    


