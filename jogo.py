import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Cancele a Física ")
altura = 566
largura = 1080
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/fundo.jpg")
newton = pygame.image.load("assets/newton.png")
maça = pygame.image.load("assets/maça.png")




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("A Física Jamais será derrotada !!",True,branco)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    newtonX = 500
    newtonY = 400
    movimentoNewtonX = 0
    larguraNewton = 120
    alturaNewton = 110
    alturaMaça = 250
    larguraMaça = 50
    posicaoMaçaX = 400
    posicaoMaçaY = -240
    velocidadeMaça = 1
    pontos = 0
    pygame.mixer.music.load("assets/musicafundo.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    maçaSound = pygame.mixer.Sound("assets/sommaça.mp3")
    maçaSound.set_volume(1)
    pygame.mixer.Sound.play(maçaSound)

    batida = pygame.mixer.Sound("assets/batida.mp3")
    batida.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoNewtonX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoNewtonX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoNewtonX = 0
            
        if jogando:
            if posicaoMaçaY > altura:
                posicaoMaçaY = -240
                posicaoMaçaX = random.randint(0,largura)
        
                pontos = pontos + 1
                pygame.mixer.Sound.play(maçaSound)
            else:
                posicaoMaçaY =posicaoMaçaY + velocidadeMaça

            if newtonX + movimentoNewtonX >0 and newtonX + movimentoNewtonX< largura-larguraNewton:
                newtonX = newtonX + movimentoNewtonX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(newton, (newtonX,newtonY))
            
            gameDisplay.blit(maça, (posicaoMaçaX,posicaoMaçaY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXNewton = list(range(newtonX, newtonX+larguraNewton))
            pixelsYNewton = list(range(newtonY, newtonY+alturaNewton))

            pixelXMaça = list(range(posicaoMaçaX, posicaoMaçaX+larguraMaça))
            pixelYmaça = list(range(posicaoMaçaY, posicaoMaçaY+alturaMaça))

            colisaoY = len(list(set(pixelYmaça) & set(pixelsYNewton) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMaça) & set(pixelsXNewton) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batida)


        pygameDisplay.update()
        clock.tick(60)

jogar()

