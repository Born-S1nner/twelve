label act7:

    scene bg roundtable
    show jaden normal
    j "For a long time, we have battle with the forces of evil."
    j "While we can't wipe out the entire evil, we can put a stop to corruption."
    j "Moragana and Nova has some intel about it."
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
    j "What do you propose we should do?"

    menu:
        "Save them":
          m "We should do everything we can to save them."
          $ pacifier_points += 1
        "Destroy them":
          m "We can't risk the possibility of leaving one evil atom alive."
          $ destroyers_points +=1

    show jaden happy
    j "It's settle then. Let's get working!"

    scene bg facility
    m "{i}{b}Guess that reduce the number of planets that are corrupted by evil.{/b}{/i}"
    m "{i}{b}Hope that resolves majority of the problems in the universe.{/b}{/i}"
    m "{i}{b}Oh, the door is still open.{/b}{/i}"
    m "{i}{b}Not sure if I should enter the room this time.{/b}{/i}"
    menu:
        "Enter the room":
           $ traitor_points += 1
           jump inspect4
        "Continue walking":
           jump walk_away

    label inspect4:
        m "{i}{b}Here goes nothing.{/b}{/i}"
        jump return_office04

    label walk_away:
       m "{i}{b}Maybe next time?{/b}{/i}"
        jump return_office04

    label return_office04:
        scene bg office
        m "{b}{i}{/i}{/b}"
    
    if traitor_points != current_total_respect:
        $ traitor_ending = True
    else:
        if world_endgoal <= destroyers_points:
            $ destroyer_ending = True
        elif world_endgoal <= pacifier_points:
            $ pacifier_ending = True
        else:
            $ middle_ground_ending = True