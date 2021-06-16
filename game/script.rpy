
label start:

    call act1
    if badending:
        jump ending
    call act2
    if badending:
        jump ending
    call act3
    if badending:
        jump ending
    
label ending:
    if badending:
        "Bad ending"
    else:
        "end"
    return