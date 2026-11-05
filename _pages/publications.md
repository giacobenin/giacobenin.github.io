---
permalink: /publications/
title: "Publications"
---

The full list is on [Google Scholar](https://scholar.google.com/citations?user=fa77M2IAAAAJ).

{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign current_year = "" %}
{% for pub in pubs %}
  {% assign year = pub.date | date: "%Y" %}
  {% if year != current_year %}
## {{ year }}
    {% assign current_year = year %}
  {% endif %}
- {% if pub.paperurl %}[**{{ pub.title }}**]({{ pub.paperurl }}){% else %}**{{ pub.title }}**{% endif %}  
  {{ pub.authors }}. *{{ pub.venue }}*.
{% endfor %}
