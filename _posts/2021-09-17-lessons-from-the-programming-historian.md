---
layout: post
title: "Lessons from The Programming Historian"
date: 2021-09-17 08:09
categories: [digital humanities, projects, collaboration, digital publishing]
---

I had a debrief with Zoe and Sarah, unwatched the main repository, and have gone about finalizing the last little things. So it’s official–I’ve left *The Programming Historian* after four and half years with the project. On the one hand, that is a shockingly small amount of time–it feels like I just got there! Where does the time go? On the other, that’s a substantial portion of my professional career. I joined the project as an editor just as I was leaving my postdoc at W&L, and some of my earliest memories of working in the Scholars’ Lab were of trying to find a good space to take an international Skype call for the journal. I’ve learned tons with the project, and a big part of me is sad to be leaving. But after 4.5 years it was time for me to move on to other things and make space for the other folks in the project to continue shaping it in new and exciting directions.

It’s somewhat customary for outgoing editors to reflect on their work with the project, and I’ve been thinking a lot about what I might say myself. Since I’m a teacher at heart and I viewed my work on PH as primarily pedagogical, I thought I would address first what I did with the group and second what I learned as a result of it. The project calls its publications "[lessons](https://programminghistorian.org/en/lessons/)," after all.

## Editorial work

While on the project I directly edited eight lessons:

- "[Exploring and Analyzing Network Data with Python](https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python)" by John R. Ladd, Jessica Otis, Christopher N. Warren, and Scott Weingart
- "[Creating Web APIs with Python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)" by Patrick Smyth
- "[Creating Mobile Augmented Reality Experiences in Unity](https://programminghistorian.org/en/lessons/creating-mobile-augmented-reality-experiences-in-unity)" by Jacob W. Greene (Fred Gibbs really edited this one - I just oversaw a substantial rewrite of it when the underlying software changed)
- "[Introduction to Audiovisual Transcoding, Editing, and Color Analysis with FFmpeg](https://programminghistorian.org/en/lessons/introduction-to-ffmpeg)" by Dave Rodriguez
- "[Crowdsourced Data Normalization with Pandas](https://programminghistorian.org/en/lessons/crowdsourced-data-normalization-with-pandas)" by Halle Burns
- "[Introduction to Jupyter Notebooks](https://programminghistorian.org/en/lessons/jupyter-notebooks)" by Quinn Dombrowski, Tassie Gniady, and David Kloster
- "[Understanding and Using Common Similarity Measures for Text Analysis](https://programminghistorian.org/en/lessons/common-similarity-measures)" by John R. Ladd
- "Interactive Fiction in the Humanities Classroom: How to Create Interactive Text Games Using Twine" by Gabi Kirilloff (this one is in the last stages of the publication process. So stay tuned for more on that lesson before too long!)

For me, editing new lessons was always the most exciting part of the work I did on *The Programming Historian*. In part, I think this was the teacher/student in me. I enjoyed helping others with their writing, I liked learning about new techniques, and I loved making good learning materials available for others to use. *The Programming Historian* offers an amazing set of educational resources, and I hope these efforts helped to build more inclusive and accessible paths into DH for others.

## Technical Work

*The Programming Historian* is built on Jekyll and served out on GitHub pages. This setup gives the team a great deal of control over the shape of the project, but it also requires a fair amount of technical facility to maintain. I spent a substantial amount of my time on the project working on the technical team, which broadly was responsible for implementing new features and helping to smooth out issues with the publishing process. Here were highlights for me:

