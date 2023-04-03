# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# define slow_fade_out = Dissolve(2.0)

label bad_end:

    scene ending
    pause 2.0
    show text "Bad End" at truecenter:
        alpha 0.00
        ease 2.0 alpha 1.00
    
    pause 5.0
    scene black with Fade(2.0, 1.0, 0.0)
    return
    

label neutral_end:

    scene ending
    pause 2.0
    show text "Neutral End" at truecenter:
        alpha 0.00
        ease 2.0 alpha 1.00
    
    pause 5.0
    scene black with Fade(2.0, 1.0, 0.0)
    return

label good_end:

    scene ending
    pause 2.0
    show text "Good End" at truecenter:
        alpha 0.00
        ease 2.0 alpha 1.00

    pause 5.0
    scene black with Fade(2.0, 1.0, 0.0)
    return
