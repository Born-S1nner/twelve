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
    w "You must be the new member, right?!" with hpunch
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
            $ day_two_respect_meter += 1
            g "I see that at least you are willing to acknowledge me."
            g "Praise on you mortal!" with hpunch
            hide giddion happy
        "No one said anything":
            hide giddion silly
            show giddion angry
            $ day_two_respect_meter -= 1
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
    j "Introducing our newest member, right here in flesh."
    "{i}clap clap clap clap{/i}"
    j "Now then, do you got something to say?"
    m "Yes..."

    hide jaden happy
    if day_one_respect_meter <= day_one_respect_threshold:
        m "I'm sorry for all the trouble I caused."
    elif day_one_respect_meter => day_one_respect_threshold and  day_one_respect_meter != day_one_respect_threshold_full:
        m "I may have offended some people; in which case, I'm sorry."
    else:
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
        $ day_two_respect_meter += 1
        $ destroyers_points += 1
        m "This universe is being consumed by evil and we must stop it."
        m "We will do what we can to end this evil once and for all."
        m "Even if it mean wiping down colonies and planets."
    "Save the planets from the evil idealist.":
        $ day_two_respect_meter += 1
        $ pacifier_points += 1
        m "This universe is being under attack by evil and we must stop it."
        m "We will do what we can to end this evil once and for all."
        m "Even if it means protecting a planet with our bare hands."

    if pacifier_points < destroyers_points:
        show giddion happy
        g "{b}HAHA{/b}, I knew that I could count on the new member!"
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
    else:
        show bobby model
        b "Glad to know that you have good intentions."
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
        
    scene bg roundtable
    show jaden normal
    j "Alright, alright guys."
    j "Let's settle down and continue on with the meeting."
    j "He does not choose sides; he makes the ultimate decision."
    j "He can ask anyone and listen to anyone if they have a problem with the final decision."
    j "Maybe he could acknowledge your desicion."
    j "isn't that right?"
    hide jaden normal
    menu:
        "That's right":
            $ day_two_respect_meter += 1
        "It depends":
            $ day_two_respect_meter -= 1
    show jaden happy
    j "Alright! Moving on to the next topic."
    j "We have yet to discover the source of evil."
    j "However, Moragana and Nova got some intel about it."
    j "Morgana, tell us your report on your findings?"
    hide jaden happy
    show moragana happy
    mo "Okay, I went far east to find a other advancing civilization."
    mo "I visited planet Gormorrah once again, where it was once been a peaceful civilization."
    mo "Unfortunately, that very same planet got corrupted and I had to end it before they speard any further."
    m "{b}{i}She ended a planet by herself.{/i}{/b}"
    mo "I knew the planet had been infected, so I used my scent to tracee the source."
    mo "It was when I discover a strange nebula cloud that had a preciluar evil scent."
    mo "Since, I'm not good at space stuff, I asked Nova to check out the strange nebula."
    hide morgana happy
    show nova normal
    n "I was called by Morgana and told me to check out the nebula."
    n "I went there and it had a sterange color."
    n "There was no way to describe the very nature of the nebula because it's composition isn't the same as regular nebula."
    n "Instead of hydrogen and nitrogen, I found a new element that is not from the periodic table."
    n "I did some rreseach by moving the nebula into a nearby planet call Sodom."
    n "As soon as it got close to a planet, the nebula absorbed Sodom and corrupted it like how Morgana described it with Gomorrah."
    hide nova normal
    show morgana normal
    mo "What I propose is that the source of evil isn't a person, but rather a corrupt element."
    mo "It can't be created nor destroyed, but it can take my forms."
    hide morgana happy
    show nova normal
    n "To ensure that none of us where corupted, I asked Kira to scan us if we have any within everyone."
    n "Kira took a look at the evil nebula and used it as a scale to trace them."
    n "Kira has confirm that none of us in the Tweleve are corrupted whatsoever."
    n "The real problem is what would happen if one of us gets infected."
    hide nova normal
    show morgana normal
    mo "We made a pledge to never betray a member of the Tweleve, but what if one of us gets corrupted?"
    hide morgana normal
    show kira model
    k "I have predicted that evil was a gene or something invaded like a parasite."
    k "But to think that evil itself takes a form of an atom."
    k "It would be ashame to deal with with powerful beings that could challenge us."
    k "In fact, one of us could even disturb our goal along the way."
    hide kira model
    show vod normal
    v "That is a possibility if every one of us continue to go out there."
    v "However, you claimed that everyone is clean as of right now."
    v "If none of us get contaminated by the evil virus thing, then we should be good."
    a "The problem isn't about us getting contaminated; it's about how we handle the evil atoms without us getting infected."
    v "You have a point there, but nebula manage to move them without getting infected."
    v "So, we could sweep them into one place."
    hide vod normal
    show nova normal
    n "We can't count on me to always move them out."
    n "I had a hard time moving them and some of the evil nebula scattered and infected nearby objects."
    n "I only got lucky, but my luck could run out when I'm not careful enough."
    hide nova normal
    show jaden normal
    j "So we need a plan that can gaurantee our safety and the safety of the universe"
    m "What if..."
    hide jaden normal
    menu:
        "we drag the evil atoms elsewhere":
            $ day_two_respect_meter += 1

            m "we take those evil atoms and complied them into the planet."
            m "The evil atoms are only dangerous when they need a host to take."
            m "Afterwhich, they can't spread "
            m"They even die along with the host adn not affect anything around them."
            show bobby model
            b "are you suggeting mass genocide until all evil atoms are cleared."
            m "we don't have to kill them, we herd them into one location"
            b "Put they could be potentially dangerous if left unchecked."
            m "But we coul-"

        "we find a cure to surpress the evil atoms":
            $ day_two_respect_meter -= 1
            m "Find something that can eliminate the traits of evil."
            m "It could be a vaccine that can prevent anyone that could be affected."
            show kira model
            k "Don't mistake this crisis as a pandemic. It's much more serious."
            k "We can't soley rely on medicine and vaccines to do the work."
            k "What if the evil atoms can mutate into a deadlier stage."
            k "And even if there was a vaccine to begin with, we can't provide the entire universe as we don't know every single being."
            k "This evil atom has went under our radar and we don't know where it comes from."
            k "They could be a bio-weapon or a natural cause phenomenom."
            m "But we coul-"

    show giddion angry
    g "Well, it sounds to me that we got nothing to compete against the evil atoms."
    hide giddion angry
    show sally normal
    s "Not quite."
    s "I got a better suggestion."
    s "First of, we deal with the evil atoms itself that float in space."
    s "Since matter can't be created nor destroyed, we should compile them into somewhere else."
    s "I could make a machine that could suck out those evil atoms, compresss them, and place them in a planet."
    s "Then have Nova or Tony move them carefully to a desired, isolated location."
    s "Second, we deal with those inhabited planets that are affected."
    s "Since a planet could be infected, the evil atoms becomes unable to infect anything."
    s "Have Randy or Giddion destroy the planets until the evil atms are considered dead."
    s "Finally, dealing with those habited planets that are affected."
    hide sally normal
    show nova normal
    n "How do we deal with them?"
    n "Not all planets are worth saving."
    hide nova normal
    show jaden happy
    j "We could have the new member make that decision."
    j "He could save the planet or destroy the planet."
    j "It's his job to make those decision."
#    menu:
#        "":
#        "":
    j "Let's get working!"
    scene bg office
    m "Another day of me"