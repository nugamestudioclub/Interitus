# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label graveyard_start:

    scene bg graveyard

    show evelyn neutral at midcenter

    "The graveyard seems to be oddly peaceful in comparison to the horrors inside the house."
    "Evelyn could imagine why Kat chose this place as her hideout."
    "The dead seem to stay dead here."

    show evelyn neutral:
        ease 1.0 midleft

    show katherine shocked at midright, fade_in:
    
    k "Evelyn...?"

    e "Kat! Wow. I know it's been so long, but I... Your family is looking for you."

    show katherine neutral

    "There is a pensive sadness to Kat's demeanor. She remains silent."

    menu:

        "\"I want to apologize. For before.\"":
            jump graveyard_choice1_1

        "\"Let's get out of here.\"":
            jump graveyard_choice1_2

        "\"What the hell has happened to you since '06?\"":
            jump graveyard_choice1_3

label graveyard_choice1_1:

    k "Go on, then."

    show evelyn grimace at midleft

    e "Shit... Okay, I shouldn't have done... what I did. I think about it everyday."

    show katherine smile at midright

    k "Hmm..."

    show evelyn happy at midleft

    e "I just got all emotional for a 'hmm'?"

    k "Maybe if you help me, I'll be more talkative."

    e "As you command... my lady? What's up with the dress?"

    k "That's a long story for a different day. Let's get out of here first."

    show evelyn neutral at midleft
    show katherine neutral at midright

    e "Alright, let's move."

    $ relationship_katharine += 2

    jump graveyard_choice1_end

label graveyard_choice1_2:

    show katherine neutral at midright
    show evelyn neutral at midleft

    k "So I can have some grand reunion with my family?"

    e "So no more creepy shit happens."
    e "I know you don't talk to them... but they were worried."

    k "Were you?"

    e "Worried? Of course I was, Kat. You just disappeared."
    e "I thought I was going to have to attend a funeral."

    k "We should probably get going."
    k "And by that I mean find a way to leave this place."

    e "Great plan."

    $ relationship_katharine += 1

    jump graveyard_choice1_end

label graveyard_choice1_3:

    k "I could ask you the same question."

    show katherine neutral at midright
    show evelyn neutral at midleft

    e "I mean, you've clearly had a mid-life crisis."

    show katherine angry at midright

    k "Oh, sure. Like being here was my choice."

    e "How did you get here?"

    k "Long story."

    e "Don't explain anything, then."
    e "Just let me wonder why you abandoned everyone."

    k "Abandoned everyone?!"
    k "You abandoned me! I thought I could trust you back then!"
    k "I guess you haven't changed."

    e "I'm here now, aren't I?"
    e "Let's leave this shithole."

    k "Fine."

    $ relationship_katharine -= 2

    jump graveyard_choice1_end


label graveyard_choice1_end:

    show katherine neutral:
        ease 1.0 midcenter

    show aaron neutral at midright, fade_in

    a "Well, if we want to get through to the other sections of the castle, we'll need the key."
    a "And that will be hard to do since–"

    e "Yeah, that thing in the ballroom has it. I saw it earlier."

    a "I mean, sometimes he goes to different parts of the castle, so if we wait, we–"

    e "Wait? How long?"

    show aaron enraged at midright

    a "I don't know–"

    e "We just need to distract it, long enough to grab the key."

    a "And how do you know that? Kat, has she told you she {i}fucking died{/i} earlier and came back?"
    a "Just like one of those things!"

    show evelyn angry at midleft

    e "And why did I die? You took an axe to my neck, asshole!"

    k "There's something about this place."
    k "Things– people– don't stay dead."

    e "Fine. Fine. Sure. Look, I know how we can get the key because I saw how this thing moves."
    e "Just follow my lead."

    jump ballroom2_start


