## Trabajo final Informática 1

## Estudiante 1: Emanuel Cruz Tabares
## Estudiante 2: Raul Molina  

INDICACIONES GENERALES
Desarrollar una aplicación CRUD (Create, Read, Update and Delete) en Python que permita almacenar y gestionar información de los fármacos que se encuentran en diferentes infraestructuras de IPS de la ciudad de Medellín. Dicha aplicación contará con una entrada y salida de información en el editor de Python y almacenamiento de la información en una base de datos MySQL.
El desarrollo del script deberá hacer lo que se describe a continuación:

1.	El algoritmo debe contar con un menú Principal que permita Gestionar la información de: medicamentos, proveedores, ubicaciones y salir. La única forma de ingresar a este menú será si el usuario se encuentra registrado al sistema.

2.	Una vez se ingrese a una de las tres opciones, allí se debe tener la opción de hacer la aplicación CRUD para cada ítem, decir, si se ingresa a la opción de medicamentos, allí el usuario verá otro menú que tenga las opciones de:
 2.1.	Ingresar un nuevo medicamento.
 2.2.	Actualizar la información de un medicamento. Usando el número de lote como parámetro de búsqueda.
 2.3.	Buscar un medicamento. Usando el número de lote como parámetro de búsqueda.
 2.4.	Ver la información de todos los medicamentos almacenados.
 2.5.	Eliminar un medicamento. Usando el número de lote como parámetro de búsqueda.
 2.6.	Volver al menú principal Si se selecciona una opción diferente a las anteriores, el algoritmo deberá sacar una alerta de error y volver a este mismo menú para que el usuario haga la selección nuevamente.

3.	Para las opciones de los proveedores y ubicaciones, se debe contar con menús similares al descrito en el numeral anterior, pero adaptado a cada caso. Es decir, ingresa, ver, actualizar y eliminar responsables e ingresa, ver, actualizar y eliminar ubicaciones de los medicamentos.
Nota: En cualquiera de los tres casos (medicamentos, proveedores y ubicación), cuando se solicite mostrar información, se debe hacer en forma ordenada.

4.	Para el caso de las opciones de ingresar datos, se deberá solicitar la información que se muestra a continuación:
•	Usuarios:
o	User
o	Password

•	Medicamentos:
o	Lote
o	Nombre del medicamento
o	Distribuidor
o	Cantidad en bodega
o	Fecha de llegada
o	Precio de venta

•	Proveedores
o	código
o	Nombre
o	Apellido
o	Número del documento de identidad
o	Entidad

•	Ubicaciones
o	Código (alfanumérico)
o	Nombre de la ubicación
o	Teléfono

5.	La aplicación debe validar la información numérica que se ingrese usando la sentencia try/except, es decir, los que en los numerales anteriores (5.1, 5.2, 5.3) dicen “tipo numérico”, si el usuario ingresa letras, se activen las excepciones para permitir corregir esta opción.

6.	La validación de los datos que se pide en el numeral anterior se debe hacer usando funciones, las cuales deberán ser usadas como tipo módulo, es decir, importadas desde el módulo (archivo .py) y llamando las funciones desde el script principal.

7.	La base de datos MySQL deberá estar configurada con los siguientes parámetros:
a)	Nombre de la base de datos: informatica1
b)	Usuario: informatica1
c)	Contraseña: bio123
d)	Tablas: estarán nombradas y configuradas según lo considerado por cada medicamento.

8.	La base de datos contará con 3 tablas, una para almacenar la información de los medicamentos, los proveedores y las posibles ubicaciones en las IPS.

9.	Para generar la aplicación CRUD debe realizarse con funciones para cada opción descrita. Observación: Como son tres tablas diferentes, la forma más sencilla es hacer esto es una función por cada menú por cada evento del CRUD. Es decir, cuatro funciones para el CRUD de los medicamentos, cuatro para el CRUD de los proveedores y cuatro para el CRUD de ubicaciones. Ahora bien, si encuentra la forma de mejorar esta opción, es decir, optimizar el código de tal forma que haga menos funciones, mucho mejor.
 
10.	Las tres tablas deberán tener información previamente cargada para poder hacer la consulta desde un principio, por favor, aunque la información que ingrese va a ser ficticia, esta debe tener coherencia, no se aceptan campos incoherentes.

11.	Consulte cómo funciona la librería tkinder e implementelo en su trabajo para el diseño del sistema, no tiene que realizar todo el programa utilizando la librería, puede seleccionar en qué parte va a diseñarlo. Adjunto un ejemplo de cómo utilizar tkinder.

12.	Importante: las tablas de la base de datos deben estar relacionadas, es decir, cuando se vaya a ingresar la información de nuevo medicamento, en el campo del responsable se debe mostrar la información disponible para cada caso. Por ejemplo:
12.1.	Se pide ingresar el responsable y en la tabla responsables de la base de datos hay 5 registros, es decir, 5 opciones, cuando se le pida al usuario escoger esta opción será algo como:
o	101 - Jorge Andrés Camacho
o	203 - María Camila Arias Restrepo
o	345 – Laura Constanza Duque Marín
o	421 – Isabel Cristina Romero Muñoz
o	500 – Juan Camilo Hoyos Diaz.
*	El código asociado y el nombre y apellido del responsable en la tabla
Para el caso de la ubicación del medicamento, deberá ser igual, pero se debe listar las ubicaciones disponibles en la tabla. Por ejemplo:
o	1234 – Hospital San Vicente
o	1203 – Hospital Pablo Tobón Uribe
o	5588 – Hospital Alma Mater de Antioquia
o	7800 – Clínica del Norte
*	El código asociado y el nombre la ubicación en la tabla
Todas las funciones que se utilicen para el desarrollo de este trabajo deberán estar documentadas, de tal forma que usando la función help() se pueda leer dicha documentación. Adicionalmente, el código principal debe estar documentado por secciones. OJO, No una documentación línea por línea, sino una documentación por segmentos de código. Por ejemplo, una breve descripción de los hacen un número determinado de líneas de código. Algo así como descripción de las variables, descripción de los procesos y resultados a mostrar, etc.


OBSERVACIONES DE ENTREGA
•	El trabajo se realizará en los grupos asignados al inicio del curso.
•	Se debe entregar el trabajo en un repositorio de GitHub, añadir el enlace a la entrega, no se admite una entrega diferente.
•	En la cabecera del script se deben colocar los nombres de los autores como un comentario (integrantes del grupo).
 
•	Todas las funciones y script desarrollado deben estar documentado.
•	Cualquier intento de fraude o copia de código (parcial o completo) entre los diferentes equipos implicará una calificación de 0.0 para todos los involucrados sin posibilidad de recuperación.
•	Si al ejecutar el script hay algún error, sin importar cual sea, el trabajo se calificará sobre 3.0.



¡Muchos éxitos!

