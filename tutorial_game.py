import random
import pyasge
import GameObject
from gamedata import GameData


def isInside(sprite_1: pyasge.Sprite, sprite_2: pyasge.Sprite) -> bool:
    pass


class MyASGEGame(pyasge.ASGEGame):
    """
    The main game class
    """

    def __init__(self, settings: pyasge.GameSettings):
        """
        Initialises the game and sets up the shared data.

        Args:
            settings (pyasge.GameSettings): The game settings
        """
        pyasge.ASGEGame.__init__(self, settings)
        self.renderer.setClearColour(pyasge.COLOURS.BLACK)

        # create a game data object, we can store all shared game content here
        self.data = GameData()
        self.data.inputs = self.inputs
        self.data.renderer = self.renderer
        self.data.game_res = [settings.window_width, settings.window_height]

        # register the key and mouse click handlers for this class
        self.key_id = self.data.inputs.addCallback(pyasge.EventType.E_KEY, self.keyHandler)
        self.mouse_id = self.data.inputs.addCallback(pyasge.EventType.E_MOUSE_CLICK, self.clickHandler)

        # set the game to the menu
        self.menu = True
        self.play_option = None
        self.exit_option = None
        self.menu_option = 0

        # This is a comment
        self.data.background = pyasge.Sprite()
        self.initBackground()

        #
        self.menu_text = None
        self.start_text = None
        self.initMenu()

        #
        self.scoreboard = None
        self.initScoreboard()

        # Initialising the asteroid
        self.asteroid = GameObject.Asteroid()
        self.initAsteroid()

        # Initialising player ship
        self.player = GameObject.Ship()
        self.initPlayer()

        self.projectile = GameObject.Projectile()
        self.initProjectile()

    def initBackground(self) -> bool:
        pass

    def initAsteroid(self) -> bool:

        if self.asteroid.sprite.loadTexture("/data/images/kenney_simple-space/PNG/Retina/meteor_detailedLarge.png"):
            self.asteroid.move_speed = 8
            self.asteroid.sprite.z_order = -10
            self.asteroid.sprite.x = 100
            self.asteroid.sprite.y = 100
            self.asteroid.move_direction = [1, 0]
            self.spawn(self.asteroid)
            return True
        pass

    def initPlayer(self) -> bool:
        # This code initialises the spaceship code, similar to how the fish were loaded in,
        # and positions it at the centre of the screen
        if self.player.sprite.loadTexture("data/images/kenney_simple-space/PNG/Retina/ship_G.png"):
            self.player.move_speed = 8.0
            self.player.sprite.x = self.data.game_res[0] / 2 - self.player.sprite.width / 2
            self.player.sprite.y = self.data.game_res[1] / 2 - self.player.sprite.height / 2
            self.player.sprite.scale = 0.5

            # This code will ensure that player ship collisions remain consistent, you can leave it how it is
            self.player.collisionSprite.loadTexture("data/images/kenney_simple-space/PNG/Retina/ship_G.png")
            self.player.collisionSprite.x = self.data.game_res[0] / 2 - self.player.sprite.width / 2
            self.player.collisionSprite.y = self.data.game_res[1] / 2 - self.player.sprite.height / 2
            self.player.collisionSprite.scale = 0.5
            return True
        return False

    def initProjectile(self) -> bool:
        # This is where you should initialise your projectiles
        self.projectile.sprite.loadTexture("/data/images/kenney_simple-space/PNG/Retina/star_tiny.png")
        pass

    def spawn(self, gameObject: GameObject) -> None:
        # This is where you will set up your asteroid spawn
        # Think about both the starting position of your asteroid
        # and the starting movement direction
        # make a plan for proggramatic approach

        pass

    def initScoreboard(self) -> None:
        pass

    def initMenu(self) -> bool:
        # Initialising the title text
        self.data.fonts["MainFont"] = self.data.renderer.loadFont("/data/fonts/KGHAPPY.ttf", 80)
        self.menu_text = pyasge.Text(self.data.fonts["MainFont"])
        self.menu_text.string = "The Space Game"
        self.menu_text.position = [375, 200]
        self.menu_text.colour = pyasge.COLOURS.CADETBLUE

        self.data.fonts["SubFont"] = self.data.renderer.loadFont("/data/fonts/KGHAPPY.ttf", 48)
        self.start_text = pyasge.Text(self.data.fonts["SubFont"])
        self.start_text.string = "Press Space to Start"
        self.start_text.position = [475, 600]
        self.start_text.colour = pyasge.COLOURS.WHITE

        return True

    def clickHandler(self, event: pyasge.ClickEvent) -> None:
        pass

    def keyHandler(self, event: pyasge.KeyEvent) -> None:

        # Act only if a button has been pressed
        if event.action == pyasge.KEYS.KEY_PRESSED:

            # Closes the game whenever Escape is pressed regardless of game state
            if event.key == pyasge.KEYS.KEY_ESCAPE:
                exit()

            # If we are currently on the main menu screen
            if self.menu == True:
                # we check whether specific button (Spacebar in this case)
                # have been pressed
                if event.key == pyasge.KEYS.KEY_SPACE:
                    # We change the state from main menu to game screen
                    self.menu = False

            # If we are not in menu that means we are in main game screen
            else:
                # This is where you will implement your in-game inputs
                pass

        # This event is triggered whenever a button is released
        if event.action == pyasge.KEYS.KEY_RELEASED:
            if self.menu == True:
                pass
            else:
                # You can track which buttons have been released here
                pass
    def update(self, game_time: pyasge.GameTime) -> None:

        if self.menu:

            pass
        else:
            # update the game here
            self.asteroid.Move()
            pass

    def AsteroidScreenWrap(self, asteroid: GameObject.Asteroid()):
        # Use this function to check whether asteroid is off-screen
        # and teleport it across to the other side
        pass

    def FireBullet(self):
        # Use this function to fire a projectile from player ship in the current movement direction
        pass

    def render(self, game_time: pyasge.GameTime) -> None:
        """
        This is the variable time-step function. Use to update
        animations and to render the game-world. The use of
        ``frame_time`` is essential to ensure consistent performance.
        @param game_time: The tick and frame deltas.
        """

        if self.menu:
            # Render the menu screen here
            self.data.renderer.render(self.menu_text)
            self.data.renderer.render(self.start_text)

            pass
        else:
            # render the game here
            self.data.renderer.render(self.asteroid.sprite)
            self.data.renderer.render(self.player.sprite)
            pass


def main():
    """
    Creates the game and runs it
    For ASGE Games to run they need settings. These settings
    allow changes to the way the game is presented, its
    simulation speed and also its dimensions. For this project
    the FPS and fixed updates are capped at 60hz and Vsync is
    set to adaptive.
    """
    settings = pyasge.GameSettings()
    settings.window_width = 1600
    settings.window_height = 900
    settings.fixed_ts = 60
    settings.fps_limit = 60
    settings.window_mode = pyasge.WindowMode.BORDERLESS_WINDOW
    settings.vsync = pyasge.Vsync.ADAPTIVE
    game = MyASGEGame(settings)
    game.run()


if __name__ == "__main__":
    main()
