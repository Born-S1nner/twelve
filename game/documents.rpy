init python:
  class Docs:
    def __init__(self, time="", title="", text=""):
      self.time = time
      self.text = text
      self.title = title
  
  doc_1 = Docs(
    time = "**/**/****",
    title = "Operation Fury",
    text = """\
Since our conquest in space, we have eliminated all potentially dangerous 
planets. However, we were not aware that our methods can backfire and the
very same planets that we should defend were destroyed though collateral
damage. The overall population of the universe has decreased by a massive 
60%. It doesn't sit well with us and decided to uphold the operation. It's 
easy said than done as some of the members grew fond of destroying. I have
Morgana treat those members with therapy and magic. Can't say that it is 
gaurantee, but anything is bettter than nothing."""
  )

image paper = "images/bg/paper.jpg"
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen doc(current_doc, paper="paper"):
  style_prefix "doc"
  vbox:
    add paper
  viewport id "vp":
    child_size (710, None)
    mousewheel True
    draggable True
    has vbox
    null height 40
    text "[current_doc.title]\n[current_doc.time]\n\n[current_doc.text]" style "doc_color"

  vbar value YScrollValue(viewport="vp") style "doc_vbar"

style doc_color:
  size 32
  color "#000"
style doc_vbox:
  xalign 0.5

style doc_viewport:
    xanchor 0
    xsize 720
    xpos 280

style doc_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700
  
label showdoc(doc=None, paper=None):
  if doc == None:
    return
  window hide
  if paper:
      show screen doc(doc, paper=paper)
  else:
      show screen doc(doc)
      
  $ pause()
  hide screen doc
  hide doc_dismiss
  with Dissolve(.5)
  
  window auto
return