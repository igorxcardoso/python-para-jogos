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

  # Informações do mouse
  janela.informacoes_do_mouse()

  # Evento de clique no tabuleiro  
  jogo_da_velha.evento_de_clique(janela)

  # Desenha o tabuleiro
  matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
  ]

  # Desenha o tabuleiro
  jogo_da_velha.tabuleiro(janela.configuracao, matriz)

  # Desenha os X e O
  jogo_da_velha.desenha_x_e_o(janela, 'vermelho', 'azul')

  # Atualiza a janela
  janela.atualizar()