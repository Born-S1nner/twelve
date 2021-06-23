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
    "Go around the facility":

  menu:
    "Enter the room":
      jump inspect2

    "Contine walking":
      m "{i}{b}Maybe next time?{/b}{/i}"
      jump return_office2

  label inspect4:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    
    scene bg secret

    jump return_office2

  label return_office2:
