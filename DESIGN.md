<!-- design-tokens:generated:start -->

### Token and class sources

- `config/styles.css`
- `snippets/theme-styles.liquid`

### Custom properties

- `--color-surface` — settings-backed
- `--color-surface-secondary` — settings-backed
- `--color-on-surface` — settings-backed
- `--color-on-surface-secondary`
- `--color-border`
- `--color-accent` — settings-backed
- `--color-army`
- `--color-rule`
- `--color-interactive` — settings-backed
- `--color-interactive-text` — settings-backed
- `--color-button-primary` — settings-backed
- `--color-button-primary-text` — settings-backed
- `--color-button-secondary`
- `--color-button-secondary-text`
- `--color-button-outline-border` — settings-backed
- `--color-button-outline-text` — settings-backed
- `--color-sale`
- `--color-compare`
- `--color-success`
- `--color-warning`
- `--color-warning-text`
- `--color-critical`
- `--color-info`
- `--color-overlay`
- `--color-overlay-strong`
- `--color-overlay-subtle`
- `--radius-sm`
- `--radius`
- `--radius-lg`
- `--radius-button` — settings-backed
- `--radius-card` — settings-backed
- `--radius-input` — settings-backed
- `--font-body` — settings-backed
- `--font-heading` — settings-backed
- `--ease-ui`
- `--ease-drawer`
- `--default-transition-timing-function`
- `--spacing-page`
- `--spacing-margin`
- `--spacing-touch-target`
- `--spacing-dialog-max-height`
- `--spacing-hero`
- `--spacing-drawer-width`
- `--spacing-notification-width`
- `--shadow`
- `--shadow-lg`
- `--shadow-xl`
- `--aspect-landscape`
- `--safe-area-inset-top`
- `--safe-area-inset-right`
- `--safe-area-inset-bottom`
- `--safe-area-inset-left`
- `--safe-area-inset-inline`
- `--safe-area-inset-inline-start`
- `--safe-area-inset-inline-end`

### Component classes (`@layer components`)

- `placeholder-texture`
- `swatch-sm`
- `swatch-md`
- `swatch-lg`
- `button-primary`
- `button-secondary`
- `button-outline`
- `button-ghost`
- `button-surface`
- `quantity-selector-outlined`
- `quantity-selector-filled`
- `richtext`
- `overlay-panel`
- `remove-icon-top`
- `remove-icon-bottom`
- `stagger-fade-in`
- `nav-has-dropdown`
- `nav-dropdown`
- `nav-disclosure`
- `nav-disclosure-icon`
- `nav-dropdown-inner`
- `nav-dropdown-group`
- `nav-dropdown-item`
- `nav-dropdown-row`
- `nav-dropdown-disclosure`
- `nav-dropdown-submenu`
- `nav-submenu-inner`

<!-- design-tokens:generated:end -->

# DESIGN.md for Shopify “Base Theme”

This document is the design contract for this shop. AI agents read this file before design work and keep it current as the brand evolves. Agents are the audience. Optimize edits for machine reading, not human prose.

Two layers with different owners:

- **Generated tokens (marked section above):** A names-only index of what this theme adds on top of Tailwind — contributing source files, custom properties (settings-backed ones annotated), and component classes. Values are deliberately omitted; read them in the source files or Theme Settings. The index never repeats Tailwind’s built-in vocabulary; when a Tailwind-default name appears (`--radius-lg`, `--shadow-xl`), the theme re-declares it and owns its value — never assume the stock Tailwind value for an indexed name. The index must be kept in sync when tokens or classes are added, removed, or renamed, either manually by the Canvas Agent or programmatically via `pnpm run design:generate`.
- **Body:** Brand direction, rationale, Do/Don’t rules, component recipes, meaning and sensibilities. Agents write and grow this layer with the merchant.

## Current design position

> Treat every point in this section as replaceable. None of it is a brand decision until touched by a merchant/agent conversation.

