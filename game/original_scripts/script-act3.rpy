label act3:
    scene bg deep
    with fade
    pause
    "{i}Beep, beep beep!{/i}" with vpunch
    scene bg office
    with fade
    "{i}Beep, beep, beep!{/i}"
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
    w "You must be the new member, [name]s, right?!" with hpunch
    m "Who said that?"

    show bobby model
    with moveinright
    
    b "It's me, Bobby!"
    m "Ah, you must also be one of the Tweleve, are you?"
    b "If I'm in the deep, then yes."

    show randy model at right
    with moveinright

    m "{b}Waah{/b}" with hpunch
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
    w "{b}This must be the new member of the Tweleve!{/b}" with hpunch
    
    show vod normal at right
    with moveinright
    
    b "Hey Vod! Glad to see that you never change."
    v "This little human is the one to decide on the fate of planets, huh."
    b "You know what they say, \"don't grudge a book by it's face.\" "
    v "You mean \"Don't judge a book by it's cover.\""
    b "Yeah, what you said."
    
    hide vod normal
    show vod angry at right
    
    v "Look human, I don't care what you're intentions here."
    v "If you plan to betray the Tweleve, you will be punished in the depths of punish land."
    
    menu:
        "Confront Vod":
            v "Are you trying to stand up against me!"
        "Step back":
            v "You look more patheic than a weasel."
            v "I'mma show you why weaklings don't belong to the Tweleve."
    
    j "Don't scare [name] with your fangs, Vod."
    
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
    w "{b}Did somebody say Giddion!!!{/b}" with hpunch
    m "Who was that?"
    n "Oh no, here he comes."

    show giddion silly
    g "My name had been called around here."
    g "Did you summon me, mere mortal?"

    menu:
        "We were just talking about you":
            hide giddion silly
            show giddion happy
            g "I see that at least you are willing to acknowledge me."
            g "Praise on you mortal!" with hpunch
            hide giddion happy

        "No one said anything":
            hide giddion silly
            show giddion angry
            g "Don't lie in front of my face!" with hpunch
            g "I heard you mention my name!"
            hide giddion angry

    show giddion normal
    n "Gosh, tone down your voice."
    n "You don't need to scream every time you show up."
    show giddion happy
    g "That's what happens when you venture in a no sound zone for too long."
    g "You can't tell how loud your voice is and things sound awfully too quite."
    
    scene bg roundtable

    m "{b}{i}I decided to leave the two as I felt left out of the conversation.{/i}{/b}"
    m "{b}{i}It's probably normal for the new member to be left out.{/i}{/b}"
    m "{b}{i}It appears everyone showed up to the meeting.{/i}{/b}"
    
    show morgana happy at left
    show kira model
    show sally happy at right
    m "{b}{i}You got Moragana and Sally talking while Kira is calmly tolerating their chat.{/i}{/b}"
    
    pause
    scene bg roundtable
    show tony model at left
    show bobby model
    show randy model at right
    m "{b}{i}Then you got Bobby talking to the two mutes.{/i}{/b}"
    
    show nova normal at left
    show giddion angry at right
    m "{b}{i}Then there are the two arguing like a couple.{/i}{/b}"
    
    pause
    scene bg roundtable
    show vod normal at left
    show jaden normal model
    m "{b}{i}Finally; Jaden, Android, and Vod are making sure that everyone is present.{/i}{/b}"
    
    scene bg roundtable 
    m "I wonder if I even fit in to be part of the Tweleve."
    m "Every one of them are beyound my capability."
    m "I guess Vod is r-"

    show jaden normal
    j "Alright everyone, let's gather around to the table." with hpunch

    m "Everyone stop talking and went to take a seat very seriously."
    m "The atmosphere went dead silent as soon as Jaden command them to start the meeting."
    
    hide jaden normal
    show jaden happy
    j "What are you waiting for, taking a seat with us."
    m "Ah, yes."
    j "This meeting is special for obvious reason."
    j "Since our quest to eliminate all evil, we stumble upon a difficult question."
    j "What does define evil?"
    j "Who are we to judge on who is evil and how is not."
    j "Because of our immense power, we can't comprehand the lives of the weak."
    j "That is why I propose a the solution to introduce a newer and weaker member."
    j "Introducing our newest member, [name]."
    "{i}clap clap clap clap{/i}"
    j "Now then, do you got something to say?"
    m "Yes..."

    hide jaden happy
    m "I'm sorry for all the trouble I caused."
    m "I may have offended some people; in which case, I'm sorry."
    m "I'm grateful to be working with you."
    m "I won't say much."
    m "I'm looking forward to be working with y'all guys."
    m "Excuse me"

    show jaden normal
    with moveinleft
    
    j "Okay, what a small talk."
    j "Anyway, I would like to ask you for your opinion."
    j "What do you plan to do in your position?"
    hide jaden normal
    menu:
        "Destroy the plants that are deemed evil.":
            $ destroyers_points += 1
            m "This universe is being consumed by evil and we must stop it."
            m "We will do what we can to end this evil once and for all."
            m "Even if it mean wiping down colonies and planets."
        
        "Save the planets from the evil idealist.":
            $ pacifier_points += 1
            m "This universe is being under attack by evil and we must stop it."
            m "We will do what we can to end this evil once and for all."
            m "Even if it means protecting a planet with our bare hands."
        
        "Um.. yes": 
            pass

    if pacifier_points < destroyers_points:
        show giddion happy
        g "{b}HAHA{/b}, I knew that I could count on [name]!"
        show kira model at left
        with moveinright
        k "A mere mortal could see evil around the world."
        show randy model at right 
        with moveinright
        r "..."
        
        scene bg roundtable

        show vod angry
        with moveinleft
        v "I see that you don't take consideration about different perspectives."
        show bobby model at left
        b "Not this time, Vod."
        b "There's still way to change his view"
        show sally happy at right
        with moveinleft
        s "Oh, he will change his views after he sees his hands cover in blood."
    
    elif pacifier_points > destroyers_points:
        show bobby model
        b "Glad to know that you have good intentions, [name]."
        show vod normal at left
        with moveinleft
        v "You don't seem like a bad person to begin with."
        show sally happy at right
        with moveinleft
        s "Progression at it's finest!"

        scene bg roundtable
    
        show giddion happy
        g "Ah come on! What's good on protecting planets."
        g "We're not guardians."
        show kira model at left
        with moveinright
        k "I knew you are too sensitive to see the truth."
        show randy model at right 
        with moveinright
        r "..."

    else:
        show jaden sad
        a "Seems to me that [name] is suffering from stage fright."
        show morgana sad at left
        m "I don't remember seeing him get so nervous before."
        show nova sad at right
        n "It may be best to forget about this moment." 

    scene bg roundtable
    show jaden normal
    j "Alright, alright."
    j "[name] does not have to choose sides; he makes the ultimate decision."
    j "[name] can ask anyone and listen to anyone if they have a problem with the final decision."
    j "Maybe he could acknowledge your advice and change his desicion."
    j "isn't that right?"
    hide jaden normal
    menu:
        "That's right":
            pass
        "It depends":
            pass
    show jaden happy
    j "Let's settle down and continue on with the meeting."
    
    scene bg roundtable
    with fade
    show jaden happy
    j "And that concludes today's meeting."
    g "Finally, I can go back out there."
    s "I'mma go back on Corale."
    hide jaden happy
    
    m "{b}{i}Didn't know the meeting could go that smooth.{/i}{/b}"
    show morgana happy at left
    show nova normal at right
    mo "Hey [name], come over here and have a talk with us."
    scene bg roundtable
    menu:
        "talk to them":
            $ middle_points += 1
            jump talk2
        "ignore them":
            jump ignore

    label talk2:
        scene bg roundtable
        show morgana happy at left
        show nova normal at right
        mo "Glad to get your attention to us."
        m "What is it that you guys need?"
        n "It's about the small debate within the Tweleve."
        mo "By now, you can tell there are different opinions about your job."
        mo "However, there are only two sides to worry about."
        mo "Thoses that want to be pacifist and those that want to destroy."
        n "The Pacifiers and the Destroyers."
        m "Doesn't it contradict the foundation of the Tweleve."
        n "Not really."
        n "Having different ideas is quite common. but it doesn't break our relationship nor the foundation."
        mo "Think of it has siblings having different ideas."
        n "None of the sides hate each other, but they can clash against their ideas."
        n "After the issue discussed about our methods of handling the universe, two sides emerged."
        n "The Pacifiers wants to protect the planets and build a peaceful civilization."
        n "The Pacifiers consisit of Vod, Sally, and Bobby."
        mo "The Destroyers are the polar oppisite; they want to destroy all planets that are deemed to dangerous."
        mo "Randy, Kira, and Giddion."
        mo "You could see where it's going."
        n "The point is to be considerate about their opiniions."
        n "You won't lose their respect as the member of the Tweleve, but you will lose their respect as an ally."
        mo "That's about much we want to talk to you about, good luck."
        hide morgana happy
        with moveoutleft
        n "Be wise about your decisions."
        hide nova normal
        with moveoutleft
        m "{b}{i}Great.{/i}{/b}"
        jump ignore

    label ignore:
        scene bg facility
        m "{b}{i}Can't believe I'm part of the Tweleve.{/i}{/b}"
        m "{b}{i}I met so many faces in that meeting.{/i}{/b}"
        show bobby model
        m "{b}{i}First I met Bobby the slime.{/i}{/b}"
        m "{b}{i}He could be quite talktitive, but he's eveeryone's friend.{/i}{/b}"
        hide bobby model
        show randy model
        m "{b}{i}Then, there is Randy.{/i}{/b}"
        m "{b}{i}The Silent reptile that can destroy a planet with just one word.{/i}{/b}"
        hide randy model
        show vod normal
        m "{b}{i}Vod is another member that I've met.{/i}{/b}"
        m "{b}{i}He could be very serious and tough from the outside, bu he may have a soft side.{/i}{/b}"
        m "{b}{i}I gotta make sure to be on his good terms.{/i}{/b}"
        hide vod normal
        show nova happy
        m "{b}{i}There is the mystical Nova, born from a black hole.{/i}{/b}"
        m "{b}{i}She is guided by the stars and has remained neutral to all sides.{/i}{/b}"
        m "{b}{i}She may be my best mentor in case of difficult situation.{/i}{/b}"
        hide nova happy
        show tony model
        m "{b}{i}Another member of the Tweleve is Tony the golem.{/i}{/b}"
        m "{b}{i}Not much that I know about him because he is mute.{/i}{/b}"
        hide tony model
        show giddion silly
        m "{b}{i}Finally, there is Giddion the Hydra.{/i}{/b}"
        m "{b}{i}Never seen his true form, but it may be scary to do so.{/i}{/b}"
        m "{b}{i}Dude's hyper and energetic.{/i}{/b}"
        hide giddion silly
        m "{b}{i}I said it before, these guys are on a different level.{/i}{/b}"
        "{i}Thump{/i}" with vpunch
        "{i}Flutter{/i}" with vpunch
        m "{b}{i}What was that?{/i}{/b}"
        m "{b}{i}It came from that room.{/i}{/b}"
        m "{b}{i}Is it right to check out the noise?{/i}{/b}"
        
    menu:
        "Check it out":
            $ traitor_points += 1
            m "{b}{i}I'm just checking out the noise.{/i}{/b}"
            m "{b}{i}That's all I'm doing.{/i}{/b}"
            jump inspect
        "Leave":
            m "{b}{i}Problably best to not get involved.{/i}{/b}"
            jump continue_forward

    label inspect:
        scene bg secret
        $ tm_1 = True
        m "{b}{i}What is this place?{/i}{/b}"
        m "{b}{i}It's compiled by folders and paper.{/i}{/b}"
        m "{b}{i}What's this paper?{/i}{/b}"
        label room1:
            call screen bookshelf01
        label docpromo_1:
            call showdoc (doc_promo)
            jump room1
        label note_DG21_1:
            call showdoc (doc_DG21)
            jump room1
        label note_S1_1:
            call showdoc (doc_S1)
            jump room1
        label note_buss_1:
            call showdoc (doc_buss)
            jump room1
        label off_paper01:
            m "{b}{i}Oh my god.{/i}{/b}"
            m "{b}{i}I must stay silent for the moment.{/i}{/b}"
            m "{b}{i}I will do something about it.{/i}{/b}"
            m "{b}{i}Not today.{/i}{/b}"

    label continue_forward:
        scene bg office

        m "Another day for me."
        m "What more can I ask."
        m "The guys are out in space, while I'm here doing some paper work."
        m "How do we even get paper work?"
        a "They're important douments to confirm our actions."
        a "Without them, we can't justify our actions."
        m "That makes sense."
        m "I'll just work on these papers and then I get some sleep."
        a "Setting alarm."
        m "Make the ringtone more pleasent to my ears this time."
    