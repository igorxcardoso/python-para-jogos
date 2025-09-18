# -*- coding : utf-8 -*-
from JogoDaVelha import JogoDaVelha
from Janela import Janela

# Inicialização de uma janela
janela = Janela(resolucao_da_tela='CUSTOM', cor_da_janela='branco', titulo_da_janela='Jogo da Velha')

# Inicialização do jogo da velha
jogo_da_velha = JogoDaVelha()

while True:
  # Verifica eventos
  janela.verificar_eventos()

  # Desenha o tabuleiro
  


  matriz = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ]

  jogo_da_velha.tabuleiro(janela, matriz, 'preto', True)

  # Atualiza a janela
  janela.atualizar()