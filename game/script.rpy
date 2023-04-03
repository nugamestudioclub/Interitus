# The script of the game goes in this file.

transform midleft:
    xcenter 5/16
    yalign -0.25
    zoom 0.4

transform midright:
    xcenter 11/16
    yalign -0.25
    zoom 0.4

transform midcenter:
    xcenter 1/2
    yalign -0.25
    zoom 0.4

transform fade_in:
    alpha 0.00
    ease 1.0 alpha 1.00

transform solid:
    alpha 1.00

transform fade_out:
    alpha 1.00
    ease 1.0 alpha 0.00

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn")
define k = Character("Katherine")
define a = Character("Aaron")
define l = Character("Lord Alastor")
define radio = Character("Car Radio")

define audio.axe_kill = "/sounds/sfx/axe-kill.ogg"
define audio.bone_break = "/sounds/sfx/bone-break.ogg"
define audio.car_rumble = "/sounds/sfx/car-rumble.ogg"
define audio.flesh_tear = "/sounds/sfx/flesh-tear.ogg"
define audio.footsteps = "/sounds/sfx/footsteps.ogg"
define audio.gunshot = "/sounds/sfx/gunshot.ogg"
define audio.monster_1 = "/sounds/sfx/monster 1 sound effect.ogg"
define audio.monster_2 = "/sounds/sfx/monster 2 sound effect.ogg"
define audio.monster_1_kill = "/sounds/sfx/monster 1 kill.ogg"
define audio.monster_2_kill = "/sounds/sfx/monster 2 kill.ogg"
define audio.radio = "/sounds/sfx/radio-static.ogg"
define audio.skull_hit_concrete = "/sounds/sfx/skull-hit-concrete.ogg"

image bg car = "images/backgrounds/car.png"
image bg castle front = "images/backgrounds/castle_front.png"
image bg chapel = "images/backgrounds/chapel.png"

image evelyn none = ConditionSwitch(
    # TODO add corruption cases
    "corrupt_evelyn == 0", "evelyn_image"

)   

init python:
    renpy.music.register_channel(name="sound2", mixer="sfx", loop=False)

    def myplay(keyName, channel="music"):
        # TODO add corruption cases
        if (corrupt_evelyn == 0):
            renpy.music.play("sounds/music/No Distortion/" + keyName + ".ogg", channel, loop=True)
        
        elif (corrupt_evelyn == 1):
            renpy.music.play("sounds/music/Distortion Lvl1/" + keyName + ".ogg", channel, loop=True)
            
        elif (corrupt_evelyn >= 2):
            renpy.music.play("sounds/music/Distortion level 2/" + keyName + ".ogg", channel, loop=True)

# The game starts here.

label start:

    $ corrupt_evelyn = 0
    $ corrupt_katharine = 0
    $ corrupt_aaron = 0
    $ corrupt_alastor = 0

    $ relationship_katharine = 0
    $ relationship_aaron = 0

    $ aaron_alive = True

    jump begin
    # jump ballroom_start




    return
