# The script of the game goes in this file.

transform midleft:
    xcenter 1/3
    yalign 0.0

transform midright:
    xcenter 2/3
    yalign 0.0

transform fade_in:
    alpha 0.00
    ease 1.0 alpha 1.00

transform solid:
    alpha 1.00

transform fade_out:
    easein 1.0 alpha 0.00

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn")
define k = Character("Katherine")
define a = Character("Aaron")
define l = Character("Lord Alastor")
define radio = Character("Car Radio")

define audio.axe_kill = "sfx/axe-kill.ogg"
define audio.bone_break = "sfx/bone-break.ogg"
define audio.car_rumble = "sfx/car-rumble.ogg"
define audio.flesh_tear = "sfx/flesh-tear.ogg"
define audio.footsteps = "sfx/footsteps.ogg"
define audio.gunshot = "sfx/gunshot.ogg"
define audio.monster_1 = "sfx/monster-1-sound-effect.ogg"
define audio.monster_2 = "sfx/monster-2-sound-effect.ogg"
define audio.skull_hit_concrete = "sfx/skull-hit-concrete.ogg"

image bg car = "images/backgrounds/car.png"
image bg castle front = "images/backgrounds/castle_front.png"
image bg chapel = "images/backgrounds/chapel.png"

image evelyn none = ConditionSwitch(
    # TODO add corruption cases
    "corrupt_evelyn == 0", "evelyn_image"

)   

init python:
    renpy.music.register_channel(name="sound2", mixer="sfx", loop=False)

    def myplay(keyName, channel=None, **kwargs):
        # TODO add corruption cases
        if (keyName == ""):
            return


# The game starts here.

label start:

    $ corrupt_evelyn = 0
    $ corrupt_katharine = 0
    $ corrupt_aaron = 0
    $ corrupt_alastor = 0

    $ relationship_katharine = 0
    $ relationship_aaron = 0

    jump begin
    # jump ballroom_start




    return
