---
layout: tagpage
title: "Tag: book"
tag: book
robots: noindex
---
What follows are materials drawn from a larger book project I’m working on about an approach to digital humanities pedagogy that intersects with administrative policy to work towards a more equitable landscape for higher education. I’ll be blogging pieces of it as I go, so stay tuned for more related work in the future. Happy to hear feedback, either on social media or by email at bmw9t@virginia.edu.

{% assign all_posts = site.tags['book'] | reverse %}
{% assign meta_posts = all_posts | where_exp:"item","item.book[0].meta == True "%}
{% assign ch_1_posts = all_posts | where_exp:"item","item.book[0].ch_num == 1"%}
{% assign ch_2_posts = all_posts | where_exp:"item","item.book[0].ch_num == 2"%}
{% assign ch_3_posts = all_posts | where_exp:"item","item.book[0].ch_num == 3"%}
{% assign ch_4_posts = all_posts | where_exp:"item","item.book[0].ch_num == 4"%}
{% assign ch_5_posts = all_posts | where_exp:"item","item.book[0].ch_num == 5"%}

<ul>
  <ul>Chapter 1: Known
    <ul>Section 1
    {% assign ch_1_sec_1_posts = ch_1_posts | where_exp:"item","item.book[1].section_num == 1" %}
    {% for post in ch_1_sec_1_posts %}
      <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})<br>
        {{ post.description }}
      </li>
    {% endfor %}
    </ul>
    <ul>Section 2
      <li>
        Published as "<a href="https://cuny.manifoldapp.org/read/the-pedagogy-of-digital-humanities-budgets/section/535711a2-083e-43c8-8e9a-dd1c677eb57a">The Pedagogy of Digital Humanities Budgets</a>" in Issue 25 of The Journal of Interactive Technology and Pedagogy. 
      </li>
    </ul>
    <ul>Section 3
      {% assign ch_1_sec_3_posts = ch_1_posts | where_exp:"item","item.book[1].section_num == 3" %}
    {% for post in ch_1_sec_3_posts %}
      <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})<br>
        {{ post.description }}
      </li>
    {% endfor %}
    </ul>
  </ul>
  <ul>
  Chapter 3: Intellectualism
    <ul>Section 1
    {% assign ch_3_sec_1_posts = ch_3_posts | where_exp:"item","item.book[1].section_num == 1" %}
    {% for post in ch_3_sec_1_posts %}
      <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})<br>
        {{ post.description }}
      </li>
    {% endfor %}
    </ul>
  </ul>
</ul>

I've also written about the process of the project coming together. 

<ul>
  {% for post in meta_posts %}
  {% if post.book.meta %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})<br>
      {{ post.description }}
    </li>
    {{ post.book[0] }}
  {% endif %}
  {% endfor %}
</ul>

