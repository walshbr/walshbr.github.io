---
layout: post
title: "Octopress, GitHub, and Custom Domains"
date: 2017-02-25 12:00
comments: true
categories: 
---
I have been using GitHub to host my site as a .github.io domain for years now, but I decided to switch to something a bit easier to remember as way of consolidating a few pieces of my digital identity. I'm now up and running with [Reclaim Hosting](https://reclaimhosting.com/), and they have been fantastic in helping me to troubleshoot the issues. 

I ran into a quirky issue with my setup, though, and I thought I'd document it in case someone else runs into this in the future. My old workflow looked like this:

1 Work locally
2 Push to GitHub for version control, issue tracking, and transparency
3 GitHub serves and hosts the site

So I'm just subbing out that last piece. Noramlly this involves two steps:

* Visiting the settings page for your repository and giving it a custom domain.
* Following the instructions [here](https://help.github.com/articles/quick-start-setting-up-a-custom-domain/) to have my own registered domain point to GitHub and vice versa. In the case of Reclaim Hosting, they had their own set of instructions for making things [work](https://community.reclaimhosting.com/t/domain-mapping-to-github/270).

Reclaim helped me work out kinks, and now the workflow, as I understand it, should look like this:

1 Work locally
2 Push to GitHub for version control, issue tracking, and transparency
3 GitHub points to Reclaim, which grabs the content
4 Reclaim serves the content.

THe problem was in step four - the content kept disappearing from the Reclaim domain for reasons that took me a while to figure out. After a while, I realized that the problem was only manifesting later in the workflow but actually being caused earlier on.

When you change the custom domain settings for your repository, GitHub actually creates a file in the repository for you. When you give a GitHub repository a custom domain, it creates a [CNAME file in the repository's root](https://github.com/walshbr/walshbr.github.io/blob/master/CNAME). This file contains the custom domain, so it's pretty important. 

That was the problem. My blog is built in [Octopress](http://octopress.org/), a souped up version of Jekyll. After working on content locally, Octopress has a rake command that pushes everything to GitHub for serving. Octopress appears to wipe out the content of the repository and rebuild the whole thing everytime. That new CNAME file? It was getting destroyed everytime I pushed new content to the site, so everytime I updated my site the domain would go down. 

To get around this issue, I needed to make that CNAME file a more permanent part of the repository. I made a copy of the CNAME file locally and put it in the _source directory of local copy of the blog - this is the directory that Octopress generates the blog from, so now new builds of the site will contain the record of the custom domain. 