# -*- coding : utf-8 -*-
from JogoDaVelha import JogoDaVelha
from Janela import Janela


def verifica_fim_de_jogo(matriz_atual):
  campos_marcados = 0
  for y in range(3):
    for x in range(3):
      if matriz_atual[y][x] != '':
        campos_marcados += 1

  return True if campos_marcados == 9 else False


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
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ]

  # Desenha o tabuleiro
  jogo_da_velha.tabuleiro(janela, matriz)

  # Desenha os X e O
  jogo_da_velha.desenha_x_e_o(janela, 'vermelho', 'azul')

  # Verifica se houve vencedor
  jogo_da_velha.desenha_de_vitoria(janela)

  # Matriz atual
  matriz_atual = jogo_da_velha.matriz_do_tabuleiro

  # Verifica se o jogo acabou
  jogo_da_velha.fim_do_jogo = verifica_fim_de_jogo(matriz_atual)

  # Botões
  botao_de_novo_jogo = janela.botao((675, 225), (200, 75), 'verde', 'Novo Jogo')
  botao_de_reiniciar = janela.botao((675, 325), (200, 75), 'laranja', 'Reiniciar')
  botao_de_sair = janela.botao((695, 600), (150, 75), 'vermelho', 'Sair')

  if botao_de_sair == 'Sair':
    quit()
  elif botao_de_reiniciar == 'Reiniciar':
    jogo_da_velha.reiniciar_jogo()
  elif botao_de_novo_jogo == 'Novo Jogo':
    jogo_da_velha.novo_jogo()

  # Placar
  jogo_da_velha.placar(janela)

  # Atualiza a janela
  janela.atualizar()