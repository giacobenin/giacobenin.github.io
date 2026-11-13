---
permalink: /cv/
title: "CV"
lead: "My full work history is on [LinkedIn](https://www.linkedin.com/in/gbenincasa/)."
rows: true
print_bare: true   # print without the site header and footer
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
<div prefix="schema: https://schema.org/ foaf: http://xmlns.com/foaf/0.1/" resource="{{ site.author.id | absolute_url }}" typeof="schema:Person foaf:Person">
<meta property="schema:name foaf:name" content="{{ site.author.name }}">
<link property="schema:url foaf:homepage" href="{{ '/' | absolute_url }}">

<section class="row">
<h2 id="professional-experience">Professional Experience</h2>
<div>
{%- for job in site.data.cv.experience %}
<article class="job">
  {%- comment -%}
  Employment as a schema.org Role: person -worksFor-> EmployeeRole (roleName,
  startDate, endDate) -worksFor-> Organization. Only on the header, so the
  bullets' knowsAbout tags stay attached to the person.
  {%- endcomment %}
  <header class="job-head" property="schema:worksFor" typeof="schema:EmployeeRole">
    <meta property="schema:roleName" content="{{ job.title | xml_escape }}">
    {%- if job.start %}<meta property="schema:startDate" content="{{ job.start }}">{% endif -%}
    {%- if job.end %}<meta property="schema:endDate" content="{{ job.end }}">{% endif -%}
    {%- for key in job.employers -%}
      {%- assign org = site.data.organizations[key] -%}
      <span property="schema:worksFor" resource="http://www.wikidata.org/entity/{{ org.wikidata }}" typeof="schema:{{ org.type | default: 'Organization' }}"><meta property="schema:name" content="{{ org.name | xml_escape }}"><link property="schema:url schema:sameAs" href="{{ org.url }}"></span>
    {%- endfor -%}
    {%- comment -%} Where the job was. schema.org has no per-role location, so this uses workLocation on the role, as is common practice. {%- endcomment -%}
    {%- assign place = site.data.places[job.place] -%}
    {%- if place %}
      <span property="schema:workLocation" resource="http://www.wikidata.org/entity/{{ place.wikidata }}" typeof="schema:City"><meta property="schema:name" content="{{ place.name | xml_escape }}"><link property="schema:sameAs" href="https://sws.geonames.org/{{ place.geonames }}/"></span>
    {%- endif %}
    <h3>{{ job.title | xml_escape }}, {{ job.org | xml_escape }}</h3>
    {%- assign d = job.dates | split: " – " %}
    <p class="when"><time datetime="{{ job.start }}">{{ d[0] }}</time> – {% if job.end %}<time datetime="{{ job.end }}">{{ d[1] }}</time>{% else %}{{ d[1] }}{% endif %}</p>
    <p class="where">{% if job.note %}{{ job.note | xml_escape }} · {% endif %}{{ job.location | xml_escape }}</p>
  </header>
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
    <li><p>{{ text }}</p>
      {%- if item.tags %}
      <ul class="tech-tags" aria-label="Technologies">
        {%- for tag in item.tags -%}
          {%- include concept.html name=tag tag=true -%}
        {%- endfor -%}
      </ul>
      {%- endif %}
    </li>
  {%- endfor %}
  </ol>
</article>
{%- endfor %}
</div>
</section>

{%- comment -%}
Education: person schema:alumniOf each school; a degree is also
schema:hasCredential an EducationalOccupationalCredential recognizedBy the
school(s). Schools come from _data/organizations.yml.
{%- endcomment %}
<section class="row">
<h2 id="education">Education</h2>
<div>
{%- for ed in site.data.cv.education %}
<article class="job">
  <header class="job-head">
    {%- for key in ed.schools -%}
      {%- assign school = site.data.organizations[key] -%}
      <span property="schema:alumniOf" resource="http://www.wikidata.org/entity/{{ school.wikidata }}" typeof="schema:{{ school.type | default: 'Organization' }}"><meta property="schema:name" content="{{ school.name | xml_escape }}"><link property="schema:url schema:sameAs" href="{{ school.url }}"></span>
    {%- endfor %}
    {%- if ed.exchange %}{% assign xs = site.data.organizations[ed.exchange] %}
      <span property="schema:alumniOf" resource="http://www.wikidata.org/entity/{{ xs.wikidata }}" typeof="schema:{{ xs.type | default: 'Organization' }}"><meta property="schema:name" content="{{ xs.name | xml_escape }}"><link property="schema:url schema:sameAs" href="{{ xs.url }}">{% if xs.parent %}{%- for o in site.data.organizations -%}{%- if o[1].wikidata == xs.parent %}{% assign par = o[1] %}{% endif -%}{%- endfor -%}<span property="schema:parentOrganization" resource="http://www.wikidata.org/entity/{{ xs.parent }}" typeof="schema:{{ par.type | default: 'Organization' }}"><meta property="schema:name" content="{{ par.name | xml_escape }}"></span>{% endif %}</span>
    {%- endif %}
    {%- if ed.degree %}
    <h3 property="schema:hasCredential" typeof="schema:EducationalOccupationalCredential"><meta property="schema:name" content="{{ ed.title | xml_escape }}"><meta property="schema:credentialCategory" content="degree">
      {%- for key in ed.schools %}<link property="schema:recognizedBy" href="http://www.wikidata.org/entity/{{ site.data.organizations[key].wikidata }}">{% endfor -%}
      {{ ed.title | xml_escape }}</h3>
    {%- else %}
    <h3>{{ ed.title | xml_escape }}</h3>
    {%- endif %}
    <p class="where">
      {%- for key in ed.schools -%}{{ site.data.organizations[key].name | xml_escape }}{% unless forloop.last %} · {% endunless %}{%- endfor -%}
      {%- if ed.note %} ({{ ed.note | xml_escape }}){% endif -%}
    </p>
    {%- if ed.exchange %}
    <p class="where">Includes an exchange at the {{ site.data.organizations[ed.exchange].name | xml_escape }}</p>
    {%- endif %}
  </header>
</article>
{%- endfor %}
</div>
</section>
</div>
