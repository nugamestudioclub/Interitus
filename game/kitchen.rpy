# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label kitchen_start:

    scene bg kitchen

    "The castle seems to creak and groan as the three harrowed travelers make their way across the entrance hall and toward the door of the eastern wing."
    "With a click, the small brass key turns in place, and the doors swing open to reveal a grand banquet hall."
    "The seats are empty. The table is set. The candles are lit. The shades are drawn."
    "Evelyn goes first, carefully examining the room for signs of a clue, a monster, another person, anything, but there's nothing else to find."
    "With a signal, Kat and Aaron follow cautiously in her footsteps close behind, and the three of them together proceed through a door to the north."
    "Beyond that door is a kitchen, grand yet barren."
    "Flies buzz around rotting meat, plates and pots lie scattered on the floor, and at the end of the kitchen is a large double door with a lock."

    k "Is it safe?"

    a "Not another crazy ass monster in here, is there?"

    e "It's clear."

    a "But it's just another fucking dead end."

    e "Help me try to break this door open."

    "The three of them approach and study the door closely."

    a "I can see through the crack in the door. There's a stairwell going down to some sort of cellar."

    e "Can you see anything down there?"

    a "Only some crates, some barrels, nothing useful."

    e "Why is the lock for the door on the other side..."
    e "Nevermind. You've got an axe, right? Let's just break down the whole thing."

    a "Tried that already. Forcing your way through shit doesn't work here."

    k "...there's a small gap above the door. We can't crawl through it, but we could toss something over to the other side?"

    a "To unlock a door? What could we possibly throw over?"

    k "One of us."

    a "There's no way any of us are fitting through that."

    e "Let alone getting up there."

    k "Not an entire person, no..."

    a "What the hell is that supposed to mean?"

    k "When we die, we regenerate."
    k "Any blood we lost, any flesh that was severed, any limbs that were torn off."
    k "So if someone's head is cut off, they should still regenerate."

    e "But which {i}part{/i} will regenerate?"

    a "You're not actually suggesting we try this, are you? Have you both lost it?"

    e "What choice do we have?"

    k "It's not like it matters anyway. We'll just come back."

    a "Have you not been paying attention? Everytime we revive, we come back... wrong."
    a "You're looking more and more like a zombie with every room we pass."
    a "And Kat's face looks like it's fucking peeling off her skull."
    a "We can't keep doing this ourselves. There won't be any of ourselves left to save."

    e "Then what? What do you suggest?"

    a "...I don't know."

    k "It's fine, Aaron. Escaping this place is what's important. It's just a matter of..."

    e "Of who's going to have to die this time."

    $ kitchen_choice1_aaron_reject = False

label kitchen_choice1_start:

    menu:

        "\"I'll do it\"":
            jump kitchen_choice1_eve

        "\"It was your idea, Kat.":
            jump kitchen_choice1_kat

        "\"Young people regenerate faster." if not kitchen_choice1_aaron_reject:
            jump kitchen_choice1_aaron

label kitchen_choice1_eve:

    k "Evelyn, are you sure?"

    if corrupt_evelyn > 1:
        
        k "You're really not looking so good, and you've died a lot already..."

    e "It’ll be fine. I’m fine."
    e "If this is what it takes so that we can get out of here, then I’ll do it."
    e "Aaron, just, make it quick."

    a "...alright"

    "Stealing herself, Evelyn bends down and places her head against a cutting board on the counter."
    "Anxiously, Aaron takes a meat cleaver from the rack nearby, aims, and then hacks at Evelyn’s exposed neck."
    "Her limbs flail, blood gurgles and spills from her mouth, but soon she is still, and the job is done."
    "Aaron carefully lifts her head off the counter and walks over to the door."
    "Kat gave up watching a long time ago. Her eyes are clenched shut, her hands are covering her ears. Her face has gone a pale, deadly white."
    "But it’s done now. Evelyn’s head thunks as it lands on the stairs beyond the door."
    "After a few minutes, a click, and the door opens."

    k "Evelyn! God, are you okay? You look terrible."

    e "I’m fine, Kat, I’m alright. Death’s an old friend at this point."

    k "Don’t joke. I couldn’t have known that would work for sure."

    e "But it did, right? Turns out you were right."

    a "Still though, you look like shit."

    e "You shut up. Door’s open, be grateful."

    a "Fine, fine, let’s go then."

    $ relationship_katharine += 1
    $ relationship_aaron += 1
    
    jump kitchen_choice1_end

