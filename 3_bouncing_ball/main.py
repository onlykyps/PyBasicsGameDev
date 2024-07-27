import arcade

WIDTH = 800
HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.center_x = WIDTH/2
        self.change_x = 5
        self.radius = 50
    
    def on_draw(self):
        """ Called  automatically about 60 times a second to draww objects"""
        arcade.start_render()
        arcade.draw_circle_filled(self.center_x, HEIGHT/2, self.radius, arcade.color.RED)
        

    def on_update(self, delta_time):
        """ Called  automatically about 60 times a second to update objects"""
        self.center_x += self.change_x

        if self.center_x >= WIDTH - self.radius:
            self.change_x *= -1
        
        if self.center_x <= self.radius:
            self.change_x *= -1

def main():
    """ Main method """
    window = GameWindow(WIDTH,HEIGHT,"Basic Animation")
    arcade.run()

if __name__ == "__main__":
    main()