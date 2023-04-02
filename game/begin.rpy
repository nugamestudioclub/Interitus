# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label begin:

    scene bg car

    radio "Here in *static* there's a slight chance of rain this evening..."
    radio "*static* ...and for the low price of *static* you can buy this anti-aging cream! That's right, you... *static*"

    show evelyn normal at center, fade_in

    e "Goddamn rental car radio..."

    radio "{i}Don't go chasing waterfalls, stick to the...{/i} *click*"

    e "That's enough of you."
    e "Kat, I swear, if you're making me come all the way out here for nothing..."

    "Evelyn has finally arrived at the last known location of Katherine McKellan."
    "A remote castle awaits her."

    scene bg castle entrance
    show evelyn normal

    "The massive door to the stone castle feels extra tall with the sunset turning the shadows sharp."
    "Evelyn is not intimidated."

    
    show evelyn normal:
        ease 1.0 midleft
    show alastor smug at midright, fade_in
    pause 1.0

    l "I see you have found your way here in one piece. Was the journey not too difficult?"

    menu:

        "Yeah, let's cut whatever pleasantries you have planned here.":
            jump begin_choice1

        "It was fine.":
            jump begin_choice2

        "You were expecting me?":
            jump begin_choice3
        
label begin_choice1:

    show evelyn angry

    l "...right to the point, I see. You know, you ought to be a more gracious guest when handling your host."
    l "I suppose not everyone in this day and age is taught proper etiquette anymore."

    e "Yeah, I'm pretty sure I'm older than you, and I have big boy business to attend to, so are you going to let me in or not?"

    l "Very well, very well, as the lady insists. We're keeping our guests waiting, after all."

    jump begin_choiceEnd

label begin_choice2:

    l "...not exactly verbose today, are we?"
    l "Alas, it's no matter. I'm sure entrancing conversation will be plentiful once we meet our guests inside."

    e "Guests? Who are the guests?"

    l "There's no need to play coy, Miss Evelyn, I know why you're here. Let's not keep her waiting, shall we?"

    e "Look, I don't like what's going on here. Just take me to Kat."

    l "As you wish."
    
    jump begin_choiceEnd

label begin_choice3:

    l "But of course. Why, there is someone inside just anxiously awaiting your arrival. Let's not keep them waiting, shall we?"

    e "Someone? How the hell did...? Whatever, take me to them."

    l "As you wish."

    jump begin_choiceEnd

label begin_choiceEnd:

    scene bg parlor

    show evelyn normal at midleft
    show alastor smug at midright

    "The dusty parlor looks like it hasn't been properly used in years, despite its well-maintained look."
    "The strange man in front of Evelyn produces a bottle of wine, and begins to pour two glasses."

    l "Please, sit."

    "Evelyn glares, but slowly takes a seat in the velvet upholstered chair."

    e "So, where is the guest that was {i}so{/i} anxious to see me?"

    l "Where's the rush? We have all the time in the world to spend before we attend to trivial matters like that one."

    e "I'm actually in quite a rush, so please, stop bullshitting me. Is Kat here or not?"

    show alastor normal

    l "No."
    l "Not here, anyway."
    l "I'm sure you'll find her eventually, though. We do have an eternity to spend together."
    l "Perhaps you'll find her with her face melted off, features dripping down her torso as they pool into a putrid mass, organs bursting out of flayed skin, her–"

    show handgun

    show alastor scared
    show evelyn angry

    e "Take me to her, or you'll end up with a bullet in your brain."

    show alastor smug

    l "Oh dear, lost your composure, have you? Does it pain you to think about her suffering, to hear her calling desperately for help, and being able to do {i}nothing{/i}–"

    play sound gunshot

    hide alastor

    pause 1.0

    play sound2 skull_hit_concrete

    pause 1.3

    e "Fucking bastard…"

    "Evelyn decides to search the body for any useful information, and discovers a key in his back pocket."
    "Evelyn rolls the body over to its side, exposing the gunshot wound in his forehead."
    "She thought that perhaps she would be feeling some sort of guilt as of now, but her mind had already moved on from the blood seeping onto the carpet."
    "She was now focused on the locked door in front of her, and what lies beyond it."

    jump ballroom_start