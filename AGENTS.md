# AGENTS.md

Guidance for coding agents (and humans) working on this repo: the personal
site of Giacomo Benincasa, built with Jekyll and published by GitHub Pages
from `main`, root folder. There is **no theme**: the layouts and stylesheet in
this repo are the whole design. See `README.md` for editing basics.

## Ground rules

- Don't change wording (About text, CV bullets, publications, navigation)
  beyond what was asked. Content edits are the owner's call.
- Ask before deleting files or force-pushing.
- Look things up instead of guessing: Wikidata IDs, URLs, author lists.
  Check that every URL you add loads.
- A change is done only when the GitHub Pages build for your commit has
  succeeded and the live page shows it (see "Verify" below).

## Where content lives

| What | File |
|---|---|
| Site settings, profile links (hero, footer, `sameAs`), your name in publications (`author.publication_name`) | `_config.yml` |
| Top navigation | `_data/navigation.yml` |
| CV roles and bullets, each bullet's `tags`; per job `employers`, `place`, `start`, `end` (YYYY-MM) | `_data/cv.yml` |
| Employers and schools (name, Wikidata ID, official site, optional schema.org `type`, optional `parent` Wikidata ID) | `_data/organizations.yml` |
| Education (title, `degree: true`, `schools`, `note`, `exchange`), shown as the CV's Education row | `education` in `_data/cv.yml` |
| Work locations (name, Wikidata ID, GeoNames ID), referenced by `place` in `cv.yml` | `_data/places.yml` |
| Technologies and concepts (tags and inline mentions) | `_data/technologies.yml` (field reference at the top) |
| Co-author home pages, keyed by name as written in `authors` | `_data/coauthors.yml` |
| Conference/workshop series (venues), rendered by `_includes/venue.html` | `_data/venues.yml` |
| Publications, one file each: `title`, `date`, `authors` (list), `et_al`, `venue`, `pubtype` (`patent`/`paper`), `paperurl` | `_publications/` |
| Page templates | `_pages/` (`cv.md`, `publications.md` render the data above) |
| Shared RDFa markup for a technology/concept | `_includes/concept.html` |
| Layouts: `default` (top bar, footer, `{% seo %}`), `home` (hero + About row), `page` (big title, optional `lead`, rows) | `_layouts/` |
| All styles | `assets/css/main.scss` |

## Design (Minimal Swiss)

- One typeface (Inter Tight, from Google Fonts), black on white, one accent
  (`$accent`, orange). Variables are at the top of `assets/css/main.scss`.
- Pages are a stack of `<section class="row">` blocks: a small uppercase
  `h2` label in the left column, content in the right (2fr). Below 820px the
  grid collapses to one column. Check both widths after layout changes.
- Page titles end in an orange full stop (`<span class="dot">.</span>`).
- Front matter on pages: `layout` (`page` by default, `home` for About),
  `lead` (Markdown intro under the title), `rows: true` when the page emits
  its own rows (CV, Publications), `label` for a plain page's row label.
- CV bullets are numbered (`ol.items`); tags render as `#Name` via CSS.
- Every page sets `description` in front matter (≤ ~155 characters); `{% seo %}`
  turns it into the meta description and `og:description`. Don't hand-write
  meta/Open Graph tags.
- Keep it dependency-free: no JavaScript, no icon fonts, no theme gem.

## Semantic markup (RDFa)

The CV, Publications and About pages carry RDFa using schema.org (read by
search engines) and FOAF, side by side on the same elements. Keep them in sync.

- **Stable identifiers.** The same thing must have the same IRI everywhere:
  - The site owner: `{{ '/publications/' | absolute_url }}#g-benincasa`
    (derived from `author.publication_name`), on every page.
  - Co-authors: `…/publications/#<name | slugify>`. Names must be spelled
    identically across `_publications/` or they become different people.
  - Technologies/concepts: `http://www.wikidata.org/entity/<QID>` if a
    Wikidata item exists; otherwise `…/cv/#tech-<name | slugify>` plus the
    official docs page as `schema:url`/`schema:sameAs`.
