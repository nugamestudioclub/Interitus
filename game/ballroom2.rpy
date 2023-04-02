# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label ballroom2_start:

    scene ballroom

    show evelyn neutral at midleft, fade_in
    show katherine neutral at center, fade_in
    show arron neutral at midright, fade_in

    a "So, what exactly is the plan, lady?"

    menu:
         
        "We make a run for it. Aaron first.":
            jump ballroom2_choice1_1

        "It gets distracted by prey.":
            jump ballroom2_choice1_2

label ballroom2_choice1_1:
    
    a "Why me?"

    e "You're young and spry, go on."

    show arron scared

    a "Fine."

    hide arron

    "Aaron begins to run across the ballroom, his heavy footsteps quickly alerting the creature."

    show katherine scared

    a "Oh God..."

    "Kat turns away as Aaron is brutally mauled and partly devoured by the creature."

    "With the creature distracted by its meal, Evelyn is free to approach the mass of flesh."

    "Evelyn is able to peel the fleshy key out from the creature, allowing herself and Kat to bolt across the ballroom before the beast finishes eating."

    $ corrupt_aaron += 1

    "Aaron, newly intact, stumbles after the pair."

    a "What the fuck?!"

    e "We needed a distraction so we could get the key."
    e "And now all of us have made it."
    e "So you're welcome."

    a "I just died! It just ripped me apart! I felt all of that!!!"

    e "Maybe you shouldn't have killed me earlier, then."
    e "I felt all of that, too."

    k "We have the key. Let's just go."

    jump ballroom1_choice1_end
    

label ballroom2_choice1_2:

    a "Prey...? It’s a hunter?"

    e "Yes, and a damn good one."

    k "But it looks almost human..."

    e "Well, it’s not. Not anymore, anyway."

    a "Jesus... but then, wait, if we need prey, then..."

    menu:

        "I can be the prey.":
            jump ballroom2_choice2_eve

        "Aaron?":
            jump ballroom2_choice2_aaron

        "Kat?":
            jump ballroom2_choice2_kat

label ballroom2_choice2_eve:

    k "What do you mean?"

    e "It will be distracted enough to grab the key off its back if it's after me."
    e "See the key?"

    k "Yes, but..."
    k "That thing is going to kill you."

    show evelyn smile

    e "Nothing that I haven't done before."

    hide evelyn
    show katherine scared

    "Evelyn bolts across the ballroom, towards the monster. She makes sure to stomp her boots along the way."
    "It lunges towards her."
    "Kat turns away as Evelyn is brutally mauled and partly devoured by the creature."
    
    "With the creature distracted by its meal, Kat and Aaron are free to approach the mass of flesh."
    "Kat is able to peel the fleshy key out from the creature, allowing herself and Aaron to bolt across the ballroom before the beast finishes eating."

    $ corrupt_evelyn += 1

    "Evelyn, newly intact, stumbles after the pair."

    k "Are you alright?"

    e "I've felt better. You got the key?"

    k "Yes."

    e "Then let's go."

    jump ballroom2_choice1_end

label ballroom2_choice2_aaron:

    show aaron angry

    a "Seriously?"

    e "You were the one who stuck an axe in my neck earlier."

    e "Unless I'm misremembering?"

    a "What if I don't come back?"

    e "Then I guess it means you've escaped this hellhole, so congrats."

    k "I'm sure you would resurrect. Everything else does."
    k "Even the plants in the graveyard."

    a "Fine. Okay, yeah."

    show arron scared

    a "I guess I'm doing this."

    hide arron

    "Aaron bolts across the ballroom, towards the monster. It hears him before he can reach it."
    "Kat turns away as Aaron is brutally mauled and partly devoured by the creature."

    "With the creature distracted by its meal, Evelyn is free to approach the mass of flesh."
    "Evelyn is able to peel the fleshy key out from the creature, allowing herself and Kat to bolt across the ballroom before the beast finishes eating."

    $ corrupt_aaron += 1

    "Aaron, newly intact, stumbles after the pair."

    e "You alright?"

    a "No."

    k "This way, quickly."

    jump ballroom2_choice1_end

label ballroom2_choice2_kat:

    show aaron angry

    a "Woah, woah, seriously?!"

    k "Aaron. It's fine."
    k "Someone has to be the one to distract it."

    show aaron neutral

    e "If you can run across the ballroom, we can grab the key."
    e "It will be faster than you, but once it..."
    e "Catches you, it should buy us enough time."

    a "I don't see why you're not the one doing this, since we already know you can survive all this crazy shit?"

    k "I think, no, I know, that I'll come back, too."
    k "Things here don't stay dead. Not even the plants in the graveyard."
    k "Aaron?"

    a "Yeah?"

    k "Just... Get that key. Work {i}with{/i} Evelyn."

    e "We will."

    hide katherine

    "Kat walks across the ballroom, towards the monster. It hears her before she can reach it."
    "Evelyn and Aaron stare as Kat is brutally mauled and partly devoured by the creature."

    "With the creature distracted by its meal, Evelyn is free to approach the mass of flesh."
    "Evelyn is able to peel the fleshy key out from the creature, allowing herself and Aaron to bolt across the ballroom before the beast finishes eating."

    $ corrupt_katharine += 1

    "Kat, newly intact, stumbles after the pair."

    e "Are you alright?"

    k "Not really. Let's move on."

    jump ballroom2_choice1_end

label ballroom2_choice1_end:
    jump parlor_start