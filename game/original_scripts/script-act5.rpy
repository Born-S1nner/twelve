label act5:
  scene bg deep
  with fade
  pause
  "{i}Ring, ring, ring!{/i}" with vpunch
  scene bg office
  with fade

  a "What do you suggest to do?"
  menu:
    "Ask for help":
      jump help2
    "Go around the facility":
      jump hallway3

  label help2:
    menu:
      "Sally":
        jump sally_res
      "Giddion":
        jump giddion_res
      "Nova":
        jump nova_res
  
  label hallway3:
    menu:
      "Enter the room":
        jump inspect3

      "Contine walking":
        m "{i}{b}Maybe next time?{/b}{/i}"
        jump return_office3

    label inspect3:
      m "{i}{b}Here goes nothing.{/b}{/i}"
      call showdoc (doc_3)
      scene bg secret

      jump return_office3

  label return_office3:
    scene bg office
  a "Have you got you're anwser yet?"
  m "Yes and I know what I'm gonna do now."
  a "what is it?"
  if h2_s:
    m ""
  elif h2_d:
    m ""
  elif h2_m:
    m ""
  
  m "Make sure to tell that to Jaden."
  a "Will Do, [name]."

  $ q1_anwsered = False
  $ q2_anwsered = False
  $ q3_anwsered = False
  return