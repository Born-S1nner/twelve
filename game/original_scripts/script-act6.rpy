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
      m "Maybe I can figure this out myself?"
      m "I'm just hang outside the office and think about it myself."
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
  
  label hallway4:
    menu:
      "Enter the room":
        jump inspect4

      "Contine walking":
        m "{i}{b}Maybe next time?{/b}{/i}"
        jump return_office4

  label inspect4:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    call showdoc (doc_4)
    scene bg secret

    jump return_office4

  label return_office4:
    if h3_s:
      m ""
    elif h3_d:
      m ""
    elif h3_m:
      m ""
    $ q1_anwsered = False
    $ q2_anwsered = False
    $ q3_anwsered = False
    return