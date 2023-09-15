Instrucciones de uso del programa:

Esta web contiene 4 clases:
- Piloto
- Avión
- Aerolínea
- Destino

Para navegar entre las páginas, utilice la barra de navegación haciendo click en el nombre de la web que desee visitar:
- Inicio
- Pilotos
- Destinos
- Aviones
- Aerolíneas
- Contacto

Si hace click en "Contacto" será llevado a la parte inferior de la web donde podrá dejar sus datos.

La clase Avión está relacionada con la clase Aerolínea (ForeignKey) pues los aviones pertenecen a las aerolíneas.
Por cuestiones de tiempo se tuvieron que remover otras relaciones similares entre las clases.

El programa ya cuenta con información dentro de la base de datos, pues es lo que se muestra en el apartado estético de la web.

Para registrar elementos en la base de datos, el proceso es el siguiente:

1) Acceda a la página del objeto que desea acceder, verá una lista con los objetos ya registrados
2) Dirígase a la sección inferior y haga click en el botón de registrar el objeto
3) Una vez en la página de registro, rellene el formulario para completar los datos del objeto a registrar
4) Una vez le de al botón de registrar, será redirigido a la página principal del objeto donde encontrará la lista actualizada

Si se elimina la base de datos existente, el proceso para registrar elementos es el mismo; sin embargo, es vital que primero registre una aerolínea antes que registre un avión pues la clase de avión cuenta con un campo perteneciente a las aerolíneas existentes.

Para utilizar el formulario de búsqueda, el proceso es el siguiente:
1) Debe dirigirse a la página de aviones, en la cual al lado del botón de registrar aviones podrá ver el botón de buscar aviones
2) Haga click en el botón de buscar aviones
3) Se abrirá la página donde podrá buscar aviones por código de avión
4) Una vez escriba el código del avión, haga click en buscar
