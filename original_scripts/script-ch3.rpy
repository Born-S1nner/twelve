
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
            $ respect_meter += 1
            $ moral_meter -= 1
            $test_score += 0
        "Save the planet":
            $ respect_meter -= 1
            $ moral_meter += 1
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
    k "I have high hopes for you."
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
            $ respect_meter += 1
            $ moral_meter -= 1
        "Live a new life":
            $ respect_meter -= 1
            $ moral_meter += 1
        "Kill yourself":
            $ respect_meter -= 1
            $ moral_meter -= 1

    j "Okay okay, let's not get too deep into what ifs."
    k "I have to resupply my equipments for the next journey."
    j "Don't overowrk yourself this time. We would have a mee-"
    k "Yes, a meeting upcoming around the clock. I shall be there with the others."
    j "Great!"
    k "Hope we meet again human."
    m "I wish the same."

    hide kira
    with moveoutright
    pause
    hide jade happy
    show jaden normal

    j "Well, that went calmer than I expect."
