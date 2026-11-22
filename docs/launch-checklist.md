# Launch checklist

Do these steps in order when the Dawn theme goes live. Until then, the live theme is Horizon and must stay untouched.

## 1. Publish the theme

1. Push the final code to the "World in Common - Dawn Draft" theme (`212113097049`):
   ```sh
   SHOPIFY_STORE=nyx6qf-9z.myshopify.com SHOPIFY_THEME_ID=212113097049 sh scripts/publish-unpublished.sh
   ```
2. In Shopify Admin, go to **Online Store > Themes** and publish "World in Common - Dawn Draft".

## 2. Page templates

The page templates were assigned before launch with the Admin API (`pageUpdate` with `templateSuffix`), because Shopify Admin lists only the templates of the **live** theme. After you publish, check each page once:

| Page handle | Theme template |
| --- | --- |
| `about` | `about` |
| `learn-more` | `learn-more` |
| `manifesto` | `manifesto` |
| `open-source` | `open-source` |
| `transparency-ledger` | `transparency-ledger` |

If a page shows the plain default layout, set its **Theme template** in **Online Store > Pages**. After publish, the list shows these templates.

## 3. Final checks

- Check that the main menu and footer menu in **Online Store > Navigation** link to every page.
- Connect the `aworldincommon.com` domain.
- Remove the storefront password only when you are ready to go public.
