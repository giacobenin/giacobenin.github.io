---
permalink: /projects/
title: "Projects"
rows: true
---

{% comment %}
One <section class="row"> per project: the project name is the left-column
label. Each project is RDFa (schema.org): a WebApplication/SoftwareApplication
authored by the site owner, with schema:citation for a related paper.
{% endcomment %}
{%- capture me %}{{ '/publications/' | absolute_url }}#{{ site.author.publication_name | slugify }}{% endcapture -%}
<div prefix="schema: https://schema.org/">

<section class="row" resource="https://fairgolfteams.neocities.org/" typeof="schema:WebApplication">
<h2 property="schema:name">Fair Golf Teams</h2>
<div class="prose">
<link property="schema:author" href="{{ me }}">
<meta property="schema:applicationCategory" content="SportsApplication">
<p property="schema:description">A web app for golf directors who need to split a field of players into balanced teams. Given each player's USGA Handicap Index, the number of teams, how many best balls count, and the handicap allowance, it runs simulations to build teams that are as evenly matched as possible.</p>
<p>It implements the algorithms from
<span property="schema:citation" resource="https://doi.org/10.3233/JSA-200346" typeof="schema:ScholarlyArticle"><a property="schema:url" href="https://doi.org/10.3233/JSA-200346"><span property="schema:name">Algorithms and Software for the Golf Director Problem</span></a>, <em property="schema:isPartOf" typeof="schema:Periodical"><span property="schema:name">Journal of Sports Analytics</span></em> 6(3), <span property="schema:datePublished" content="2020-07-07">2020</span></span>.</p>
<p><a property="schema:url" href="https://fairgolfteams.neocities.org/#/">Open Fair Golf Teams</a></p>
</div>
</section>

</div>