label kitchen_choice1_kat:

    k "...me?"

    a "Evelyn enough, there’s no way we can force Kat to do this."

    e "Why not? Are you volunteering, murderer?"

    a "She literally just died minutes ago, and you’re gonna make her do it again?"

    e "Then we know it’s no big deal. She’ll come back again just like she did."

    a "Are you completely heartless?"

    k "Guys... it’s fine, just stop. I’ll do it since I have to."

    a "But–"

    k "No more fighting. Let’s just finish this."

    "Wiping the tears from her eyes, Katherine gently bends down and places her head against a cutting board on the counter."
    "Aaron crosses his arms and looks away, so Evelyn steps forward."
    "She takes a meat cleaver from the rack nearby, aims, and hacks at Katherine’s exposed neck."
    "Her limbs twitch weakly, blood gurgles and spills from her mouth, but soon she is still, and the job is done."
    "Evelyn gently lifts her head off the counter and walks over to the door."
    "Aaron gave up watching a long time ago. He stands in the corner, expression hard, eyes deadset on the corner furthest from where Evelyn stands."
    "But it’s done now. Katherine’s head thunks as it lands on the stairs beyond the door."
    "After a few minutes, a click, and the door opens."

    e "Kat..."

    k "..."

    a "...Kat, I’m sorry. It should have been me. You shouldn’t have had to-"

    k "Aaron, it’s fine. Let’s just... let’s just go."

    $ relationship_katharine -= 1

    jump ballroom1_choice1_end

label kitchen_choice1_aaron:

    if relationship_aaron < -2:

        a "Really? Me? You think I'm gonna do a goddamn thing you say after the shit you've pulled?"

        e "You will if we force you to."

        a "Like hell I will. You kill me and shove my head to the other side of that door, and I'll fucking leave you both here to rot."

        k "Evelyn, he's right. We can't force him to help us."

        e "Fuck, fine then."

        $kitchen_choice1_aaron_reject = True

        jump kitchen_choice1_start

    a "Me? You’re not talking about me, are you? Do you even know that for a fact?"

    e "Seems a likely theory to me."

    a "Son of a bitch..."

    k "Aaron please, we need you to do this for us. We’re one step closer to getting out of here, to leaving this all behind."

    a "Fucking hell… fine, fine, alright. Do it then, just make it quick."

    "Gritting his teeth, Aaron closed his eyes and put his head down against a cutting board on the counter."

    k "Evelyn..."

    e "It’s fine, Kat. I’ll do it."

    "Steadily, Evelyn takes a meat cleaver from the rack nearby, aims, and then hacks at Aaron’s exposed neck."
    "He screams, his limbs flail, blood gurgles and spills from his mouth, but Evelyn continues her work, and soon, the job is done."
    "She grabs Aaron’s head between her two hands and walks over to the door."
    "Kat gave up watching a long time ago. Her eyes are clenched shut, her hands are covering her ears."
    "But it’s done now. Aaron’s head thunks as it lands on the stairs beyond the door."
    "After a few minutes, a click, and the door opens."

    k "Aaron, are you okay...?"

    e "You {i}do{/i} look pretty bad."

    a "It’s... I’m fine. It’s fine. Let’s just go. Door’s open now."

    $ relationship_aaron -= 1

    jump kitchen_choice1_end

label kitchen_choice1_end:
    jump dungeon_start