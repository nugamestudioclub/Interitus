# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label dungeon_start:

    scene bg dungeon

    "With the door now open, the trio descends into the darkness."
    "It's cold, but Evelyn doesn't think that the chills she's getting are from the temperature."
    "They find themselves in a putrid cellar, bars in front of them, barrels behind them."

    e "We can check these barrels for anything useful."

    "A low, growling sound echoes throughout the cellar."

    show arron scared
    show kat scared

    a "Who did that?"

    play sound monster_2

    show trapped_entity at center, fade_in

    show evelyn scared

    a "What the fuck is that?!"

    t "Food... I need... Food..."
    
    e "Well, this one talks, I guess."

    t "Yes... You want to escape thisss place?"

    e "That's the idea, yeah."

    t "Hmm... There is a way... There is a way..."

    a "Then tell us."

    t "I need food... Endless hunger... endless food..."

    e "There's some stuff in the kitchen, Aaron, run up and get it."

    t "No. That's not endless... I need... One of you... Endless food... The gate is not locked..."

    k "You want to eat one of us? Over and over?"

    a "Fuck no."

    e "And this is the only way you'll tell us? If one of us goes in there with you?"

    "The creature shifts happily, anticipating food."

    t "Yes..."

    e "And how do we know that you even know how to get out of here?"

    t "I think... I'm older than the castle... But I cannot remember..."
    t "It's difficult... But there is a way... There are more enemies than it seems..."

    a "That's not helpful."

    e "It seems like he does know something, but..."
    e "More enemies than it seems? What is that supposed to mean?"

    k "This is a trap, it has to be."

    e "You're going to have to be more clear than that, or else you'll starve."

    t "Noooo... The Lord of this castle... Alastor... He is ancient, but I am older... I remember him being a child... before he was bound to this house."

    show aaron neutral

    a "So what do we have to do?"

    t "Give me food... And I will tell you..."

    if relationship_aaron < -1:
        jump dungeon_aaron_betray

    else:
        jump dungeon_no_arron_betray


label dungeon_aaron_betray:

    show aaron enraged

    "Aaron expertly steals the gun from Evelyn, raising it in the air."

    a "Go on, Evelyn! I know you're a fucking monster!"
    a "Even if you're not working with the monsters, you are one."

    e "Woah, woah, kid, chill out."

    if relationship_katharine < 0:
        jump dungeon_kat_betray

    else:
        jump dungeon_no_kat_betray

label dungeon_kat_betray:

    show evelyn scared
    
    e "Kat?"

    show katherine angry

    k "No..."
    k "Aaron, do it."
    k "We're getting out of here."

    e "Wait–"

    play sound gunshot

    show evelyn at fade_out

    "Evelyn's body is dragged into the cell, the trapped entity gleefully devouring his meal."
    "In between mouthfuls of flesh, the entity reveals all."

    jump fate_sealed

    return

label dungeon_no_kat_betray:

    show evelyn scared

    k "Put the gun down, Aaron."

    a "Why? You know how selfish she's been the whole time?"
    a "And I thought she did something to you before?!"
    a "You still trust her?!"
    
    e "Please..."

    "The trapped entity begins reaching through the bars."
    "Kat grabs the axe that clattered to the ground after Aaron stole the gun. She raises it to Evelyn."
    
    k "I'm sorry."

    play sound axe_kill

    show aaron at fade_out

    "Kat swings sideways, cutting into Aaron, causing him to drop the gun."
    "Evelyn drags Aaron, helplessly bleeding out, into the cage."
    "He makes a small groan of protest as the entity begins to eat him alive."

    jump dungeon_aaron_dead

label dungeon_no_aaron_betray:

    k "We're not just going to sacrifice one of us. We all get out, or no one does."

    e "Yeah."

    $ dungeon_failed_interrogation = False

label dungeon_interrogation_begin:

    menu:

        "\"You're not getting any of us. I'll make you talk.\"" if not dungeon_failed_interrogation:
            jump dungeon_interrogate

        "Shoot Aaron":
            jump dungeon_shoot

label dungeon_interrogate:

    "The entity shifts around, almost taunting Evelyn."

    e "You still feel pain, don't you?"

    play sound gunshot

    "The entity hisses as a bullet goes through it."

    e "And I can stay here torturing you for as long as you want."

    a "Fuck yeah, let me at him!"

    "Aaron raises his axe."

    "Be careful, he won't tell you anything if you hurt him too much."

    menu:

        "\"I'll bring some food down for him. Then we can eat it in front of him.\"":
            jump dungeon_food

        "\"I'll grab the meat cleaver from upstairs. Once the rest of his limbs are gone, maybe he'll talk.\"":
            jump dungeon_axe

label dungeon_food:

    "A few moments later, Evelyn returns with some rotting food from the kitchen. She splits a moldy piece of bread in half and hands it to Aaron."

    e "Cheers."

    "The entity makes a low growl as he watches the food just out of his grasp."

    e "You want some? Maybe we'll even let you out of this cage. If you tell us how to leave."

    t "Please... I need food..."

    e "It's all yours, and everything out in the world, if you just tell us."

    a "This bread is delicious."

    t "Just one slice! One... please... and I'll tell you!"

    "Evelyn tosses a tiny crumb of bread into the cage and the trapped entity devours it. The entity falls to the floor, and starts to speak between rasping breaths."

    jump dungeon_end

label dungeon_axe:

    "Evelyn returns a moment later, and begins chopping the already-decaying flesh off of the entity."
    "Low moans echo through the cell, before stopping."

    k "I think that's enough."

    "Rasped breathing begins again. The entity begins to twitch."

    e "Tell us."

    k "It's not going to work."

    t "You're not... Getting me... I NEED FOOD!"

    $ relationship_katharine -= 1

    jump dungeon_interrogation_begin

label dungeon_shoot:

    play sonud gunshot

    show arron at fade_out

    show katherine scared

    k "Oh my God..."

    "Aaron lets out a cry of pain, clutching his chest where the bullet struck him."

    e "We have to give it what it wants if we want out of here."

    k "You're right... you're right..."

    "Evelyn drags Aaron, helplessly bleeding out, into the cage."
    "He makes a small groan of protest as the entity begins to eat him alive."

    $ relationship_katharine -= 1

    jump dungeon_aaron_dead


label dungeon_aaron_dead:

    e "Thank you, Kat."

    show evelyn neutral

    "Between mouthfuls of flesh, the entity begins to reveal what he knows."

    $ aaron_alive = False

    jump dungeon_end


label dungeon_end:

    t "There are two... bound to this castle as of now... kill them both, and with enough sanity... You may be able to escape while their souls are weak..."

    e "Two? Alastor and who else?"

    if aaron_alive:
        a "The monster in the ballroom?"

    else:
        k "The monster in the ballroom?"

    t "No... no, the second soul is very much intact... I know this much... But no more..."

    k "Thank you."

    e "So, we kill Alastor again, and... Look for the second person?"

    k "I guess..."
    k "Let's get out of this basement."

    e "Yeah."

    jump parlor2_start
