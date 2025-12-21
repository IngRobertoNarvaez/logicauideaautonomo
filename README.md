Link Canva Presentacion

https://www.canva.com/design/DAG7t2NRklY/jhRHHuxn1yw3z8_MEDkl6w/edit?utm_content=DAG7t2NRklY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


Dentro del proyecto se uso el lenguaje Python para resolver el final del proyecto donde de igual forma se uno librerias de Py

El propósito principal de tu juego es crear una simulación interactiva que demuestre conceptos fundamentales de programación, lógica y diseño de videojuegos en Python usando Pygame.

Python
Qué es: Un lenguaje de programación de alto nivel, fácil de leer y aprender.
Para qué se usó:
Programar toda la lógica del juego 
Manejar eventos del teclado 
Dibujar los gráficos y actualizar la pantalla normalmente usando librerías como Pygame

Pygame 
Una librería de Python para crear videojuegos.
Para qué se usó:
Dibujar la ventana del juego, paletas, pelota y texto.
Controlar la actualización de pantalla y animaciones.
Gestionar entrada del usuario y sonidos.

VS Code (Visual Studio Code)
Un editor de código muy popular, ligero y con muchas extensiones.
Para qué se usó:
Escribimos el código fuente en Python.
Ayuda con resaltado de sintaxis, autocompletado y depuración.
Permite organizar los archivos del proyecto y ejecutar scripts directamente.

Lo imp0ortante usado para el codigo 

import pygame: importar la biblioteca Pygame Sirve para crear el juego en este caso

import sys: importar el módulo del sistema que nos sirve para el cierre correcto

import random: importar el módulo de funciones aleatorias que nos sirve para el movimiento de la pelota

pygame.init(): Es la función encargada de iniciar todos los módulos de Pygame como son ventanas, fuentes, sonido, eventos, permitiendo que el resto del juego funcione correctamente.

WIDTH y HEIGHT para establecer el tamaño de la pantalla.

pygame.display.set_mode() se usó para crear la ventana del juego.

pygame.display.set_caption() sirvió para ponerle el nombre “PONG” a la ventana.

clock = pygame.time.Clock() controla la velocidad del juego

player_paddle = pygame.Rect:  crea la paleta del jugador y la coloca en la izquierda.

enemy_paddle = pygame.Rect: crea la paleta del enemigo y la coloca en la derecha.

ball = pygame.Rect: crea la pelota en el centro.

ball_dx:  dirección horizontal inicial (derecha o izquierda).

ball_dy: dirección vertical inicial (arriba o abajo).

draw_menu()
limpia la pantalla
dibuja el título “PONG”
dibuja opciones “Jugar” y “Salir”

reset_ball()
pone la pelota en el centro
le da nueva dirección aleatoria

main_game()
mueve paletas
mueve pelota
detecta rebotes
suma puntos
dibuja todo
detecta ganador

En mi caso para poder ejecutar el proyecto Pong tuve que recurrir al PowerShell debido a que una mala instalacion y configuracion del PY y VSCODE no me deja emular en el terminal del mismo y par lograr esa
emulacin se uso lo siguiente 

Python

cd "C:\Users\narva\Documents\Proyecto final"
dir
py -3.12 pong.py



