---
permalink: /publications/
title: "Publications"
---

Selected publications. The full list is on [Google Scholar](https://scholar.google.com/citations?user=fa77M2IAAAAJ).

{% comment %}
Each publication is marked up with RDFa using both schema.org (read by search
engines) and FOAF. Co-author home pages come from _data/coauthors.yml.
{% endcomment %}
{% assign sections = "patent:Patents|paper:Journals & Conferences" | split: "|" %}
<div prefix="schema: https://schema.org/ foaf: http://xmlns.com/foaf/0.1/ dc: http://purl.org/dc/terms/">
{% for section in sections %}
  {%- assign parts = section | split: ":" -%}
  {%- assign pubs = site.publications | where: "pubtype", parts[0] | sort: "date" | reverse -%}
  {%- if pubs.size > 0 %}
<h2 id="{{ parts[0] }}s">{{ parts[1] }}</h2>
<ul>
    {%- for pub in pubs %}
      {%- if pub.pubtype == "paper" %}{% assign pubclass = "schema:ScholarlyArticle" %}{% else %}{% assign pubclass = "schema:CreativeWork" %}{% endif %}
  <li typeof="{{ pubclass }} foaf:Document">
    {%- if pub.paperurl -%}
    <a property="schema:url" href="{{ pub.paperurl }}"><strong property="schema:name dc:title">{{ pub.title }}</strong></a>
    {%- else -%}
    <strong property="schema:name dc:title">{{ pub.title }}</strong>
    {%- endif -%}
    <br>
    {%- for author in pub.authors -%}
      {%- assign homepage = site.data.coauthors[author] -%}
      <span property="schema:author foaf:maker" typeof="schema:Person foaf:Person">
      {%- if homepage -%}
        <a property="schema:url foaf:homepage" href="{{ homepage }}"><span property="schema:name foaf:name">{{ author }}</span></a>
      {%- else -%}
        <span property="schema:name foaf:name">{{ author }}</span>
      {%- endif -%}
      </span>
      {%- unless forloop.last %}, {% endunless -%}
    {%- endfor -%}
    {%- if pub.et_al %}, et al.{% else %}.{% endif %} <em>{{ pub.venue }}</em>.
    <meta property="schema:datePublished" content="{{ pub.date | date: '%Y' }}">
  </li>
    {%- endfor %}
</ul>
  {%- endif %}
{% endfor %}
</div>
