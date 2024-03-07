import pygame

def movimentar(x, y, velocidade):
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    return x,y 

pygame.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Primeiro jogo em Python")


janela_aberta = True
x = 400
y = 300
velocidade = 10

while janela_aberta:   
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        
    x,y = movimentar(x, y, velocidade)

    janela.fill((0,0,0))
    

    pygame.draw.circle(janela, (0, 0, 255), (x,y), 50)
    pygame.display.update()

pygame.quit()