“Base Theme” ships intentionally brandless: a wireframe for a future brand identity, molded through merchant/agent conversations. The current position is substrate, not brand:

- Achromatic ink-on-white: Near-black “on surface” text on white “surface” backgrounds, light-gray “surface secondary” recesses, hairline borders.
- One colored placeholder accent used as punctuation: Focus rings, info states, small emphasis. Interactive elements are near-black, not colored.
- Flat cards (no radius), softly rounded buttons and inputs.
- Humanist sans pairing: Manrope body, Inter headings, with regular-weight headings so hierarchy comes from scale.
- Snappy, physical motion: Separate easing tokens for controls vs drawers/dialogs (~300ms entrances / ~200ms exits). No purely decorative animations.
- No ornament: No decorative gradients or patterns. Shadows are reserved for overlays and dialogs. Any “overlay gradients” are functional image-legibility treatments, not decoration.

## Brand direction

> Once direction is set, this section is protected. Propose changes to the merchant before rewriting it.

- **Brand overview:** World in Common: a media/product/research project about building systems that help people belong. Sells political-streetwear style shirts (first product: one T-shirt) that fund the work. Audience: young, critical, curious people who distrust both corporate nonprofits and crypto hype.
- **Brand image (thesis):** An independent magazine printed on a café receipt: black ink on warm paper, one red stamp of conviction.
- **Direction:** Typography-led editorial layouts, no stock-photo heroes. Black, warm white, deep red as punctuation, army green used sparingly. Receipt and ledger details (dashed rules, mono metadata, line items with leaders) carry the transparency idea visually. Subtle photocopy grain over the whole page. Never corporate-nonprofit, generic eco-green, gradients, or crypto imagery.
- **Feelings → consequences:**
  - Provocative → huge, tight Libre Franklin 800 headlines in sentence case; statements, not slogans.
  - Warm → warm white paper surface (#F4F0E8), Lora serif body, plain human copy.
  - Honest → receipts and ledgers as UI: dashed rules, `font-mono` labels, visible "TBD / awaiting real costs" placeholders instead of fake numbers.
  - Underground / irreverent → black full-bleed bands, red stamp blocks, photocopy grain.
  - Clear → generous whitespace, single column on mobile, 65ch measure.

### Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Ink | #111111 | `on_surface` / `interactive` | text, black bands, primary buttons |
| Warm paper | #F4F0E8 | `surface` | page background |
| Newsprint | #E7E0D2 | `surface_2` | recessed panels, receipts |
| Deep red | #A3161A | `accent` | stamp bands, emphasis, focus |
| Army green | #4A5233 | `--color-army` (private) | rare secondary punctuation (closing bands, tags) |
| Rule | ink @18% | `--color-rule` (private) | ledger hairlines |

### Typography

- Display: Libre Franklin 800 (`type_heading_font`), line-height ~1.0, tracking tight, sentence case. Fallback: sans-serif.
- Body: Lora 400 (`type_primary_font`), 1.6 line height, max 65ch. Fallback: serif.
- Accent: system `font-mono`, uppercase xs/sm with wide tracking, for receipt/ledger labels only.

### Spacing & components

- Sharp corners everywhere (buttons, cards, inputs). No shadows except overlays.
- Sections: `py-16 md:py-24`, `max-w-page px-margin`.
- Receipt card: `bg-surface-secondary`, dashed `border-on-surface` rules, mono labels, dotted leaders.
- Ledger table: mono header row, hairline rows, horizontal scroll on mobile.
- Buttons: `button-primary` ink; on dark bands use `button-surface`; outline for secondary.

### Dos / Don'ts

- Do show placeholders honestly ("TBD", "Awaiting real costs"). Don't invent prices, stats, testimonials, suppliers.
- Do let type carry the hero. Don't use stock-photo heroes, gradients, bitcoin/crypto motifs, leaf/eco icons.

### Motion

- Minimal: button press scale only. No decorative animation.

## Styling system

> Architecture facts, not brand choices. These hold on every surface that edits this theme.

Tailwind CSS v4 is first-class here — in the theme and in the Canvas editor architecture that compiles it:

- Shared styling is Tailwind utility classes written directly in Liquid markup. `config/styles.css` is the single global authored stylesheet (`@import "tailwindcss" source(none)` plus explicit `@source` scans of `assets/*.js`, `blocks/`, `snippets/`, `templates/`, and `layout/`). CSS that utilities cannot express stays with its owning block in an inline `{% style %}` tag; the tag renders with the block, so those rules ship only on pages that render it, which is why the block must render at most once per page. `{% stylesheet %}` is never used.
- The full default Tailwind vocabulary — utilities, responsive prefixes, state variants, arbitrary properties — is available and is the default styling tool. Reach for standard Tailwind classes first; this file deliberately does not enumerate them.
- Use Tailwind's canonical candidate forms and shorthands. `tailwindcss canonicalize` can explain improvements, but its sorted output is not a formatting target. Preserve existing class order and Liquid interpolation boundaries when applying its recommendations.
- A Tailwind JIT compile runs on change: when theme source (`.liquid`, `assets/*.js`, `config/styles.css`) changes in the Canvas editor, Canvas/Sidekick recompiles the stylesheet, so any statically visible class in scanned sources ships in production CSS without manual registration.
- `@theme` tokens extend that vocabulary with token-derived utilities (`bg-surface`, `text-on-surface`, `rounded-button`, `ease-ui`). Prefer these over arbitrary values whenever a token exists.

## Token API

The design system has two token surfaces with different change mechanisms:

- **Public (settings-backed):** every custom property annotated “settings-backed” in the generated index. Theme Settings (`config/settings_schema.json`) drive these through the runtime bridge (`snippets/theme-styles.liquid`); the bridge renders after the compiled stylesheet, so the bridge value always wins. Change these through Theme Settings so the merchant sees and owns the choice; a competing value written in CSS is overridden at runtime.
- **Private (build-time):** every unannotated custom property in the index (spacing, shadows, easing, overlays, semantic colors, fixed radii). Change their initial values in `config/styles.css`.

Compiler and editing-surface constraints:

- `config/styles.css` is the global authored source of truth. Canvas/Sidekick compiles it after theme-source changes and persists generated `assets/styles.min.css`, which the storefront loads. Edit the source; never edit the generated asset. Block-owned selectors stay co-located in their block's single `{% style %}` tag so unrelated pages never load them.
- Change public tokens through Theme Settings and private tokens in `config/styles.css`. New `@theme` tokens and statically discoverable utility classes become available when Canvas/Sidekick recompiles the source.
- Classic Edit Code does not itself invoke the compiler. A source edit made only through that surface can leave the generated asset stale; use a compiler-backed workflow rather than editing `assets/styles.min.css`.

Promoting a private token to a setting (making it public):

1. Add the setting to `config/settings_schema.json` (respect the theme-settings cap in `AGENTS.md`).
2. Emit the property from the `:root` block in `snippets/theme-styles.liquid`, converting the setting value as needed.
3. Keep the schema default and the CSS initial value identical; in the theme repository, `spec:audit` fails when they diverge.
4. Update the generated token index — the property gains the settings-backed annotation.

## Hard constraints

> These hold regardless of brand direction. `AGENTS.md` carries the full rules.

1. **Use the theme’s real token names only.** The generated tokens section is the entire theme-token vocabulary; standard Tailwind utilities are fair game where no token applies. Never invent parallel token names, and never write raw palette values where a token exists.
2. **Change brand-wide values through the token API** (see above) — Theme Settings for public tokens, CSS token values for private ones, honoring the live-shop constraints — never by scattering arbitrary values through markup.
3. **Utility candidates must be statically visible.** Tailwind compiles with `source(none)`; use complete class names in scanned markup, schema values, literal mappings, or embedded LiquidDoc examples. Standalone Markdown is outside the scan. Select whole classes rather than assembling fragments; documented external presets use explicit layered base CSS instead of duplicate safelists.
4. **Canonicalize candidates, not class-list formatting.** Prefer canonical utilities over redundant, deprecated, or unnecessarily arbitrary equivalents. Keep the source order stable and apply only semantic canonicalizer recommendations, especially around Liquid output and control-flow tags.
5. **Contrast is non-negotiable:** 4.5:1 for body text, 3:1 for large text, and 3:1 for visual cues required to identify controls or states; adjust lightness until it passes while keeping the hue. The initial “Base Theme” may contain exceptions; whether debt or intentional, do not repeat or worsen them.
6. **Motion uses the easing tokens** and is gated behind `motion-safe:`; never bare `ease`.
7. **Commerce contracts stay intact:** Shopify money filters for prices, translation keys for user-facing strings, quantity rules, and checkout submitter names.

## Do / Don’t

> Grows by addition as merchant preferences appear. One line per rule with the token or value inline. Ask the merchant before removing or changing a rule.

### Do

- Use “background surface” + “text on surface” tokens for content regions and a “background surface secondary” token for recessed regions.
- Use a “color accent” token as punctuation (focus, small emphasis), never as a large surface.
- Use stock Tailwind utilities in templates and blocks. Typography sizes belong to the Heading/Text size selectors; font families still follow merchant settings. Avoid custom classes and tokens when Tailwind supplies the treatment.
- Typography blocks default to `text-pretty`. Use regular heading weight and Tailwind default line heights; reserve overrides for an intentional call-site treatment.
- Verify collection-card text against the actual image when choosing an “overlay”, and recheck every non-white overlay after changing the interactive palette. A “dark overlay” default is not a contrast guarantee.

### Don’t

- Don’t use arbitrary values (`bg-[#...]`, `rounded-[Npx]`) where a token utility exists.
- Don’t add hover zoom transforms to product, resource, or collection card imagery; the product page gallery’s subtle `motion-safe` hover zoom is the sanctioned exception.
- Don’t introduce fonts outside the two theme font settings.

## Component recipes

> How tokens combine for this shop’s components. Update a recipe when a component is restyled; add one when a new pattern is installed.

### Standalone text link

Use the public `link` block for ordinary standalone navigation. Keep links underlined with on-surface text, a secondary on-surface hover color, the accent focus outline, a 44px minimum block-axis target, and `active:scale-[0.97]` press feedback. Do not substitute it for command/form buttons, card overlays, menu links, or platform-owned links.

### Gift-card artwork

The standalone gift-card page is the sanctioned exception to the brandless substrate's no-ornament rule. Its single code-owned Plain material may use a token-derived gradient face, edge and glint highlights, a restrained card shadow, and a static dimensional tilt pose, with pointer-following motion and a hover lift only for fine pointers when motion is allowed. Keep identity, value, message, and metadata fully readable without motion. Do not reuse this decorative treatment on product or resource cards.

### Password invitation

Use one split-screen launch composition: editorial media and caption beside a restrained brand/message panel, with password entry as the primary action and opening updates as the quieter secondary action. Resolve media from the existing image block so a merchant-selected image wins over Brand cover art and the first-product fallback; when no image resolves, remove the media panel rather than leaving a vacant split. Keep both real Shopify forms in separate native dialogs, preserve a no-JavaScript password path, and never introduce alternate password designs or controls that select between them.

## Maintaining this file

- **Update** the generated token index when custom properties or `@layer components` classes are added, removed, or renamed; value-only changes never touch it. In the theme repository, `pnpm run design:generate` syncs the marked section; without that tooling, mirror the name changes manually.
- **Grow** the authored layer when global styles change or merchant preferences emerge. Record new dislikes as Don’t rules immediately.
- **Guard:** An out-of-date `DESIGN.md` is worse than none. If the generated tokens section and the theme source disagree, the source is right — update before designing.
