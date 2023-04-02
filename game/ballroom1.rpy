# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label ballroom1_start:

    scene bg ballroom

    show evelyn neutral at center, fade_in

    "A grand ballroom in front of Evelyn, she gets the distinct feeling that she isn't alone."

    show creature at midright, fade_in
    show evelyn scared at solid:
        ease 1.0 midleft 
    
    pause 1.0

    "The creature seems to stumble into every pillar, lifting its head in response to the creak of the door hinge, but not paying it much mind."
    "There is an open door at the end of the ballroom."
    "The main entrance to the castle is locked. And Evelyn isn't finished here."
    "Evelyn knows where she needs to go, and the creature is in the way."

    $ saw_wait = False
    
label ballroom1_choice1_start:

    menu:

        "Shoot the creature.":
            jump ballroom1_choice1_shoot

        "Call out to the creature":
            jump ballroom1_choice1_call

        "Run to the open door.":
            jump ballroom1_choice1_run

        "Sneak across the room." if saw_wait:
            jump ballroom1_choice1_sneak

        "Wait.":
            jump ballroom1_choice1_wait

        
    
label ballroom1_choice1_shoot:

    "The bullet sinks into the creature's flesh, but not enough to stop it."
    "The creature hurls itself towards the sound of the gunshot, barely giving Evelyn enough time to shoot it again."
    "The creature rips into Evelyn, pinning her to the ground as it slices further and further through her torso."
    "The creature's jagged teeth tighten around Evelyn's neck, life squeezing out of her."
    jump ballroom1_choice1_dead

label ballroom1_choice1_call:

    "Suddenly, the creature whips its head to face Evelyn."
    "She hardly has a moment to flee before it's bounding across the room, teeth bared and saliva dripping from its hanging jaw."
    "In an instant, its maw snaps closed around her, and she crumples to the ground, lifeless."
    jump ballroom1_choice1_dead

label ballroom1_choice1_run:

    "Evelyn runs as fast as she can across the ballroom, her boots clicking against the elegant flooring."
    "Unfortunately, the creature is faster, following the sounds of the boots, clipping Evelyn's back."
    "Evelyn falls forward, the creature digging in, teeth and hands grasping at strands of flesh that it rips from her body."
    jump ballroom1_choice1_dead

label ballroom1_choice1_wait:

    $saw_wait = True

    "Evelyn pauses at the doorway, carefully observing the creature's shamblings across the room."
    "At one point, its head turns to face her, sending chills down her spine."
    "Yet, the creature makes no indication that it saw her."
    "In fact, there's no indication that this creature can see at all."
    "There's a pattern to its movements, but Evelyn's footsteps across the hard floor will no doubt draw its attention."
    jump ballroom1_choice1_start

label ballroom1_choice1_sneak:

    "Carefully, Evelyn crouches down and removes her boots, silently unlacing each one as the creature continues its procession across the ballroom floor."
    "Then, with boots in hand, she steadily inches her way past the creature and toward the door, her steps hardly making a sound as she goes."
    "At the doorway, she pauses and turns back once more to observe the creature."
    "Her theory was right, it hadn't noticed her at all."
    "As it lay crouched against a wall with its gnarled back to her, she saw something..."
    "A small brass key, embedded into the twisted flesh around its spine."
    "She swallows, steadying herself, before stepping through the doorway and out into the courtyard."
    jump ballroom1_choice1_end


label ballroom1_choice1_dead:

    show evelyn neutral at fade_out
    show creature at fade_out
    pause 1.0

    "Evelyn is dead."

    "...but not for long."
    "After a while, Evelyn's crumpled body begins to rise, {i}almost{/i} the same as it was before the creature decided to attack."

    $ corrupt_evelyn += 1

    e "Holy shit."

    "Evelyn feels off. Her vision is different. Her limbs feel twisted. She can't think clearly. But she {i}is{/i} still alive... right?"
    "The creature is still in the room, hunched against a wall in one corner, seemingly satiated by the fresh meal."
    "Cautiously at first, and then fleeing at full sprint, Evelyn escapes through the open ballroom door, keeping her eyes dead set on her killer all the while."
    "It doesn't even move, just keeps licking its distended hands clean of her blood, as the brass key embedded in its back glistens like an eye, watching her."
    jump ballroom1_choice1_end

label ballroom1_choice1_end:
    jump chapel_start
