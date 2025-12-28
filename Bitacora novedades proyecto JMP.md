25/12/25 23:58



-se hizo funcionar los archivos Json del menu de clientes para sobrescribir y redactar los datos propuestos. 

-agregue el archivo "main".

-cambios hechos en functions\_clientes.py

&nbsp;	-se uso un nuevo comando "import = os" ¨.path" ".dirname" "(\_\_file\_\_)"

&nbsp;	-se cambio la ruta usada en la(s) líneas 6, 13. Añadiéndole "encoding = -8" además de cambiar la ruta de "datos" por "datos\_clientes"

&nbsp;	-se creo una nueva variable "BASE\_DIR" y "datos\_clientes"

-cambios hechos en menu\_clientes.py

&nbsp;	-se cambio los textos     

&nbsp;	print("\\n menu \\n")

&nbsp;   	print("1. Agregar cliente")

&nbsp;   	print("2. Listado de clientes")

&nbsp;   	print("3. volver al menu principal")

&nbsp;	de las líneas 3,4 y 5 a las líneas 7,8,9 y 10. se realizo este cambio para mantener las opciones dentro del bucle "while true" por motivos de practicidad y visualización general en la consola.





26/12/25 22:15



\- se agrego el modulo "menu\_productos.py"

\- se agrego la función "functions\_productos"

\- se implemento la lógica relacionada a cada modulo

**nota importante** \[en el modulo "functions\_productos" se implemento el cambio a la función "obtener\_productos\_flexible" la cual esta bien implementada pero no se ha encontrado ni anexado algun uso real,recordatorio para anexarla a futuras revisiones, esto se hizo para que el usuario pueda buscar tanto por ID "PID" como por nombre del producto (con relacion a este modulo) pero no se ha podido anexar a ninguna funcion util]





26/12/25



-se soluciono y se aplico la nota anterior, ya se le dio uso real a la implementación 

-se añadió una nueva función llamada "normaliar\_texto" su implementación se usara para facilitar la búsqueda por nombre al usuarion sin que se vea afectada la base de datos, se implemento como un completento de la función "obtener\_productos\_flexibles"



nota \[hay observaciones en 3 aspectos. 1. se duplica de manera inconsistente la información en el submodulo ("#5 cambiar precio de producto" / liena 53:85 / menu\_productos) encontrar la liena que da ese fallo de datos, 2. no se ha posido solucionar la falla de "poder editar productos tanto con nombre como por ID (PID)" atención a esto antes de continuar 3. hacer los respectivos cambios en el submodulo ("2. editar producto" / linea 22:40 / menu\_productos)]



nota \[probar los demás modulos y posibles variables que pueda desarrollar el cliente antes de continuar, una vez que este en funcionamiento de lo básico, proseguir a continuar con el modulo de "registro de ventas por cliente"] 



nota \[al terminar el modulo "menu\_productos" crear un commit y subirlo a github]  

