
default passed = 4
default test_score = 0

define respect_meter = 0
define moral_meter = 0

default badending = False

label start:
    $ act = 0

    $ act = 1
    call act1_main
    call act2
    call act3
    call act4
    call act5
    call ending

label ending:
    if badending:
        "Bad ending"

    "end"
    return