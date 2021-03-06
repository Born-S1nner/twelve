label act5:
  scene bg deep
  with fade
  pause
  "{i}Ring, ring, ring!{/i}" with vpunch
  scene bg office
  with fade
  
  m " The same ringtone still?"
  a "Can't do anything about it."
  m "Your suppose to be an AI."
  a "And your suppose to be up right now."
  m "Far point."
  m "What do we got this time?"
  a "There is a planet name Genisi that Jaden would like you to decide."
  a "Like the last homework, would you like some help from the experts?"
  menu:
    "Ask for help":
      jump help2

    "Go around the facility":
      m "Maybe I can figure this out myself?"
      m "I'm just hang outside the office and think about it myself."
      a "Okay, good luck."
      m "Thanks."
      jump hallway3

  label help2:
    m "Who are the experts of Genisi this time?"
    a "The experts would be Sally, Giddion, and Nova."
    m "{b}{i}Seems like I got put into this situation on purpose.{/i}{/b}}"
    m "{b}{i}I should choose one person to get some info about Genisi.{/i}{/b}}"
    
    menu:
      "Sally":
        jump sally_res
      "Giddion":
        jump giddion_res
      "Nova":
        jump nova_res
  
  label nova_res:
    m "Show me the way to Nova."
    a "Alright, I'll notify Nova."
    
    scene bg facility
    m "{b}{i}Wonder if it was a good idea to ask Nova for help.{/i}{/b}"
    m "{b}{i}I mean she is the GAlaxy herself...{/i}{/b}"
    m "{b}{i}But does she know anything about Genisi itself...{/i}{/b}"
    m "{b}{i}Ah, there she is!{/i}{/b}"
    show sally happy
    s "Did you needed spmething from me?"
    m "Just a few questions about Genisi."
    s "Let's see then."
    m "Alright..."

    label nova_questions:
      show nova happy
      menu:
        "What do you personally think about Genisi?" if q1_anwsered == False:
          hide nova happy
          show nova normal
          
          n "Personally, I believe that Genisi is a intelligent planet blinded by knowledge."
          n "So long as they don't expand, they are harmless creatures."
          m "Okay..."

          hide nova normal
          jump nova_questions

        "What would Genisi's future be like if left untouch?" if q2_anwsered == False:
          hide nova happy
          show nova normal
          
          n "It would be a mental breakdown for them."
          m "Why is that?"
          n "They are not prepare to see the truth."
          m "Reasonable..."
          
          hide nova normal
          jump nova_questions

        "What good use would Genisi be to the Tweleve?" if q3_anwsered == False:
          hide nova happy
          show nova normal

          n "We could see how far can civilization go."
          n "If they succeed, that's cool."
          n "If they don't, that's a shame." 
          m "Riiight."

          hide nova normal
          jump nova_questions

        "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          m "I got enough off Genisi."
          n "Let me know on what you decide on Genisi."
          m "Okay."
          n "May the stars look after you"

          hide nova happy
          with moveoutright
          m "Yeah, stars..."

          $ h2_m = True
          $ homework_2 = True
          $ middle_points += 1
          if tm_3:
            jump return_office2
          else: 
            jump hallway2

  label sally_res:
    m "Show me the way to Sally."
    a "Alright, I'll notify Sally."
    
    scene bg facility
    m "{b}{i}Wonder if it was a good idea to ask Sally for help.{/i}{/b}"
    m "{b}{i}I mean she the genius and all...{/i}{/b}"
    m "{b}{i}But can she be unbias about it...{/i}{/b}"
    m "{b}{i}Ah, there she is!{/i}{/b}"
    show sally happy
    s "Guess you wanted to here something from the geius, right?"
    m "Just a few questions about Genisi."
    s "Let me hear them questions."
    m "Alright..."
    
    label sally_question:
      show sally happy
      menu:
        "What do you personally think about Genisi?" if q1_anwsered == False:
          s "It's a planet full of smart people."
          s "They like to expand their mind and knowledge."
          m "Have you work with them before?"
          s "Yes and I made some cool inventions from their knowledge."
          jump sally_question

        "What would Genisi's future be like if left untouch?" if q2_anwsered == False:
          s"It would be glorious!" with hpunch
          m "{b}{i}That was more passionate than Giddion.{/i}{/b}" 
          jump sally_question

        "What good use would Genisi be to the Tweleve?" if q3_anwsered == False:
          s "They could be our guine pig."
          m "Guine pig?"
          s "Yes, they could take the first step and we follow them without getting harm."
          m "I see where you going..."
          jump sally_question

        "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          m "I got enough off Genisi"
          hide sally happy
          show sally silly
          s "Hope you plan to save GEnisi because there is no other planet like GEnisi elsewhere."
          m "I'll take note on that."
          s "Okay, I'm off to Geniva, bye"
          hide sally silly
          with moveoutright
          m "Enjoy the trip."
          $ h2_s = True
          $ homework_2 = True
          $ pacifier_points += 1
          jump hallway3
        
  label giddion_res:
    m "Show me the way to Giddion."
    a "Alright, I'll notify Giddion."
    
    scene bg facility
    m "{b}{i}Wonder if it was a good idea to ask Giddion for help.{/i}{/b}"
    m "{b}{i}He would probably not take my questions seriously.{/i}{/b}"
    m "{b}{i}There he is!{/i}{/b}"
    show giddion happy
    g "Ha ha. I see you have something to talk about with me."
    m "Just a few questions about Genisi."
    g "Hit me with them questions."
    m "Alright..."

    label giddion_question:
      show giddion happy
      menu:
        "What do you personally think about Genisi?" if q1_anwsered == False:
          hide giddion happy
          show giddion angry
          g "They are arrogant traitors."
          g "They claimed to leave me in return for peace."
          g "Turns out they planned to set up."
          m "I bet you were angry."
          g "Yes I am!" with hpunch
          g "Imagine sleeping and suddenly you get a nuke as your alarm clock."
          m "Make sense."

          hide giddion angry
          jump giddion_question 

        "What would Genisi's future be like if left untouch?" if q2_anwsered == False:
          hide giddion happy
          show giddion normal
          g "It would be a disaster."
          m "Why do you say that?"
          g "Imagine giving monkeys a gun."
          g "They would figure out how to use it until they get killed."
          m "Are you implying they would kill themselves by their own creation."
          g "Yes."
          hide giddion normal
          jump giddion_question 

        "What good use would Genisi be to the Tweleve?" if q3_anwsered == False:
          hide giddion happy
          show giddion normal
          g "There isn't."
          m "Right to the point..."
          hide giddion normal
          jump giddion_question 

        "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          m "I got enough off Genisi."
          hide giddion happy
          show giddion angry
          g "If you plan to destroy Genisi, let me do it."
          m "Gotch you."
          g "Good."
          hide giddion angry
          with moveoutright
          m "{b}{i}Genisi are not going to have a good time.{/i}{/b}"
          $ h2_d = True
          $ homework_2 = True
          $ destroyers_points += 1
          jump hallway3

  label hallway3:
    m "hmm!"
    m "{i}{b}That room is still open.{/b}{/i}"
    if tm_2 or tm_1:
      m "{i}{b}Maybe, I'll find somthing more inside.{/b}{/i}"
    else:
      m "{i}{b}Maybe, I'll find somthing interesting there.{/b}{/i}"

    m "{i}{b}No, No.{/b}{/i}"
    m "{i}{b}I shouldn't be snooping around in where my nose doesn't belong.{/b}{/i}"
    m "{i}{b}Then again, I'm a member of the Tweleve...{/b}{/i}"
  
    menu:
      "Enter the room":
        m "{i}{b}Just a peak won't hurt.{/b}{/i}"
        $ tm_3 = True
        jump inspect3

      "Contine walking":
        m "{i}{b}Nah, I can't keep thinking about that stuff.{/b}{/i}"
        m "{i}{b}Maybe next time?{/b}{/i}"
        if homework_2:
          jump return_office3
        else: 
          jump nova_res

    label inspect3:
      scene bg secret
      m "{i}{b}If I look clearly...{/b}{/i}"
      m "{i}{b}Ah! Here's something!{/b}{/i}"
      call showdoc (doc_3)
      
      m "{i}{b}So that's how the Tweleve was formed.{/b}{/i}"
      m "{i}{b}Better leave before someone see me here.{/b}{/i}"
      if homework_2:
        jump return_office3
      else: 
        jump nova_res

  label return_office3:
    scene bg office
    a "Have you got you're anwser yet?"
    m "Yes and I know what I'm gonna do now."
    a "what is it?"
    if h2_s:
      m "Let Genisi be safe for now."
    elif h2_d:
      m "Have Giddion destroy Genisi."
    elif h2_m:
      m "Keep an eye on Genisi fo any advancements."

    m "Make sure to tell that to Jaden."
    a "Will Do, [name]."

    $ q1_anwsered = False
    $ q2_anwsered = False
    $ q3_anwsered = False
    return