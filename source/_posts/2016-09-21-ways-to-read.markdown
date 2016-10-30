---
layout: post
title: "Text Analysis Workshop: Four Ways to Read a Text"
date: 2016-09-21 11:51
comments: true
categories: 
---

*[Crossposted on the [WLUDH blog](http://digitalhumanities.wlu.edu/blog/2016/09/22/text-analysis-workshop-four-ways-to-read-a-text/).]*

On Monday I visited [Mackenzie Brooks](http://library.wlu.edu/about/library-directory/mackenzie-brooks)'s course on "Data in the Humanities" to introduce digital text analysis to her students. I faced a few challenges when planning for the visit:

* **Scope** - I had two hours for the workshop and a lot of material to cover. I was meant to introduce anything and everything, as much as I wanted in a general overview of text analysis.  
* **Background** - This course is an introductory digital humanities course that counts as a science credit at W&L, so I assumed no prior knowledge of programming. Mackenzie will be covering some things with them later in the course, but at this stage I needed to avoid anything really technical. 
* **Length** - Two hours was both a lot of time and no time at all. It was certainly not enough time to teach anyone to program for the first time. As an aside, I often find it hard to gauge how much material is appropriate for anything longer than 75 minutes.
* **Content** - Since this was meant to be a general overview of the field, I did not want to lean too heavily on analysis by tools. I worried that if I did so the takeaway for the students would be how to use the tools, not the underlying concepts that the tools aided them in exploring.

I wound up developing a workshop I called "Introduction to Text Analysis: Four Ways to Read a Text." Focusing on four ways meant that I felt comfortable cutting a section if things started to go long. It also meant that I was developing a workshop model that could easily fit varying lengths in the future. For example, I'll be using portions of this workshop throughout my introduction to text analysis lectures in my own course this fall. The approach would necessarily be pretty distant - I couldn't go into much detail for any one method in this time. Finally, I wanted the students to think about text analysis concepts first and then come to tools that would help them to do so, so I tried to displace the tools and projects from the conversation slightly. The hope was that, by enacting or intuiting the methods by hand first, the concepts would stick more easily than they might otherwise. 

The basic structure of the workshop was this: 

1. I introduce a basic methodology for reading. 
2. Students are presented with a handout asking them to read in a particular way with a prompt from me. They complete the exercise. 
3. We talk about the process. We clarify the concept a little more together, and the students infer some of the basic difficulties and affordances of the approach.
4. Then I show a couple tools and projects that use that method for real results.

The four ways of reading I covered were close reading, bags of words, topic modeling, and sentiment analysis. So, to use the topic modeling portion as an example, any one of those units looked something like this:

1. I note how, until now, we have been discussing how counting words gives us a sense of the overall topic or scope of the text. Over time and in close proximity, individual words combine to give us a sense of what a text is about.
2. I give the students three paragraphs with the words scrambled and out of order (done pretty quickly in Python). I ask the students to get in groups and tell me what the underlying topics or themes are for each excerpt. They had to produce three single-word topics for each paragraph, and paragraphs could share topics.
3. We talk about how were able to determine the topics of the texts even with the paragraphs virtually unreadable. Even out of order, certain words in proximity together suggest the underlying theme of a text. We can think of texts as made up of a series of topics like these, clusters of words that occur in noticeable patterns near one another. We have human limits as to how much we can comprehend, but computers can help us run similar, mathematical versions of the same process to find out what words occur near each other in statistically significant patterns. The results can be thought of as the underlying topics or discourses that make up a series of documents. A lot of hand waving, I know, but I am assuming here that students will examine topic modeling in more detail at a later date. Better, I think, to introduce the broad strokes than lose students in the details.
4. I then share [Mining the Dispatch](http://dsl.richmond.edu/dispatch/pages/intro) as an example of topic modeling in action to show the students the kinds of research questions that can be explored using this method.

So, in essence, what I tried to do is create a hands-on approach to teaching text analysis concepts that is flexible enough to fit a variety of needs and contexts. My handouts and slides are all up on [a github repository](https://github.com/bmw9t/waystoread). Feel free to share, reuse, and remix them in any way you would like.