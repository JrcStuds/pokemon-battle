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
        self.joysticks = {}

        g.pokemon_spritesheet = pygame.image.load("assets/images/pokemon.png").convert()

        g.scene_manager = scenes.SceneManager()
        g.scene_manager.change_scene(scenes.Menu())


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.JOYDEVICEADDED:   # assign new key to Joystick in dict
                joy = pygame.joystick.Joystick(event.device_index)
                self.joysticks[joy.get_instance_id()] = joy
            if event.type == pygame.JOYDEVICEREMOVED:   # remove corresponding instance of Joystick
                del self.joysticks[event.instance_id]

            # reset the keys being pressed this frame
            g.keys = {
                "up": False,
                "down": False,
                "left": False,
                "right": False,
                "a": False,
                "b": False
            }

            # go through each event that would represent a control
            if event.type == pygame.KEYDOWN:
                for k in g.CONTROLS.keys():
                    if event.key in g.CONTROLS[k]: g.keys[k] = True
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: g.keys["a"] = True
                if event.button == 1: g.keys["b"] = True
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 1:
                    if event.value <= -0.99: g.keys["up"] = True
                    if event.value >= 0.99: g.keys["down"] = True
                if event.axis == 0:
                    if event.value <= -0.99: g.keys["left"] = True
                    if event.value >= 0.99: g.keys["right"] = True
            if event.type == pygame.JOYHATMOTION:
                if event.value[1] == 1: g.keys["up"] = True
                if event.value[1] == -1: g.keys["down"] = True
                if event.value[0] == -1: g.keys["left"] = True
                if event.value[0] == 1: g.keys["right"] = True
                    
            # pass down the handle_event function to the current scene
            if hasattr(g.scene_manager.current_scene, "handle_event"):
                g.scene_manager.current_scene.handle_event(event)


    def update(self):
        # pass down the update function to the current scene
        if hasattr(g.scene_manager.current_scene, "update"):
            g.scene_manager.current_scene.update(self.dt)


    def draw(self):
        self.display.fill("black")

        # create a list of fblits from the current scene's draw function
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


