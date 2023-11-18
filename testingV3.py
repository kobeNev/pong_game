
import pygame
 
pygame.init()
 
font = pygame.font.Font('freesansbold.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong_game")
 
clock = pygame.time.Clock()    
FPS = 30
 
 #classes

 
class Paddle:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.Rect = pygame.Rect(x, y, width, height)
        self.paddle = pygame.draw.rect(screen, self.color, self.Rect)

    def display(self):
        self.paddle = pygame.draw.rect(screen, self.color, self.Rect)
 
    def update(self, yFac):
        self.y = self.y + self.speed*yFac
 
        if self.y <= 0:
            self.y = 0

        elif self.y + self.height >= HEIGHT:
            self.y = HEIGHT-self.height
 
        self.Rect = (self.x, self.y, self.width, self.height)
 
    """def displayScore(self, text, score, x, y, color):
        text = font.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)"""
 
    def getRect(self):
        return self.Rect
 
 
class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.x, self.y), self.radius)
        self.firstTime = 1
 
    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.x, self.y), self.radius)
 
    def update(self):
        self.x += self.speed*self.xFac
        self.y += self.speed*self.yFac
 
        # If the ball hits the top or bottom surfaces, 
        # then the sign of yFac is changed and 
        # it results in a reflection
        if self.y <= 0 or self.y >= HEIGHT:
            self.yFac *= -1
 
        if self.x <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.x >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
 
    def reset(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.xFac *= -1
        self.firstTime = 1
 
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
 
    def getRect(self):
        return self.ball
 
# Game Manager
 
 
def main():
    running = True
 
    # Defining the objects
    paddle1 = Paddle(20, 0, 10, 100, 10, GREEN)
    paddle2 = Paddle(WIDTH-30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, BLUE)
 
    listOfPaddles = [paddle1, paddle2]
 
    # Initial parameters of the players
    YFac1, YFac2 = 0, 0
 
    while running:
        screen.fill(BLACK)
 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    YFac2 = -1
                if event.key == pygame.K_DOWN:
                    YFac2 = 1
                if event.key == pygame.K_w:
                    YFac1 = -1
                if event.key == pygame.K_s:
                    YFac1 = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    YFac2 = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    YFac1 = 0
 
        # Collision detection
        for paddle in listOfPaddles:
            if pygame.Rect.colliderect(ball.getRect(), paddle.getRect()):
                ball.hit()
 
        # Updating the objects
        paddle1.update(YFac1)
        paddle2.update(YFac2)
        point = ball.update()
 
        # Someone has scored
        # a point and the ball is out of bounds.
        # So, we reset it's position
        if point:   
            ball.reset()
 
        # Displaying the objects on the screen
        paddle1.display()
        paddle2.display()
        ball.display()
 
        pygame.display.update()
        clock.tick(FPS)     
 
 
if __name__ == "__main__":
    main()
    pygame.quit()