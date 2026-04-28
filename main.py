import pygame
import assets.config.globals as g
import scripts.scenes as scenes



class Game():
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        self.display = pygame.display.set_mode(g.DISPLAY_RECT.size, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        g.scene_manager = scenes.SceneManager()
        g.scenes = { "menu": scenes.Menu, "battle": scenes.Battle }
        g.scene_manager.change_scene(g.scenes["battle"])


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.JOYDEVICEADDED:
                self.joysticks.append(pygame.joystick.Joystick(event.device_index))
            if event.type == pygame.JOYDEVICEREMOVED:
                self.joysticks.remove(event.instance_id)

            if hasattr(g.scene_manager.current_scene, "handle_event"):
                g.scene_manager.current_scene.handle_event(event)


    def update(self):
        if hasattr(g.scene_manager.current_scene, "update"):
            g.scene_manager.current_scene.update(self.dt)


    def draw(self):
        self.display.fill("black")

        fblits = []
        if hasattr(g.scene_manager.current_scene, "draw"):
            fblits.extend(g.scene_manager.current_scene.draw())
        self.display.fblits(fblits)

        pygame.display.flip()


    def run(self):
        while self.running:
            g.scene_manager.update()
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(g.FPS) / 1000
        
        pygame.joystick.quit()
        pygame.quit()



if __name__ == "__main__":
    game = Game()
    game.run()


