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
    .nojekyll       serve the files as-is on GitHub Pages

The page works without JavaScript; the language switcher and mobile menu are enhancements.

## Photo credits

Local JPEGs, not hotlinked. Authors, licenses, and source URLs are in [CREDITS.md](CREDITS.md) and the page footer.

- Village photos: Wikimedia Commons, Creative Commons share-alike. Do not strip attribution; share-alike licenses apply.
- Room interiors: Pexels License (attribution not required, given anyway). Generic stock, not this property.
