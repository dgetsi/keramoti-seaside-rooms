# Keramoti Seaside Rooms / Δωμάτια Κεραμωτής

Placeholder bilingual (Greek + English) landing page for a sample guesthouse in Keramoti (Κεραμωτή), Kavala, Greece. This is not a live booking site and does not describe a verified business.

Rooms, amenities, contact details, and prices on the page are placeholders. The room interiors are **sample stock photos, clearly labelled as such** — each one carries a bilingual "Δείγμα / Sample" badge and a "stock placeholder, not this guesthouse" caption. They do not show this property. The village and harbour photographs are real pictures of Keramoti from Wikimedia Commons.

## View it

Live on GitHub Pages: <https://dgetsi.github.io/keramoti-seaside-rooms/>

This repo is public. You can also clone or download the ZIP and open `index.html` directly in a browser — there is no build step. Keep `index.html`, `styles.css`, `script.js`, and the `images/` folder together.

## Structure

    index.html      markup, all bilingual copy
    styles.css      single stylesheet, CSS custom properties for the palette
    script.js       language switcher, mobile nav, scroll spy — progressive enhancement only
    images/         Keramoti village photos (Wikimedia Commons)
    images/rooms/   generic stock room interiors (Pexels), labelled as samples
    OWNER_DOD.md    owner checklist before real photos, prices, and contact
    CREDITS.md      photo attribution (Wikimedia + Pexels)
    .nojekyll       serve the files as-is on GitHub Pages

The page works without JavaScript; the language switcher and mobile menu are enhancements.

## Photo credits

Local JPEGs, not hotlinked. Authors, licenses, and source URLs are in [CREDITS.md](CREDITS.md) and the page footer.

- Village photos: Wikimedia Commons, Creative Commons share-alike. Do not strip attribution; share-alike licenses apply.
- Room interiors: Pexels License (attribution not required, given anyway). Generic stock, not this property.

## Owner readiness (KER-001)

Stack stays **static HTML/CSS/JS** on GitHub Pages (progressive enhancement only; no form backend).

Before publishing real property claims:

- Follow **[OWNER_DOD.md](OWNER_DOD.md)** — concrete gates for real photos, prices, and when to remove sample badges.
- Contact / enquire uses **labelled placeholders** (display-only dummy `hello@example.com`, phone/hours slots). No live mailto, no real inbox claim, no “message sent”, no PII form (ADR-KER-001: static only).
- Keep sample badges and Wikimedia attribution in [CREDITS.md](CREDITS.md) until the DoD photo/price gates pass.

