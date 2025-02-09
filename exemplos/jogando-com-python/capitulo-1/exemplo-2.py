import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Atualizando a Tela")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill((0, 0, 0))  # Preenche a tela com preto
    
    # Desenha um retângulo vermelho
    pygame.draw.rect(tela, (255, 0, 0), (100, 100, 200, 150))

    pygame.display.update()  # Atualiza a tela para mostrar o retângulo

pygame.quit()