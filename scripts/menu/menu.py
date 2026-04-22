from scripts.ui.scene import SceneBaseClass
from scripts.ui.text import Text



class Menu(SceneBaseClass):
    def __init__(self, header: str = ""):
        super().__init__()

        self.background = "#ffffff"
        self.elements.append(Text((0, 0), header))