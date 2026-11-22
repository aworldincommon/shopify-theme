# Launch checklist

Do these steps in order when the Dawn theme goes live. Until then, the live theme is Horizon and must stay untouched.

## 1. Publish the theme

1. Push the final code to the "World in Common - Dawn Draft" theme (`212113097049`):
   ```sh
   SHOPIFY_STORE=nyx6qf-9z.myshopify.com SHOPIFY_THEME_ID=212113097049 sh scripts/publish-unpublished.sh
   ```
2. In Shopify Admin, go to **Online Store > Themes** and publish "World in Common - Dawn Draft".

## 2. Assign the page templates

Shopify Admin lists only the templates of the **live** theme. So the custom page templates can be assigned only after step 1.

Go to **Online Store > Pages**. For each page, set **Theme template**:

| Page handle | Theme template |
| --- | --- |
| `about` | `about` |
| `learn-more` | `learn-more` |
| `manifesto` | `manifesto` |
| `open-source` | `open-source` |
| `transparency-ledger` | `transparency-ledger` |

Before launch, preview a template on its page with `?view=<template>`, for example `/pages/about?view=about`.

## 3. After the templates are assigned

- Add the pages to **Online Store > Navigation** (main menu and footer menu).
- Connect the `aworldincommon.com` domain.
- Remove the storefront password only when you are ready to go public.
