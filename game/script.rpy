
default passed = 4
default test_score = 0

define respect_meter = 0
define moral_meter = 0

default badending = False

    $ act = 1
label start:

###Need to find a way for ren to call act1_mai from a different folder
    $ act = 1
    call act1_main

    $ act = 2    
    call act2
    
    $ act = 3
    call act3

    $ act = 4
    call act4

    $ act = 5
    call act5
    
    call ending

label ending:
    if badending:
        "Bad ending"

    "end"
    return