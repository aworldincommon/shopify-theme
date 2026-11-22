# World in Common Theme Instructions

This is a standard Shopify Dawn-based theme. Use Shopify Liquid, JSON templates, sections, snippets, CSS, and JavaScript according to Dawn's existing conventions.

## Rules

- Read `DESIGN.md` before visual work.
- Read `WRITING.md` before writing or editing any public copy. Affirm, then invite; never shame the reader.
- Extend existing Dawn sections where practical; create a custom section when the composition genuinely needs one.
- Keep merchant-editable copy in section settings or blocks and use translation keys for fixed UI strings.
- Preserve accessible headings, landmarks, focus states, responsive behavior, and Shopify routes.
- Do not add invented product data, prices, claims, testimonials, or private information.
- Keep the live theme untouched. Work on the unpublished theme or a development theme only.
- Run `shopify theme check --path .` and `python3 scripts/check_public_content.py` before committing.
- Run `git diff --check` before committing.
- Do not edit generated or minified assets unless Dawn's workflow requires it.
