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
    a "Your first homework involves planet "

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
    
    show paper02
    
    m "{i}{b}Was that how the Tweleve was formed!{/b}{/i}"
    m "{i}{b}I thought they did it out of sheer goodness.{/b}{/i}"
    m "{i}{b}It was just a way to avoid a battle between them.{/b}{/i}"
    m "{i}{b}It's not so bad, but what will happen when they get bored.{/b}{/i}"
    m "{i}{b}Being the strongest doesn't mean peaceful truce.{/b}{/i}"
    m "{i}{b}The Tweleve could break up if they want to.{/b}{/i}"
    m "{i}{b}Just best hope that day doesn't come.{/b}{/i}"
    jump return_office2

  label return_office2:
