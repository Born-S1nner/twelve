label act3:
    scene bg deep
    with fade
    pause
    "Beep, beep beep!" with vpunch
    scene bg office
    with fade
    "Beep, beep, beep!"
    m "What's that noise?"
    a "It's the alarm system, I have it on so you won't be late to the meeting."
    a "The alarm system has proven to be efficent."
    m "Almost too efficent."
    m "Let me get myself ready and I'll be out there."
    a "Alright, take your time."

    scene bg facility
    with wipeleft
    m "How far is the meeting?"
    scene bg awaken facility
    a "It should take 10 minutes to get there."
    scene bg facility
    m "It's that far, I'm gonna have to rely on you to show me the directions."
    w "You must be the new member, rihgt?!" with hpunch
    m "Who said that?"

    show bobby model
    with moveinright
    
    b "It's me, Bobby!"
    m "Ah, you must also be one of the Tweleve, are you?"
    b "If I'm in the deep, then yes."

    show randy model at right
    with moveinright

    m "Waah" with hpunch
    b "Oh, that's Randy."
    b "He don't talk much, so he would show up in surprise."
    r "..."
    m "Why does he stay muted and wear a mask?"
    b "If you havn't figure it out yet, his voice could destroy a planet."
    b "A single word could shattter the deep into pieces."
    r "..."
    b "Regardless, why are you here on the hallway?"
    m "I was on the way to the meeting."
    b "Ah yes, the meeting... must be your first time going there."
    m "Yes it is, can you show the way to the meeting?"
    b "Why of course, I can always help a brother out! Follow me!"

    hide bobby model
    with moveoutleft
    hide randy model
    with moveoutleft

    m "Wait hold up!"    

    scene bg roundtable

    m "This must be where the meeting takes place."
    
    show bobby model at left
    with moveinleft

    b "Were you doubting me on the way here?"
    m "No, I'm new here around the deep."
    b "Oh right, sorry for being concern about you."
    m "Concern?"
    w "This must be the new member of the Tweleve!" with hpunch
    
    show vod normal at right
    with moveinright
    
    b "Hey Vod! Glad to see that you never change."
    v "This little human is the one to decide on the fate of planets?"
    b "You know what they say, \"don't grudge a book by it's face.\" "
    v "You mean \"Don't judge a book by it's cover.\""
    b "Yeah, what you said."
    
    hide vod normal
    show vod angry at right
    
    v "Look human, I don't care what you're intentions here."
    v "If you plan to betray the Tweleve, you will be punished in the depths of punish land."
    
    menu:
        "Confront Vod":
            $ day_two_respect_meter -= 1
            v "Are you trying to stand up against me!"
        "Step back":
            $ day_two_respect_meter += 1
            v "You look more patheic than a weasel."
            v "I'mma show you why weaklings don't belong to the Tweleve."
    
    j "Don't scare the beginner with your fangs, Vod."
    
    show jaden normal 
    with moveinleft
    
    j "We all agree to be nice to the new member, remember?"
    v "It was a mojority vote, I didn't agree to this."
    
    hide jaden normal
    with moveoutleft
    show jaden angry
    
    j "I sense you got a problem with how the Tweleve runs the universe."
    b "Hold up, we can't start a fight just now."
    w "Bobby is right, it's rude to start an argument in front of the newest member." with hpunch

    hide bobby model
    with moveoutleft
    show nova angry at left
    with moveinleft
    j "Nova! When did you get here so quick?"
    n "Don't dodge the current situation, Jaden." with hpunch
    n "We are more mature to know that fist fights don't resolve anything."
    t "Are you saying that I'm too savage to be handle?"
    n "If I did, I would have said it right away."
    n "The rest of the guys would be here any minute."
    n "We are having a meeting with a new member for the first time."
    n "We should leave a good impression so that he would feel confident around us."

    hide vod angry
    show vod normal at right
    hide jaden angry
    show jaden normal

    j "You have a point. Sorry that you got to side that side of me."
    v "..."
    n "Vod. Jaden said his apology and you should too."
    v "..."
    v "Sorry."

    hide vod normal
    with moveoutright
    hide nova angry
    show nove sad at left
    
    n "Vod was never good at apologizing. I hope you could forgive him."
    m "It's alright. I can tolerate a few opinions."
    "{i}Thump. Thump. Thump.{/i}" with vpunch
    m "What was that?"
    "{i}Thump. Thump. Thump.{/i}" with vpunch
    
    show bobby at right
    with moveinleft
    b "That must be Tony."
    m "Tony?"
    
    scene bg roundtable 
    "{i}Thump.{/i}" with vpunch
    "{i}Thump.{/i}" with vpunch
    "{i}Thump.{/i}" with vpunch
    show tony model at right
    with moveinright

    t "..."
    b ""
    show bobby at left
    with moveinleft
    b "Hey Tony, How you been doing?"
    t "..."
    b "I see you are doing good too."
    m "How does Bobby know what they are saying?"

    scene bg roundtable
    show nova happy

    n "That's because Bobby can read minds telepathically."
    n "He knows what every can said, even if they are mute or consider non-living."
    m "That's cool."
    m "Bobby must be happy to talk to anyone."

    hide nova happy
    show nova sad
    
    n "Well, things weren't the same before you showed up."
    n "Bobby originally didn't speak because of his body condition."
    n "Since no one could hear him, Bobby would cause trouble just to get our attention."
    n "Kira realized the problem and decided to give bobby a voice."
    n "Now, Bobby would find any opportunity to speak."
    n "Bobby makes the atmosphere more lively despite being in the middle of sapce."
    n "Otherwise, I would have to hear Giddion's chantings"
    w "Did somebody say Giddion!!!" with hpunch
    m "Who was that?"
    n "Oh no, here he comes."

    show giddion model
    g "My name had been called around here."
    g "Did you summon me, mere mortal?"

    menu:
        "We were just talking about you":
            $ day_two_respect_meter += 1
            g "I see that at least you are willing to acknowledge me."
            g "Praise on you mortal!" with hpunch
        "No one said anything":
            $ day_two_respect_meter += 1
            g "Don't lie in front of my face!" with hpunch
            g "I heard you mention my name!"

    n "Gosh, tone down your voice."
    n "You don't need to scream every time you show up."
    g ""
#    menu:
#        "":
#        "":
#    menu:
#        "":
#        "":
#    menu:
#        "":
#        "":
#    menu:
#        "":
#        "":