---
layout: post
title: "Embedding COinS Metadata on a Page Using the Zotero API"
date: 2016-02-15 09:33
comments: true
categories: [W&L, documentation]
---

*[Crossposted on the [Washington and Lee University Digital Humanities Blog](http://digitalhumanities.wlu.edu/blog/2016/02/15/embedding-coins-data-on-a-page-using-the-zotero-api/)]*

This year I am working with Mackenzie, Steve McCormick, and his students on the [Huon d'Auvergne](http://www.huondauvergne.org/) project, a digital edition of a Franco-Italian romance epic. Last term we finished TEI-encoding of two of the manuscripts and put them online, and there is still much left to do. Making the digital editions of each manuscript online is a valuable scholarly endeavor in its own right, but we've also been spending a lot of time considering other ways in which we can enrich this scholarly production using the digital environment.

All of which brings me to the [bibliography](http://www.huondauvergne.org/biblio_temp) for our site. At first, our bibliography page was just a transcription of a text file that Steve would send along with regular updates. This collection of materials is great to have in its own right, but a better solution would be to leverage the many digital humanities approaches to citation management to produce something a bit more dynamic.

Steve already had everything in a Zotero, so my first step was to integrate the site's bibliography with the Zotero collection that Steve was using to populate the list. I found a [python 2 library called zot_bib_web](https://github.com/davidswelt/zot_bib_web) that could do all this quite nicely with a bit of modification. Now, by running the script from my computer, the site's bibliography will automatically pull in an updated Zotero collection for the project. Not only is it now easier to update our site (no more copying and pasting from a word document), but now others can contribute new resources to the same bibliography on Zotero by requesting to join the group and uploading citations. The project's bibliography can continue to grow beyond us, and we will capture these additions as well.

Mackenzie suggested that we take things a bit further by including [COiNS](https://en.wikipedia.org/wiki/COinS) metadata in the bibliography so that someone coming to our bibliography could export our information into the citation manager of their choosing. Zotero's API can also do this, and I used a piece of the [pyzotero](https://github.com/urschrei/pyzotero) Python library to do so. The first step was to add this piece to the zot_bib_web code:

  zot = zotero.Zotero(library_id, library_type, api_key)
  coins = zot.collection_items(collection_id, content='coins')
  coin_strings = [str(coin) for coin in coins]
  for coin in coin_strings:
    fullhtml += coin

Now, before the program outputs html for the bibliography, it goes out to the Zotero API and gets COinS metadata for all the citations, converts them into a format that will work for the embedding, and then attaches each returned span to the HTML for the bibliography.

Now that I had the data that I needed, I wanted to make it work a bit more cleanly in our workflow. Initially, the program returned each bibliographic entry in its own page and meant for the whole bibliography to also be a stand-alone page on the website. I got rid of all that and, instead, wanted to embed them within the website as I already had it. I have the python program exporting the bibliography and COinS data into a small HTML file that I then attach to a div with an id of "includedContent". inserted in the bibliography page. I use some jQuery to do so:

    $(function(){
      $("#includedContent").load("/zotero-bib.html");
    });


Instead of distributing content across several different pages, I mark a placeholder area on the main site where all the bibliographic data and metadata will be dumped. All of the relevant data gets saved in a file 'zot-bib.html' that gets automatically included inside the shell of the bibliography.html page. From there, I just modified the style so that it would fit into the aesthetic of the site.

Now anyone going to our bibliography page with a Zotero extension will see this in the right of the address bar:

<img src="{{ root_url }}/assets/images/zotero-extension.jpg" alt="Image of zotero functioning as an extension next to the sidebar.">

Clicking on the folder icon will bring up the Zotero interface for downloading any of the items in our collection.

<img src="{{ root_url }}/assets/images/zotero-download.jpg" alt="Bulk downloading citations using zotero.">

And to update this information we only need to run a single python script from the terminal to re-generate everything.

The code is not live on the Huon site just yet, but you can download and manipulate these pieces from an example file I uploaded to the [Huon GitHub repository](https://github.com/wludh/huondauvergne/blob/zotero/zot_bib_web/zot_example.py). You'll probably want to start by installing zot_bib_web first to familiarize yourself with the configuration, and you'll have a few settings to update before it will work for you: the library id, library type, api key, and collection ID will all need to be updated for your particular case, and the jQuery excerpt above will need to point to wherever you output the bibliography file.

These steps have strengthened the way in which we handle bibliographic metadata so that it can be more useful for everyone, and we were really only able to do it because of the many great open source libraries that allow others to build on them. It's a great thing - not having to reinvent the wheel.
