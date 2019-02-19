---
layout: post
title: "Close and Distant Reading with Command Line"
date: 2019-01-17 08:14
categories: 
---
Alison Booth and I are co-teaching a graduate course this semester on Digital Literary Studies. As a part of the course, we're having a series of technical workshops - command line, Python, text analysis, encoding, and markup. The scheduling worked out such that these workshops wound up being on Wednesdas, with the discussions of critical theory on digital humanities and literary method mostly on Mondays. That's all fine and good, but I worried that neatly dividing the class out in that way would create a divide between the one day of the week where the students were actively discussing and the other when they were mostly in hands on workshops. Rather than having a hacking day and yacking day, I wanted to see what I could to create an environment for hack-yacking. So when I taught the first workshop on command line I wanted to try something slightly different from what I normally do. 

Teaching programming well is very difficult. An easy, low-hanging fruit way to go about is to connect your laptop and type in front of the students, explaining your keystrokes as you go and asking them to mirror your actions. Another approach I've seen is to use slides to do something similar - sharing code examples and interspersing theoretical concepts as you go. Both of those approaches are all to the good, but they feel a bit too much like lecturing to me. I was trained as a teacher of English, which means that my bread and butter is the discussion seminar. So when teaching this workshop on command line I wanted to push things a little more to see how much discussion I could incorporate into a technical skills workshop. How could I use this experience to help the students begin to think about technology as something that they could engage critically with? as something that was not so alien from their normal work of thoughtful, critical discussion?

My goals for the seventy-five minute session, then, were as follows:

* Introduce the concept of the graphical user interface (GUI)
* Introduce the concept of the command line
* Give practice with the command line
* Use the command line to do something that connected with the discussion we had been having the previous day. 

The overriding concern for me was to communicate the technical skills they needed while not making it a "watch what I type" workshop. First, I shared several different images of graphical user interfaces. 

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/liewcf/14123978540" title="LENOVO Yoga Tablet 8"><img src="https://farm4.staticflickr.com/3710/14123978540_2e09c97bbd_k.jpg" width="2048" height="1365" alt="LENOVO Yoga Tablet 8"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

I framed the activity as continuous with their usual practice of analyzing prose, poetry, or photographs. In the same way that every piece of a text could be interpreted and and described, so too can technology. This piece was inspired by Erin Rose Glass. When she visited the Scholars' Lab last semester for a talk on surveillance capitalism she had the audience close read the Microsoft Word interface, and I thought the move did a great job of defamiliarizing an everyday piece of technology and subjecting it to critique. In this case, I asked my students questions about the construction of the experience the GUI:

* What kind of assumptions does the GUI make of its users?
* What kind of an experience does it want you to have?
* How does it structure your experience?
* What kind of audience does it have in mind?

We had an interesting conversation about accessibility, design, and assumed expertise. I especially wanted the students to note how the GUI makes immediately apparent a range of options to the user. But those options are also limited. So the interface sacrifices possibility for practicality. This discussion set us up well for the next image I presented to them - a terminal window.

![terminal window]({{ root_url }}/assets/images/terminal.jpg)

Again, I paused for discussion. I primarily wanted them to note that the lack of clearly visible options for the terminal meant that it assumed a particular level of audience for its users. For better or for worse, it assumes that you know what you're doing. I could have just told the students all this, of course, but I wanted them to arrive at these ideas themselves. So I mostly framed the activity with questions and helped to direct discussion. In some small way, I hoped the activity would show them that the close reading and analytical skills they developed in other English classes would still be applicable here, even though the objects of study might be different.

With some sense of what the command line was, I took them through a variety of commands with the terminal. This component of the class felt the most like a typical introduction to the command line in that I offered a command, we executed it together, and then reflected on the results. The commands we covered mostly focused on navigating the file system and adding or deleting files:

- cd
- ls
- pwd
- touch
- rm
- mkdir
- cp
- mv
- man 

Nothing too fancy or tricky. I wanted the students to get the terminal under the fingers so that they'd be prepared to work with it for the rest of the course. 

The last activity I did with the class used the terminal to "read" an article that the students read for session using a variety of different command line commands. At each step along the way to think about the kinds of reading enabled or inhibited by the commands.

First I had the students use the curl command to copy down the text of a web page onto their computer. This web page happened to have the contents of an article that they read:

```
$ curl walshbr.com/materials/bode.txt 
```

The curl command spits the text of this page onto their screen, which lead to an interesting conversation about this as a type of reading. I asked the students to characterize the kind of reading it did or did not seem to enable. For one, they noted the lack of an ability to paginate through the text, which seemed to imply that the command was meant for readers that planned to take in the text all at once. As data. As in, curl might be meant to be used by machines thinking about a text as data to be used rather than a thing to be read in a more humanistic sense. 

NOTE: need to figure out an example they can use - bode is gone now b/c TOS

The next mode of reading used the same command but sent the results into a text file called 

grab the text and send it to a file called bode.txt

$ curl walshbr.com/materials/bode.txt > bode.txt

get all of the text for bode

$ cat bode.txt

page through bode one page at a time

$ less bode.txt

search through the text for a word

$ grep reading bode.txt

count the instances of a particular word

$ grep reading bode.txt -c

Things that they noticed:
capitalization matters
computers read quite literally, with no context or knowledge.
the students posited, after johanna drucker and others have suggested, that this form of reading might be the closest reading of all.
cat vs less - cat pulls in the whole text. Might be a hint that they have different assumed audiences in mind - one is more likely computational.
less gets you stuck in the text - can't stop paging!