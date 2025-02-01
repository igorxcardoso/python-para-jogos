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

  def __init__(self, **kwargs) -> None:
    try:
      self.screen_resolution = kwargs.pop('resolucao_da_tela', 'CUSTOM')
      self.color = kwargs.pop('cor_da_janela', 'azul')
      self.window_title = kwargs.pop('titulo_da_janela', 'Nome da Janela')

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