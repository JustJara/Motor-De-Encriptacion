# Proyecto de Aula Codigo Limpio

## Autores

Josué Gómez Granda
Felipe Villa Jaramillo
Juan Pablo Cardona Bedoya

## ¿Qué es y para qué es?

Se desarrolla un motor de encripción con el objetivo de proporcionar un mecanismo para que un emisor cifre un mensaje o información
sensible, para que un receptor autorizado o el emisor después puedan acceder al mensaje descifrado.

## ¿Cómo lo hacemos funcionar?

-Prerrequisitos: Hay que tener instalado un IDE de preferencia se recomienda el uso de VisualStudio Code ya que en este IDE fue desarrollado, tener instalada la última versión de Python disponible.


## ¿Cómo está hecho?

Describir la arquitectura del proyecto, bibliotecas usadas, dependencias de otros proyectos

Las librerías usadas son math, y random, con las cuales se tendrán más opciones matemáticas y se podran generar los números aleatorios
necesarios para que el programa se ejecute correctamente.

en cuanto a la organización de los módulos:

En el proyecto contamos con 2 carpetas principales src y tests.
Dentro de src contamos con otras dos carpetas, las cuales son las siguientes:

- encriptation_algorithm -> en esta carpeta se encuentra el archivo encriptation_algorithm.py donde esta la lógica necesaria para que el motor de encripción funcione correctamente junto con las excepciones

- encriptation_console -> en esta carpeta se encuentra el archivo encriptation_console.py donde se encuentra la implementación
para mostrar una interfaz por consola.

Dentro de la carpeta tests contamos con un solo archivo, test_cases.py, en este archivo se encuentran 20 implementados 20 casos de prueba, entre estos casos de prueba hay 3 casos de prueba de encripción, 3 casos de prueba de desencripción, 8 casos de prueba de error (4 de encripción y 4 de desencripción) y finalmente 6 casos de prueba excepcionales (3 de encripción y 3 de desencripción)

## ¿Cómo puede usarlo el usuario?

- En caso de encriptación: 
	1. Tienes que brindar el mensaje que desees encriptar
	2. El programa te pedirá la clave pública (public key) la cual deberás ingresar para cifrar el mensaje, los números que ingreses para esta deberán ser primos
	3. El programa te entregará el mensaje encriptado 

- En caso de desencriptación:
	1. Tienes que brindar el mensaje ya encriptado
	2. EL programa te pedirá la clave pública (public key) con la que fue cifrado el mensaje para poder desencriptarlo
	3. El programa te entregará el mensaje desencriptado