- **Identity sources, in order:** Wikidata item → official product/docs page
  → a term defined on the site (`type: DefinedTerm` plus `description`, shown
  on hover via `.defined`). Never link a page you couldn't load.
  AWS services also get `provider: Q456157` (Amazon Web Services).
- **One renderer.** Produce technology/concept markup only through
  `_includes/concept.html` (`tag=true` for CV tags, `standalone=true` outside
  a block that already has the person as subject, e.g. the About page).
  Concepts with `mention: true` are marked up automatically wherever their
  exact name appears in a CV bullet.
- **Employment** uses the schema.org Role pattern on each `.job-head`: person
  `worksFor` an `EmployeeRole` (`roleName`, `startDate`, `endDate`) that
  `worksFor` the Organization. Keep it on the header only: wrapping the
  bullets would move their `knowsAbout` tags from the person to the role.
- **Education**: the person is `schema:alumniOf` each school; a degree is also
  `schema:hasCredential` an `EducationalOccupationalCredential`
  (`credentialCategory` "degree") `recognizedBy` its school(s) — only the
  degree-granting schools, never an exchange host.
- **Exchanges** that counted towards a degree go in that degree's `exchange`
  (not a separate entry): shown as an "Includes an exchange at …" line and
  marked `alumniOf` the host. Departments use `type: EducationalOrganization`
  with `parent` (rendered as `schema:parentOrganization`) set to the university.
- **Work locations** are `schema:City` (Wikidata IRI, GeoNames `sameAs`) on the
  role via `schema:workLocation`. Never use the organization's `location`:
  that would say where the company is, not where the job was.
- **Venues** are not skills: they render as `schema:EventSeries` that the page
  `schema:mentions` (via `_includes/venue.html`), never as `knowsAbout`.
- IRIs use `site.url` (`https://gbenin.casa`) on purpose, so they stay stable
  when the custom domain is restored. Don't switch them to github.io.

## Build constraints

- GitHub Pages builds with the `github-pages` gem: **Jekyll 3.10, Liquid 4**.
  - Liquid 5 filters (e.g. `remove_last`) don't exist and fail **silently**.
  - `{% include %}` parameters must be plain variables or literals, not
    `entry[0]`; assign to a variable first. This fails the build.
  - In `_pages/*.md`, write raw HTML (not Markdown) inside RDFa blocks;
    kramdown leaves block HTML alone.
- Root `.md` files are rendered as pages by `jekyll-optional-front-matter`,
  so non-site docs (README, AGENTS.md, CLAUDE.md) must be listed in
  `exclude` in `_config.yml`.
- Local builds need **Ruby 3.3** (`brew install ruby@3.3`, then put
  `/opt/homebrew/opt/ruby@3.3/bin` first on PATH). Ruby 4.x can't resolve
  `github-pages` 232, and macOS system Ruby 2.6 is too old. Install gems
  into `vendor/bundle` (git-ignored); don't commit `Gemfile.lock`.

## Verify

After pushing to `main`:

1. Wait for the `pages-build-deployment` run for your commit:
   `gh run list -R giacobenin/giacobenin.github.io -L 1`. On failure, read
   `gh run view <id> --log-failed`; Liquid errors show up there.
2. Fetch the live page (https://gbenin.casa/...) and check the change.
3. For markup changes, extract the RDF (e.g. with `pyRdfa3` + `rdflib` in a
   throwaway virtualenv) and confirm identities, counts and links. Don't
   rely on reading the HTML.

## Git and hosting

- Push to `main` over HTTPS; there is no SSH key on the owner's machine. If
  plain `git push` isn't authenticated, use
  `git -c credential.helper='!gh auth git-credential' push origin main`.
- Commit messages: imperative subject, short body saying why.

## Hosting

- Live at https://gbenin.casa (custom domain via `CNAME`; DNS at GoDaddy: four
  A records for `@` to 185.199.108–111.153, `www` CNAME to
  `giacobenin.github.io`). HTTPS is enforced; giacobenin.github.io redirects.
- Don't delete `CNAME`: that switches the custom domain off.
