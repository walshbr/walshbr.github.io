---
layout: post
title: "Octopress, GitHub, and Custom Domains"
date: 2017-02-25 12:00
comments: true
categories: [tips]
---
I have been using GitHub to host my site as a .github.io domain for years now, but I decided to switch to something a bit easier to remember as way of consolidating a few pieces of my digital identity (I had been variably using bmw9t and walshbr as public-facing usernames in different places). I'm now up and running with [Reclaim Hosting](https://reclaimhosting.com/), and they have been fantastic in helping me to troubleshoot the issues. 

I ran into a quirky issue with my setup, though, and I thought I'd document it in case someone else runs into this in the future when trying to mix Octopress, GitHub, and custom domain mapping. My old workflow looked like this:

1. Work locally.
2. Push to GitHub for version control, issue tracking, and transparency.
3. GitHub serves and hosts the site.

So I'm just changing that last piece to include Reclaim. Normally this involves two steps:

* Visiting the settings page for your GitHub repository and giving it a custom domain.
* Following the instructions [here](https://help.github.com/articles/quick-start-setting-up-a-custom-domain/) to have your own registered domain point to GitHub and vice versa. In the case of Reclaim Hosting, they had their own set of instructions for making things [work](https://community.reclaimhosting.com/t/domain-mapping-to-github/270).

Reclaim helped me work out kinks, and now the workflow, as I understand it, looks like this:

1. Work locally
2. Push to GitHub for version control, issue tracking, and transparency
3. GitHub points to Reclaim, which grabs the content
4. Reclaim serves the content.

The problem I ran into appeared to be in step four - the content kept disappearing from the Reclaim domain for reasons that took me a while to figure out. Things would periodically return to the Reclaim splash page suggesting I had no content there. After a while, I realized that the problem was only manifesting later in the workflow but actually being caused earlier on.

When you change the custom domain settings for your repository, GitHub actually creates a file in the repository for you. When you give a GitHub repository a custom domain, it creates a [CNAME file in the repository's root](https://github.com/walshbr/walshbr.github.io/blob/master/CNAME). This file contains the custom domain, so it's pretty important. 

That was the problem. My blog is built in [Octopress](http://octopress.org/), a souped up version of Jekyll. After working on content locally, Octopress has a rake command that pushes everything to GitHub. Octopress appears to wipe out the content of the repository and rebuild the whole thing every time. That new CNAME file? It was getting destroyed each time I pushed new content to the site, so whenever I updated my site the domain would appear to go down. The project kept forgetting that it had a custom domain.

To get around this issue, I needed to make that CNAME file a more permanent part of the repository. I made a copy of the CNAME file locally and put it in the _source directory of the Octopress project - this is the directory that Octopress generates the blog from, so now new builds of the site will contain the record of the custom domain. Things seem more or less stable now, though I have fingers and toes crossed.