- Twitter bot - Early on, the team wanted a bot that would regularly publicize lessons and give more ongoing recognition to authors. I took it on as a new member looking for ways to contribute to the project. The thing is still chugging along despite all odds!  [The bot](https://github.com/programminghistorian/proghistbot) almost certainly could have been designed more elegantly (I didn't really know what I was doing at the time), but if you're interested in such things, the stack for it is as follows:
  - [Heroku](https://www.heroku.com/) runs at regular intervals using an add-on called "Heroku Scheduler." It starts up every day at particular times and begins the process of determining what type of tweet to send out.
  - Depending on the day and time, Heroku runs a Python script to assemble tweets with variables to determine whether we're tweeting in En, Fr, Es, Pt, or sending out communications notices.
  - The script then connects to a google spreadsheet that collects all of the raw material for tweets.
  - The Python script assembles all this and tweets for us.
- I helped to launch the Portuguese version of the project. Matt Lincoln set up the [multilingual infrastructure](https://matthewlincoln.net/2020/03/01/multilingual-jekyll.html) for the group, and I helped implement the Pt journal as the first new language launch since he left.
- I conducted an accessibility audit of our lessons and acted on the results. There is still a lot of work left to do, and the conversation about implementing some of the findings from myself and others is still ongoing. But I was able to make a lot of changes to contrast, alt texts, markup, and more to solve a range of basic problems and put us in a better, more inclusive place.
- I fixed small errors, squashed more substantial bugs, and implemented minor design changes when I couldn't help myself. More on that below.

## Lessons Learned

I learned a lot from *The Programming Historian* that does not neatly fit onto a GitHub ticket in the same way as the above lessons and features. In the years I have worked with it, the project underwent a substantial number of changes, some more clearly publicized than others. We launched French and Portuguese language publications. We became a registered charity in the United Kingdom and implemented a robust series of fundraising plans. We hired our first staffer to help with the project. Even the structure of the project changed considerably in the last few years: we shifted from an organization where everyone had a bit of a hand in every conversation to an elaborate committee system where editors could more easily focus their efforts on the parts of the project they were passionate about. I had little to do with many of these important efforts, but I did want to acknowledge all of the great work by others on the project. I also learned a lot from these efforts! I want to close by sharing just a few of those lessons.

### Unglamorous Gardening

If I'm honest, most of the technical work I did was not flashy. I spent a lot of time mucking around in pull requests, squashing bugs so that the work could continue. It's just too easy for something to go wrong at any stage: a smart quote instead of a straight quote, a caption for an image that doesn't escape its quotation marks, a broken link, etc. These are not difficult things to fix, but each piece of our setup–markdown, GitHub, Jekyll–adds another layer of obscurity between the editors and the work that needs to be done. A lot of my work on the technical team was to try to deal with those issues so work could just keep going. Matt once referred to ongoing lesson maintenance as "garden-tending work" on [a ticket](https://github.com/programminghistorian/jekyll/issues/238) (though I'm sure the metaphor did not originate there), and wading into errors messages often similarly feels like slipping on some gardening gloves to go work in the dirt. How might the DH community better recognize the importance of this sort of vital maintenance? Of the ongoing labor of cultivation, of garden-tending?

### Pedagogy is research is pedagogy is research is pedagogy

A recurring debate on the team is whether the primary identity of the project is one of pedagogy or research. Are the publications produced by *The Programming Historian* articles? Are they lessons? Are they both? For me, the distinction has never made much sense, perhaps because for those of us working in pedagogy there can be no distinction made between teaching and research. For my money, one of the key contributions from *Programming Historian* is in the way it troubles the distance that might otherwise be found between scholarship and pedagogy in conversations elsewhere. It's an internal debate that I hope never settles for *The Programming Historian*, except perhaps to decide that one needn't choose between the two categories, as they are not exclusive.

### International in Vision

Without question, the most valuable piece of the project was in how it opened my thinking, teaching, and network to people and communities beyond those working in English and beyond those working in North America. It was immensely educational and enjoyable to work with collaborators from the Spanish, French, and Portuguese teams and to support their work through the technical team. I learned to be more a thoughtful collaborator and to practice the [#BenderRule](https://thegradient.pub/the-benderrule-on-naming-the-languages-we-study-and-why-it-matters/) when doing my own work on text analysis in English. I became a better teacher and scholar through working with this outstanding group.

### (Not a) Historian

The project is called *The Programming Historian*. I am not a historian, either by training, credentialing, or methodology. More than once in the last 4.5 years the question "But how will this appeal to digital historians?" was invoked to help resolve a particular editorial problem for the problem. As my background is in literary studies, I often felt like I had been accidentally let into a party that wasn't meant for me, but this was more due to imposter syndrome than to any specific actions on the part of my collaborators. After all, the project is useful for humanists more generally–*The Programming Historian* even says as much as part of the one-sentence summary of its mission: "We publish novice-friendly, peer-reviewed tutorials that help humanists learn a wide range of digital tools, techniques, and workflows to facilitate research and teaching." My joining the project coincided with accepting my first full-time job in digital humanities, with fully taking on DH as a career and identity apart from my disciplinary training. Perhaps not by coincidence, then, my collaborators on the project challenged me to think more expansively about my own disciplinary training and the place I could have in the broader DH community.

---

I could go on, but I'll leave it there, as this post already took me a long time to get out. My first encounter with *The Programming Historian* was as an author publishing a [lesson on audacity](https://programminghistorian.org/en/lessons/editing-audio-with-audacity). Later, Amanda Visconti, the Scholars' Lab, and I published a lesson on [collaborative authorship using Jekyll](https://programminghistorian.org/en/lessons/collaborative-blog-with-jekyll-github). My experiences as an author working with the project were always wonderful. If you're a student or early-career scholar, do check out *The Programming Historian* as a possible publication venue for your work! The process is speedy (usually less than a year from submission to publication, typically held up by the author just needing time to write), the review open, and the proposal stage flexible and reasonable. And if you use *The Programming Historian* in your research or teaching, do keep an eye out for the next time the team is recruiting editors! Stepping into an editorial role with them has been one of the great joys of my professional life. I've learned more about collaboration, digital publishing, and pedagogy than I ever would have imagined, and you can't ask for a better group of colleagues to work with. I'm very much looking forward to seeing where they head in the coming years.
