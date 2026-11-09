---
permalink: /projects/
title: "Projects"
rows: true
description: "Software projects by Giacomo Benincasa, including Fair Golf Teams, a web app that builds balanced golf teams."
---

{% comment %}
Projects live in _data/projects.yml. One <article class="row"> per project:
the project name is the left-column label. Each project is RDFa (schema.org)
authored by the site owner, with schema:citation for a related paper. The same
data feeds the page's JSON-LD (_includes/jsonld.html).
{% endcomment %}
{%- capture me %}{{ site.author.id | absolute_url }}{% endcapture -%}
<div prefix="schema: https://schema.org/">
{% for p in site.data.projects %}
<article class="row" resource="{{ p.id }}" typeof="schema:{{ p.type | default: 'SoftwareApplication' }}">
<h2 property="schema:name">{{ p.name | xml_escape }}</h2>
<div class="prose">
<span property="schema:author" resource="{{ me }}" typeof="schema:Person"><meta property="schema:name" content="{{ site.author.name | xml_escape }}"></span>
{%- if p.category %}<meta property="schema:applicationCategory" content="{{ p.category }}">{% endif %}
<p property="schema:description">{{ p.description | xml_escape }}</p>
{%- if p.paper %}
<p>It implements the algorithms from
<span property="schema:citation" resource="https://doi.org/{{ p.paper.doi }}" typeof="schema:ScholarlyArticle"><a property="schema:url" href="https://doi.org/{{ p.paper.doi }}"><cite property="schema:name">{{ p.paper.title | xml_escape }}</cite></a>, <em property="schema:isPartOf" typeof="schema:Periodical"><meta property="schema:name" content="{{ p.paper.journal | xml_escape }}">{{ p.paper.journal | xml_escape }}</em> {{ p.paper.issue }}, <time property="schema:datePublished" datetime="{{ p.paper.date }}" content="{{ p.paper.date }}">{{ p.paper.date | slice: 0, 4 }}</time></span>.</p>
{%- endif %}
<p><a property="schema:url" href="{{ p.url }}">Open {{ p.name | xml_escape }}</a></p>
</div>
</article>
{% endfor %}
</div>
