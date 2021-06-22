
label start:
    call act1
    if quick_death_ending:
        jump ending
    call act2
    
    call act3
    
    call act6
    
label ending:
    if quick_death_ending:
        "Game Over: load a previous saving spot or reset from the start"
    else:
        if traitor_ending:
            call te
#        elif pacifier_ending:
#            call pe
#        elif destroyer_ending:
#            call de
#        else middle_ground_ending:
#            call mge
    ":end"
    return