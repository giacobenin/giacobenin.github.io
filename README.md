# gbenin.casa

Personal site of Giacomo Benincasa, built with Jekyll and the
[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme,
hosted on GitHub Pages.

## Publish

1. Create an empty public repo on GitHub named `giacobenin.github.io`
   (no README, license or .gitignore).
2. From this folder:

   ```sh
   git remote add origin git@github.com:giacobenin/giacobenin.github.io.git
   git push -u origin main
   ```

3. In the repo, open Settings → Pages and set Source to "Deploy from a branch",
   branch `main`, folder `/ (root)`.
4. Custom domain: at the registrar for gbenin.casa, add A records for `@` pointing to
   185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and a
   CNAME record for `www` pointing to `giacobenin.github.io`. Then enter `gbenin.casa`
   in Settings → Pages and tick "Enforce HTTPS" once the DNS check passes.

## Run locally

```sh
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Edit

- Profile, sidebar links, theme skin: `_config.yml`
- Top navigation: `_data/navigation.yml`
- Pages: `_pages/`
- Publications: one file per paper in `_publications/`
  (front matter: `title`, `date`, `authors` as a list, optional `et_al: true`,
  `venue`, `pubtype` — `patent` or `paper` — and optional `paperurl`)
- Co-author links: `_data/coauthors.yml` maps each author name, as written in
  `authors`, to their home page. The Publications page marks authors up with
  schema.org and FOAF (RDFa).
- Photo: add `assets/images/profile.jpg` and uncomment `avatar` in `_config.yml`
