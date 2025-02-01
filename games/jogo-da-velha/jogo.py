from JogoDaVelha import JogoDaVelha
from Janela import Janela
import pygame

# Criação da janela para o jogo
janela = Janela(resolucao_da_tela='CUSTOM', cor_da_janela='vermelho', titulo_da_janela='Jogo da Velha')

# Cria a janela
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.KEYDOWN:
      if pygame.key.name(event.key) == 'escape':
        ...

  janela.atualizar()