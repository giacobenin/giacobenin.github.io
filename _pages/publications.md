---
permalink: /publications/
title: "Publications"
lead: "Selected publications. The full list is on [Google Scholar](https://scholar.google.com/citations?user=fa77M2IAAAAJ)."
rows: true
description: "Selected patents and papers by Giacomo Benincasa on tactical, mobile ad hoc and IoT networking, middleware and information dissemination."
---

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
<section class="row">
<h2 id="{{ parts[0] }}s">{{ parts[1] }}</h2>
<ol class="pubs">
    {%- for pub in pubs %}
      {%- if pub.pubtype == "paper" %}{% assign pubclass = "schema:ScholarlyArticle" %}{% else %}{% assign pubclass = "schema:CreativeWork" %}{% endif %}
  <li><article class="pub" typeof="{{ pubclass }} foaf:Document">
    <time class="yr" datetime="{{ pub.date | date: '%Y' }}">{{ pub.date | date: '%Y' }}</time>
    <div>
    {%- if pub.paperurl -%}
    <a class="pub-title" property="schema:url" href="{{ pub.paperurl }}"><cite property="schema:name dc:title">{{ pub.title }}</cite></a>
    {%- else -%}
    <cite class="pub-title" property="schema:name dc:title">{{ pub.title }}</cite>
    {%- endif -%}
    <p class="meta">
    {%- for author in pub.authors -%}
      {%- assign homepage = site.data.coauthors[author] -%}
      {%- capture aid %}{{ '/publications/' | absolute_url }}#{{ author | slugify }}{% endcapture -%}
      {%- comment -%} One stable IRI per person, so the same co-author is one node across publications. The name is in <meta>; the visible element is the link or plain text. {%- endcomment -%}
      {%- if author == site.author.publication_name -%}
        {%- comment -%} The site owner: bold, no visible link, but tied to this site and the profiles in _config.yml. {%- endcomment -%}
        <strong property="schema:author foaf:maker" resource="{{ aid }}" typeof="schema:Person foaf:Person"><meta property="schema:name foaf:name" content="{{ author }}"><link property="schema:url foaf:homepage" href="{{ '/' | absolute_url }}">
        {%- for link in site.author.links %}<link property="schema:sameAs foaf:account" href="{{ link.url }}">{% endfor -%}
        {{ author }}</strong>
      {%- elsif homepage -%}
        <span property="schema:author foaf:maker" resource="{{ aid }}" typeof="schema:Person foaf:Person"><meta property="schema:name foaf:name" content="{{ author }}"><a property="schema:url foaf:homepage" href="{{ homepage }}">{{ author }}</a></span>
      {%- else -%}
        <span property="schema:author foaf:maker" resource="{{ aid }}" typeof="schema:Person foaf:Person"><meta property="schema:name foaf:name" content="{{ author }}">{{ author }}</span>
      {%- endif -%}
      {%- unless forloop.last %}, {% endunless -%}
    {%- endfor -%}
    {%- if pub.et_al %}, et al.{% else %}.{% endif %} <em>{{ pub.venue }}</em>.</p>
    <meta property="schema:datePublished" content="{{ pub.date | date: '%Y' }}">
    </div>
  </article></li>
    {%- endfor %}
</ol>
</section>
  {%- endif %}
{% endfor %}
</div>
