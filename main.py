import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from logger import log_state

def main():
    pygame.init()
    print("Starting Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    text_x = 10
    text_y = 10
    score_value = 0

    def draw_score(text_x, text_y):
        font = pygame.font.SysFont("Arial", 32)
        score_text = font.render("Score: " + str(score_value), 1, (255, 255, 255), None)
        screen.blit(score_text, (text_x, text_y))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield1 = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(color=(0, 0, 0))
        draw_score(text_x, text_y)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player1) == True:
                print("Game over!")
                print(f"Final Score: {score_value}")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
                    score_value += 1
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        log_state()

        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
