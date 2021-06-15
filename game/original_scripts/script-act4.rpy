label act4:
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
    m "I wonder if it's a good idea to ask a question?"
    menu:
        "ask a question":
            jump curious
        "remain silent":
            $ respect_meter += 1
            jump silence

label curious:
    m "Fuck it, I'm gonna do it."
    m "Who is Sally?"
    
    hide jaden happy
    show jaden normal

    j "what do you mean?"
    jump arrival

label silence:
    m "I don't want to bother Jaden nor sound nosey."
    m "It's best to remain si-"

    hide jaden happy
    show jaden normal
    
    j "You know, it's okay to ask something if you have a question."
    j "No one can tell you to be silent. You have every right to know."
    j "Afterall, you are part of the Tweleve, and we don't discriminate anyone based on anything."
    j "So tell me, whats on your mind?"
    
    jump arrival

label arrival:
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
    "VROOOOMMM"
    
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

label sally_intro:
    s "Let me make a proper introdution to the newbie over here."
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
    j "Tell them about you origin!"

    hide sally happy
    show sally silly

    s "Well, I am a Dwarf Gnome from the planet Tesarock."
    s "It's the home of inovation and technology. The planet of oppurtunity and intelligence."
    s "However, Tesarock was also a corrupt planet that was on the brink of war."
    s "Had it not been for the Tweleve, I wouldn't be here and Tesarock would be committing mass genocide to other worlds."
    s " I know your little brain is curious about me, What do you want to know more about me?"

    menu:
        "How tall are you?":
            $ respect_meter -= 1
            jump rudeness
        "What have you inveted so far?":
            $ respect_meter += 1
            jump politeness

label rudeness:
    hide sally silly
    show sally angry
    
    s "Are you fucking kidding me!"
    s "Jaden! did you menetion about my height?"
    
    show jaden normal at right
    with moveinright

    j "He is just a little curious, almost too curious that someone got his tongue."

    jump end_act4

label politeness:
    s "Well, I did build this ship by stratch."
    s "I also made Android mobile around the universe, create anti-gravity, build anti-black hole, started a new physic laws..."
    
    show jaden normal at right
    with moveinright

    j "Don't kill the new member to death by boredom."

    jump end_act4

label end_act4:
    j "Anyway, I should remind you that the meeting is tomorrow."

    hide sally silly
    hide sally angry
    show sally normal
    
    s "Is the newbie gonna be part of the meeting?"
    j "He is officially part of the Tweleve, so he is obligated to be there."
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

    j "You heard mention about the meeting many times..."
    j "If I didn't, they would forget about it and start a new mission."
    j "I suggest you take some rest until Andriod calls you for the meeeting."
    m "Okay, I'll head back to my office."

label recap:
    scene bg office
    m "That was a lot to take in for me."
    m "First, I'm part of the Tweleve."
    m "Then, I choose to decide the faith of a planet."
    m "Now, I am going to meet the rest of the Tweleve."
    m "To recap, I have met five out of the eleven Tweleve members."
    m "They are unique and different in their own way."
    show sally angry
    m "Sally is the smartest Tweleve and the greatest inventor."
    m "Despite her anger issues, she could be a kind person if you don't say anything bad to her."
    hide sally angry
    show kira model
    m "Kira is the Healer of the Tweleve."
    m "His knowledge about magic and spells may be far superior than any Tweleve."
    m "While his role to dispell evil is quite known, the rest of his identity remains a mystery."
    hide kira model
    show morgana silly
    m "Morgana is a pure Succubus and a demon lord."
    m "She may be filrty at times, but she likes to have fun when there is no work needed for her."
    m "Might be best to stay on her good term and avoid losing her intrest."
    hide morgana silly
    scene bg awaken facility
    m "Android is the Superior A.I. in the universe."
    m "Android has eyes everywhere, so I better be at good behavior at all times."
    m "Android could be the one to save me or disown me."
    scene bg office
    show jaden happy
    m "Finally, Jaden is the main figure of the Tweleve."
    m "Quite strange that a Jade Emperor would be part of this group."
    m "Then again, Jaden may have something in his mind that no one else can see."
    m "Whatever the case could be, he would have the final word for my existence."
    hide jaden happy
    m "I only met five of them, yet they are on another level."
    m "I don't even known what's it going to be with the other members."
    m "It probably be best to just rest and see what happens next."
