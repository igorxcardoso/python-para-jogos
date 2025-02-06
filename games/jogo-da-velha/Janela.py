# -*- coding : utf-8 -*-
import pygame

class Janela:
  configuracao = None
  # Cores disponíveis
  COLORS: dict = {
    'branco': (255, 255, 255),
    'cinza': (150, 150, 150),
    'preto': (0, 0, 0),
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'laranja': (255, 165, 0)
  }
  # Resoluções disponíveis
  RESOLUTIONS: dict = {
    'HD': (1280, 720),
    'FHD': (1920, 1080),
    'CUSTOM': (900, 700)
  }
  screen_resolution: str
  color: str
  window_title: str
  mouse: dict
  mouse_0: dict
  last_click_status: tuple

  def __init__(self, **kwargs) -> None:
    self.screen_resolution = kwargs.pop('resolucao_da_tela', 'CUSTOM')
    self.color = kwargs.pop('cor_da_janela', 'azul')
    self.window_title = kwargs.pop('titulo_da_janela', 'Nome da Janela')

    try:
      # Inicializa a janela 
      self.configuracao = pygame.display.set_mode(self.RESOLUTIONS[self.screen_resolution])

      # Define o título da janela
      pygame.display.set_caption(title=self.window_title)

      # Preenche a janela com a cor escolhida
      self.configuracao.fill(self.COLORS[self.color])

      # Informações do mouse
      self.mouse_0 = {'x': None, 'y': None, 'left button': None, 'clicked': False}
      self.mouse = ((0, 0), (False, False, False), (False, False, False))

      # Último estado de clique
      self.last_click_status = (False, False, False)

      self.home_menu = True
      self.pause_menu = False
      self.game_difficulty = 0
    except:
      print('Erro ao criar a janela')
  
  def atualizar(self) -> None:
    pygame.display.update()
  
  def verificar_eventos(self) -> None:
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.KEYDOWN:
      if pygame.key.name(event.key) == 'escape':
        ... 

    self.__preencher_janela()

  def __preencher_janela(self) -> None:
    pygame.draw.rect(self.configuracao, self.COLORS[self.color], (0, 0, self.configuracao.get_width(), self.configuracao.get_height()))


  def __mouse_clicou(self, input):
    if self.last_click_status == input:
      return False, False, False

    left_button = input[0] and not self.last_click_status[0]
    center_button = input[1] and not self.last_click_status[1]
    right_button = input[2] and not self.last_click_status[2]

    self.last_click_status = input
    return left_button, center_button, right_button


  def informacoes_do_mouse(self) -> None:
    self.verificar_eventos()
    mouse_position = pygame.mouse.get_pos()
    mouse_input = pygame.mouse.get_pressed()
    mouse_click = self.__mouse_clicou(mouse_input)
    self.mouse = (mouse_position, mouse_input, mouse_click)
    # print(mouse_position, mouse_input, mouse_click)


  def botao(self, position, size, color, text, index_of_qtd=(1, 1), border_color='preto', border_width=5, font_color='preto', text_size=32):
    width = self.configuracao.get_width()
    height = self.configuracao.get_height()

    if isinstance(position, tuple):
      x, y = position
    elif position == 'center':
      x = (width / 2) - (size[0] / 2)
      if index_of_qtd[1] > 1:
        btn_height = size[1] * index_of_qtd[1]
        gap_height = (size[1] / 2) * (index_of_qtd[1] - 1)
        total_height = btn_height + gap_height
        margin_y = (height - total_height) / 2
        y = margin_y + ((size[1] * 1.5) * (index_of_qtd[0] - 1))
      else:
        y = (height / 2) - (size[1] / 2)
    else:
      raise ValueError("Invalid position type. Must be tuple or 'center'.")

    # Draw Button Background
    pygame.draw.rect(self.configuracao, self.COLORS[color], (x, y, size[0], size[1]))

    # Efeito Hover
    if self.__mouse_is_over(x, y, size):
      self.transparent_surface(x, y, size[0], size[1])

    # Draw Button Border
    pygame.draw.rect(self.configuracao, self.COLORS[border_color], (x, y, size[0], size[1]), border_width)

    # Draw Button Text
    font = pygame.font.SysFont("Consolas", text_size, bold=True)
    text_surface = font.render(text, True, self.COLORS[font_color])
    text_x = x + (size[0] / 2) - (text_surface.get_width() / 2)
    text_y = y + (size[1] / 2) - (text_surface.get_height() / 2)
    self.configuracao.blit(text_surface, (text_x, text_y))

    # Direção de clique
    return text if self.__mouse_is_over(x, y, size) and self.mouse[2][0] else None


  def __mouse_is_over(self, x, y, size):
    mx, my = self.mouse[0]
    return x <= mx <= x + size[0] and y <= my <= y + size[1]


  def transparent_surface(self, position_x, position_y, size_x, size_y):
    surface = pygame.Surface((size_x, size_y))
    surface.set_alpha(128)
    surface.fill(self.COLORS['branco'])
    self.configuracao.blit(surface, (position_x, position_y))

