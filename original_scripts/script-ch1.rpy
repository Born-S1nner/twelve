
label act1_main:
    "..."
    scene bg deep
    with fade
    "..."
    m "This is space, the place where humanity wish to explore."
    m "To us humans, space holds great potential to expand our knowledge."
    m "However..."
    m "We, humans, have hype our expectations to believe that space is our final frontier."
    m "There is nothing fascinating for humans to learn in space."
    m "If anything, space is just a lucid dream to get away from our corrupted world."

    m "..."
    j "I see that you are enjoying the view." with hpunch

    scene bg deepship
    with zoomout
    pause
    show jaden normal
    with moveinleft

    m "Aah! Sorry for dosing off!"
    m "I should be ready for the interview."

    hide jaden normal
    show jaden happy

    j "It's not a 9-5 job, so there is no interview anything like that."
    j "I am here to see you before we get started."
    j "You can leave right now while you still can."
    m "No, no, I made myself clear to commit this role."
    m "Just hit me with the truth."
    j "ho, I like a determined person who's ready for anything."
    j "Let's begin."
    j "Welcome to the Tweleve."
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
            $ badending = True
            hide jaden happy
            show jaden angry

            j "Fuck, we were so close!" with hpunch
            j "Kira do the memory wash again."
            
            hide jaden angry
            with moveoutleft
            
            j "Sensitive creatures!"
            jump ending

        "I accept":
            j "Good, we are on the role."    
            j "Let me show you around this place."
            $ moral_meter += 1
            hide jaden happy
            with moveoutleft