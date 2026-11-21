#!/bin/sh
set -eu

case " $* " in
  *' --publish '*|*' --live '*|*' --allow-live '*)
    printf '%s\n' 'Refusing live-theme flags. Use this wrapper only for an unpublished theme.' >&2
    exit 2
    ;;
esac

REPO_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$REPO_ROOT"
python3 scripts/check_public_content.py

: "${SHOPIFY_STORE:?Set SHOPIFY_STORE to the .myshopify.com domain}"
THEME_ID="${SHOPIFY_THEME_ID:-212078035289}"
exec shopify theme push \
  --store "$SHOPIFY_STORE" \
  --theme "$THEME_ID" \
  --path . \
  --no-input \
  "$@"
