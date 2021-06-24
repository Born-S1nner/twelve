label act4:
  scene bg deep
  with fade
  pause
  "{i}Ring, ring, ring!{/i}" with vpunch
  scene bg office
  with fade
  "{i}Ring, ring, ring!{/i}"
  m "Great, now it's the ringing bell."
  "{i}Ring, ring, ring!{/i}"
  m "Okay, okay, I'm awake now."
  a "It appears that you don't like the ringtone."
  a "Most humans find this ringtone to be pleasent."
  m "Most humans, it makes me feel uncomfortable."
  m "Let just get the day started."
  a "In that caase, let me inform you on some notification."
  a "Jaden is not in the deep at this moment."
  a "He told me to leave you the message."
  m "What's the message?"
  a "Playing the message..."
  j "Yo [name]!"
  m "Jaden?"
  j "Sorry that you won't find me, but I came across some important task."
  j "I won't be back for three days."
  j "I'll just leave you to do some homework while I'm gone."
  J "Each day, you will have to determine the fate of four planets."
  j "You can ask anyone to help you out on your homework, including Android."
  j "Just make sure to get one planet done per day."
  j "Shouldn't be a hard task, think of it as a warm-up."
  j "Well then, see you in three days."
  m "{b}{i}Can't believe that I'm stranded in the deep.{/i}{/b}"
  m "{b}{i}Jaden won't be here to protect me.{/i}{/b}"
  m "{b}{i}Afterall, he has other things to focus on.{/i}{/b}"
  m "{b}{i}I should be stong to fend for myself.{/i}{/b}"
  a "What would you like to do today."
  m "Guess I'll have to do the homework from Jaden."
  m "Android! What's the homework?"
  a "Your first homework involves planet VanGulf."
  a "A small planet with the population of 2,000 people."
  a "I could give you all the details about the planet, but Jaden wants you to ask the experts yourself."
  menu:
    "Ask for help":
      jump help1
    "Go around the facility":
      m "Can't make that decision right now."
      m "I'll just gonna go out and think about myself."
      a "Okay, good luck."
      m "Thanks."
      jump hallway2

  label help1:
    m "Who are the experts to VanGulf?"
    a "The experts would be Bobby, Morgana and Kira."
    m "{b}{i}Great, I got two opposing sides to determine the faith of this planet.{/i}{/b}}"
    m "{b}{i}I should choose one person to get some info about VanGulf.{/i}{/b}}"
    menu :
      "Ask Bobby":
        $ pacifier_points += 1
        m "{b}{i}Bobby is the most talkative member compare to silent Kira.{/i}{/b}}"
        m "{b}{i}He would probably know more about Vangulf.{/i}{/b}}"
        m "Take me to Bobby's location."
        a "Okay. I'll shall inform him of your arrival."
        jump bobby_res

      "Ask Kira":
        $ destroyers_points += 1
        m "{b}{i}Kira appears as the smartest and logical member compare to Bobby.{/i}{/b}}"
        m "{b}{i}He would advise me about the current conditions of VanGulf{/i}{/b}}"
        m "Take me to Kira's Location"
        a "Okay. I'll shall inform him of your arrival."
        jump kira_res
      
      "Ask Morgana":
        m "{b}{i}Morgana is unbiased and is quite intrested with other people.{/i}{/b}}"
        m "{b}{i}She might give me some clear perspective of VanGulf{/i}{/b}}"
        m "Take me to Morgana's Location"
        a "Okay. I'll shall inform her of your arrival."
        jump morgana_res        

label bobby_res:
  scene bg facility
  m "{b}{i}If I remember correctly, Bobby should be around here.{/i}{/b}"
  m "{b}{i}Oh, there he is.{/i}{/b}"
  m "Hey Bobby!"
  show bobby model
  b "Oh, hey [name]!"
  b "What brings you here?"
  m "Just wanted to ask you about VanGulf."
  b "Oh.. well then, ask me anything"
  
  label bh_questions:
    menu:
      "?" if q1_anwsered == False:
          $ q1_anwsered = True
          jump bh_a1
      "?" if q2_anwsered == False:
          $ q2_anwsered = True
          jump bh_a2
      "?" if q3_anwsered == False:
          $ q3_anwsered = True
          jump bh_a3
      "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          jump bh_done

  label bh_a1:
  
    jump bh_questions
        
  label bh_a2:
        
    jump bh_questions

  label bh_a3:
        
    jump bh_questions

  label bh_done:
    $ homework_1 = True
    m "That should be it."
    jump return_office2

