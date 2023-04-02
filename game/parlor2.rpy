# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label parlor2_start:

    scene bg parlor

    if aaron_alive:
        jump parlor2_aaron_alive
    
    else:
        jump parlor2_aaron_dead


label parlor2_aaron_alive:

    show alastor at right, fade_in
    show evelyn angry at midleft, fade_in
    show katherine angry at center, fade_in
    show aaron enraged at midright, fadein

    l "Ah, you've returned I see. Have fun in the kitchen?"

    e "We had a blast."

    l "Wonderful. Wine, anyone? Oh, and do put the gun down, Evelyn."

    e "I'll keep it pointed at you, thanks."

    a "We met a friend in the basement."

    l "Oh, you made it into the cellar, did you?"

    e "We had a great chat."

    l "That is quite interesting, really. Well, I must apologize for what I have to do with you next, Evelyn. And Aaron. You used to be a good butler, once."

    e "And what's happening with Kat?"

    show katherine neutral

    e "Kat?"

    l "She already knows. Every intact soul in the castle is right here with us."
    l "And Kat knows her place."

    "Evelyn has two bullets left. Two bullets, two souls bound to the house. Now she must make her choice."

    menu: 

        "Shoot Alastor and Kat":
            jump parlor2_aaron_alive_choice1_1
        
        "Shoot Alastor and Aaron":
            jump parlor2_aaron_alive_choice1_2
        
        "Shoot Kat and Aaron":
            jump parlor2_aaron_alive_choice1_3

        "Shoot no one":
            jump parlor2_aaron_alive_choice1_4
        
        "\"Kat. Please.\"" if relationship_katharine > 2 and corrupt_evelyn < 4:
            jump parlor2_aaron_alive_choice1_5

label parlor2_aaron_alive_choice1_1:

    play sound gunshot

    pause 0.5

    play sound2 gunshot

    pause 1.0

    "With a quick flick of her wrist, Evelyn guns down Lord Alastor and her dearest friend."

    show aaron scared

    a "Why would you do that?!"

    e "Open the door."

    if corrupt_evelyn < 4:

        "The door clicks open, and the pair are able to step outside."

        a "Kat was...?"

        e "Yeah. I don't know why… Maybe that wasn't even the real Kat…"
        e "My car is still here. Let's get out of here."

        jump end
        
        return
    
    else:

        "Aaron is able to step through the door, but Evelyn is unable."
        "She is too far gone. The castle has claimed her."

        jump fate_sealed

        return

label parlor2_aaron_alive_choice1_2:

    play sound gunshot

    pause 0.5

    play sound2 gunshot

    pause 1.0

    "With a quick flick of her wrist, Evelyn guns down Lord Alastor and Aaron."

    e "The door, Kat, quickly!"

    "Kat moves towards the door, but it doesn't budge. The force keeping them inside has not weakened."

    e "What's wrong? Kat?"

    k "I'm sorry, Evelyn."
    k "Which is more than you'll ever be."

    jump fate_sealed

    return

label parlor2_aaron_alive_choice1_3:

    play sound gunshot

    pause 0.5

    play sound2 gunshot

    pause 1.0

    "With a quick flick of her wrist, Evelyn guns down Aaron and her dearest friend."

    l "Oh my, what a development!"

    "Evelyn rushes to the door, but the force still keeps her in."

    l "What did you think would happen, Evelyn? I'm afraid you're going to be joining the cellar dwellers now."
    l "You could have made such a great drinking buddy, such a shame."

    "Alastor tears into Evelyn. She wakes up next to a starved entity."

    jump fate_sealed

    return

label parlor2_aaron_alive_choice1_4:

    "Alastor launches himself at Evelyn, pinning her to the ground, leaving her defenseless."

    l "What did you think would happen, Evelyn? I'm afraid you're going to be joining the cellar dwellers now."
    l "You could have made such a great drinking buddy, such a shame."

    "Alastor tears into Evelyn. She wakes up next to a starved entity."

    jump fate_sealed

    return

