import pygame,sys,random,math
pygame.init()
# FUNCTIONS
over_font = pygame.font.Font(None,55)
def game_over():
    render = over_font.render(f"Game Over And Your Score Is {score}",True,(0,255,0))
    window.blit(render,(100,300))

def bullet(x,y):
    window.blit(bulletImg,(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 37:
        return True
    else:
        return False
    
font = pygame.font.Font(None,24)
def score_draw():
    render = font.render(f"Score Is {score}",True,(255,0,0))
    window.blit(render,(25,25))
window = pygame.display.set_mode((800,600))
bgc = pygame.image.load("assets/background.png")

playerImg = pygame.image.load("assets/player.png")
playerX = 336
playerMovement = 0

score = 0

bulletImg = pygame.image.load('assets/bullet.png')
bulletY = 400
bulletX = playerX
bullet_fired = False

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_movement = 0
num_enemy = 6

for i in range(num_enemy):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0,536))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(5)
    enemyY_change.append(50)
while True:
    window.blit(bgc,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerMovement = 15
            if event.key == pygame.K_LEFT:
                playerMovement = -15
            if event.key == pygame.K_SPACE:
                if bullet_fired == False:
                    bullet_fired = True
        if event.type == pygame.KEYUP:
            playerMovement = 0
    playerX += playerMovement

    # ENEMY 
    for i in range(num_enemy):
        if enemyY[i] >= 500:
            for j in range(num_enemy):
                enemyY[j] = 2100
            game_over()
            break
        
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 536:
           enemyX_change[i] = -5
           enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            score += 1
            enemyX[i] = random.randint(0,536)
        window.blit(enemyImg[i],(enemyX[i],enemyY[i]))
    print("loop endef")
    if bullet_fired:
        bulletY -= 15
        if bulletY <= 0:
            bulletY = 500
            bullet_fired = False
        bullet(bulletX,bulletY)
    if not bullet_fired:
        bulletY = 500
        bulletX = playerX
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    window.blit(playerImg,(playerX,500))
    score_draw()
    pygame.display.update()
    pygame.time.Clock().tick(120)