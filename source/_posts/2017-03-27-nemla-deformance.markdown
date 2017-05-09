---
layout: post
title: "Remixing the Sound Archive: Cut-up Poetry Recordings"
date: 2017-03-27 13:47
comments: true
categories: 
---
*[Recently I spoke at NEMLA 2017 with [Ken Sherwood](http://www.sherwoodweb.org/) and [Chris Mustazza](https://sites.sas.upenn.edu/mustazza/biocv). The panel was on "Pedagogy and Poetry Audio: DH Approaches to Teaching Recorded Poetry/Archives," and my own contribution extended some [past experiments](http://walshbr.com/blog/2015/01/12/deformance-talk/) with using deformance as a mode of analysis for audio recordings. The talk was given from notes, but the following is a rough recreation of what took place.]*

![introductory slide]({{ root_url }} images/nemla/slide01.jpg)

Robust public sound archives have made a wide variety of material accessible to students and researchers for the first time, and they provide helpful records of the history of poetic performance throughout the past century. But they can also appear overwhelming in their magnitude, particularly for students: where to begin listening? This talk argues that we can help students start to explore these archives if we think about the archives as more than just an account of past performances: they can provide the materials for resonant experiments in poetry composition. I want to think about new ways to explore these archives through automatic means, through the use of software that algorithmically explores the sound collection as an object of study. 

This talk thus models an approach to poetry recordings founded in the deformance theories of Jerome McGann and Lisa Samuels and the cut-up techniques of the Dadaists. In the presentation, I prototype a pair of class assignments that asks students to slice up audio recordings of a particular poet, reassemble them into their own compositions, and reflect on the process. These acts of playful destruction and reconstruction help students think about poems as constructed sound objects and about poets as sound artists. By diving deeply into the extant record for a particular poet, students might produce performative audio essays that enact a reading of that artist’s sonic patterns. By treating sound archives as the raw ingredients for poetic remixes, we can explore and remake sound objects while also gaining new critical insight into performance practices. In the process of remixing the sound archive, we can encourage students to engage more fully with it. 

So I'll frame the interventions and theoretical frameworks I'm making before proposing two different models for how to approach such an assignment depending on the instructor’s own technical ability and pedagogical goals: one model that uses Audacity and another that uses Python to cut and reassemble poetry recordings. I'll demonstrate example compositions from the latter. It will get weird.

![provocations for the talk]({{ root_url }} images/nemla/slide02.jpg)

So there are a couple provocations at the center of my talk founded in an assumption about the way students hear poetry recordings. In my experience, they often hear them not as sound artifacts but as representations of text. They might come to these recordings looking to hear the poet herself speak, or they might be looking to get new perspectives on the poem. But they fundamentally are interested in hearing the text, in hearing these things as analogues to print. This is all well and good - the text is clearly a part of what makes poetry recordings special, but I think our challenge as teachers of poetry is to help students find what really makes these objects unique - the sound artifacts themselves. I want to help the students dig into the sound, into the digital sound in particular. 

![provocations 2 - work in the medium]({{ root_url }} images/nemla/slide03.jpg)

My approach to this need to get students to look beyond the text and towards the sound is to get them working with these materials as sound. We're going to engage them in the medium. They're going to get their hands dirty. We're going to take sound - which might seem abstract and amorphous - and make it something they can touch, take apart, and reassemble. They're going to think about sound as something concrete and constructed.

![audacity icon slide]({{ root_url }} images/nemla/slide04.jpg)

One approach to this might be something like [Audacity](http://www.audacityteam.org/). If you’re not familiar, Audacity is an open source tool that lets you input sound clips and then edit them in a pared down interface. If you have an MP3 on your computer, right click it to open it in Audacity, and you'll get something like this:

![waveform in audacity]({{ root_url }} images/nemla/slide05.jpg)

A waveform. Already we're a bit alienated from the text because this visualization doesn't really allow you to read the poem as such. You'd have to click and play to get that experience. Now you can’t do everything in Audacity, and that’s what I like about it. When I was a music major in college I remember getting introduced to some pretty beefy sound software - [Pro Tools](http://www.avid.com/pro-tools) and [Digital Performer](http://www.motu.com/products/software/dp). I also remember feeling pretty overwhelmed by what they had to offer. So many options! Hundreds and thousands of things to click on! What I like about Audacity is that it is a bit more stripped down. Instead of giving you all the potential options in the universe, it does a smaller subsert really well. Record, edit, mix. Audacity is also open source, so it's free while the other ones are quite expensive.

![first assignment in audacity]({{ root_url }} images/nemla/slide06.jpg)

I'd suggest having your students actually engage with recordings using this software. Here is an example assignment you might put together that asks them to essentially put together an audio essay. Using Audacity, I would have them assemble their own sound recording that mixes in examples from other poetry recordings. First, have them work through a tutorial on editing audio with audacity that I put together for [The Programming Historian](http://programminghistorian.org/lessons/editing-audio-with-audacity). The Programming Historian provides tutorials for a variety of digital humanities tools and methods. This one on Audacity is meant for absolute beginners, and it coaches people through working with the interface. Over the course of the lesson, readers wind up producing a small podcast. 

Now in the context of the lesson, readers use a stub Bach recording. I'd have students read through the lesson and assemble an essay that analyzes poetic sound recordings. Instead of writing a paper on a recording, the students actually integrate their audible evidence into a new sound object, assembling the podcast by hand. Citation description can join together. 

You can imagine having a student pay close attention to the audible qualities of the sounds they are discussing. The sky is the limit, but, personally, I like to imagine students analyzing TS Eliot’s voice by mimicking his style. Or you could imagine an analysis of his accent that tries to position his sense of locality/nation/and globe by examining clips from a number of recordings with cliips of other speakers from around the world.

![pros and cons of audacity]({{ root_url }} images/nemla/slide07.jpg)

I see several benefits to having students work in this way. Students learn a lot about Audacity producing these kinds of audio essays, and I think there is something to be said for having them engage with such a fundamental tool for engaging with audio. There are far more tutorials for the software besides my own, so they're well supported to take on this reasonably intuitive interface.

But there are also limitations here. For one, this is a really slow process. Your students, after all, are engaging with a medium that they can only really experience in time. If you're working with four hours of recordings, you really have to have listened to all of that sound to work with it. And to make anything useful, you'll probably want to have listened to it multiple times and made some notes. That's a long process!

What's more - the assembling process is deliberate. You are asking students to put together clips bit by bit in accordance with a particular reading. And I think is the real problem that I want to address - the medium here is unlikely to show you anything new. It is a great opportunity to illustrate a reading or analysis that you might have, but, ultimately, the process of assembling the clips is less the focus of the production. You want to produce an interpretation, so you illustrate it with sound.

So I want to ask: what are some other ways students can work with audio that might show us truly new things? And how can we get around the need to listen slowly? I want to suggest that we might get more out of such assignments by framing them around creativity and play, by embracing chance-based composition techniques. 

![deformance quotation]({{ root_url }} images/nemla/slide08.jpg)

In shifting the interpretative dimensions in this way, drawing on an idea that comes from Jerome McGann and Lisa Samuels: deformance. At the heart of their essay on "[Deformance and Interpretation](http://www2.iath.virginia.edu/jjm2f/old/deform.html)" is a quote from Emily Dickinson:

> “Did you ever read one of her Poems backward, because the plunge from the front overturned you? I sometimes (often have, many times) have -- a Something overtakes the Mind –”

McGann and Samuels take her very literally, and they proceed to model how reading a poem backwards, line by line, can offer generate readings. As I recall, this process illustrated two main ideas. The first was that reading destructively and deformatively in this way exposes new parts of the poetry to you that you might not otherwise notice. You get a renewed sense of the constructedness of a poem, and the materials of it rise to the surface. The idea behind their work was that by reshaping, warping, demolishing a poem, you actually learned something about its material components and, thus, the original poem itself. The second idea was that all acts of interpretation deformed their objects of study in this way. By interpreting, the poem and our sense of it changed. So destructive reading performs this process in the fullest sense. 

![cut up poetry]({{ root_url }} images/nemla/slide09.jpg)

In thinking about this performative form of reading, I was struck at how similar it sounded to aleatory 

To make the link between the Audacity assignments I was discussing earlier 

![]({{ root_url }} images/nemla/slide10.jpg)

So we have an approach to the first provocation – we can encourage an examination of the material aspects of poetry recordings by having students get their hands dirty.
Have them engage. Have them cut up. Have them warp.
Have them shape.
But the question is – how?
Algorithmic cut-ups

![]({{ root_url }} images/nemla/slide11.jpg)

My approach to this was to use Python.
By working with a machine I was able to produce something that could read hours of audio far quicker than I
I could also work with extant audio software packages to redistribute the audio according to algorithms/interpretations.
All the code I used is available as gist at the bottom link – it took some tinkering to get running, so feel free to get in touch if you wanted to try these things yourself. I can offer lessons learned.


So I’ll do something a bit different for this portion. Rather than give an assignment example up front, I’ll just show you some of the things you can do with Python and why they might be meaningful from an interpretive standpoint. Then I’ll offer reflections at the end.

So my steps here were:
I assembled a small corpus of recordings – all the recordings of The Waste Land that were on LibiVox.
A bunch of installation and configurations were necessary to get the packages going.Then I started playing, exploring all the options Python had.


![]({{ root_url }} images/nemla/slide12.jpg)

	if it is a litter box recording
	<s> 4.570 4.590 0.999800
	if 4.600 4.810 0.489886
	it 4.820 4.870 0.127322
	is 4.880 4.960 0.662690
	a 4.970 5.000 0.372315
	litter 5.010 5.340 0.939406
	box 5.350 5.740 0.992825
	recording(2) 5.750 6.360 0.551414

The standard Python workflow begins by reading in all the recordings and transcribing them. This relies on software called Pocketsphinx. 

Transcription, obviously, is a pretty vexed process just like OCR. Check out how bad this is. What you’re looking at here is a segment from the transcription along with a series of words that the program thinks it heard.

“This is a librivox recording.” becomes “If it is a litter box recording.”

Although my cat might be proud, this shows that the process of working algorthmically is inaccurate. 

![]({{ root_url }} images/nemla/slide13.jpg)

	the wasteland
	i t. s. eliot
	if it is a litter box recording
	oliver box recordings are in the public domain
	for more information or to volunteer
	these visits litter box dot org
	according my elizabeth client
	the wasteland
	i t. s. eliot
	section one
	ariel of the dead
	april is the cruelest month
	reading lie lacks out of the dead land mixing memory and designer
	staring down roots with spring rain
	winter kept us warm
	having earth and forgetful snow
	feeding a little life with tribes two birds


I think this is great! From an interpretive standpoint, this exposes artifacts from the remaking process and shows how each intervention in the text remakes it. You can’t work with a text without changing it. In this case, literally. So this is a longer version of the wasteland transcription from one recording. Also note that multiple recordings will be transcribed differently! Literally, every single attempt to read the text through Python produces a new text. Right in line with the performative interpretations that McGann and Samuels describe.

![]({{ root_url }} images/nemla/slide14.jpg)

<audio controls>
	<source src="{{ root_url }}/mp3s/nemla/voice-sound-supercut.mp3" type="audio/mpeg">
	<source src="{{ root_url }}/ogg/nemla/voice-sound-supercut.ogg" type="audio/ogg">Your browser does not support this audio format.
</audio>

When this package transcribes things, it tags each of the words with a timestamp. So you can disassemble and reassemble the text at will. This allows you to dig into the sound in a new way. Rather than painstakingly assembling readings, you can search across the recording in the same way that you might a text file. In this case, I’ve searched across all the recordings for instances of “sound” and “voice” and mashed up all those instances. You can also use regular expressions to search, allowing for pretty complicated interpolations.Now keep in mind that this is only searching across the transcriptions, which we already noted were inaccurate. So it’s proper to say that this is not telling you something about the text so much as about the recordings themselves. The program is producing a performative reading of the recordings. It’s allowing you to compare multiple recordings in a particular way that would be pretty painstaking to do by hand. 

![]({{ root_url }} images/nemla/slide15.jpg)

<audio controls>
	<source src="{{ root_url }}/mp3s/nemla/speaking-with-text.mp3" type="audio/mpeg">
	<source src="{{ root_url }}/ogg/nemla/speaking-with-text.ogg" type="audio/ogg">Your browser does not support this audio format.
</audio>

Since we have all the transcriptions, we can also create performative readings of our own. Rather than getting all instances of one word, we can put together a text and have it spoken through the text.
By passing the program and passage, it will search through for instances of each word and try to reassemble them into a whole. The reading becomes the recording. But before I play it, let’s read through it.

> Approaching sound in this way is a way for our students to reconstitute their own ideas through the very sound artifacts that they are studying. In so doing, they learn to consider them as sound, as material objects that can be turned over, re-examined, disrupted, and reassembled. But look at how much is gone. How much gets lost. The recording is notable for its absences, its gaps.


That should give you a hint about what kind of recording is about to come out.

Play it.

The recording itself performs the idea, which is that working in Python in this way produces a reading that is somewhat out of control of the user. You can’t really account ahead of time for what will be warped and misshaped. So the result is really sound art as much as sound interpretation.

![]({{ root_url }} images/nemla/slide16.jpg)

<audio controls>
	<source src="{{ root_url }}/mp3s/nemla/demon-voice.mp3" type="audio/mpeg">
	<source src="{{ root_url }}/ogg/nemla/demon-voice.ogg" type="audio/ogg">Your browser does not support this audio format.
</audio>

And one last one. While trying to mash up all the silences in the recording to get a supercut of people breathing, I made a conversion error. Because of my mistake, I accidentally dropped a millisecond every five or six milliseconds in the recording. From this I learned how to make pretty much anyone sound like a demon.

I think moments of serendipity like this are crucial, because they expose the recording qua recording. This is an effect analogous to compression – artifacts get created in the recording process that change it in some way. The process of approaching it leaves nothing unchanged.

![]({{ root_url }} images/nemla/slide17.jpg)

So to review

![]({{ root_url }} images/nemla/slide18.jpg)

So my assignment for python might go something like this.

It suggests that you really get a lot out of dancing across these recordings.

Let the praxis generate the theory – doesn’t have to be the other way around.
Your students can serendipitously learn new things from them.In this case, I can imagine it generating a discussion of regionalism and accents from the librivox participants that threw the transcriber off.

Or you might get a new sense of the particular vocabulary of recorded words in a text, and what it leaves out.

Or you might get a renewed sense of how interpretation is a two-way street that changes our texts as we take them in.

![]({{ root_url }} images/nemla/slide19.jpg)

So to review – 

I think approaches like these are useful for exposing students to sound archives not as sacrosanct pieces of cultural history but as materials to be used, re-used, and remixed into their own work. Approaching the sound recording as the cult-like recording of author certainly has its place, but I’ve deliberately chosen only amateur readers here to suggest that, instead, we can get a lot out of thinking through these recordings as things that are performed and re-preformed, as media objects in their own right distinct from the text itself worth of their own study. And if these whacky assignments yield only that insight and nothing more for the students, well, I’d think of that as a job well done.

![]({{ root_url }} images/nemla/slide20.jpg)

Thanks!
