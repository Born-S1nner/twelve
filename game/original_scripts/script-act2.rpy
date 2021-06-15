label act2:
    scene bg facility
    with fade
    show jaden happy
    with moveinleft
    
    j "The deep is our one and only spacehip that we have as our headquarters."
    j "Normally, I would have all the twelve on board."
    j "However, most of them are on important missions thoughout the galaxy."
    j "You would see them when they come back for the meeting."
    m "Would I be tasked to go out in space?"
    
    hide jaden happy
    show jaden silly

    j "No, humans can't survive the harsh conditions in space."
    
    hide jaden silly
    show jaden happy
    
    j "Instead, you can just chill right here in the deep."
    j "Andriod is in charge of the deep, so you can howl at her if you need help."
    j "Isn't that right, Android?"
    
    scene bg awaken facility
    show jaden happy
    a "Affirmative."
    scene bg facility
    show jaden happy
    
    j "That's right, Android is one with the ship, so be aware about keeping the deep clean."

    scene bg awaken facility
    show jaden happy
    a "It appears that Morgana is back from Earth."
    scene bg facility
    show jaden happy

    j "Ho, great timing."
    j "Android, show him to his office setup, I gotta handle some business with Morgana before he meets her."
    
    scene bg awaken facility
    show jaden happy
    
    a "It won't be a problem."
    a "Just leave the task to me."
    scene bg facility
    show jaden happy
    
    j "I can always count on you."
    j "You hang out with Android, I'll be back for a moment."

    hide jaden happy
    with moveoutleft

    scene bg awaken facility
    a "What do you want to do?"
    scene bg facility

    menu:
        "Talk with Android":
            $ moral_meter += 1
            m "I actually want to learn more about you."

            scene bg awaken facility
            a "Interesting."
            a "What do you want to learn about me?"
            scene bg facility

            jump a_questions
        
        "Head to the office":
            jump end_act2


    label a_questions:
        menu:
            "What are you exactly?" if q1_anwsered == False:
                $ q1_anwsered = True
                jump a1
            "Do you have a body?" if q2_anwsered == False:
                $ q2_anwsered = True
                jump a2
            "How do I call you for anything?" if q3_anwsered == False:
                $ q3_anwsered = True
                jump a3
            "Let's continue this some other time."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
                jump end_act2

    label a1:
        scene bg awaken facility
        a "I am an super advanced algrorithm with the largets data storage in the universe."
        a "Any information across the universe is under my knowledge."
        scene bg facility
        
        m "Can you put that in human terms?"
        
        scene bg awaken facility
        a "Highly-advanced AI."
        scene bg facility
        
        m "Got it!"

        jump a_questions

    label a2:
        scene bg awaken facility
        a "Unfornately, my current body is going under maintance."
        a "Either way, I don't see any point in having a human form."
        scene bg facility
        m "I guess no fan service."
        
        jump a_questions

    label a3:
        scene bg awaken facility
        a "Just simply call for me as I remain inside the deep most of the time."
        a "I will notify you if I am absent."
        scene bg facility
        m "That's good to know."

        jump a_questions

    label end_act2:
        scene bg awaken facility
        a "Let me show you the way to your office."
        scene bg facility
        m "Okay!"

        scene bg office
        a "Here is your office."
        m "Looks very organized for me."
        a "Jaden has ensured to make you feel like home."
        a "We welcome you with open arms."
        m "Thank you. I'm glad to be part of the Tweleve."
        
        "{i}knock knock{/i}" with vpunch
        a "It must be Morgana."
        m "Who?"
        a "One of the member of the Tweleve."
        a "She is what you humans call a Succubus. Best advise to not touch her."
        m "Hold up, is she coming over here?"
        a "Yes, I'll leave you two alone."
        m "Wait, I-"
        a "Android signed off."
        m "Great."
        "{i}knock knock knock{/i}" with vpunch
        m "Ah.. yes, come on in!"

        show morgana normal
        with moveinright

        mo "What's with your lack of response."
        mo "I've been knocking the door and you didn't anwser."
        m "Sorry, I was ending my guidance with Android."

        hide morgana normal
        show morgana happy

        mo "It's alright. I'll forgive you this once."
        mo "Just don't keep me waiting next time, alright sweetie."
        m "Yes, of course."

        hide morgana happy
        show morgana normal

        mo "Now then, let me introduce myself."
        mo "Ny name is Morgana de Amon. A literal hellspawn from the planet Escuro."
        mo "Though I may be classified as a demon lord, your lord views me as a Succubus."
        mo "No, I am not a perverted masochist, but I can be a little sadistic sometimes."
        mo "You should be thanking Kira for making you resistant to me."
        mo "Normal humans would by dying of heart attack just from being around me."
        m "I heard, I'll do the best I can to avoid any physical contact with you."
        
        hide morgana normal
        show morgana silly
        
        mo "Oh, were you expecting more from me?"

    menu:
        "No":
            jump choke
        "What do you mean?":
            $ respect_meter += 1
            jump joke

    label choke:
        hide morgana silly
        show morgana angry
        mo "I see your not the type to take a joke."
        m "It's not that, I just-"
        mo "No need to explain yourself."
        mo "I should be apologizing for getting into someone's space."
        jump end_act2

    label joke:
        mo "Let's just say I can make person feel like it's their first time?"
        m "No please no, I wasn't th-thinking of doing a-anything to you." with hpunch
        mo "haha, don't worry I was just joking around."
        mo "It's always funny to tease a good hearted person."
        m "Ah, I see. Good one."
        jump end_act2

    label end_act2:
        hide morgana happy
        hide morgana angry
        show morgana normal

        mo "Anyway, we should meet up with jaden for your first day."
        m "Yes, let's go."
        hide morgana normal
        with moveoutright
        m "Good job me."
