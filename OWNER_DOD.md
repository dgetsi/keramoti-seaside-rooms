# Owner definition of done (DoD) — KER-001

**EL · Ορισμός ολοκλήρωσης για τον ιδιοκτήτη** · **EN · Owner readiness checklist**

This page is still a **sample / fictional** guesthouse site. Use this checklist before claiming a real property, publishing real rates, or removing sample labels. Keep [CREDITS.md](CREDITS.md) attribution for Wikimedia place photos.

---

## EL · Τι να αντικαταστήσετε · EN · What to replace

| Item | EL | EN |
|------|----|----|
| Room interiors | Αντικαταστήστε τα `images/rooms/sample-*.jpg` με πραγματικές φωτογραφίες του καταλύματος. | Replace `images/rooms/sample-*.jpg` with real photos of **this** property. |
| Fictional name | Αν έχετε πραγματική επωνυμία, αντικαταστήστε «Δωμάτια Κεραμωτής / Keramoti Seaside Rooms» σε τίτλο, brand, hero, footer. | If a real trading name arrives, replace the fictional “Δωμάτια Κεραμωτής / Keramoti Seaside Rooms” in title, brand, hero, and footer. |
| Sample amenities | Επαληθεύστε ή αφαιρέστε κάθε παροχή με ετικέτα «δείγμα / sample». | Verify or remove every amenity marked “δείγμα / sample”. |
| Sample room copy | Αντικαταστήστε ενδεικτικούς τύπους δωματίων και περιγραφές με επαληθευμένο κείμενο. | Replace sample room types and blurbs with verified copy. |
| Placeholder email | Στο `#contact`, αντικαταστήστε `hello@example.com` με πραγματικό inbox του ιδιοκτήτη. | In `#contact`, replace `hello@example.com` with the owner’s real inbox. |
| Phone / hours slots | Συμπληρώστε τα πεδία-σύμβολα τηλεφώνου και ωρών απάντησης **μόνο** αν είναι επαληθευμένα. | Fill the phone and reply-hours placeholder slots **only** when verified. Do not invent numbers. |

---

## EL · Ετικέτες να αφαιρεθούν μόνο μετά από επαλήθευση · EN · Labels to remove only after verified content

Remove these **only** when the matching real content is live and checked:

- Notice bar: `SAMPLE SITE` / «Δείγμα ιστοσελίδας»
- Room badges: «Δείγμα / Sample»
- Tags: `SAMPLE · ΔΕΙΓΜΑ`, `SAMPLE COPY`, `SAMPLE CONTACT`
- Stock captions: “stock placeholder, not this guesthouse” / ισοδύναμα EL
- Hero flag and section notes that say the property is fictional / placeholder
- Contact copy that says the address is dummy / nothing is received
- Price lines that say “Rate: not available — sample page”

Until then, **keep** every sample badge and caption.

---

## EL · Τι πρέπει να μείνει μέχρι επαλήθευση · EN · What must stay until verified

| Gate | Stay until… |
|------|-------------|
| Sample banners / notice bar | Real property identity and contact are verified |
| No prices on room cards | Owner supplies verified rates (see price gates below) |
| `noindex, nofollow` meta | Site is no longer a sample demo (owner decision) |
| Wikimedia CREDITS / footer attribution | Always for Commons place photos (share-alike) — do not strip |
| Place vs property distinction | Always: Keramoti place facts ≠ property claims |
| OSM iframe attribution | Always keep map credit to OpenStreetMap contributors |

---

## Photo gates (concrete)

**Pass only when all are true:**

1. Every room card image is a photo of **this** property (not Pexels/stock).
2. File names/paths updated; broken `src` checked.
3. `alt` text updated: remove “Sample stock photo / Φωτογραφία-δείγμα”; describe the real room in EL and EN.
4. Room badges and stock captions removed **after** alts and images are real.
5. Village/harbour Wikimedia images may stay; CREDITS.md and footer links stay for those files.
6. Do **not** claim stock or Commons images are owned by the guesthouse.

---

## Price gates (concrete)

**Pass only when all are true:**

1. Owner has supplied currency, season/rules, and at least one verified rate (or an explicit “rates on request” policy that is real).
2. No invented phone numbers or invented euro amounts appear on the page.
3. Sample “Rate: not available — sample page” lines are replaced with the verified text (or removed if rates live elsewhere).
4. Until then: keep “no prices” / sample price lines; do not add fake tariffs.

---

## Enquire path (owner fill)

On the sample page `#contact` (ADR-KER-001):

- Slots labelled for **email**, **phone**, **preferred reply hours** are placeholders until filled.
- Dummy `hello@example.com` stays as **display-only** labelled sample — **no live mailto / no real inbox** while the site is sample.
- When a verified real email is set (DoD pass): you may then offer a labelled `mailto:` to that address only.
- **Do not** add a PII-collecting form (no POST storing name/email/phone) unless a separate privacy-compliant flow is implemented later.
- **Do not** show fake “message sent” UX.
- **Do not** imply enquire reaches a live inbox while sample badges remain.

---

## On-page teaser

A short bilingual DoD pointer appears in the contact section and footer (`OWNER_DOD.md`). Keep that link while the site remains sample-ready.

---

## Quick pre-publish self-check

- [ ] Real photos + alts (photo gates)
- [ ] Real or omitted prices (price gates)
- [ ] Real email (and phone/hours only if verified)
- [ ] Sample badges/tags/notice removed only after the above
- [ ] CREDITS.md intact for Wikimedia
- [ ] EL/EN parity on contact and critical claims
- [ ] `noindex` reviewed intentionally
