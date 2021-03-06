# Definitions.rpy
# This section defines stuff for your mod!
# Use this as a starting point if you would like to override with your own.

#define if you are a traitor
default traitor_points = 0
default current_total_respect = 1

#Times you have betray their back
define tm_1 = False
define tm_2 = False
define tm_3 = False
define tm_4 = False
define tm_5 = False

# If you get your homework done
define homework_1 = False
define h1_s = False
define h1_d = False
define h1_m = False

define homework_2 = False
define h2_s = False
define h2_d = False
define h2_m = False

define homework_3 = False
define h3_s = False
define h3_d = False
define h3_m = False

#Three-type questions
define q1_anwsered = False
define q2_anwsered = False
define q3_anwsered = False

#multiple choice questions
default passed = 4
default test_score = 0

#Characters
default name = ""
define m = Character("[name]")

define u = Character("Unknown")
define w = Character("???", color="#ffffff")

define j = Character("Jaden", color="#009900")
define a = Character("Andriod", color="#2eb8b8")
define mo = Character("Morgana", color="#9900cc")
define k = Character("Kira", color="#660000")
define s = Character("Sally", color="#cccc00")#204 204 0
define b = Character("Bobby", color="#00ffcc")#0 255 204
define r = Character("Randy", color="#0033cc")#0 51 204
define v = Character("Vod", color="#e62e00")#230 46 0 
define n = Character("Nova", color="#400080")#64 0 128
define t = Character("Tony", color="#ff9900")#255 153 0
define g = Character("Giddion", color="#99cc00")#153 204 0

# what determines your side on the argument(destroyer or pacifier)
define destroyers_points = 0
define pacifier_points = 0
define middle_points = 0
define world_endgoal = 2

## Multiple endings
# gameover
default quick_death_ending = False
#become Tweleve's friend
default middle_ground_ending = False
# betray the Tweleve by invading privacy and failing to meet the rp requirements
default traitor_ending = False
# side with the destroyers
default destroyer_ending = False
# side with the pacifiers
default pacifier_ending = False

#python 
init python:
  def pause(time=None):
    global _windows_hidden
    if not time:
      _windows_hidden = True
      renpy.ui.saybehavior(afm=" ")
      renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
      _windows_hidden = False
      return
    if time <= 0:
      return
    _windows_hidden = True
    renpy.pause(time)
    _windows_hidden = False