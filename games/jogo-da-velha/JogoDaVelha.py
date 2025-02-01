import pygame

class JogoDaVelha:
  offset: int = 50
  COLORS: dict = {
    'branco': (255, 255, 255),
    'cinza': (150, 150, 150),
    'preto': (0, 0, 0),
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'laranja': (255, 165, 0)
  }
  rows: int = 0
  cols: int = 0
  size: int = 0


  def tabuleiro(self, window, matriz, cor='preto'):
    if self.verifica_matriz(matriz):
      if self.size == 3:
        pygame.draw.line(window, self.COLORS[cor], (self.offset + 200, self.offset), (self.offset + 200, self.offset + 600), 9)
        pygame.draw.line(window, self.COLORS[cor], (self.offset + 400, self.offset), (self.offset + 400, self.offset + 600), 9)
        pygame.draw.line(window, self.COLORS[cor], (self.offset, self.offset + 200), (self.offset + 600, self.offset + 200), 9)
        pygame.draw.line(window, self.COLORS[cor], (self.offset, self.offset + 400), (self.offset + 600, self.offset + 400), 9)
      else:
        self.tabuleiro_didatico(window, cor)
    else:
      print('Matriz inválida')


  def tabuleiro_didatico(self, window, cor):
    cell_size = 500 // max(self.rows, self.cols)

    # Desenha as linhas verticais
    for i in range(1, self.size):
      x = self.offset + i * cell_size
      pygame.draw.line(window, self.COLORS[cor], (x, self.offset), (x, self.offset + self.size * cell_size), 9)

    # Desenha as linhas horizontais
    for i in range(1, self.size):
      y = self.offset + i * cell_size
      pygame.draw.line(window, self.COLORS[cor], (self.offset, y), (self.offset + self.size * cell_size, y), 9)

    # Desenha os números das posições
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 25, bold=True)
    for row in range(self.rows):
      for col in range(self.cols):
        x = self.offset + col * cell_size + cell_size // 2 - 17  # Ajuste de posição
        y = self.offset + row * cell_size + cell_size // 2 - 2 # Ajuste de posição
        text = font.render(f"({row},{col})", True, self.COLORS['verde'])  # Texto da posição
        window.blit(text, (x, y))  # Desenha o texto na tela


  def verifica_matriz(self, matriz) -> bool:
    if not isinstance(matriz, list):
      return False

    self.size = len(matriz)
    self.rows = self.size
    self.cols = self.size

    if self.size == 0:
      return True

    for l in matriz:
      if not isinstance(l, list):
        return False
      if len(l) != self.size:
        return False

    return True