label kira_res:
  scene bg facility
  m "{b}{i}If I remember correctly, Kira should be right around here.{/i}{/b}"
  m "{b}{i}Oh, there he is.{/i}{/b}"
  m "Yo, Kira!"
  show kira model
  k "I prefer if you greet me properly, [name]."
  m "Sorry about that."
  
  label kh_questions:
    menu:
      "?" if q1_anwsered == False:
          $ q1_anwsered = True
          jump kh_a1
      "?" if q2_anwsered == False:
          $ q2_anwsered = True
          jump kh_a2
      "?" if q3_anwsered == False:
          $ q3_anwsered = True
          jump kh_a3
      "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          jump kh_done

  label kh_a1:
  
    jump kh_questions
        
  label kh_a2:
        
    jump kh_questions

  label kh_a3:
        
    jump kh_questions

  label kh_done:
    m "That should be it."
    $ homework_1 = True
    jump return_office2

label morgana_res:
  scene bg facility
  if tm_2:
    m "{b}{i}Hope no one saw mein the room.{/i}{/b}"
    m "{b}{i}Wait, I hear someone.{/i}{/b}"
    m "{b}{i}Is that Morgana?{/i}{/b}"
    m "{b}{i}I should approach her before I look suspicous next to the room.{/i}{/b}"
  else:
    m "{b}{i}If I remember correctly, Morgana should be right around here.{/i}{/b}"
    m "{b}{i}Oh, there she is.{/i}{/b}"
  m "Um, M-Morgana!"
  show morgana normal
  mo "Oh, if it isn't [name]."
  m "Yea, got some situation with VanGulf that I want you to help me."
  mo "Okay, let me hear it."
  
  label mh_questions:
    menu:
      "?" if q1_anwsered == False:
          $ q1_anwsered = True
          jump mh_a1
      "?" if q2_anwsered == False:
          $ q2_anwsered = True
          jump mh_a2
      "?" if q3_anwsered == False:
          $ q3_anwsered = True
          jump mh_a3
      "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
          jump mh_done

  label mh_a1:
  
    jump mh_questions
        
  label mh_a2:
        
    jump mh_questions

  label mh_a3:
        
    jump mh_questions

  label mh_done:
    m "That should be it."
    if tm_2:
      jump return_office2
    else: 
      jump hallway2

# heading back
label hallway2:
  m "Huh!"
  if tm_1:
    m "{i}{b}Is that the room where I found that document{/b}{/i}"
  else:
    m "{i}{b}Is that the room where I heard some noise coming from?{/b}{/i}"
  
  m "{i}{b}It is!{/b}{/i}"
  m "{i}{b}That room is still open.{/b}{/i}"
  m "{i}{b}Wonder what I should do?{/b}{/i}"
  
  menu:
    "Enter the room":
      $ traitor_points += 1
      jump inspect2

    "Contine walking":
      m "{i}{b}There's no need for me to enter the room.{/b}{/i}"
      m "{i}{b}Maybe I'll do it some other time.{/b}{/i}"
      if homework_1:
        jump return_office2
      else: 
        jump morgana_res

  label inspect2:
    $ tm_2 = True
    m "{i}{b}Here goes nothing.{/b}{/i}"
    
    scene bg secret
    m "{i}{b}Guess the room has been cleaned before me.{/b}{/i}"
    m "{i}{b}There isn't much to look around except for files and folders.{/b}{/i}"
    m "{i}{b}Maybe I should look at one of the paper in the files.{/b}{/i}"
    m "{b}{i}Oh, let's look at this paper.{/i}{/b}"
    call showdoc (doc_2)
    
    m "{i}{b}Was that how the Tweleve was formed!{/b}{/i}"
    m "{i}{b}I thought they did it out of sheer goodness.{/b}{/i}"
    m "{i}{b}It was just a way to avoid a battle between them.{/b}{/i}"
    m "{i}{b}It's not so bad, but what will happen when they get bored.{/b}{/i}"
    m "{i}{b}Being the strongest doesn't mean peaceful truce.{/b}{/i}"
    m "{i}{b}The Tweleve could break up if they want to.{/b}{/i}"
    m "{i}{b}Just best hope that day doesn't come.{/b}{/i}"
    jump morgana_res

label return_office2:
  scene bg office
  
  
  $ q1_anwsered = False
  $ q2_anwsered = False
  $ q3_anwsered = False
  return