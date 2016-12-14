---
layout: post
title: "Ripper Press Reports Dataset"
date: 2016-12-12 09:51
comments: true
categories: 
---
*[Crossposted on the [WLULDH blog](http://digitalhumanities.wlu.edu/blog/2016/12/12/new-resource/).]*

[Crossposted on my personal blog.]

Update: since posting this, [Laura McGrath](http://laurabmcgrath.com/) reached out about finding an error in the CSV version of the data. The version linked to here should be cleaned up now. In addition, you will want to follow steps at the end of this post if using the CSV file in Excel. And thanks to [Mackenzie Brooks](https://digitalhumanities.wlu.edu/blog/author/mackenzie-brooks/) for her advice on working with CSV files in Excel.

This semester I have been co-teaching a course on "Scandal, Crime, and Spectacle in the Nineteenth Century" with [Professor Sarah Horowitz](https://www.wlu.edu/directory/profile?ID=x2047) in the history department at W&L. We've been experimenting with ways to make the work we did for the course available for others beyond our students this term, which led to an [open coursebook on text analysis](https://bmw9t.github.io/blog/2016/10/24/text-analysis-coursebook/) that we used to teach some basic digital humanities methods.

I'm happy to make available today another resource that has grown out of the course. For their final projects, our students conducted analyses of a variety of historical materials. One of our student groups was particularly interested in [Casebook: Jack the Ripper](http://casebook.org/press_reports/), a site that gathers transcriptions of primary and secondary materials related to the Whitechapel murders. The student group used just a few of the materials on the site for their analysis, but they only had the time to copy and paste a few things from the archive for use in [Voyant](http://voyant-tools.org/). I found myself wishing that we could offer a version of the site's materials better formatted for text analysis.

So we made one! With the permission of the editors at the Casebook, we have scraped and repackaged one portion of their site, the collection of press reports related to the murders, in a variety of forms for digital researchers. More details about the dataset are below, and we've drawn from the descriptive template for datasets used by Michigan State University while putting it together. Just write to us if you're interested in using the dataset - we'll be happy to give you access to them under the terms described below. And also feel free to get in touch if you have thoughts about how to make datasets like this more usable for this kind of work. We're planning on using this dataset and others like it in future courses here at W&L, so stay tuned for more resources in the future.

---

**Title**

Jack the Ripper Press Reports Dataset

**Download**

The dataset can be downloaded [here](https://wlu.box.com/s/vfywfpwrivpb7iqc681mzu42tqjez0q9). Write walshb@wlu.edu if you have any problems accessing the dataset. This work falls under a [cc by-nc license](https://creativecommons.org/licenses/by-nc/2.0/). Anyone can use this data under these terms, but they must acknowledge, both in name and through hyperlink, [Casebook: Jack the Ripper](http://casebook.org/press_reports/) as the original source of the data.

**Description**

This dataset features the full texts of 2677 newspaper articles between the years of 1844 and 1988 that reference the Whitechapel murders by Jack the Ripper. While the bulk of the texts are, in fact, contemporary to the murders, a handful of them skew closer to the present as press reports for contemporary crimes look back to the infamous case. The wide variety of sources available here gives a sense of how the coverage of the case differed by region, date, and publication.

**Preferred Citation**

Jack the Ripper Press Reports Dataset, Washington and Lee University Library.

**Background**

The Jack the Ripper Press Reports Dataset was scraped from [Casebook: Jack the Ripper](https://casebook.org/) and republished with the permission of their editorial team in November 2016. The Washington and Lee University Digital Humanities group repackaged the reports here so that the collected dataset may be more easily used by interested researchers for text analysis.

**Format**

The same dataset exists here organized in three formats: two folders, 'by_journal' and 'index', and a CSV file.

* by_journal: organizes all the press reports by journal title.
* index: all files in a single folder.
* casebook.csv: a CSV file containing all the texts and metadata.

Each folder has related but slightly different file naming conventions:

* by_journal:
    * journal_title/YearMonthDayPublished.txt
    * eg. augusta_chronicle/18890731.txt
* index:
    * journal_title_YearMonthDayPublished.txt
    * eg. augusta_chronicle_18890731.txt

The CSV file is organized according to the following column conventions:

* id of text, full filename from within the index folder, journal title, publication date, text of article
* eg. 1, index/august_chronicle_18890731.txt, augusta_chronicle, 1889-07-31, "lorem ipsum…"

**Size**

The zip file contains two smaller folders and a CSV file. Each of these contains the same dataset organized in slightly different ways.

* by_journal - 24.9 MB
* index of all articles- 24.8 MB
* casebook.csv - 18.4 MB
* Total: 68.1 MB uncompressed

**Data Quality**

The text quality here is high, as the Casebook contributors transcribed them by hand.

**Acknowledgements**

Data collected and prepared by Brandon Walsh. Original dataset scraped from [Casebook: Jack the Ripper](http://casebook.org/press_reports/) and republished with their permission.

---

If working with the CSV data in Excel, you have a few extra steps to import the data. Excel has character limits on cells and other configurations that will make things go sideways unless you take precautions. Here are the steps to import the CSV file:

1 Open Excel.
2 Make a blank spreadsheet.
3 Go to the Data menu.
4 Click “Get External Data”.
5 Select “Import Text File”.
6 Navigate to your CSV file and select it.
7 Select “Delimited” and hit next.
8 In the next section, uncheck "Tab" and check "Comma", click next.
9 In the next section, click on the fifth column (the column one to the right of the date column).
10 At the top of the window, select "Text" as the column data format.
11 It will take a little bit to process.
12 Click ‘OK’ for any popups that come up.
13 It will still take a bit to process.
* Your spreadsheet should now be populated with the Press Reports data.