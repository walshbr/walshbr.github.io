---
layout: tagpage
title: "Tag: book"
tag: book
robots: noindex
---
What follows are materials drawn from a larger book project I’m working on about an approach to digital humanities pedagogy that intersects with administrative policy to work towards a more equitable landscape for higher education. I’ll be blogging pieces of it as I go, so stay tuned for more related work in the future. Happy to hear feedback, either on social media or by email at bmw9t@virginia.edu.

<ul>
{% for post in site.tags['book'] %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})<br>
    {{ post.description }}
  </li>
{% endfor %}
</ul>
<hr>