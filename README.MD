 # Proyecto de Aula Código Limpio

## Autores

- Felipe Villa Jaramillo
- Juan Pablo Cardona Bedoya
- Josué Gómez Granda

## ¿Qué es y para qué es?

Se desarrolla un motor de encripción con el objetivo de proporcionar un mecanismo para que un emisor cifre un mensaje o información
sensible, para que un receptor autorizado o el emisor después puedan acceder al mensaje descifrado.

## ¿Cómo lo hacemos funcionar?

- Prerrequisitos: 
	1. Tener instaladas las últimas versiones de Python y de pip disponibles.

	2. Tienes 2 opciones, se recomienda el uso del entorno virtual.
		1. Deberás crear un entorno virtual utilizando virtualenv, ejecuta los siguientes comandos 1 por 1:
			- <pre>python -m venv my_project</pre>
			- Si estás en Windows ejecuta el siguiente comando:
			<pre>my_project\Scripts\activate</pre>
			- Si estás en MacOS o alguna distribución de Linux:
			<pre>source my_project/bin/activate</pre>

			- Después de tener crear el entorno virtual y activarlo deberías de ver algo similar a esto:
				- (my_project) /encryption_engine$

			- Instalar las librerias necesarias para ejecutar el proyecto:
				- Kivy <pre>pip install "kivy[base]"</pre>
				- psycopg2 <pre>pip install psycopg2-binary</pre>
				
		2. Realizar todo el siguiente procedimiento sin crear el entorno virtual:

			- Instalar la libreria kivy

				- Para instalarla por medio de pip (instalador de paquetes de python) ejecute el siguiente comando en la terminal:
					<pre>python -m pip install "kivy[base]"</pre>

				- Para más información acceder a la documentación oficial: https://kivy.org/doc/stable/gettingstarted/installation.html

			- Instalar la libreria psycopg2-binary

				- Para instalarla por medio de pip ejecutar el siguiente comando en la terminal de preferencia:
				<pre>pip install psycopg2-binary</pre>

				- Para más información consultar la documentación original: https://www.psycopg.org/docs/
	
	3. Tener una base de datos en Neon Tech

		- Para crearla debes ir a la pagina oficial de Neon Tech: https://neon.tech.

			1. Debes iniciar sesión en su sitio web, o registrarte si no tinenes una cuenta creada.

			2. Creas un nuevo proyecto.
			
			3. Te diriges al apartado que dice "Dashboard".
			
			4. En el apartado Database, selecciona la base de datos donde quieras guardar la base de datos y su información.

			5. Haz click donde dice "ConnectionString", se desplegará un menú.
			
			6. Selecciona la que dice "Parameters only".
			
		- ¿Qué hacer con la información?.

			1. Una vez la página te muestre los parámetros de la base de datos dírigete a la carpeta "src".

			2. Allí deberás entrar a la carpeta "controller".
			
			3. En la carpeta controller, entra al archivo "secret_config_example".
			
			4. Finalmente deberás seguir los pasos indicados en el archivo 'secret_config_example.py' para continuar
			con el proceso de conexión con la base de datos.
			
## ¿Cómo está hecho?

Las librerías usadas son math, y random, con las cuales se tendrán más opciones matemáticas y se podran generar los números aleatorios
necesarios para que el programa se ejecute correctamente.

Para la interfaz grafica, la libreria usada es kivy.

En cuanto a la base de datos, se utilizó PostgreSQL con la libreria de python psycopg2 que permite la conexión de la base de datos y el programa.

en cuanto a la organización de los módulos:

- En el proyecto contamos con 3 carpetas principales sql_sentences, src y tests:

	1. Dentro de sql_sentences contamos con todas las sentencias necesarias para realizar las diferentes consultas que requiere el programa.

	2. Dentro de src contamos con otras cuatro carpetas, las cuales son las siguientes:
		
		- console -> en esta carpeta se encuentra el archivo encriptation_console.py donde se encuentra la implementación
		para mostrar una interfaz por consola.

		- controller -> en esta carpeta se encuentra el archivo database_controller.py donde se encuentra la implementación
		para controlar las consultas hacia la base de datos. Por otro lado se encuentra el archivo secret_config_example.py en donde se deja una plantilla
		para que el usuario que ejecutará la aplicación haga la conexión a su base de datos propia.

		- encriptation_algorithm -> en esta carpeta se encuentra el archivo encriptation_algorithm.py donde esta la lógica necesaria para que el motor de encripción funcione correctamente junto con las excepciones

		- GUI -> en esta carpeta se encuentra el archivo encryptation_gui.py, la implementación para ejecutar la aplicación con una interfaz gráfica.

	3. Dentro de la carpeta tests contamos con otras dos carpetas, las cuales son las siguientes:

		- database_tests -> en esta carpeta se almacena un archivo llamado database_test_cases.py el cual contiene todos los casos de prueba para la base de datos.

		- encryption_engine_tests -> en esta carpeta se almacena un archivo llamado test_cases.py el cual contiene todos los casos de prueba para el motor de encripción.

## ¿Cómo usar el programa?

- Antes de ejecutar cualquier comando, es necesario que hagas una copia del archivo 'secret_config_example.py' y renombrarlo de la siguiente manera:
'secret_config.py', dentro de este archivo que copiaste es donde insertaras tus credenciales de NeonTech para poder hacer uso de la base de datos. Si no se hace este paso el programa no funcionará.


- Para ejecutar el programa de encripción desde la interfaz por consola, deberá ingresar el siguiente comando:
	- <pre>python app.py</pre>

- Para ejecutar el programa de encripción desde la interfaz gráfica de Kivy, deberá ingresar el siguiente comando:
	- <pre>python src/GUI/encryptation_gui.py</pre>

- En caso de encriptación: 
	1. Tienes que brindar el mensaje que desees encriptar.
	2. El programa te pedirá la clave pública (public key) la cual deberás ingresar para cifrar el mensaje, los números que ingreses para esta deberán ser primos.
	3. El programa te entregará el mensaje encriptado.
	4. Puedes guardar el mensaje dando click en el botón 'Guardar mensajes'.
	
- En caso de desencriptación:
	1. Tienes que brindar el mensaje ya encriptado.
	2. EL programa te pedirá la clave pública (public key) con la que fue cifrado el mensaje para poder desencriptarlo.
	3. El programa te entregará el mensaje desencriptado.

- En caso de Registrar su usuario:
	1. Tienes que ingresar un nombre de usuario en el campo indicado.
	2. Tienes que ingresar la contraseña en el campo indicado.
	3. Tienes que confirmar tu contraseña ingresada anteriormente en el campo indicado.

- En caso de Iniciar Sesión:
	1. Tienes que ingresar tu nombre de usuario con el que te registraste.
	2. Tienes que ingresar la contraseña con la que registraste tu nombre de usuario.

## ¿Cómo ejecutar los tests?

Para ejecutar los casos de prueba deberá de escrbir en la terminal de python los siguientes comandos:
- Este ejecutará los casos de prueba para el motor de encripción:
<pre>python tests/encryption_engine_tests/test_cases.py</pre>

- Este ejecutará los casos de prueba para la base de datos:
<pre>python tests/database_tests/database_test_cases.py</pre>



