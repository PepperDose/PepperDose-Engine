from DSEngine import *
from pygame import Vector2
from pygame.key import *
from sys import exit

class Player:
    def __init__(self, init_pos=Vector2(0, 0), def_img="Test.png"):
        self.position = init_pos
        self.default_img = Image2D(def_img)
        self.sheet1 = Spritesheet(0, "Test.png", "Test1.png")
        self.animsheet = AnimationSheet(self.default_img, walk=self.sheet1)
        self.player = AnimatedSprite2D(self.animsheet, 1, self.position)
    
    def render(self, window: Window):
        movement = Vector2(0, 0)
        if window.pressed_keys[K_w]:
            movement.y -= 0.1
        if window.pressed_keys[K_s]:
            movement.y += 0.1
        if window.pressed_keys[K_d]:
            movement.x += 0.1
        if window.pressed_keys[K_a]:
            movement.x -= 0.1
        
        if movement != Vector2(0, 0):
            if not self.player.playing:
                self.player.play_sheet("walk")
        else:
            self.player.stop_playing()

        self.player.move(movement*window.delta)
    
    def init(self, window: Window):
        self.player.init(window)

def main():
    window = Window(title="Grief", size=(1280, 720))
    player = Player()
    player.init(window)
    while True:
        window.frame()
        player.render(window)

if __name__ == "__main__":
    main()