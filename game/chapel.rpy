# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label chapel_start:

    scene bg chapel

    show evelyn neutral at center

    "Through the door, there is a small courtyard, and beyond it, a chapel with a graveyard built around the back."
    "Evelyn tries to run alongside the outside of the castle, only to find herself physically unable to walk past a certain point."
    "Something here was wrong. This castle felt…alive, almost."
    "Evelyn decides to approach the small chapel, hoping to find anything to lead her to Kat."

    show evelyn neutral:
        ease 1.0 midleft

    show aaron enraged at midright, fade_in

    a "Not today, fucker!"

    show axe

    play sound bone_break

    pause 1.5

    hide evelyn

    "Evelyn falls to the ground, blood splattering from her neck where the axe has been lodged."

    show aaron scared

    a "Shit. Shit."

    "After a few minutes, the axe begins to be pushed out of Evelyn's neck. The river of blood turns to a trickle, then stops."

    $ corrupt_evelyn += 1

    if corrupt_evelyn > 0:

        e "Holy shit."

        "Evelyn feels off. Her vision is different. Her limbs feel twisted. She can't think clearly. But she is still alive… right?"
        
    a "Oh my God, what the fuck?!"

    "The man raises his axe again, prepared to kill again."

    show evelyn angry at midleft, fade_in

    e "Get that thing away from me! What the hell are you doing?!"

    "The man backs up slightly, but does not let go of his weapon."

    a "Stop it! Y–you just came back to life! You're working with {i}him{/i}!"

    e "What? You just fucking hit me in the neck with a fucking axe! Who are {i}you{/i} talking about?!"

    a "Who are {i}you{/i}?!"

    menu:

        "I'm just looking for a friend! Would you put the axe down?":
            jump chapel_choice1_1

        "Who are you?!":
            jump chapel_choice1_2
        
label chapel_choice1_1:

    a "A friend? Here?"

    show aaron neutral

    e "As far as I know, yes. This is the last place I–"

    a "So you've trapped yourself here with them."

    e "Obviously I wasn't trying to! How did you end up here, if you know so much?"

    a "I... I don't remember. But- just describe your friend!"

    e "Her name is Kat, she's my age–"

    a "Shit. Kat? She's not… accepting visitors now."

    menu:

        "Why? Did you kill her, too?":
            jump chapel_choice_2_1

        "Just tell her Evelyn is here to…apologize. Just talk to her.":
            jump chapel_choice_2_2

label chapel_choice_2_1:

    a "No, Jesus Christ, why would I–"

    "Evelyn glares."

    a "No, I didn't."

    e "Good. Take me to her then."

    show aaron angry

    a "No way! You're like some crazy zombie or something, you came back from the dead!"
    a "You're getting the axe again."

    e "Do whatever you like. Not like the axe worked last time anyway."

    show aaron neutral

    a "...shit, lady. You're kind of nuts."

    e "Let's go already."

    jump chapel_choice1_end

label chapel_choice_2_2:

    a "Oh... shit... so you two have got a history, huh?"
    a "Fucking hell. Fine. Just come with me, you can tell her yourself."

    e "...thank you."

    a "But don't try anything sneaky, alright? Stay where I can see you."

    e "What exactly do you think I'm going to do?"

    a "I don't know. You're the zombie here."

    e "You're on thin ice, young man. You still owe me a life, don't forget."

    a "Oh, my bad. Next one I find, I'll let you know."

    e "Let's go already."

    $ relationship_aaron += 1

    jump chapel_choice1_end


label chapel_choice1_2:

    a "If you don't answer my questions, I'll fucking kill you again!"

    show handgun

    e "And if you don't calm down right now, I'll blast a hole in your head, and we'll try this again after you've had a taste of death too."

    show aaron scared

    a "..."

    hide axe

    a "Jesus, fine, alright, calm down lady, fuck. Just cause you're some deathless freak doesn't mean we all are."

    e "How do you know? Have you died before?"

    show aaron neutral

    a "Not recently, no. And I don't intend on trying it anytime soon."

    e "Good. Then, why don't you tell me everything you know."

    a "Lady, I don't know shit. Don't remember how I got here, don't know what the hell is happening."

    e "Well, have you seen anybody else?"

    a "...no, no one."

    menu:
        
        "\"Did you forget who has the gun pointed at who here? Talk.\"":
            jump chapel_choice3_1

        "\"Please, if you've seen her... I need to know. It's important.\"":
            jump chapel_choice3_2

label chapel_choice3_1:

    show aaron scared

    a "Fine. Yeah, sure. There was a woman, Kat, I found her earlier."

    e "Kat! So she is here... take me to her then. Now."

    a "Christ, alright lady, relax. Let's go then."

    $ relationship_aaron -= 1

    jump chapel_choice1_end

label chapel_choice3_2:

    a "...shit, you're talking about Kat, right?"

    e "Yes! Please, where is she?"

    a "If all you really want is to see here, then fine, alright, I'll take you."

    a "But could you put the gun away at least?"

    e "Not a chance. You {i}did{/i} murder me. Or did you forget?"

    a "...yeah, fine, whatever. Let's go then."

    $ relationship_aaron -= 1

    jump chapel_choice1_end

label chapel_choice1_end:
    jump graveyard_start


