define m = Character("Me")
define Character("???" color="#ffffff")
define j = Character("Jaden", color="#009900")
define a = Character("Andriod", color="#2eb8b8")
define mo = Character("Morgana", color="#9900cc")
define k = Character("Kira", color="#660000")
define s = Character("Sally", color="#cccc00")
define b = Character("Bobby", color="#00ffcc")
define r = Character("Randy", color="#0033cc")
define v = Character("Vod", color="#e62e00")

define g = Character("Giddion", color="#99cc00")
define t = Character("Tony", color="#ff9900")
define n = Character("Nova", color="#40080")

default passed = 4
default test_score = 0

define respect_meter = 0
define moral_meter = 0

default badending = False

label start:

label ending:
    if badending:
        "Bad ending"

    "end"
    return