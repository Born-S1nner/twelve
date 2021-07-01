label pe:
  scene bg office
  m "{i}{b}I guess this marks a week working under the Tweleve.{/b}{/i}"
  m "{i}{b}Not sure I made the right choice to side with the Pacifiers.{/b}{/i}"
  m "{b}{i}It's not everyday where I want to wake up and destroy some planets.{/i}{/b}"
  m "{b}{i}I can't make the final judgement to every living being with a soul.{/i}{/b}"
  m "{b}{i}What if I end up taking someone's normal life.{/i}{/b}"
  m "{i}sigh{/i}"
  a "[name], Jaden would like to see you at the meeting room."
  m "Of course, I'll be there."

  scene bg deepship
  show jaden normal

  m "You needed me, Jaden."
  j "Yes [name]."
  j "When we first met here, I said to myself if I have made the right decision."
  j "I told Android to make a room full of documents to test your loyalty."
  j "Even with the door open, you never enter the room out of curiosity."
  j "It shows that you are well concern about other people's privacy."
  
  hide jaden normal
  show jaden happy
  
  j "You have past the real test of loyalty."
  j "You get to stay with the Tweleve."
  m "Thank you Jaden, it means a lot to me to ear your praise."
  
  hide jaden happy
  show jaden silly
  
  j "It's not over yet, we still got work to do."
  
  hide jaden silly
  "{i}VROOOOMMM{/i}"

  show bobby model at right
  with moveinleft
  show sally silly
  with moveinleft
  show vod normal at left
  with moveinleft

  b "Heard the news about your test."
  s "Congradulation!"
  m "Thanks everyone."
  
  hide sally silly
  show sally happy
  
  s "Vod, you got to show some respect to [name]."
  v "..."
  v "Fine!"

  hide vod normal
  show vod silly at left

  v "Thanks for hearing me out."
  m "You're welcome, Vod."
  m "Good to be working with y'all guys."

  "You recieved the Pacifier's ending for not picking a fight."