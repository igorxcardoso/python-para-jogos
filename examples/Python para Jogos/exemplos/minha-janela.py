from Janela import Janela

# Inicialização de uma janela
janela = Janela(
  resolucao_da_tela=(900, 700),
  cor_da_janela='branco',
  titulo_da_janela='Título da Janela'
)

while True:
  # Atualiza a janela
  janela.atualizar()