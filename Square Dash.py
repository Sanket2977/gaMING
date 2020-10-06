import pygame
pygame.init()
win = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Game of Squares")
bluex = 100
bluey = 100
redX = 500
redY = 500
bluevel =100
redVel =100
run = True

def drawGame():
     win.fill((25,215,69))
     pygame.draw.rect(win, (23, 3, 255), (bluex, bluey, 20,20))
     pygame.draw.rect(win, (4, 1,2), (redX, redY, 40, 40))
     pygame.display.update()

while run:
      pygame.time.delay(100)

      if redX < bluex - 10:
          redX = redX + redVel 
          drawGame() 
      elif redX > bluex + 10:
          drawGame()
          redX = redX - redVel
      elif redY < bluey - 10: 
          redY = redY + redVel 
      elif redY > bluey + 10:
          redY = redY - redVel
      else:
          run = False
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
            bluex -= bluevel

      if keys[pygame.K_RIGHT]:
            bluex += bluevel
      
      if keys[pygame.K_UP]:
            bluey -= bluevel
      
      if keys[pygame.K_DOWN]:
            bluey += bluevel
      
      drawGame()
          
pygame.quit()  

