import arcade
import arcade.color
import arcade.key

WIDTH = 800
HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.center_x = width/2
        self.center_y = height/2

        self.radius = 50

        self.set_mouse_visible(False)

    def on_draw(self):
        """ Called  automatically about 60 times a second to draww objects """
        arcade.start_render()
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.RED)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called  automatically about 60 times a second to detect mouse motion """

        self.center_x = x
        self.center_y = y
    
    # def on_update(self, delta_time):
    #     """ Called  automatically about 60 times a second to update objects """
    
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