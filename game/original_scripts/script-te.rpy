label te:
  scene bg office
  m "{i}{b}I guess this marks a week working under the Tweleve.{/b}{/i}"
  m "{i}{b}I wonder if anyone found out that I have been entering that room.{/b}{/i}"
  m "{i}{b}Jaden and Android hasn't said anything up to this point.{/b}{/i}"
  m "{i}{b}Probably best to stay quiet about it.{/b}{/i}"
  m "{i}{b}I feel bad for sneaking behind there back.{/b}{/i}"
  m "{i}sigh{/i}"
  a "[name], Jaden would like to see you at the meeting room."
  m "Oh, okay."
  m "{i}{b}Wonder what Jaden what's with me?{/b}{/i}"
  scene bg roundtable
  show jaden normal
  j "I see that you have showed up, [name]."
  m "What is it that need, Jaden?"
  j "You know what you have done."
  j "You have betrayed our backs and looked into our classified information."
  m "Wha- How did you know?!" with hpunch
  j "It doesn't take the smartest detective to figure it out."
  j "You seemed to forget that Android has eyes everywhere in the deep."
  m "Look, I didn't know what I was getting into. I was jus-"
  hide jaden normal
  show jaden angry
  j "Just what!"
  j "Let me recap on what you did behind our back..."

  if tm_1:
    j "You enter the private room the second day and read the document about Universe's population."
  if tm_2:
    j "You enter the room the third day and snoop into the documents about the formation of the Tweleve."
  if tm_3:
    j "You enter the room the fourth day and snoop into the documents about the seach for immortality."
  if tm_4:
    j "You enter the room the fifth day and snoop into the documents about the project phoniex incident."
  if tm_5:
    j "You enter the room the sixth day and snoop into the documents about other members' personal files."

  j "Do I need to clarify your actions?"
  m "No, I mean th-"
  j "{b}Silence{/b}" with hpunch
  j "I don't want to hear another excuse from you."
  j "We trusted you with open arms and this is how you repay us!"
  hide jaden angry
  show jaden sad
  j "{i}sigh{/i}"
  j "I didn't want to believe that you would betray our back."
  j "You are the first member to went against the code and betray us."
  j "I believe that your actions must align with your punishment."
  j "Your punishment for betraying the Tweleve will be..."
  j "{b}Hell!!!{/b}" with hpunch
  m "Wait, I can ex-"
  j "Take him away Morgana."
  mo "{b}blow{/i}" with vpunch
  mo "Good bye, [name]."
  