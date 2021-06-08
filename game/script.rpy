define m = Character("Me")
define j = Character("Jaden", color="#009900")
define a = Character("Andriod", color="#2eb8b8")
define mo = Character("Morgana", color="#9900cc")
define k = Character("Kira", color="#660000")

default passed = 4
default test_score = 0

default jaden_respect = False
default android_respect = False
default morgana_respect = True
default badending = False

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
        $ badending = True
        hide jaden happy
        show jaden sad
        j "Sorry, you are still an ignorant simp that believes in every little thing."
        j "I don't take clout-chasing influencers into the twelve."
        j "I expected much from you."
        j "Kira, do the memory wash again."
        hide jaden sad
        with moveoutleft
        "Zapped" with vpunch
        j "Let's hope they get the questions right this time."
        jump ending

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
            hide jaden happy
            with moveoutleft

label act2:
    scene bg facility
    with fade
    show jaden happy
    with moveinleft
    
    j "The deep is our one and only spacehip that we have as our headquarters."
    j "Normally, I would have all the twelve on board."
    j "However, most of them are on important missions thoughout the galaxy."
    j "You would see them when they come back."
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

label choice_1:
    scene bg awaken facility
    a "What do you want to do?"
    scene bg facility

    menu:
        "Talk with Android":
            $ android_respect = True
            m "I actually want to learn more about you."

            scene bg awaken facility
            a "Interesting."
            a "What do you want to learn about me?"
            scene bg facility

            jump a_questions
        
        "Head to the office":
            jump end_act2

define q1_anwsered = False
define q2_anwsered = False
define q3_anwsered = False

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
    
    "knock knock"
    a "It must be Morgana."
    m "Who?"
    a "One of the member of the Tweleve."
    a "She is what you humans call a Succubus. Best advise to not touch her."
    m "Hold up, is she coming over here?"
    a "Yes, I'll leave you two alone."
    m "Wait, I-"
    a "Android signed off."
    m "Great."

label mo_intro:
    scene bg office
    "knock knock knock"
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
        $ morgana_respect = True
        jump joke

label choke:
    hide morgana silly
    show morgana angry
    mo "I see your not the type to take a joke."
    m "It's not that, I just-"
    mo "No need to explain yourself."
    mo "I should be apologizing for getting into someone's space."
    jump end_act2ii

label joke:
    mo "Let's just say I can make person feel like it's their first time?"
    m "No please no, I wasn't th-thinking of doing a-anything to you." with hpunch
    mo "haha, don't worry I was just joking around."
    mo "It's always funny to tease a good hearted person."
    m "Ah, I see. Good one."
    jump end_act2ii

label end_act2ii:
    hide morgana happy
    hide morgana angry
    show morgana normal

    mo "Anyway, we should meet up with jaden for your first day."
    m "Yes, let's go."
    hide morgana normal
    with moveoutright
    m "Good job me."

label act3:
    scene bg deepship
    show morgana happy at right
    with moveinright
    mo "Guess who I found Jaden!"

    show jaden normal at left
    with moveinleft
    j "I see you found him in his office already."
    mo "You can't hide the scent of a human, even with Kira's power."
    
    hide jaden normal
    show jaden silly at left
    
    j "It'll take a lot more to fool your senses."
    mo "You know how it goes."
    
    hide jaden silly
    show jaden normal at left
    hide morgana happy
    show morgana normal at right

    j "Anyway, lets get down to some business."
    mo "Fair point."
    j "You must past on this first attempt on your wise decision."
    j "Android, pull up to Urth."
    a "On the way, Jaden."

    scene bg earthview
    show jaden normal at left
    hide morgana happy
    show morgana normal at right

    pause
    j "Over here is the planet known as Urth."
    j "It is on stage 0 for the time being, but the inhabitants are quite leveled minded for a stage 0."
    j "Each one of them has their own identity, tounge, ideas, and beliefs."
    j "There are calm ones, weak ones, timid ones, neutral ones, sad ones, crazy ones, angry ones, evil ones, etc."
    j "We have planned to destroy the planet, but we want to let you do their judgement."
    j "What do you think we should do to the planet?"

