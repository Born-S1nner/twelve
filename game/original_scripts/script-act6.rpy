label act6:
  a "What would you like to do today."
  menu:
    "Do the Homework":
    "Go around the facility":

  menu:
    "Enter the room":
      jump inspect4

    "Contine walking":
      m "{i}{b}Maybe next time?{/b}{/i}"
      jump return_office4

  label inspect5:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    
    scene bg secret

    jump return_office4

  label return_office4: