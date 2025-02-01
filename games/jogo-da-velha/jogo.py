from JogoDaVelha import JogoDaVelha
from Janela import Janela
import pygame


def verifica_fim_de_jogo(self):
  ...



# Criação da janela para o jogo
janela = Janela(resolucao_da_tela='CUSTOM', cor_da_janela='branco', titulo_da_janela='Jogo da Velha')

jogo_da_velha = JogoDaVelha()

# Cria a janela
while True:
  # Verifica os eventos da janela
  janela.verificar_eventos()

  janela.informacoes_do_mouse()

  # Desenha o tabuleiro
  matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
  ]
  jogo_da_velha.tabuleiro(janela.configuracao, matriz)

  # Atualiza a janela
  janela.atualizar()