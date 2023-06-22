---
layout: page
title: Blog Archive
permalink: /archive
order: 6
---

In addition to the chronological feed below, the following tag cloud might make it easier to explore past posts.

{% include archive.html %}

<div id="blog-archives">
{% assign reverse_posts = site.posts | reversed %}
{% for post in reverse_posts %}
{% capture this_year %}
  {{ post.date | date: "%Y" }}
{% endcapture %}
{% unless year == this_year %}
  {% assign year = this_year %}
  <h2>{{ year }}</h2>
{% endunless %}
<article>
  {% include archive_posts.html %}
</article>
{% endfor %}
</div>
