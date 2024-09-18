import curses
from random import randint

# Configurações da tela
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()  # Obtém a altura e largura da tela
w = curses.newwin(sh, sw, 0, 0)  # Cria uma nova janela
w.keypad(1)  # Habilita a entrada do teclado
w.timeout(100)  # Define o tempo limite de atualização da janela

# Inicializa a cobra e a comida
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]
w.addstr(int(food[0]), int(food[1]), "🍏")  # Adiciona a maçã

key = curses.KEY_RIGHT  # Inicia o jogo movendo para a direita

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calcula a nova posição da cobra
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Verifica colisões
    if (new_head[0] in [0, sh] or
        new_head[1] in [0, sw] or
        new_head in snake):
        curses.endwin()
        quit()

    # Adiciona a nova cabeça da cobra
    snake.insert(0, new_head)

    # Verifica se a cobra comeu a comida
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                randint(1, sh - 1),
                randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addstr(int(food[0]), int(food[1]), "🍏")  # Adiciona a nova maçã
    else:
        # Remove a cauda da cobra
        tail = snake.pop()
        w.addstr(int(tail[0]), int(tail[1]), ' ')  # Limpa a cauda

    # Desenha a cobra
    for segment in snake:
        w.addstr(int(segment[0]), int(segment[1]), "■")  # Desenha a cobra com um quadrado sólido
