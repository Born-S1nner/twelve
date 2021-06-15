
label start:

    call act1
    if badending:
        jump ending
    call act2
    call act3
    
label ending:
    if badending:
        "Bad ending"
    else:
        "end"
    return