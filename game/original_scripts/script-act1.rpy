
label act1:
    "..."
    scene bg deep
    with fade
    "..."
    u "This is space, the place where humanity wish to explore."
    u "To us humans, space holds great potential to expand our knowledge."
    u "However..."
    u "We, humans, have hype our expectations to believe that space is our final frontier."
    u "There is nothing fascinating for humans to learn in space."
    u "If anything, space is just a lucid dream to get away from our corrupted world."

    u "..."
    w "I see that you are enjoying the view." with hpunch

    scene bg deepship
    with zoomout
    pause
    show jaden normal
    with moveinleft

    u "Aah! Sorry for dosing off!"
    u "I should be ready for the interview."

    hide jaden normal
    show jaden happy

    w "It's not a 9-5 job, so there is no interview anything like that."
    w "I am here to see you before we get started."
    w "You can leave right now while you still can."
    u "No, no, I made myself clear to commit this role."
    u "Just hit me with the truth."
    w "ho, I like a determined person who's ready for anything."
    w "Let's begin."

    $ name = renpy.input("What is your name?:", length=32)
    $ name = name.strip()
    $ persistent.player_name = name
    if name == "":
        $ name = "Omar"
    else:
        $ name = persistent.player_name
    
    m "My name is [name]"
    w "Well [name]."
    w "Welcome to the Tweleve."
    j "I am Jaden the Jade Emperor that is part of the group called the Tweleve."
    j "There are twelve of us from each species that are deemed too powerful for the universe, with the exception of you."
    j "We all could fight a pointless battle, but we instead choose to work together to eliminate all evil in our universe."
    j "Our job is to destroy all life that are deemed too dangerous or evil to be left unchecked."

    hide jaden happy
    show jaden normal

    j "We were so good at our job that we almost wiped out all life on this universe."
    j "As you can tell, we run into some issues as to which planet should be destroyed or which to spare."
    j "Upon days of debating, I propose an anwser to our problem."

    hide jaden normal
    show jaden happy

    j "The solution was simple, have someone more weaker to be part of the tweleve."
    j "That is where you come in check."
    j "To prevent another incident like this, you must make the calls on who gets to life and who gets to die."
    j "Humans are very weak compare to us, but they have strong sense of morals in their mind."
    j "I believe that a human would be gret for this position."
    j "The tweleve could use someone like you, what do you say?"

    menu:
        "I refuse":
            $ quick_death_ending = True
            hide jaden happy
            show jaden angry

            j "Fuck, we were so close!" with hpunch
            j "Kira do the memory wash again."
            
            hide jaden angry
            with moveoutleft
            "{i}Zap{/i}" with vpunch
            j "Sensitive creatures!"

        "I accept":
            j "Good, we are on the role."    
            j "Let me show you around this place."
            hide jaden happy
            with moveoutleft
    return