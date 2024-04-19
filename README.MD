# Proyecto de Aula Código Limpio

## Autores

Felipe Villa Jaramillo
Juan Pablo Cardona Bedoya
Josué Gómez Granda

## ¿Qué es y para qué es?

Se desarrolla un motor de encripción con el objetivo de proporcionar un mecanismo para que un emisor cifre un mensaje o información
sensible, para que un receptor autorizado o el emisor después puedan acceder al mensaje descifrado.

## ¿Cómo lo hacemos funcionar?

-Prerrequisitos: Hay que tener instalado un IDE de preferencia se recomienda el uso de VisualStudio Code ya que en este IDE fue desarrollado, tener instaladas las últimas versiones de Python y de pip disponibles.

Tener instalada la libreria kivy

Para instalarla por medio de pip (instalador de paquetes de python)

hay que hacer los siguientes pasos

En caso de ser usuario de los sistemas operativos Windows, macOS, Linux, BSD y RPi.

1. Abrir la terminal de python desde visual studio code
	- Para abrir la terminal de python es necesario ubicarse en la parte de arriba a la izquierda del visual studio code, darle click a la
	opción terminal, y seguidamente darle click a la opción new terminal o en español nueva terminal.

2. Instalar el kivy
	- Para instalar la librería kivy hay que copiar el siguiente comando en la terminal:
	python -m pip install "kivy[base]"
	cuando el comando ya este escrito en la terminal pulsa la tecla 'ENTER'.

- Para más información acerca de la instalación de Kivy, acceder a la documentación oficial: https://kivy.org/doc/stable/gettingstarted/installation.html


## ¿Cómo está hecho?

Las librerías usadas son math, y random, con las cuales se tendrán más opciones matemáticas y se podran generar los números aleatorios
necesarios para que el programa se ejecute correctamente.

Para la interfaz grafica, la libreria usada es kivy.

en cuanto a la organización de los módulos:

En el proyecto contamos con 2 carpetas principales src y tests.
Dentro de src contamos con otras dos carpetas, las cuales son las siguientes:

- encriptation_algorithm -> en esta carpeta se encuentra el archivo encriptation_algorithm.py donde esta la lógica necesaria para que el motor de encripción funcione correctamente junto con las excepciones

- encriptation_console -> en esta carpeta se encuentra el archivo encriptation_console.py donde se encuentra la implementación
para mostrar una interfaz por consola.

- GUI -> en esta carpeta se encuentra el archivo encryptation_gui.py, la implementación para ejecutar la aplicación con una interfaz gráfica.

Dentro de la carpeta tests contamos con un solo archivo, test_cases.py, en este archivo se encuentran 20 casos de prueba implementados , entre estos casos de prueba, hay 3 casos de prueba de encripción, 3 casos de prueba de desencripción, 8 casos de prueba de error (4 de encripción y 4 de desencripción). Finalmente 6 casos de prueba excepcionales (3 de encripción y 3 de desencripción)



## ¿Cómo usar el programa?


- Para ejecutar el programa de encripción desde la interfaz por consola, deberá ingresar el siguiente comando:
	- python3 app.py

- Para ejecutar el programa de encripción desde la interfaz gráfica de Kivy, deberá ingresar el siguiente comando:
	- python3 src/GUI/encryptation_gui.py

- En caso de encriptación: 
	1. Tienes que brindar el mensaje que desees encriptar
	2. El programa te pedirá la clave pública (public key) la cual deberás ingresar para cifrar el mensaje, los números que ingreses para esta deberán ser primos
	3. El programa te entregará el mensaje encriptado 

- En caso de desencriptación:
	1. Tienes que brindar el mensaje ya encriptado
	2. EL programa te pedirá la clave pública (public key) con la que fue cifrado el mensaje para poder desencriptarlo
	3. El programa te entregará el mensaje desencriptado


## ¿Cómo ejecutar los tests?

Para ejecutar los casos de prueba deberá de escrbir en la terminal de python el siguiente comando:
	- python3 tests/test_cases.py



