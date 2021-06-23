label act5:
  menu:
    "Enter the room":
      jump inspect3

    "Contine walking":
      m "{i}{b}Maybe next time?{/b}{/i}"
      jump return_office3

  label inspect5:
    m "{i}{b}Here goes nothing.{/b}{/i}"
    
    jump return_office3

  label return_office3: