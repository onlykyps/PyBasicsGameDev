import arcade

WIDTH = 800
HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        # image from imaginelabs.rocks
        self.player = arcade.Sprite("images/tank.png")
        self.player.center_x = 200
        self.player.center_y = 300

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        arcade.start_render()
        self.player.draw()
        
    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update our objects."""
        self.player.update()

    def on_key_press(self, key, modifiers):
        """ Called automatically whenever a key is pressed. """
        if key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5
        elif key == arcade.key.UP:
            self.player.change_y = 5 
        elif key == arcade.key.DOWN:
            self.player.change_y = -5

    def on_key_release(self, key, modifiers):
        """ Called automatically whenever a key is released. """
        if key == arcade.key.LEFT:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP:
            self.player.change_y = 0 
        elif key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    """ Main method """
    window = GameWindow(WIDTH, HEIGHT, "Sprites")
    arcade.run()


if __name__ == "__main__":
    main()




