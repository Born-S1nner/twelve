label act6:
  scene bg deep
  with fade
  pause
  "{i}Ring, ring, ring!{/i}" with vpunch
  scene bg office
  with fade
  
  a "What would you like to do today."
  menu:
    "Ask for help":
      jump help3

    "Go around the facility":
      m "If it just an isolated planet, I don't got to think too much about it."
      m "I'll figure this out myself."
      a "Okay, good luck."
      m "Thanks."
      jump hallway4

  label help3:
    m "Who are the experts of Libra?"
    a "They would be Tony, Randym and Vod."
    m "{b}{i}Two mutes and one angry kitty.{/i}{/b}"
    m "{b}{i}How am I suppose to work with them?{/i}{/b}"
    m "{b}{i}I'll just do my best and pick of them.{/i}{/b}"
    menu:
      "Tony":
        m "Tony sounds more wiser and calmer on my opinion."
        a "Alright, I'll wish you luck."
        jump tony_res
      "Randy":
        jump randy_res
      "Vod":
        jump vod_res

  label tony_res:
    scene bg facility
    "{i}Thump.{/i}" with vpunch
    "{i}Thump.{/i}" with vpunch
    "{i}Thump.{/i}" with vpunch
    if tm_4:
      m "{b}{i}Shit, it's tony.{/i}{/b}"
      m "{b}{i}Better act cool.{/i}{/b}"
    else:
      m "{b}{i}Yep, that's Tony alright.{/i}{/b}"
      m "{b}{i}Just ask some questions and maybe he will talk or something.{/i}{/b}"

    show tony model
    
    m "Hey Tony"
    t "..."
    m "I had some questions to talk about Libra."
    m "Care to answer them?"
    t "..."
    m "What makes Libra so special?"
    t "..."
    m "Is there a reason to keep it safe?"
    t "..."
    m "Is Libra taking up space?"
    t "..."
    m "..."
    m "Welp, good having a talk with you."
    m "Hope we see each other again sometime."
    t "..."
    m "Bye..."
    m "{b}{i}No use. I'll just leave before I make myself look-{/i}{/b}"
    t "Good bye, fallen king."
    m "You say something!" with hpunch
    hide toney model
    with moveoutright
    m "{b}{i}Good, now he wants to talk and leaves.{/i}{/b}"
    m "{b}{i}Nothing I can do about it.{/i}{/b}"
    m "{b}{i}I'll just make it up or something.{/i}{/b}"

    $ h3_m = True
    $ homework_3 = True
    $ middle_points += 1
    if tm_4:
      jump return_office2
    else: 
      jump hallway2

  label randy_res:
    scene bg facility
    m "{b}{i}Randy can't talk or he will destroy the deep.{/i}{/b}"
    m "{b}{i}Best to make them simple yes or no questions to make it easy for him.{/i}{/b}"
    m "{b}{i}There he is.{/i}{/b}"
    show randy model
    m "Randy."
    r "..."
    m "Have some questions about Libra here..."
    m "You just have to say yes or no if you want."
    m "You can just shake your head to give me a response."
    r "Talk little."
    m "Alright then, let's get started."
    label randy_question:
      menu:
        "Is Libra special to be protected?" if q1_anwsered == False:
          r "No"
          jump randy_question

        "Is it good to keep it safe?" if q2_anwsered == False:
          r "No"
          jump randy_question

        "Is Libra taking up space?" if q3_anwsered == False:
          r "Yesss."
          jump randy_question

        "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          m "Alright, I got what I need."
          m "Thanks for cooperating, Randy."
          r "Yesss."
          hide randy model
          with moveoutright
          m "{b}{i}So he can talk...{/i}{/b}"
          $ h3_d = True
          $ homework_3 = True
          jump hallway2
  
  label vod_res:
    scene bg facility
    m "{b}{i}{/i}{/b}"
    show vod normal
    label vod_question:
      show vod normal
      menu:
        "What makes Libra so special?" if q1_anwsered == False:
          v "The isolated planet could serve as a stress relief for the Tweleve."
          m "Stress relief?"
          v "Even the powerful beings in the universe can be victims to mental illness."
          v "It's good to take a step back and enjoy the beautiful environment of Libra."
          m "I see..."
          hide vod normal
          jump vod_question

        "Is there a reason to keep it safe?" if q2_anwsered == False:
          v "If Libra is gone, I would find a hard time to find a quiet and peaceful place like Libra."
          m "There are more planets like Libra in the universe."
          hide vod normal
          show vod angry
          v "Don't you dare say it like that!"
          m "What?"
          v "Saying all planets are the same is like saying all humans are the same."
          v "They may be made by flesh and bones, but they are also different."
          m "I get it. Sorry."
          v "You better be."
          hide vod angry
          jump vod_question

        "Is Libra taking up space?" if q3_anwsered == False:
          hide vod normal
          show vod silly
          v "Not at all!"
          v "If anything, there is a lot of space for one planet."
          v "We're talking about the universe."
          m "You got a point there."
          hide vod silly
          jump vod_question

        "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          m "I got enough off Libra."
          hide vod normal
          show vod angry
          v "I better expect to see Libra in one piece."
          m "Don't worry, I'll get sent to Jaden and the final ordeal will be set."
          v "Hmp."
          hide vod normal
          with moveoutright
          m "{b}{i}Is he acting like a bully or something?{/i}{/b}"
          $ pacifier_points += 1
          $ h3_s = True
          $ homework_3 = True
          jump hallway4

  label hallway4:
    scene bg facility
    menu:
      "Enter the room":
        jump inspect4

      "Contine walking":
        m "{i}{b}Maybe next time?{/b}{/i}"
        if homework_3:
          jump return_office4
        else: 
          jump tony_res

  label inspect4:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    scene bg secret
    m "{i}{b}There's two files I could read.{/b}{/i}"
    m "{i}{b}Which one should I read first?{/b}{/i}" 
    menu:
      "File 1":
        call showdoc (doc_4)
      "File 2":
        call showdoc (doc_5)
    
    m "{i}{b}Not much to understand at this point.{/b}{/i}"
    m "{i}{b}Might need something to give behind the context.{/b}{/i}"
    m "{i}{b}Nah, I've snoop too much, I'll just head out with what I know.{/b}{/i}"

    if homework_3:
      jump return_office4
    else: 
      jump tony_res

  label return_office4:
    scene bg office
    a "Did you find a solution?"
    m "Yes, I believe..."
    if h3_s:
      m "Save Libra as a Stress relief spot."
    elif h3_d:
      m "Libra should be sestroyed due to lack of activity."
      m "It's a empty planet that takes up space, literally."
    elif h3_m:
      m "Keep them on isolation until further notice."
      m "They don't do much other than living their own life."
      m "Best to keep them isolated."
    a "Noted"
    m "Man, I didn't expect this task to be this hard."
    a "Jaden never said it was going to be easy."
    m "I know, but I still new to the Tweleve."
    a "You'll get used to it."
    m "I hope I do..."
    
    $ q1_anwsered = False
    $ q2_anwsered = False
    $ q3_anwsered = False
    return