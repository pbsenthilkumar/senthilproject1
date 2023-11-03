import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 10
ENEMY_COUNT = 5
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)
BULLET_COLOR = (0, 0, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player
player_width, player_height = 50, 50
player_x = (WIDTH - player_width) / 2
player_y = HEIGHT - player_height
player_x_change = 0

# Enemy
enemies = []
enemy_width, enemy_height = 50, 50
for _ in range(ENEMY_COUNT):
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = random.randint(50, 200)
    enemies.append([enemy_x, enemy_y])

# Bullet
bullet_width, bullet_height = 10, 30
bullet_x = 0
bullet_y = HEIGHT
bullet_state = "ready"  # "ready" or "fire"

# Score
score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(window, PLAYER_COLOR, (x, y, player_width, player_height))

# Function to draw an enemy
def draw_enemy(x, y):
    pygame.draw.rect(window, ENEMY_COLOR, (x, y, enemy_width, enemy_height))

# Function to fire a bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(window, BULLET_COLOR, (x + player_width / 2 - bullet_width / 2, y, bullet_width, bullet_height))

# Function to check for collisions
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if enemy_x < bullet_x < enemy_x + enemy_width and enemy_y < bullet_y < enemy_y + enemy_height:
        return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_x_change = PLAYER_SPEED
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Move the player
    player_x += player_x_change

    # Boundaries for the player
    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # Move the enemy
    for i in range(ENEMY_COUNT):
        enemies[i][1] += ENEMY_SPEED
        if enemies[i][1] > HEIGHT:
            enemies[i][0] = random.randint(0, WIDTH - enemy_width)
            enemies[i][1] = random.randint(50, 200)

        # Collision detection
        collision = is_collision(enemies[i][0], enemies[i][1], bullet_x, bullet_y)
        if collision:
            bullet_state = "ready"
            bullet_y = HEIGHT
            score += 1
            enemies[i][0] = random.randint(0, WIDTH - enemy_width)
            enemies[i][1] = random.randint(50, 200)

        draw_enemy(enemies[i][0], enemies[i][1])

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= BULLET_SPEED

    # Bullet boundaries
    if bullet_y <= 0:
        bullet_state = "ready"
        bullet_y = HEIGHT

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the player
    draw_player(player_x, player_y)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.update()

# Quit the game
pygame.quit()