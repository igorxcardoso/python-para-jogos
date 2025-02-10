from JogoDaVelha import JogoDaVelha
from Janela import Janela

# Inicialização de uma janela
janela = Janela(
  resolucao_da_tela=(900, 700),
  cor_da_janela='branco',
  titulo_da_janela='Jogo da Velha'
)

# Inicialização do jogo da velha
jogo_da_velha = JogoDaVelha()

while True:
  # Informações do mouse
  janela.informacoes_do_mouse()

  # Evento de clique no tabuleiro  
  jogo_da_velha.evento_de_clique(janela)

  # Desenha o tabuleiro
  matriz = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ]

  # Desenha o tabuleiro
  jogo_da_velha.tabuleiro(janela, matriz)

  # Desenha os X e O
  jogo_da_velha.desenha_x_e_o(janela, 'laranja', 'azul')

  # Atualiza a janela
  janela.atualizar()