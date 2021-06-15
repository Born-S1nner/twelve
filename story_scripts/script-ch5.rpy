label act5:
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
    "You must be the new member, rihgt?!" with hpunch
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

label meeting:
    scene bg roundtable
    m "This must be where the meeting takes place."
    
    show bobby model at left
    with moveinleft
    b "Were you doubting me on the way here?"
    m "No, I'm new here around the deep."
    b "Oh right, sorry for being concern about you."
    m "Concern?"
    "This must be the new member of the Tweleve!" with hpunch
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
    
    j "Don't scare the beginner with your fangs, Vod."
    show jaden normal 
    with moveinleft
    
    j "We all agree to be nice to the new member, remember?"
    v "It was a mojority vote, I didn't agree to this."
    
    hide jaden normal
    with moveoutleft
    show jaden angry
    
    j "I sense you got a proble with how the Tweleve runs the universe."
    b "Hold up, we can't start a fight just now."
    "Bobby is right, it's rude to start an argument in front of the newest member."

    hide bobby model
    with moveoutleft
    show nova angry at left
    with moveinleft
    n "We are more mature to know that fist fights don't resolve anything."
    t "Are you saying that I'm too savage to be handle?"
    n "If I did, I would have said it right away."
    n "We are having a meeting with the new member being here for the first time."
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
