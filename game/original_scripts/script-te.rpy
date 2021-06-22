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
  j "I see that you have showed up."
  show jaden angry
  j "Let me recap on what you did behind our back..."

  if tm_1:
    j "You enter the private room the second day and read the document about Universe's population."
  if tm_2:
    j "You enter the room the third day and snoop into the documents about the formation of the Tweleve."
  if tm_3:
    j "You enter the room the fourth day and snoop into the documents about the seach for immortality."
  if tm_4:
    j "You enter the room for the fifth time and snoop into the documents about the project phoniex incident."
  if tm_5:
    j "You enter the room for the sixth time and snoop into the documents about other members' personal files."

  j "Do I need to repeat it again?"