
default badending = False

label start:

    call act1
    if badending:
        jump ending
    call act2
    call act3
    call act4
    call act5
    
    call ending

label ending:
    if badending:
        "Bad ending"
    else:
        "end"
    return