# Definitions.rpy

# This section defines stuff for your mod!
# Use this as a starting point if you would like to override with your own.

## Note: For Android, make sure to change the default package name of to 
## your own package name in options.rpy under define package_name. 
##Your package name is what you defined in Ren'Py Launcher in the Android section

#define moraility in this game
define moral_meter = 0
#define respect in this game
default respect_meter = 0

#total RP per day of your impresssion with the Tweleve
default day_one_respect_threshold_full = 6
default day_one_respect_threshold = 3

default day_two_respect_threshold_full = 6
default day_two_respect_threshold = 3

#Three-type questions
define q1_anwsered = False
define q2_anwsered = False
define q3_anwsered = False

#multiple choice questions
default passed = 4
default test_score = 0

#Characters
define m = Character("Me")
define w = Character("???", color="#ffffff")
define j = Character("Jaden", color="#009900")
define a = Character("Andriod", color="#2eb8b8")
define mo = Character("Morgana", color="#9900cc")
define k = Character("Kira", color="#660000")
define s = Character("Sally", color="#cccc00")
define b = Character("Bobby", color="#00ffcc")
define r = Character("Randy", color="#0033cc")
define v = Character("Vod", color="#e62e00")
define n = Character("Nova", color="#40080")

define g = Character("Giddion", color="#99cc00")
define t = Character("Tony", color="#ff9900")

# ending

default badending = False
