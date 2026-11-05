---
permalink: /cv/
title: "CV"
---

My full work history is on [LinkedIn](https://www.linkedin.com/in/gbenincasa/).

<!-- To offer a PDF, add assets/files/cv.pdf and uncomment the next line. -->
<!-- [Download my CV (PDF)](/assets/files/cv.pdf) -->

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

<h2 id="professional-experience">Professional Experience</h2>
{% for job in site.data.cv.experience %}
<h3>{{ job.title | xml_escape }}</h3>
<p><strong>{{ job.org | xml_escape }}</strong>{% if job.note %} ({{ job.note | xml_escape }}){% endif %} · {{ job.location | xml_escape }}<br>
<em>{{ job.dates }}</em></p>
<ul>
  {%- for item in job.items %}
  <li>{{ item.text | xml_escape }}
    {%- if item.tags %}
    <span class="tech-tags">
      {%- for tag in item.tags -%}
        {%- assign tech = site.data.technologies[tag] -%}
        {%- if tech.wikidata -%}
        <span class="tech-tag" property="schema:knowsAbout foaf:topic_interest" resource="http://www.wikidata.org/entity/{{ tech.wikidata }}" typeof="schema:Thing"><span property="schema:name">{{ tag | xml_escape }}</span></span>
        {%- else -%}
        <span class="tech-tag" property="schema:knowsAbout foaf:topic_interest" resource="{{ '/cv/' | absolute_url }}#tech-{{ tag | slugify }}" typeof="schema:Thing"><span property="schema:name">{{ tag | xml_escape }}</span></span>
        {%- endif -%}
      {%- endfor -%}
    </span>
    {%- endif %}
  </li>
  {%- endfor %}
</ul>
{% endfor %}
</div>
