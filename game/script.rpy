define m = Character("Me")
define j = Character("Jaden", color="#009900")
define a = Character("Andriod", color="#2eb8b8")

default passed = 4
default test_score = 0

label start:
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

label act1:
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
        j "Let's hope they get the questions right this time."
        jump start

label end_act1:
    j "Finally, a worthy human with a clean mindset."
    j "Welcome to the tweleve."
    j "Let me tell you more about the Tweleve..."
    j "There are twelve of us from each species that are deemed too powerful for the universe, with the exception of you."
    j "We all could fight a pointless battle, but we instead choose to work together to eliminate all the nuisance in our universe."
    j "Our job is to destroy all life that are deemed too dangerous or evil to be left unchecked."

    hide jaden happy
    show jaden normal

    j "We were so good at our job that we almost wiped out all life on this universe."
    j "As you can tell, we run into some issues as to what planet should be destroyed or who to spare."
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
            $ test_score -= test_score
            hide jaden happy
            show jaden normal

            j "Fuck, we were so close!" with hpunch
            j "Kira do the memory wash again."
            
            hide jaden normal
            with moveoutleft
            
            j "Sesitive creatures!"
            jump start

        "I accept":
            j "Good we are on the role."    
            j "Let me show you around this place."
            hide jaden happy
            with moveoutleft

label act2:
    scene bg facility
    with fade
    show jaden happy
    with moveinleft
    
    j "The deep is our one and only spacehip that we have during our crusade."
    j "Normally, I would have all the twelve on board."
    j "However, most of them are on important mission thoughout the galaxy."
    j "You would see when they come back."
    m "Would I be tasked to go out in space?"
    
    hide jaden happy
    show jaden normal

    j "No, humans can't survive the harsh conditions in space."
    
    hide jaden normal
    show jaden happy
    
    j "Instead, you can just chill right here in the deep."
    j "Andriod is in charge of the deep, so you can howl at her if you need help."
    j "Isn't that right, Android?"
    
    scene bg awaken facility
    a "Affirmative."
    scene bg facility

    j "That's right, Android is one with the ship, so be aware about keeping the deep clean."

    scene bg awaken facility
    a "It appears that Morgana is back from Earth."
    scene bg facility

    j "Ho, great timing."
    j "Android show he to his office setup, I gotta handle some business with Morgana before he meets her."
    
    scene bg awaken facility
    a "It won't be a problem."
    a "Just leave the task to me."
    scene bg facility

    j "I can alway count on you."
    j "You hang out with Android, I'll be back for a moment."

    hide jaden happy
    with moveoutleft

label choice_1:
    scene bg awaken facility
    a "What do you want to do?"
    scene bg facility

    menu:
        "Talk with Android":
            jump android_interact
        "Head to the office":
            jump office

label android_interact:
    pass
label office:
    pass
