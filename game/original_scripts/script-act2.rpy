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
    a "What do you want to do, [name]?"
    scene bg facility

    menu:
        "Talk with Android":
            m "I actually want to learn more about you."

            scene bg awaken facility
            a "Interesting."
            a "What do you want to learn about me?"
            scene bg facility

            jump a_questions
        
        "Head to the office":
            jump end_talk


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
                jump end_talk

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

    label end_talk:
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
            hide morgana silly
            show morgana angry
            mo "I see your not the type to take a joke."
            m "It's not that, I just-"
            mo "No need to explain yourself."
            mo "I should be apologizing for getting into someone's space."

        "What do you mean?":
            mo "Let's just say I can make person feel like it's their first time?"
            m "No please no, I wasn't th-thinking of doing a-anything to you." with hpunch
            mo "haha, don't worry I was just joking around."
            mo "It's always funny to tease a good hearted person."
            m "Ah, I see. Good one."

    hide morgana happy
    hide morgana angry
    show morgana normal

    mo "Anyway, we should meet up with jaden for your first day."
    m "Yes, let's go."
    hide morgana normal
    with moveoutright
    m "Good job me."

    scene bg deepship
    show morgana happy at right
    with moveinright
    mo "Guess who I found Jaden!"

    show jaden normal at left
    with moveinleft
    j "I see you found [name] in his office already."
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
    j "What do you think we should do to the planet, [name]?"

    label options:
        $ test_score -= test_score
        menu:
            "Destroy the planet":
                $test_score += 0
            "Save the planet":
                $test_score += 2
            "...":
                $test_score += 4
        
        if test_score == 0:
            hide jaden normal
            hide morgana normal
            show jaden happy at left
            show morgana sad at right

            j "Well know, I can see you don't trust in their diverse mindsets."
            j "Having diferent minds could led to massive conflicts in the long run."
            j "I say we destroy the planet"
            
            hide jaden happy
            show jaden normal at left
            
            j "What's the matter, Morgana?"
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

    scene bg deepship
    show jaden normal at left
    show morgana normal at right

    mo "Welp, I got to get going to bed."
    j "Oh yeah, its almost time for your sleep."
    mo "Don't let the newbie get near my room or else he would sufficate."
    m "I'll do my best to stay away."
    j "And don't sleep for too loong becase we will have a meeting in a bit."
    mo "Okay, see you when I'm awake again."

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

    scene bg facility
    show jaden happy
    j "He should be here somewhere..."
    j "oh, there he is!"

    show kira model at right
    with moveinright

    k "..."
    j "Kira, you know that you must introduce youreself to the new brother, [name]."
    k "You know how I feel about newcomers, especially humans."
    j "You must understand the conditions for the Tweleve."
    k "To remain sane, we must have the most moral kind, a human."
    k "Well then I should greet myself."
    k "I am Kira, the healer of the Tweleve and death to Evil."
    m "It's an honor to meet you, Kira."
    m "I heard you have protected me from many potential death."
    k "I can't allow one of us to die."
    k "I can sense a good nature in your soul."
    k "I have high hopes for you, [name]."
    m "I shall live up to your expectation."

    hide jaden happy
    show jaden silly

    j "Hey now, you shouldn't make him feel tense, Kira."
    j "We should treat him like a new younger brother."
    j "It'll take time for him to get adjusted around here."
    k "Will then, lets find out."
    k "What would you do if you're friend backstabbed you and survived?"

    menu:
        "Revenge":
            pass
        "Live a new life":
            pass
        "Kill yourself":
            pass

    j "Okay okay, let's not get too deep into what ifs."
    k "I have to resupply my equipments for the next journey."
    j "Don't overowrk yourself this time. We would have a mee-"
    k "Yes, a meeting upcoming around the clock. I shall be there with the others."
    j "Great!"
    k "Hope we meet again, [name]."
    m "Same here."

    hide kira
    with moveoutright
    pause
    hide jade happy
    show jaden normal

    j "Well, that went calmer than I expect."

    scene bg facility awaken
    show jaden normal
    a "Sally has just finished her mission and is on her way back to the Deep."
    scene bg facility
    show jaden happy
    j "Great timing."
    j "Let us head back to the station and see what's up."

    scene bg deepship
    show jaden happy
    pause
    m "{i}{b}I wonder if it's a good idea to ask a question?{/b}{/i}"
    
    menu:
        "ask a question":
            m "{i}{b}Fuck it, I'm gonna do it.{/b}{/i}"
            m "Who is Sally?"
        
            hide jaden happy
            show jaden normal

            j "what do you mean?"

        "remain silent":
            m "{i}{b}I don't want to bother Jaden nor sound nosey.{/b}{/i}"
            m "{i}{b}It's best to remain si-{/b}{/i}"

            hide jaden happy
            show jaden normal
            
            j "You know [name], it's okay to ask something if you have a question."
            j "No one can tell you to be silent. You have every right to know."
            j "Afterall, you are part of the Tweleve, and we don't discriminate anyone based on anything."
            j "So tell me, whats on your mind?"
        
    m "Well, I don't have a clue about Sally in general?"
    j "Oh right, I have yet to introduce you to the remaining guys."
    j "What do you know about Sally so far?"
    m "I can only assume she is also a part of the Tweleve, but that's about it."
    
    hide jaden normal
    show jaden happy
    
    j "Intresting, I don't want to ruin the surprise so tell you without spoiling the fun."
    j "Just imagine her as a tiny genius."
    
    hide jaden happy
    show jaden normal
    
    j "But don't mention anything about size to her. She will get cranky about it."
    "{i}VROOOOMMM{/i}"
    
    hide jaden normal
    show jaden silly
    
    j "HO, here comes the genius herself, Sally!"
    
    show sally angry at left
    with moveinleft
    
    s "Don't act like I didn't hear you talking about my size!"
    s "I have eyes everywhere on my ship."
    m "Her ship?"
    j "Ah yes, Sally was the one who build the Deep."
    
    hide sally angry
    show sally embrass at left
    
    s "Awww... I wanted to make myself look cool in front of the newbie."
    j "Well you know what they say."
    j "You can't fool people for who you really are."
    
    hide sally embrass
    show sally normal at left
    
    s "I think you just made that up right at the spot."
    j "You caught me."
    s "Let me make a proper introdution to the newbie over there."
    j "Sure thing, let me give you the spotlight."

    hide jaden silly
    with moveoutright
    hide sally normal
    show sally happy 
    with moveinleft

    s "The name's Sally Sulzberger from the Tweleve."
    s "I am the best engineer and genius of the universe."
    s "Anything you can think of, I can make them come true."
    s "I could build an army of robots or a super cool PB&J sandwich maker."
    j "Tell [name] about you origin!"

    hide sally happy
    show sally silly

    s "Well, I am a Dwarf Gnome from the planet Tesarock."
    s "It's the home of inovation and technology. The planet of oppurtunity and intelligence."
    s "However, Tesarock was also a corrupt planet that was on the brink of war."
    s "Had it not been for the Tweleve, I wouldn't be here and Tesarock would be committing mass genocide to other worlds."
    s " I know your little brain is curious about me, What do you want to know more about me?"

    menu:
        "How tall are you?":
            hide sally silly
            show sally angry

            s "{b}Are you fucking kidding me!{/b}"
            s "{b}Jaden{/b}! did you menetion about my height?"

            show jaden normal at right
            with moveinright

            j "He is just a little curious, almost too curious that someone got his tongue."

        "What have you inveted so far?":
            hide sally silly
            show sally happy
            s "Well, I did build this ship by stratch."
            s "I also made Android mobile around the universe, create anti-gravity, build anti-black hole, started a new physic laws..."
            
            show jaden normal at right
            with moveinright

            j "Don't kill the new member to death by boredom."

    j "Anyway, I should remind you that the meeting is tomorrow."

    hide sally silly
    hide sally angry
    show sally normal
    
    s "Is the newbie gonna be part of the meeting?"
    j "[name] is officially part of the Tweleve, so he is obligated to be there."
    s "Sounds reasonable, I see no problem with that."
    s "However, the rest of thet guys would feel discomfortable about his presence."
    j "Relax, I got that situation handle out."
    s "I hope so."
    
    hide sally normal
    show sally happy

    s "Welp, I got to get some rest after the long mission."
    s "See you on the meeting, newbie!"
    m "Yea, see you later."

    hide sally happy
    with moveoutright
    hide jaden normal
    show jaden happy
    with moveinright

    j "You mention about the meeting many times..."
    j "If I didn't, they would forget about it and start a new mission."
    j "I suggest you take some rest until Andriod calls you for the meeeting, [name]."
    m "Okay, I'll head back to my office."

    scene bg office

    m "{b}{i}That was a lot to take in for me.{/i}{/b}"
    m "{b}{i}First, I'm part of the Tweleve.{/i}{/b}"
    m "{b}{i}Then, I choose to decide the faith of a planet.{/i}{/b}"
    m "{b}{i}Now, I am going to meet the rest of the Tweleve.{/i}{/b}"
    m "{b}{i}To recap, I have met five out of the eleven Tweleve members.{/i}{/b}"
    m "{b}{i}They are unique and different in their own way.{/i}{/b}"

    show sally angry

    m "{b}{i}Sally is the smartest Tweleve and the greatest inventor.{/i}{/b}"
    m "{b}{i}Despite her anger issues, she could be a kind person if you don't say anything bad to her.{/i}{/b}"

    hide sally angry
    show kira model

    m "{b}{i}Kira is the Healer of the Tweleve."
    m "{b}{i}His knowledge about magic and spells may be far superior than any Tweleve.{/i}{/b}"
    m "{b}{i}While his role to dispell evil is quite known, the rest of his identity remains a mystery.{/i}{/b}"

    hide kira model
    show morgana silly

    m "{b}{i}Morgana is a pure Succubus and a demon lord.{/i}{/b}"
    m "{b}{i}She may be filrty at times, but she likes to have fun when there is no work needed for her.{/i}{/b}"
    m "{b}{i}Might be best to stay on her good term and avoid losing her intrest.{/i}{/b}"

    hide morgana silly
    scene bg awaken facility

    m "{b}{i}Android is the Superior A.I. in the universe."
    m "{b}{i}Android has eyes everywhere, so I better be at good behavior at all times."
    m "{b}{i}Android could be the one to save me or disown me."

    scene bg office
    show jaden happy

    m "{b}{i}Finally, Jaden is the main figure of the Tweleve."
    m "{b}{i}Quite strange that a Jade Emperor would be part of this group."
    m "{b}{i}Then again, Jaden may have something in his mind that no one else can see."
    m "{b}{i}Whatever the case could be, he would have the final word for my existence."

    hide jaden happy

    m "{b}{i}I only met five of them, yet they are on another level."
    m "{b}{i}I don't even known what's it going to be with the other members."
    m "{b}{i}It probably be best to just rest and see what happens next."

    $ test_score -= test_score
    $ q1_anwsered = False
    $ q2_anwsered = False
    $ q3_anwsered = False
    return