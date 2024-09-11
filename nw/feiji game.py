import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen_width = 1500
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("飞机大战")

# 加载图像
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")  
bullet_img = pygame.image.load("bullet.png")

# 玩家类
class Player:
    def __init__(self):
        self.image = player_img
        self.x = screen_width // 2
        self.y = screen_height - 100
        self.x_change = 0

    def move(self):
        self.x += self.x_change
        if self.x < 0:
            self.x = 0
        elif self.x > screen_width - self.image.get_width():
            self.x = screen_width - self.image.get_width()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# 敌人类
class Enemy:
    def __init__(self):
        self.image = enemy_img
        self.x = random.randint(0, screen_width - self.image.get_width())
        self.y = random.randint(-100, -40)
        self.y_change = 1 #random.randint(1, 3)

    def move(self):
        self.y += self.y_change
        if self.y > screen_height:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, screen_width - self.image.get_width())

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# 子弹类
class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.x = x
        self.y = y
        self.y_change = -5

    def move(self):
        self.y += self.y_change

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# 检查碰撞
def is_collision(enemy, bullet):
    distance = ((enemy.x - bullet.x) ** 2 + (enemy.y - bullet.y) ** 2) ** 0.5
    return distance < 27

# 创建玩家对象
player = Player()

# 创建敌人列表
enemies = [Enemy() for _ in range(1)]

# 创建子弹列表
bullets = []

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -5
            elif event.key == pygame.K_RIGHT:
                player.x_change = 5
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.x + player.image.get_width() // 2 - bullet_img.get_width() // 2, player.y)
                bullets.append(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0

    # 移动玩家
    player.move()

    # 移动敌人
    for enemy in enemies:
        enemy.move()

    # 移动子弹
    for bullet in bullets:
        bullet.move()

    # 检查碰撞
    for enemy in enemies:
        for bullet in bullets:
            if is_collision(enemy, bullet):
                bullets.remove(bullet)
                enemy.y = random.randint(-100, -40)
                enemy.x = random.randint(0, screen_width - enemy.image.get_width())

    # 绘制屏幕
    screen.fill((0, 0, 0))
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()

    # 更新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