label parlor2_aaron_alive_choice1_5:

    k "What, Evelyn? What do you–"

    e "Let us go."

    a "What...?"

    show evelyn grimace

    e "I'm sorry. I'm sorry for everything I did. I should have never told your family those things, and you have every right to hate me."
    e "But I have missed every day for almost twenty years."
    e "Let me at least try to make it up to you?"
    e "We can leave, right now."

    a "How heartwarming, but–"

    play sound gunshot

    pause 1.0

    "Evelyn lowers her gun, Alastor dropping to the ground."

    show alastor at fade_out

    show katherine smile

    k "God, Evelyn, you've changed."
    k "I'm so sorry. I don't… I don't even remember how I got here."
    k "Let's go."

    "Kat walks to the door, and briefly weakens the force enough for the trio to walk through."

    k "I'm sorry, too, Aaron."
    k "Let's go home, Evelyn."

    show evelyn smile

    jump end

    return

label parlor2_aaron_dead:

    show alastor at midright, fade_in
    show evelyn angry at midleft, fade_in
    show katherine angry at center, fade_in

    l "Ah, you've returned I see. Have fun in the kitchen?"

    e "We had a blast."

    l "Wonderful. Wine, anyone? Oh, and do put the gun down, Evelyn."

    e "I'll keep it pointed at you, thanks."

    l "Oh, you made it into the cellar, did you? That's where that stench is from."

    e "We had a great chat with your friend down there."

    l "That is quite interesting, really. Well, I must apologize for what I have to do with you next, Evelyn."

    e "And what's happening with Kat?"

    show katherine neutral

    e "Kat?"

    l "She already knows. Every intact soul in the castle is right here with us."
    l "And Kat knows her place."

    "Evelyn has two bullets left. Two bullets, two souls bound to the house. Now she must make her choice."

    menu:

        "Shoot Alastor and Kat":
            jump parlor2_aaron_dead_choice1_1
        
        "Shoot no one:":
            jump parlor2_aaron_dead_choice1_2

        "\"Kat. Please.\"" if relationship_katharine > 2 and corrupt_evelyn < 4:
            jump parlor2_aaron_dead_choice1_3
        
label parlor2_aaron_dead_choice1_1:

    play sound gunshot

    pause 0.5

    play sound2 gunshot

    pause 1.0 

    "With a quick flick of her wrist, Evelyn guns down Lord Alastor and her dearest friend."

    e "I'm sorry, Kat."

    if corrupt_evelyn < 4:

        "Evelyn approaches the door, the force just weak enough for her to slip through."
        "She stumbles through the door frame, her newfound freedom compelling her forward."
        jump end
        
        return
    
    else:

        "Evelyn is unable to step through the door."
        "She is too far gone. The castle has claimed her."

        jump fate_sealed

        return

label parlor2_aaron_dead_choice1_2:

    "Alastor launches himself at Evelyn, pinning her to the ground, leaving her defenseless."

    l "What did you think would happen, Evelyn? I'm afraid you're going to be joining the cellar dwellers now."
    l "You could have made such a great drinking buddy, such a shame."

    "Alastor tears into Evelyn. She wakes up next to a starved entity."

    jump fate_sealed

label parlor2_aaron_dead_choice1_3:

    k "What, Evelyn? What do you–"

    e "Let us go."

    a "What...?"

    show evelyn grimace

    e "I'm sorry. I'm sorry for everything I did. I should have never told your family those things, and you have every right to hate me."
    e "But I have missed every day for almost twenty years."
    e "Let me at least try to make it up to you?"
    e "We can leave, right now."

    a "How heartwarming, but–"

    play sound gunshot

    pause 1.0

    "Evelyn lowers her gun, Alastor dropping to the ground."

    show alastor at fade_out

    show katherine smile

    k "God, Evelyn, you've changed."
    k "I'm so sorry. I don't… I don't even remember how I got here."
    k "Let's go."

    "Kat walks to the door, and briefly weakens the force enough for the two to walk through."

    k "Let's go home, Evelyn."

    show evelyn smile

    jump end

    return

