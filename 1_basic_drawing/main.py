import arcade
import arcade.color
import arcade.color

WIDTH = 800
HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
    
    def on_draww(self):
        """ Called  automatically about 60 times a second to draww objects"""
        arcade.start_render()
        arcade.draw_text("Hellow, world!", 100,HEIGHT/2,WIDTH/2, arcade.color.BLACK
                         ,30)
        arcade.draw_circle_filled(100, 100, 50, arcade.color.RED)
        arcade.draw_rectangle_filled(500, 100, 200, 100, arcade.color.GREEN)
        arcade.draw_line(100, 100, 500, 100, arcade.color.BLACK, line_width=3)


    def on_update(self, delta_time):
        """ Called  automatically about 60 times a second to update objects"""
        pass

def main():
    """ Main method """
    window = GameWindow(WIDTH,HEIGHT,"Basic Drawing")
    arcade.run()

if __name__ == "__main__":
    main()