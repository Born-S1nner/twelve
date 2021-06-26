label act6:
  scene bg deep
  with fade
  pause
  "{i}Ring, ring, ring!{/i}" with vpunch
  scene bg office
  with fade
  
  a "What would you like to do today."
  menu:
    "Ask for help":
      jump help3

    "Go around the facility":
      m "If it just an isolated planet, I don't got to think too much about it."
      m "I'll figure this out myself."
      a "Okay, good luck."
      m "Thanks."
      jump hallway4

  label help3:
    m "Who are the experts of Libra?"
    a ""
    menu:
      "Tony":
        jump tony_res
      "Randy":
        jump randy_res
      "Vod":
        jump vod_res

  label tony_res:
    scene bg facility
    m "{b}{i}{/i}{/b}"
    $ h3_m = True
    $ homework_3 = True
    if tm_4:
      jump return_office2
    else: 
      jump hallway2

  label randy_res:
    scene bg facility
    m "{b}{i}{/i}{/b}"
    $ h3_d = True
    $ homework_3 = True
    jump hallway2
  
  label randy_res:
    scene bg facility
    m "{b}{i}{/i}{/b}"
    $ h3_s = True
    $ homework_3 = True
    jump hallway2

  label hallway4:
    scene bg facility
    menu:
      "Enter the room":
        jump inspect4

      "Contine walking":
        m "{i}{b}Maybe next time?{/b}{/i}"
        if homework_3:
          jump return_office4
        else: 
          jump tony_res

  label inspect4:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    call showdoc (doc_4)
    scene bg secret

    jump return_office4

  label return_office4:
    scene show bg office
    a "Did you find a solution?"
    m "Yes, I believe..."
    if h3_s:
      m ""
    elif h3_d:
      m ""
    elif h3_m:
      m "Keep them on isolation until further notice."
      m "They don't do much other than living their own life."
      m "Best to keep them isolated."
    
    $ q1_anwsered = False
    $ q2_anwsered = False
    $ q3_anwsered = False
    return