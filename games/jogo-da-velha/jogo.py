from JogoDaVelha import JogoDaVelha
from Janela import Janela
import pygame

# Criação da janela para o jogo
janela = Janela(resolucao_da_tela='CUSTOM', cor_da_janela='vermelho', titulo_da_janela='Jogo da Velha')

jogo_da_velha = JogoDaVelha()

# Cria a janela
while True:
  # Verifica os eventos da janela
  janela.verificar_eventos()

  # Desenha o tabuleiro
  matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
  ]
  jogo_da_velha.tabuleiro(janela.configuracao, matriz)

  # Atualiza a janela
  janela.atualizar()