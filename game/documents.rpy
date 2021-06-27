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
  doc_2 = Docs(
    time = "**/**/****",
    title = "12 Foundation",
    text = """\
Do you know what walks on two legs and 
think about the universe, humans. I 
have taken interest in looking how this 
specie tries to make sense on the 
universe. The other guys don’t find my 
view interesting, so I meddle with the 
human world to get a glimpse of their 
lives. Before I know it, I am their 
leader and ruler of their kind. How can the 
last specie of the universe could 
be so ignorant to put me, the destroyer of 
all life, in charge? Let me 
clarify myself to those that do listen. 
I am part of a group called the 12. 
There are twelve of us from each species 
that are deemed too powerful for the 
universe. We all could fight a pointless 
battle, but we choose to work together 
to eliminate all nuisance in our universe. 
From there, we destroyed all life 
that are deemed too dangerous to be left 
unchecked."""
  )
  doc_3 = Docs(
    time = "**/**/****",
    title = "Operation Jellyfish",
    text = """\
We, Tweleve, are the most powerful being in the entire universe. If there is one 
thing that could beat us is death. It's that very idea that I want to challenge. 
I'm no mad genius to know that going against the law of nature is a bad idea. 
Many species have tried and failed to complete them. As the Jade Emperor, It 
will be an honor to find immortality to further help my goal. The one thing I 
must avoid is to have everyone know about this plan. Anyone would go insane if 
they know that I'm chasing after immortality. Once I find them, I must give 
Tweleve strongest beings in the universe to join me."""
  )
  doc_4 = Docs(
    time = "**/**/****",
    title = "Operation Phoinex",
    text = """\
Something went wrong with our project. I might have created something despicable 
to the universe. The vary same substance to find the cure to death has begun to 
backfire. Anyone that absorb the potion would commit the henious act of evil. No 
one should be allow to touch this substance. I must find a way to dispose 
this thing."""
  )
  doc_5 = Docs(
    time = "**/**/****",
    title = "Operation Retirement",
    text = """\
Earth is initial place for retirement to enjoy
our celebration of completing our mission. 
If there is anything to be happy, it’s that 
we don’t have to go to war amongst each
other. Everyone in the group has got bored
of fighting in battlefields. I don’t blame
since we always win even with our hands
tied. The only threat that we encountered
was trying to retrieve some ore from a
black hole. If anyone wants to know what
it’s like to be superior, well it sucks. So
much hype of being a “god” kinda ruined
the whole conquest in space. That is
way we have to rely on Earth to give us
the excitement that we crave for ages.
Earth is big enough for all of us to reside.
The humans that reside in this world are
something else to describe. They all
seemed to be divided or something as
they are not unified as one. Such a shame
that they’re not going with their
disagreementsand segregation.
Since the last these creatures are dumb
and ignorant, we decided to reside
with them until the star explode."""
  )
# individual files for act 7
  doc_j = Docs(
    time = "**/**/****",
    title = "Jaden's Birthday",
    text = """\
Today is my 90th birthday and the Tweleve have decided to throw a surprise party. If I'm going to be honest with you, I never felt so happy to be alive. Back when I was still ruling Earth, everyone wished that I was gone. And so, I left and departed Earth without looking back. I even gifted them the Scroll and my blood line to look after them while I'm gone. I feel so fortunate to come across every member of the Tweleve. Every one of us have been rejected or taken advantage by society. We came from a shitty past that still haunts us til this day. However, we carry those sorrows and grief with pride and marched forward to the future. I, Jaden the Jade Emperor, will not let go of the Tweleve. There will be a future for the Tweleve.
    """
  )
  doc_m = Docs(
    time = "**/**/****",
    title = "Morgana's entitlement",
    text = """\

    """
  )
  doc_r = Docs(
    time = "**/**/****",
    title = "Randy's voice",
    text = """\

    """
  )
  doc_s = Docs(
    time = "**/**/****",
    title = "Sally's intelligence",
    text = """\

    """
  )
  doc_k = Docs(
    time = "**/**/****",
    title = "Kira's revenge",
    text = """\

    """
  )
  doc_g = Docs(
    time = "**/**/****",
    title = "Giddion's throne",
    text = """\

    """
  )
  doc_b = Docs(
    time = "**/**/****",
    title = "Bobby's lunch",
    text = """\

    """
  )
  doc_t = Docs(
    time = "**/**/****",
    title = "Tony's isolation",
    text = """\

    """
  )
  doc_v = Docs(
    time = "**/**/****",
    title = "Vod's fury",
    text = """\

    """
  )
  doc_n = Docs(
    time = "**/**/****",
    title = "Nova's space",
    text = """\

    """
  )
  doc_a = Docs(
    time = "**/**/****",
    title = "Android's wish",
    text = """\

    """
  )
  doc_o = Docs(
    time = "**/**/****",
    title = "Subject [name]",
    text = """\
aowiergfoaeipvrnfawo;imcfoawiuPARALLELvroaincuo
aw8noaw84ncCLONEvaw84y3vtaw39p48tv9p834wvtpa
3333333333333333333333333333333333333333
qcpnawe8urvwaeo4vtnua3o4u9nvt3a94uct0394
nucf012121oiwrunfvowieruvncoaweunREDDoaw
ieuvnowEARTHe8urcvwe938w4vtp9a3w8
    """
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