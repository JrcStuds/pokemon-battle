import pygame, random
import assets.config.settings as settings
from scripts.scenes.battle import Battle
from scripts.scenes.menu import Menu



class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(settings.DISPLAY_SIZE, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        self.scene = Menu(self)


    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                
                case pygame.QUIT:
                    self.running = False

                case pygame.MOUSEBUTTONDOWN:
                    for element in self.scene.elements:
                        if hasattr(element, "is_clicked"):
                            element.is_clicked(pygame.mouse.get_pos())


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
            self.dt = self.clock.tick(settings.FPS) / 1000
        
        pygame.quit()


    def change_scene(self, scene, type):
        if scene == "menu" and type == "random":
            self.scene = Menu(self, f"menu {random.randint(1, 10)}")



if __name__ == "__main__":
    game = Game()
    game.run()


