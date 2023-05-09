# José Antonio Sánchez Villicaña
## Tarea 4 - Programación en Python
### Antecedentes
La finalidad de este programa es poner en práctica las sentencias de manejo de archivos, como utilizar una ruta absoluta para acceder a un archivo, extraer su contenido, crear un archivo, escribir en un archivo, etc. También se pone en práctica el uso de expresiones regulares.

### Problema
El programa va a recibir un archivo de texto con una secuencia de DNA y lo va a convertir en un archivo tipo fasta con esa secuencia.

### Metodología
1. Pedimos la ruta absoluta del archivo de texto con la secuencia de DNA
2. Pedimos la ruta absoluta del directorio donde vamos a guardar el archivo fasta convertido
3. Pedimos el nombre del archivo de salida (sin la extensión fasta)
4. Abrimos el archivo de texto, extraemos el contenido
5. Creamos el archivo fasta, le damos el formato fasta, agregamos el contenido del archivo de texto
6. Cerramos archivos

### Observaciones
Por algún motivo no me dejaba meter la sección de TESTING en en el encabezado, me aparecia el error **'SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 1370-1371: truncated \UXXXXXXXX escape'** y sólo pude resolverlo poniendo la sección fuera del encabezado. Intenté poner la ruta entre comillas, mover la sección en la parte de en medio del encabezado, nada me funcionó excepto sacar la sección por completo.

### Resultados

Imagen adjunta en carpeta doc de esta tarea.