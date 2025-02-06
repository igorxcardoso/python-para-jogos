from JogoDaVelha import JogoDaVelha
from Janela import Janela

# Inicialização de uma janela
janela = Janela(
  resolucao_da_tela=(900, 700),
  cor_da_janela='branco',
  titulo_da_janela='Título da Janela'
)

# Inicialização do jogo da velha
jogo_da_velha = JogoDaVelha()

while True:
  # Atualiza a janela
  janela.atualizar()

  # Matriz n x n
  matriz = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
  ]

  # Criar um tabuleiro n x n
  jogo_da_velha.tabuleiro(janela, matriz)