label options:
    $ test_score -= test_score
    menu:
        "Destroy the planet":
            $ jaden_respect == True
            $ morgana_respect == False
            $test_score += 0
        "Save the planet":
            $ jaden_respect == False
            $ morgana_respect == True
            $test_score += 2
        "...":
            $test_score += 4
    
    if test_score == 0:
        hide jaden normal
        hide morgana normal
        show jaden happy at left
        show morgana sad at right
        j "Well know, I can see you don't just in their diverse mindsets."
        j "Having diferent minds could led to massive conflicts in the long run."
        j "I say we destroy the planet"
        
        hide jaden happy
        show jaden normal at left
        
        j "Wha't the matter, Morgana?"
        mo "Oh nothing, it just feel a little sad to let food go to waster."
        mo "Now in times, it's getting quite hard to find any fresh blood."
        
        hide jaden normal
        show jaden happy at left

        j "Now, now... time has passed by for a long time."
        j "More humans should be walking on two feet by now. They could anywhere at this moment."
        m "Wait what do y-"
        mo "Fair point. Can you let Android do the task for now?"
        a "Sure thing, Android remove Urth's core."
        a "Sure thing"
        
        scene bg earthdestroy
        show jaden happy at left
        show morgana normal at right

        j "Well then, should we continue the guide?"
        m "Um... sure, let's get to business."
        j "Android, take us somewhere away from here."
        a "Sure thing."

    elif test_score == 2:
        hide jaden normal
        hide morgana normal
        show jaden sad at left
        show morgana happy at right

        j "I see, a pity to see your true nature."
        mo "Now, now, you did agree to go along with your idea."
        j "Fair point."
        j "Just need to get over this addiction."
        mo "Let's just come back to Urth in a few space to check on their expanding condition."
        j "Alright, alright. Android, take us somewhere away from here."
        a "Sure thing."
    else:
        j "We can't have you sleeping on this important decision, you need to pick."
        jump options

label act3_end:
    scene bg deeplightspeed
    show jaden normal at left
    show morgana normal at right
    mo "Welp, I got to get going to bed."
    j "Oh yeah, its almost time for your sleep."
    mo "Don't let the newbie get near my room or else he would sufficate."
    m "I'll do my best to stay away."
    mo "Good, see you when I'm awake again."
    m "Okay."
    hide morgana normal
    with moveoutright
    hide jaden normal
    show jaden happy
    j "Should have you meet the healer of the Tweleve?"
    m "Y'all got a healer?"
    j "Well, he is technacilly a healer from the start, but he learned more than heal magic to become more powerful."
    j "Normally, someone like him would be consider a threat, but he share the same values of surpresssing evil."
    j "He's a broken man, so go easy on him when we meet him."
    m "We are meeting him now!?"
    j "When Morgana goes to sleep, Kira would show up to put her in a calm state."
    j "He helps us reduce our catastrophic power level at minimum."
    j "He is always busy with his own agenda, so right now might be a good chance to meet him."
    j "Android, tell Kira that we are paying a visit."
    a "Right on it, Jaden."

label kira_intro:
    scene bg facility
    show jaden happy
    j "He should be here somewhere..."
    j "oh, there he is!"

    show kira model at right
    with moveinright

    k "..."
    j "Kira, you know that you must introduce youreself to the new brother."
    k "You know how I feel about newcomers, especially humans."
    j "You must understand the conditions for the Tweleve."
    k "To remain sane, we must have the most moral kind, a human."
    k "Well then I should greet myself."
    k "I am Kira, the healer of the Tweleve and death to Evil."
    m "It's an honor to meet you, Kira."
    m "I heard you have protected me from many potential death."
    k "I can't allow one of us to die."
    k "I can sense a good nature in your soul."

label ending:
    if badending:
        "Bad ending"

    "end"
    return