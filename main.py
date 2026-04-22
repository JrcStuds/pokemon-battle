import pygame, random
import assets.config.settings as settings
from scripts.battle.battle import Battle
from scripts.menu.menu import Menu



class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(settings.DISPLAY_SIZE, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        self.scene = Menu()


    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                
                case pygame.QUIT:
                    self.running = False

                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            self.scene = Menu(f"This is menu {random.randint(1, 10)}")
                            print("spacebar pressed")


    def update(self):
        pass


    def draw(self):
        self.display.fill("black")

        fblits = []
        fblits.append((self.scene.draw(), (0, 0)))
        self.display.fblits(fblits)

        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000
        
        pygame.quit()



if __name__ == "__main__":
    game = Game()
    game.run()


