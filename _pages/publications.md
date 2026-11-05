---
permalink: /publications/
title: "Publications"
---

Selected publications. The full list is on [Google Scholar](https://scholar.google.com/citations?user=fa77M2IAAAAJ).

{% assign sections = "patent:Patents|paper:Journals & Conferences" | split: "|" %}
{% for section in sections %}
  {% assign parts = section | split: ":" %}
  {% assign pubs = site.publications | where: "pubtype", parts[0] | sort: "date" | reverse %}
  {% if pubs.size > 0 %}
## {{ parts[1] }}

{% for pub in pubs %}
- {% if pub.paperurl %}[**{{ pub.title }}**]({{ pub.paperurl }}){% else %}**{{ pub.title }}**{% endif %}  
  {{ pub.authors }}{% assign last = pub.authors | slice: -1 %}{% if last != "." %}.{% endif %} *{{ pub.venue }}*.
{% endfor %}
  {% endif %}
{% endfor %}
