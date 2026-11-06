---
permalink: /cv/
title: "CV"
lead: "My full work history is on [LinkedIn](https://www.linkedin.com/in/gbenincasa/)."
rows: true
description: "Professional experience of Giacomo Benincasa, senior software engineer at Amazon, previously at Optym/Amadeus, IHMC and the University of West Florida."
---

<!-- To offer a PDF, add assets/files/cv.pdf and add a link to `lead` above:
     [Download my CV (PDF)](/assets/files/cv.pdf) -->

{% comment %}
Content lives in _data/cv.yml; technology tags are defined in
_data/technologies.yml. The page is marked up with RDFa: the site owner (the
same person IRI as on the Publications page) knowsAbout each technology,
identified by its Wikidata item where one exists.
{% endcomment %}
{%- assign me = site.author.publication_name | slugify -%}
<div prefix="schema: https://schema.org/ foaf: http://xmlns.com/foaf/0.1/" resource="{{ '/publications/' | absolute_url }}#{{ me }}" typeof="schema:Person foaf:Person">
<meta property="schema:name foaf:name" content="{{ site.author.name }}">
<link property="schema:url foaf:homepage" href="{{ '/' | absolute_url }}">

<section class="row">
<h2 id="professional-experience">Professional Experience</h2>
<div>
{%- for job in site.data.cv.experience %}
<div class="job">
  {%- comment -%}
  Employment as a schema.org Role: person -worksFor-> EmployeeRole (roleName,
  startDate, endDate) -worksFor-> Organization. Only on the header, so the
  bullets' knowsAbout tags stay attached to the person.
  {%- endcomment %}
  <div class="job-head" property="schema:worksFor" typeof="schema:EmployeeRole">
    <meta property="schema:roleName" content="{{ job.title | xml_escape }}">
    {%- if job.start %}<meta property="schema:startDate" content="{{ job.start }}">{% endif -%}
    {%- if job.end %}<meta property="schema:endDate" content="{{ job.end }}">{% endif -%}
    {%- for key in job.employers -%}
      {%- assign org = site.data.organizations[key] -%}
      <span property="schema:worksFor" resource="http://www.wikidata.org/entity/{{ org.wikidata }}" typeof="schema:Organization"><meta property="schema:name" content="{{ org.name | xml_escape }}"><link property="schema:url schema:sameAs" href="{{ org.url }}"></span>
    {%- endfor %}
    <h3>{{ job.title | xml_escape }}, {{ job.org | xml_escape }}</h3>
    <span class="when">{{ job.dates }}</span>
    <span class="where">{% if job.note %}{{ job.note | xml_escape }} · {% endif %}{{ job.location | xml_escape }}</span>
  </div>
  <ol class="items">
  {%- for item in job.items %}
    {%- comment -%} Mark up concepts flagged `mention: true` where they appear in the text. {%- endcomment -%}
    {%- assign text = item.text | xml_escape -%}
    {%- for entry in site.data.technologies -%}
      {%- if entry[1].mention and text contains entry[0] -%}
        {%- assign concept_name = entry[0] -%}
        {%- capture concept -%}{% include concept.html name=concept_name %}{%- endcapture -%}
        {%- assign text = text | replace: concept_name, concept -%}
      {%- endif -%}
    {%- endfor %}
    <li><div>{{ text }}
      {%- if item.tags %}
      <span class="tech-tags">
        {%- for tag in item.tags -%}
          {%- include concept.html name=tag tag=true -%}
        {%- endfor -%}
      </span>
      {%- endif %}
    </div></li>
  {%- endfor %}
  </ol>
</div>
{%- endfor %}
</div>
</section>
</div>
