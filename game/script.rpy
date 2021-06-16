
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
    if quick_death_ending:
        "Game Over: load a previous saving spot or reset from the start"
    else:
        "end"
    return