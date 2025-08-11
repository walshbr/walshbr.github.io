---
layout: post
title: "Bash-it Plugins"
date: 2013-08-11 16:41
comments: true
tags: [tools, tips]
---
Sometimes things go wrong. When this happens, I often find a temporary solution that works fine in the moment, but implementing the fix repeatedly can get annoying over time. Here is something that I had been ignoring for a while and only recently took the time to fix.

I use <a href="https://github.com/revans/bash-it">bash-it</a>, which has lots of neat tricks and functions. Since installing it, however, I had been getting a message every time I open up a terminal window:

``sorry, the z plugin is incompatible with the fasd plugin. you may use either, but not both.``

The message doesn't stop you from going about your business, so I never really read it very closely: bash-it tells you everything you need to know. When installing, bash-it prompts you to make a variety of decisions about how many plugins you will use on a regular basis. I told bash-it to enable everything by default, but this decision caused a conflict between two plugins.

To see which plugins you have enabled, open a terminal window and type:

``$ bash-it show plugins``

In the output, you should see some flavor of the following diagnosing the problem:

``z [x]     maintains a jump-list of the directories you actually use  
z is DEPRECATED, use fasd instead``

Plugin z causes an error when activated with a newer plugin with the same functionality. Bash-it gives you the fix:

``$ bash-it disable plugin z``

After that, your terminal should run free of the message.