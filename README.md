# SMART HORSES 
## Introducción
Es un juego entre dos adversarios en el que cada uno controla un caballo sobre
un tablero de ajedrez. En el tablero hay siete casillas que le permiten obtener de 1 a 7 puntos
al primer caballo que las alcance. El objetivo del juego es obtener más puntos que el adversario.
El juego termina cuando no queden más casillas con puntos. A continuación se muestra un posible
estado inicial del juego. Las posiciones iniciales de los caballos y de las siete casillas con puntos
son aleatorias.

<p align="center">
  <img src="https://i.postimg.cc/63Fnh7Rz/Captura-de-pantalla-2023-06-21-14-36-34.png" alt="Nuestro tablero de la app">
</p>

## Aclaraciones
Smart horses presenta tres niveles de dificultad (principiante, amateur, y experto) que el
usuario puede seleccionar al iniciar el juego. Se debe construir un árbol minimax con decisiones
imperfectas. La profundidad límite del árbol depende del nivel seleccionado por el usuario. Para
el nivel principiante se utiliza un árbol de profundidad 2, para amateur de profundidad 4, y para
experto de profundidad 6.

# PASOS A SEGUIR PARA INICIAR EL JUEGO
- Descargar el archivo por medio del git clone o por zip
- Situarte con la terminal en la raiz de la carpeta creada en la descarga y ejecutar el comando **python3 main.py run** o **python main.py run** dependiendo de cual tengas
- Te saldrá la siguiente interfaz

<p align="center">
  <img src="https://i.postimg.cc/C5fHyCYW/Captura-de-pantalla-2023-06-21-14-49-25.png" alt="Nuestra interfaz inicial">
</p>

Le debes dar a "Jugar" para iniciar el juego o "Créditos" para saber el nombre de sus creadoras.

- Esta es la interfaz al darle en el botón "Jugar"

<p align="center">
  <img src="https://i.postimg.cc/FsCdbk4S/Captura-de-pantalla-2023-06-21-14-54-16.png" alt="Nuestra interfaz de juego">
</p>

Aquí debes seleccionar el modo de juego para que se despliegue el tablero con el que vas a jugar.
