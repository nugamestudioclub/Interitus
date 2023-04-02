# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label parlor_start:

    scene bg parlor

    "The three of them quickly leave the ballroom and enter the solar. Kat and Aaron hurriedly rush toward the entrance hall door, but a large, unaccompanied blood stain on the carpet stops Evelyn dead in her tracks."

    e "Oh shit..."

    k "What's wrong?"

    e "He's not here."

    a "You don’t mean the Lord, do you?"

    e "Yeah. He was here, when I left him..."

    a "Left him?"

    e "...dead on the floor, I mean."

    k "You killed someone?!"

    e "Kat, he was insane. He talked about keeping us trapped here for an eternity, about… torturing you."

    k "..."

    a "Well, I don’t blame you for offing him in the slightest. He’s fucked up for sure."

    e "You’ve seen him as well?"

    a "Yeah. I ran into him before I ran into you. He just laughed, didn’t answer any of my questions, said that monsters would finish me off before the sun even set. Dumb shit like that."

    e "Yep, that's him."

    k "But, if you killed him, then..."

    e "He must have resurrected as well."

    l "Exactly correct, I’m afraid."

    $ corrupt_alastor += 1

    show alastor at right, fade_in

    "The door from the entrance hall slowly swings open, and standing in its frame with a sadistic grin is Lord Alastor, only he’s… changed. \[Insert description here\]"

    l "Welcome friends, how happy it is for us all to be gathered here."

    show aaron enraged
    show evelyn angry

    a "What the hell is your problem, man?"

    k "Why did you bring us all here?"

    e "What is it that you want from us?"

    l "That’s to be expected I suppose. This is quite a strange situation to find oneself in."
    l "Trapped in a deathless castle, your humanity slowly draining from your punctured corpses with every drop of blood you spill. No escape, no running from the truth."
    l "It can be quite a daunting prospect, no?"

    a "Quit screwing around, asshole. These are our lives and bodies you’re toying with, you can’t just toss that shit around!"

    l "Lives, bodies, souls, hearts, and minds, what difference does it make?"
    l "All live and all die. All grow and all decay."
    l "You’re all still so concerned with such trivial passings, so enraptured by the trappings of your own lives."
    l "What do I want from you? I want you to relax. Enjoy a glass of wine with me."
    l "Let the insanity slowly seep into your skull."

    show handgun

    e "Or I could just kill you again, if you're continuing this bullshit."
    
    l "Oh Evelyn, this is exactly what I mean."
    l "You’re still holding on, still gripping so fiercely to your dwindling life."
    l "Why?"
    l "Is it because of her?"

    e "Shut up."

    l "Do you really think she’ll ever forgive you for what you did? Is losing her really the worst fate you can imagine?"

    e "Shut the fuck up, now."

    a "Because I can assure you..."

    show handgun2

    a "...it’s not."

    k "Evelyn!"

    play sound gunshot

    hide katherine

    pause 1.0

    play sound2 skull_hit_concrete

    pause 1.3


    e "Kat! Fuck!"

    a "See? It’s no different, is it? Just another soul snuffed from this world, and nothing changes."

    menu: 
        "Yeah, and you'll be no different.":
            jump parlor_choice1_1

        "Who the hell are you?":
            jump parlor_choice1_2

label parlor_choice1_1:

    "Evelyn pulls out her gun and pulls the trigger."
    "Lord Alastor crumples to the ground, again."

    show alastor at fade_out
    show arron neutral

    a "Nice."

    e "Grab Kat. We're getting the hell out of here."

    $ relationship_aaron += 1

    jump parlor_choice1_end

label parlor_choice1_2:

    "Alastor smiles to himself."

    a "I suppose the question is understandable, since I know so much about you."
    a "I own this castle, each wall, each room, each fireplace, each person."
    a "And being that I am quite upset with you all for interrupting my routines, I'd–"

    e "How do you know who I am?"

    a "Well, I learned your little secrets from–"

    "Aaron grabs the gun from Evelyn, holding it up to Alastor."
    "Evelyn has a choice on her hands."

    menu:

        "\"Put the gun down, Aaron. Let me hear what he has to say for himself.\"":
            jump parlor_choice2_1

        "Disarm him.":
            jump parlor_choice2_2

label parlor_choice2_1:

    a "Fine."

    $ parlor_choice2_val = 0

    jump parlor_choice2_end

label parlor_choice2_2:

    a "What the fuck are you doing?!"

    $ parlor_choice2_val = 1
    $ relationship_aaron -= 2

    e "Talk. Now."

    jump parlor_choice2_end

label parlor_choice2_end:

    l "Aw, you're defending me, Evelyn, how sweet."
    l "I learned a lot about you from Katherine."
    l "You didn't sound so sweet when she described you."

    e "Why is she even here?"

    l "Wandering souls tend to find their way here."
    l "And when they're here, they do tend to dwell on the past."

    if parlor_choice2_val == 0:

        e "Okay... So why is Aaron here?"

        a "Yeah, I'd like to know that as well."

        l "Another lost soul."

        e "What the h–"

        l "You've used your three questions already, dears."
    
    if parlor_choice2_val == 1:

        e "Why can't we leave?"

        l "Everyone here is stuck in a way. Some more than others."
        l "You'll get used to it, dear"

        e "What–"

        l "Oh, sorry, dears, you've used up all three of your questions."
        
    l "If anyone wants a drink, I'll be here."

    "Alastor pours himself another glass and wine and awkwardly sits in a seat, his monstrous form making it hard to settle comfortably."
    
    l "You're free to continue on with your 'adventure' through the castle."
    l "You're not going to accomplish anything, but you're welcome to try."

    a "I don't trust this."

    e "Grab Kat, let's go"

    jump parlor_choice1_end

label parlor_choice1_end:
    jump kitchen_start