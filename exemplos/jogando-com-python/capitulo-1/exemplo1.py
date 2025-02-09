import pygame

pygame.init()  # Inicializa o Pygame
tela = pygame.display.set_mode((800, 600))  # Cria a janela
pygame.display.set_caption("Meu Jogo com Pygame")  # Define o título da janela

rodando = True
while rodando:
  # Fechar a janela
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      rodando = False
