label mge:
  scene bg office
  m "{i}{b}I guess this marks a week working under the Tweleve.{/b}{/i}"
  m "{i}{b}I have tried my best to upset both sides.{/b}{/i}"
  m "{b}{i}If they want to argue with me, they should first reconsider evaluating themselves.{/i}{/b}"
  m "{b}{i}Not everything in life is fair, but we could make it better by stepping out their box.{/i}{/b}"
  m "{b}{i}Having different perspective gives you the chance to make wiser decisions.{/i}{/b}"
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
  
  show morgana happy at right
  with moveinleft
  show nova happy
  with moveinleft
  show tony model at left
  with moveinleft
  
  mo "Heard that you past the test."
  n "It'll be great to work with you."
  t "..."
  m "Glad to hear your praises."
  "You recieved the Middle Ground's ending for not picking sides."
