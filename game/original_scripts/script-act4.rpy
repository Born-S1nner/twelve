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
  menu:
    "Do the Homework":
      jump homework1
    "Go around the facility":
      jump explore1

  label homework1:
    m "Guess I'll have to do the homework from Jaden."
    m "Android! What's the homework?"
    a "Your first homework involves planet VanGulf."
    a "A small planet with the population of 2,000 people."
    a "I could give you all the details about the planet, but Jaden wants you to ask the experts yourself."
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
        a "Okay. I'll shall inform of your arrival."
        jump bobby_res

      "Ask Kira":
        $ destroyers_points += 1
        m "{b}{i}Kira appears as the smartest and logical member compare to Bobby.{/i}{/b}}"
        m "{b}{i}He would advise me about the current conditions of VanGulf{/i}{/b}}"
        m "Take me to Kira's Location"
        a "Okay. I'll shall inform of your arrival."
        jump kira_res
      
      "Ask Morgana":
        m "{b}{i}Morgana is unbiased and is quite intrested with other people.{/i}{/b}}"
        m "{b}{i}She might give me some clear perspective of VanGulf{/i}{/b}}"
        m "Take me to Morgana's Location"
        a "Okay. I'll shall inform of your arrival."
        jump morgana_res        

label bobby_res:
  scene bg facility
  m "{b}{i}If I remember correctly, Bobby should be around here.{/i}{/b}"
  m "{b}{i}Oh, there he is.{/i}{/b}"
  m "Hey Bobby!"
  show bobby model
  b "Oh, hey [name]!"

label kira_res:
  scene bg facility
  m "{b}{i}If I remember correctly, Kira should be right around here.{/i}{/b}"
  m "{b}{i}Oh, there he is.{/i}{/b}"
  m "Yo, Kira!"
  show kira model
  k "I prefer if you greet me properly, [name]."
  m "Sorry about that."

label kira_res:
  scene bg facility
  m "{b}{i}If I remember correctly, Morgana should be right around here.{/i}{/b}"
  m "{b}{i}Oh, there she is.{/i}{/b}"
  m "Um, M-Morgana!"
  show morgana normal
  k "Oh, if it isn't [name]."
  m "Yea, got some situation that I want you to help."

# heading back
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
      jump return_office2

  label inspect2:
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
    jump return_office2

  label return_office2:
