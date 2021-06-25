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
  
  label nova_res:
    menu:
      "" if q1_anwsered == False:
        jump nova_res

      "" if q2_anwsered == False:
        jump nova_res

      "" if q3_anwsered == False:
        jump nova_res
      
      "Let's wrap it up."if q1_anwsered == True or q2_anwsered == True or q3_anwsered == True:
        m "I got enough off Genisi"

        $ h2_m = True
        if tm_3:
          jump return_office2
        else: 
          jump hallway2

  label hallway3:
    menu:
      "Enter the room":
        $ tm_3 = True
        jump inspect3

      "Contine walking":
        m "{i}{b}Maybe next time?{/b}{/i}"
        if homework_2:
          jump return_office3
        else: 
          jump nova_res

    label inspect3:
      m "{i}{b}Here goes nothing.{/b}{/i}"
      scene bg secret

      call showdoc (doc_3)

      if homework_2:
        jump return_office3
      else: 
        jump nova_res

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