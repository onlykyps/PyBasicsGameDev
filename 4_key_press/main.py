import arcade

WIDTH = 800
HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    
    def on_draw(self):
        """ Called  automatically about 60 times a second to draww objects """
        arcade.start_render()
        

    def on_update(self, delta_time):
        """ Called  automatically about 60 times a second to update objects """

    def on_key_press(self, symbol: int, modifiers: int):
        """ Called automatically whenever a key is pressed """
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
        """ Called automatically whenever a key is released """
        return super().on_key_release(symbol, modifiers)

def main():
    """ Main method """
    window = GameWindow(WIDTH,HEIGHT,"Basic Animation")
    arcade.run()

if __name__ == "__main__":
    main()