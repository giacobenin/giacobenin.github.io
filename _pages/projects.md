---
permalink: /projects/
title: "Projects"
rows: true
description: "Software projects by Giacomo Benincasa, including Fair Golf Teams, a web app that builds balanced golf teams."
---

{% comment %}
Projects live in _data/projects.yml. One <section class="row"> per project:
the project name is the left-column label. Each project is RDFa (schema.org)
authored by the site owner, with schema:citation for a related paper. The same
data feeds the page's JSON-LD (_includes/jsonld.html).
{% endcomment %}
{%- capture me %}{{ '/publications/' | absolute_url }}#{{ site.author.publication_name | slugify }}{% endcapture -%}
<div prefix="schema: https://schema.org/">
{% for p in site.data.projects %}
<section class="row" resource="{{ p.id }}" typeof="schema:{{ p.type | default: 'SoftwareApplication' }}">
<h2 property="schema:name">{{ p.name | xml_escape }}</h2>
<div class="prose">
<link property="schema:author" href="{{ me }}">
{%- if p.category %}<meta property="schema:applicationCategory" content="{{ p.category }}">{% endif %}
<p property="schema:description">{{ p.description | xml_escape }}</p>
{%- if p.paper %}
<p>It implements the algorithms from
<span property="schema:citation" resource="https://doi.org/{{ p.paper.doi }}" typeof="schema:ScholarlyArticle"><a property="schema:url" href="https://doi.org/{{ p.paper.doi }}"><span property="schema:name">{{ p.paper.title | xml_escape }}</span></a>, <em property="schema:isPartOf" typeof="schema:Periodical"><span property="schema:name">{{ p.paper.journal | xml_escape }}</span></em> {{ p.paper.issue }}, <span property="schema:datePublished" content="{{ p.paper.date }}">{{ p.paper.date | slice: 0, 4 }}</span></span>.</p>
{%- endif %}
<p><a property="schema:url" href="{{ p.url }}">Open {{ p.name | xml_escape }}</a></p>
</div>
</section>
{% endfor %}
</div>
