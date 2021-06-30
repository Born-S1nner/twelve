
label start:
    #day 1
    call act1
    if quick_death_ending:
        jump ending
    call act2
    #day 2
    call act3
    #day 3
    call act4
    #day 4
    call act5
    #day5
    call act6
    #day 6
    call act7
    #day 7
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
            else middle_ground_ending:
                call mge
        ":end"
        return