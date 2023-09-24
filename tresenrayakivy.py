""""juego de tres en raya automatico"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config

# Configuración inicial de la ventana
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')

class JuegoTresEnRaya(BoxLayout):
    """
    Clase principal que maneja la lógica del juego y la interfaz gráfica.
    """
    def __init__(self, **kwargs):
        """
        Inicializa la clase, establece la orientación y crea la interfaz.
        """
        super(JuegoTresEnRaya, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.debe_reiniciar = False  # Inicialización de la variable
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.puntuacion = 0
        self.tablero = ["", "", "", "", "", "", "", "", ""]
        self.botones = []  # Añadido aquí
        self.iniciar_interfaz()
        self.reiniciar()

    def reiniciar(self):
        """
        Reinicia las variables del juego para una nueva partida.
        """
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.puntuacion = 0
        self.tablero = ["", "", "", "", "", "", "", "", ""]
        self.actualizar_botones()

    def evaluar(self, board, depth):
        """
        Evalúa el tablero para determinar si hay un ganador.

        Argumentos:
        board -- el estado actual del tablero
        depth -- la profundidad actual en el árbol de juego

        Devuelve: puntuación basada en el estado del tablero
        """
        for (x, y, z) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if board[x] == board[y] == board[z] and board[x] != "":
                return (10 / (1 ** depth) if board[x] == "X" else -10) / (10 ** depth)
        return 0

    def minimax(self, board, depth, maximizing):
        """
        Implementa el algoritmo minimax para encontrar el mejor movimiento.

        Argumentos:
        board -- el estado actual del tablero
        depth -- la profundidad actual en el árbol de juego
        maximizing -- booleano que indica si se está maximizando o minimizando

        Devuelve: None
        """
        score = self.evaluar(board, depth)
        if score != 0:
            self.puntuacion += score
            return
        if "" not in board:
            return
        for i in range(len(board)):
            if board[i] == "":
                new_board = board.copy()
                new_board[i] = "X" if maximizing else "O"
                self.minimax(new_board, depth + 1, not maximizing)
                if depth == 1:
                    if self.puntuacion < self.mejor_puntuacion:
                        self.mejor_puntuacion = self.puntuacion
                        self.mejor_posicion = new_board
                    self.puntuacion = 0

    def jugar(self, indice):
        """
        Realiza un movimiento en el tablero en la posición dada.

        Argumentos:
        indice -- la posición en el tablero donde se realizará el movimiento
        """
        if self.tablero[indice] == "":
            self.tablero[indice] = "X"
            self.minimax(self.tablero, 1, False)

    def clic_boton(self, instance):
        """
        Maneja los eventos de clic en los botones del tablero.

        Argumentos:
        instance -- la instancia del botón que fue presionado
        """
        if self.debe_reiniciar:
            self.reiniciar()
            self.debe_reiniciar = False
            return
        if "" not in self.tablero or self.evaluar(self.tablero, 0) != 0:
            self.debe_reiniciar = True
        else:
            self.reiniciar_variables_jugada()

        indice = self.botones.index(instance)
        self.jugar(indice)
        if self.mejor_posicion is not None:
            self.tablero = self.mejor_posicion
        self.actualizar_botones()

        if "" not in self.tablero or self.evaluar(self.tablero, 0) != 0:
            self.debe_reiniciar = True
        else:
            # Reiniciar las variables después de cada jugada
            self.mejor_posicion = None
            self.mejor_puntuacion = 10
            self.puntuacion = 0
    def reiniciar_variables_jugada(self):
        """
        Reinicia las variables para una nueva jugada.
        """
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.puntuacion = 0
    def actualizar_botones(self):
        """
        Actualiza el texto de los botones según el estado del tablero.
        """
        for i in range(9):
            self.botones[i].text = self.tablero[i]

    def iniciar_interfaz(self):
        """
        Inicializa la interfaz gráfica del juego.
        """
        self.botones = []
        for i in range(3):
            h_layout = BoxLayout()
            for j in range(3):
                boton = Button(font_size=50)
                # pylint: disable=no-member
                boton.bind(on_press=self.clic_boton)
                self.botones.append(boton)
                h_layout.add_widget(boton)
            self.add_widget(h_layout)

class TresEnRayaApp(App):
    """
    Clase que inicia la aplicación.
    """
    def build(self):
        """
        Construye y devuelve la interfaz gráfica del juego.
        """
        return JuegoTresEnRaya()

if __name__ == '__main__':
    TresEnRayaApp().run()

