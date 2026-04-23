import assets.config.globals as g
import scripts.scenes as scenes



class SceneManager():
    def __init__(self):
        self.current_scene = None
        self.next_scene = None
        self.previous_scene = None
    
    def update(self):
        if self.next_scene:
            self.previous_scene = self.current_scene
            self.current_scene = self.next_scene
            self.next_scene = None

    def change_scene(self, scene: object):
        self.next_scene = scene()