# World in Common Shopify Theme

## Privacy gate

Run `sh scripts/install-hooks.sh` once after cloning. The versioned pre-push hook scans tracked theme files for likely personal information and credentials without printing matched values. GitHub Actions repeats the scan on pushes and pull requests.

Before uploading to Shopify, use:

```sh
SHOPIFY_STORE=your-store.myshopify.com sh scripts/publish-unpublished.sh
```

The publish wrapper scans first and targets an unpublished theme. It refuses live-theme flags.