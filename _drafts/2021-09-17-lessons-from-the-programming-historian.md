---
layout: post
title: "Lessons from The Programming Historian"
date: 2021-09-17 08:09
categories: [digital humanities, projects, collaboration, digital publishing]
---

I’ve officially done a debrief with Zoe and Sarah, unwatched the repository, and have gone about finalizing the last little things. So it’s official - I’ve left *The Programming Historian* after four and half years with the project. On the one hand, that is a shockingly small amount of time – it feels like I just got there! Where does the time go? On the other, that’s a substantial amount of my professional career. I joined the project just as I was leaving my postdoc at W&L, and some of my earliest memories of working in the Scholars’ Lab were of trying to find a good space to take an international Skype call for the journal. I’ve learned tons with the project, and part of me is sad to be leaving. But after 4.5 years it was time for me to move on to other things and make space for the other folks in the project to continue shaping it in new and exciting directions. It’s somewhat customary for outgoing editors to reflect on their work with the project, and I’ve been thinking a lot about what I might say myself. Since I’m a teacher at heart and I viewed my work on PH as primarily pedagogical, I thought I would reflect a little on first what I did with the group and second what I learned.

## Editorial work

While on the project I directly oversaw eight lessons:

- "[Crowdsourced Data Normalization with Pandas](https://programminghistorian.org/en/lessons/crowdsourced-data-normalization-with-pandas)"
- "[Understanding and Using Common Similarity Measures for Text Analysis](https://programminghistorian.org/en/lessons/common-similarity-measures)"
- "[Introduction to Jupyter Notebooks](https://programminghistorian.org/en/lessons/jupyter-notebooks)"
- "[Introduction to Audiovisual Transcoding, Editing, and Color Analysis with FFmpeg](https://programminghistorian.org/en/lessons/introduction-to-ffmpeg)
- "[Creating Mobile Augmented Reality Experiences in Unity](https://programminghistorian.org/en/lessons/creating-mobile-augmented-reality-experiences-in-unity)" (Fred Gibbs really edited this one - I just worked on a substantial rewrite of it when the underlying software changed)
- "[Creating Web APIs with Python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
- [Exploring and Analyzing Network Data with Python](https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python)
- I'm finalizing edits on one last lesson on teaching with Twine as well! So stay tuned for more.

I loved the editorial work of the project. As much technical labor as I ever put into squashing errors or closing tickets, editing new lessons always was the most exciting part for me. In part, I think this was the teacher/student in me. I enjoyed helping others with their writing, I liked learning about new techniques, and I loved making good learning materials available for others to use. *Programming Historian* is an amazing set of educational resources, and I hope these efforts helped to build more inclusive and accessible paths into DH for others.

## Technical Work

The project is built on Jekyll and served out on GitHub pages. This setup gives the team a great deal of control over the shape of the project. It also requires a fair amount of technical facility to maintain. I spent a substantial amount of my time on PH working on the technical team, which broadly was responsible for new features and helping to smooth out issues with the publishing process. Here were highlights for me:

- Twitter bot - early on the team wanted a regular bot that would publicize lessons and give more ongoing recognition to authors. As a new member to the project looking for ways to contribute I took it on. The thing is still chugging along despite all odds! The only real ongoing work to it has been to update it for new languages. The bot almost certainly could have been designed more elegantly (I didn't really know what I was doing). But if you're interested in such things, the stack for it is…
  - Heroku runs at regular intervals using a module called "Heroku Scheduler." It fires every day at particular times to determine what type of tweet we send out.
  - Depending on the results, Heroku runs a python script to assemble tweets with variables to determine whether we're tweeting in En, Fr, Es, Pt, sending out communications notices, and whether or not it's the first tweet about the thing that week.
  - This script connects to a google spreadsheet that collects all of the raw material for tweets
  - The Python script assembles all this and tweets for us.
- I helped to launch the Portuguese version of the project. Matt Lincoln set up
- I conducted an accessibility audit of our lessons and acted on the results. There is still a lot left to do, and the conversation about implementing some of the findings from myself and others is still ongoing. But I was able to make a lot of changes to contrast, alt texts, markup, and more to solve a range of basic problems and put us in a better place.

## Lessons Learned

### Squashing

If I'm honest most of the technical work I did was not flashy. I spent a lot of time mucking around in pull requests squashing bugs so that the work could continue. It's just too easy for something to go wrong at any stage: a smart quote instead of a straight quote, a caption for an image that doesn't escape its quotation marks, a broken link, etc. These are not difficult things to fix. But each technical layer creates a barrier between an editor and the thing they need to do. A lot of my work was just squashing those things as they came up because I was comfortable reading error messages. A

### International work

The most valuable piece of the project was in how it opened my thinking, teaching, and network to people and communities beyond those working in English and beyond those working in North America.

### Pedagogy is research is pedagogy is research

A recurring debate on the team is whether its function is pedagogy or research. Are the publications journal articles? Are they lessons? Are they both? For me, the distinction has never made much sense, perhaps because for those of us working in pedagogy there can be no distinction made between teaching and research. For my money, the *Programming Historian* is most valuable for the ways it troubles the distance that might otherwise be found between scholarship and pedagogy elsewhere.

### Saying no

Good projects are formed from balanced teams where. Some people are doers. Some people are thinkers. Some people say no. Each of these types of people is valuable! The ideas people push a project to new areas, and the nay-sayers help to scope the project into something doable.

### Not a historian

The project is called *The Programming Historian*. There were several moments during project conversations in the last 4.5 years where some version of "but how will this appeal to digital historians?" was invoked. Fair and fine to think of your primary audience! But, as my background is in literary studies, I often felt like I had been accidentally let into a party that wasn't meant for me. But, of course, the project is useful for humanists more generally, and they even say as much as part of the one-sentence summary of the project.


If you're a student or early-career scholar, do check out *The Programming Historian* as a possible publication venue for your work! The process is speedy (usually less than a year from submission to publication, typically held up by the author just needing time to write), the review open, and the proposal stage flexible and reasonable. And if you use *Programming Historian* in your research or teaching do keep an eye out for the next time they're recruiting editors! Working with them has been one of the great joys of my professional life. I've learned more about collaboration, digital publishing, and pedagogy than I ever would have imagined, and you can't ask for a better group of colleagues to work with. I'm very much looking forward to seeing where they head in the coming years.
