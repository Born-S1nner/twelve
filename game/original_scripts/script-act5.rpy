label act5:
  a "What would you like to do today."
  menu:
    "Do the Homework":
    "Go around the facility":

  menu:
    "Enter the room":
      jump inspect3

    "Contine walking":
      m "{i}{b}Maybe next time?{/b}{/i}"
      jump return_office3

  label inspect5:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    
    scene bg secret
    
    jump return_office3

  label return_office3: