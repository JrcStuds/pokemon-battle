import pygame
import assets.config.settings as s
import scripts.scenes as scenes



class SceneManager():
    def __init__(self):
        self.current_scene = None
        self.next_scene = None
    
    def update(self):
        if self.next_scene:
            self.current_scene = self.next_scene
            self.next_scene = None

    def change_scene(self, scene: object):
        self.next_scene = scene()



class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(s.DISPLAY_SIZE, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        s.scene_manager = SceneManager()
        s.scenes = {
            "menu": scenes.Menu,
            "battle": scenes.Battle
        }
        s.scene_manager.change_scene(s.scenes["menu"])


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if hasattr(s.scene_manager.current_scene, "handle_event"):
                s.scene_manager.current_scene.handle_event(event)


    def update(self):
        if hasattr(s.scene_manager.current_scene, "update"):
            s.scene_manager.current_scene.update(self.dt)


    def draw(self):
        self.display.fill("black")

        fblits = []
        if hasattr(s.scene_manager.current_scene, "draw"):
            fblits.extend(s.scene_manager.current_scene.draw())
        self.display.fblits(fblits)

        pygame.display.flip()


    def run(self):
        while self.running:
            s.scene_manager.update()
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(s.FPS) / 1000
        
        pygame.quit()



if __name__ == "__main__":
    game = Game()
    game.run()


