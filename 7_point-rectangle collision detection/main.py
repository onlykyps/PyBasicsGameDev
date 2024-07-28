import arcade
import arcade.key

WIDTH = 800
HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.brick = arcade.Sprite("images/tank.png")
        self.brick.center_x = 300
        self.brick.center_y = 200

        self.brick.alpha = 100

    
    def on_draw(self):
        """ Called  automatically about 60 times a second to draww objects """
        arcade.start_render()
        self.brick.draw()
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        if (x>=self.brick.left and x<=self.brick.right) and (y>=self.brick.bottom and y<=self.brick.top):
            self.brick.alpha = 255
        else:
            self.brick.alpha = 100

        return super().on_mouse_motion(x, y, dx, dy)

    def on_update(self, delta_time):
        """ Called  automatically about 60 times a second to update objects """

    # def on_key_press(self, key, modifiers):
    #     """ Called automatically whenever a key is pressed """

    # def on_key_release(self, key, modifiers):
    #     """ Called automatically whenever a key is released """

    # def on_key_press(self, symbol: int, modifiers: int):
    #     """ Called automatically whenever a key is pressed """
    #     return super().on_key_press(symbol, modifiers)
    
    # def on_key_release(self, symbol: int, modifiers: int):
    #     """ Called automatically whenever a key is released """
    #     return super().on_key_release(symbol, modifiers)

def main():
    """ Main method """
    window = GameWindow(WIDTH,HEIGHT,"Basic Animation")
    arcade.run()

if __name__ == "__main__":
    main()