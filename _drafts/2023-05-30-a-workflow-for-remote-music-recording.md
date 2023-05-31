---
layout: post
title: "A Workflow for Remote Music Recording"
date: 2023-05-30 13:21
categories: ['collaboration','audio']
---

If you've followed me on social media for any length of time you likely know that I am a musician. I play horns with [The Hard Modes](https://thehardmodes.com/), a group that does original jazz arrangements of video game music. There's some slight overlap between my time with that group and my work in the DH world, insofar as people in the DH community often tend to enjoy video game music (Quinn Dombrowski even had us perform for the [Animal Crossing: New Digital Humanities](https://www.twitch.tv/acndighum) series!). But the COVID-19 Pandemic and resultant social distancing the last few years really made the work feel more DH-y as we tried to find ways to keep playing together remotely even while it was unsafe to do so in person. We wound up releasing an album of these remote recordings called The Lan Sessions. Greg Weaver, our bandleader, arranger, and saxophonist, talks a bit about the process in his [blog post](https://thehardmodes.com/blog/2021/1/19/enter-the-lan-sessions) introducing the project. 

Working on those tracks taught me a lot about home recording, music production, and music technology. I found it all fascinating, especially the complicated chain of events necessary to make one of these art objects come to life. For the purposes of this post, I wanted to extract from that experience a generalized workflow for others interested in remote recording projects. Full credit here goes to Greg for his guidance in how to do this work - he helped me troubleshoot throughout, and I am mostly documenting the process he shared with me (for myself as well as others). By necessity I will stay fairly high level: I won't be telling which buttons to click in which program for the simple fact that each step along the way is fairly complex. You can write whole articles just on what microphone to use, whole books on how to use Finale. Instead, I'll just aim to give a broad outline of the steps with some context for why they are necessary. I'll try to connect readers to other resources for more information on how to work through each step. One last caveat: I'm sure there are other ways to do this work. This is just the one we used.

## Workflow pt 1: The Setup

1. Complete the arrangement. 

Perhaps obvious, but it helps to have some sense of what your arrangement will be before moving to prepare things for recording. There can be broad variation in how this looks. You might do things entirely on a piano. Or you might arrange entirely in a program meant for sheet music before sending to a different piece of software to prepare the recording process. Or you could arrange entirely in a Digital Audio Workstation and skip the initial process of making sheet music. This muddies the waters somewhat, as the arranging and mixing happens in the same piece of software, but I know lots of people who do it. For our purposes we used two different programs and had to export work between them. In any case, for this workflow you will want to have some sense of the arrangement and the parts before you sit down to start tinkering with next steps. 

2. Create sheet music for the score and parts. 

The next step involves taking your arrangement from abstract idea (e.g. we will play a melody over these chords followed by two soloists and then end) and making it into concrete parts for your players to follow. The music notation software I use for this is [Finale](https://www.finalemusic.com/). Another option is [Sibelius](https://www.avid.com/sibelius). These programs are *deep*. After years I feel I am only beginning to scratch the surface of how to use them. If you've never used music notation software before, you can quickly see their necessity in this scenario: imagine you have written parts for an entire band with pencil by hand. You suddenly remember you have done so in the wrong key and have to rewrite them all (a similar thing happened to me in college). That's where Finale comes in: it lets you easily manage all parts of the process (like quickly transposing to different keys). At the end of this step in the workflow, your goal is to have a score and, most importantly, individual parts for all your musicians. You'll have sheet music to pass out but also, more importantly, have the beginnings of your a template arrangement.

Resource: I actually really like the [tutorials](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Finale_Tutorials.htm) shared on Finale's website for getting started with the software.

3. Export your arrangement as a MIDI file from Finale and import it into Logic. 

Now that we're done with sheet music, you will want to export your work to a different piece of software. To do so, you'll use the MIDI (Musical Instrument Digital Interface) format to convert your music into data that can be exchanged across programs. Once you export your arrangement as MIDI, you will then import that same MIDI file into a DAW (Digital Audio Workstation). I use Logic, but other options are Pro Tools or Ableton. We'll use the DAW for the remaining parts of the arrangement.

4. Assemble each of your tracks

Once you're in your DAW, your next goal is to get a series of tracks for your project. You will want: a full band track, individual tracks for each MIDI instrument, and a metronome track for the tempo. You might have other specific things you'll want to add, like a four measure count-in.

5. Check things out

Things are always a little wonky at this stage, so you will want to check the arrangement pretty closely by listening back to it. Firstly, every instrument will default to a piano track (this makes drum parts sound especially chaotic). So you will need to assign an appropriate instrument sound to each track to make the piece sound as expected. You also should check that each instrument individually. I have found that bass parts, for example, sometimes transfer over an octave or two below where they actually should be. 

6. Modify the project's structure to reflect the arrangement

Once you have everything in Logic and sounding alright, it's time to tinker with the structure of your arrangement. Sheet music will sometimes expect certain parts to be looped. Music notation stands in as a shorthand for this process so that you don't have pages and pages of sheet music that gets repeated. But you need your tracks here to be very literal. Move things around on a macro level to reflect exactly what you want it to sound like. For us, this usually entails taking the solo section and copy/pasting it a few times so that it repeats as expected. Your goal is to make it so that you have a track that can be played start to finish and reflect the arrangement you want. Think of it as though you are working towards a blueprint for your group.

7. Export the project and share with your group.

Now you have a mockup template for the group that you're ready to share. You'll want to export WAV files of each track, including the metronome track. You also might want to export the project as a MIDI track just in case. At this point, we shared all these files in a Google drive folder and sent an email to the group with instructions for recording (including the order in which they should do their piece).

## Workflow pt 2: Recording

All of the above is just setup for the actual recording process. 

1. Get the project

Each person imports the project tracks into their own DAW so that they have the same template to work from.

2. Record their part

Each person should have the full project at this point, broken into individual instrument tracks. To record, each person will mute the MIDI track corresponding to their particular instrument and record their own live part over it. When done, they will export their recording track and upload their materials into a shared folder. 

If you are planning to use video, you will want your players to record this at the same time. We usually had a phone recording in landscape HD at the same time we recorded the audio. And then we clap to offer an easy way up the audio and video tracks down the line.

3. Repeated by the next person

The collected multitrack recording builds up over time. With each new person, more of the instruments in the mix are live and not MIDI. You might also consider tinkering with the order in which you have people record. Greg had us record the rhythm section first, followed by soloists, followed by a second pass of the rhythm section. It was essentially reduplicating the same work, but it meant that there was perhaps a bit more of a live feel to the interplay between soloist and accompanists than there might otherwise have been.

4. Next steps

After everyone has recorded you're ready for next steps. You might send the materials off to be engineered and reprocessed for consistency. After all, everyone recorded their parts seperately so there is likely to be some massaging needed to make a track that sounds workable. You might also be interested in cutting togeter a video to share online based on the work you did. 