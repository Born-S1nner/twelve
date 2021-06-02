define m = Character("Me")
define j = Character("Jaden", color="#009900")

default passed = 4
default test_score = 0

label start:
    "..."
    scene deep
    with fade
    "..."
    m "This is space, the place where humanity wish to explore."
    m "To us humans, space holds great potential to expand our knowledge."
    m "However..."
    m "We, humans, have hype our expectations to believe that space is our final frontier."
    m "There is nothing fascinating for humans to learn in space."
    m "If anything, space is just a lucid dream to get away from our corrupted world."

label act1:
    m "..."
    j "I see that you are enjoying the view." with hpunch

    scene deepship
    with zoomout
    pause
    show jaden normal
    with moveinleft

    m "Aah! Sorry for dosing off!"
    m "I should be ready for the interview."

    hide jaden normal
    show jaden happy

    j "It's alright, your interview hasn't start just yet."
    j "I am here to see you before we get started."
    j "You can leave right now while you still can."
    m "No, no, I made myself clear to do this trail."
    m "Just hit me with some questions."
    j "ho, I like a determined person who's ready for anything."
    j "Let's begin."
    jump interview

label interview:
    j "Do you believe more in the news or your eyes?"
    menu:
        "I trust the news": 
            pass
        "I trust in my eyes only":
            $ test_score += 1

    j "Will you sacrifice the whole world for your loved ones?"
    menu:
        "Yes":
            $ test_score += 1 
        "No":
            pass
    
    j "Do you believe in God?"
    menu:
        "Yes": 
            pass
        "No":
            $ test_score += 1
    
    j "Do you wish to be popular on YouTube?"
    menu:
        "Yes": 
            pass
        "No":
            $ test_score += 1

label end_interview:
    if test_score == passed:
        jump end_act1
    else:
        $ test_score -= test_score
        hide jaden happy
        show jaden normal
        j "Sorry, you are still an ignorant simp that believes in every little thing."
        j "I don't take clout-chasing influencers into the twelve."
        j "I expected much from you."
        j "Kira, do the memory wash again."
        hide jaden normal
        with moveoutleft
        "Zapped" with vpunch
        jump start
