#!/usr/bin/env python3
"""Static page generator for Katerina apartments.

Run from the repo root:  python3 _build/build.py
Writes index.html and apartments/<slug>/index.html. No dependencies.

To add a room page: fill in its entry in APTS (text + amenities + spaces),
set "page": True, and add its 1200x630 collage to og/<slug>.jpg.
"""
import json, os
from html import escape

BASE = "https://dgetsi.github.io/keramoti-seaside-rooms/"
SITE = "Katerina apartments"
PHONE = "+30 697 763 5937"
TEL = "+306977635937"
WA = "https://wa.me/306977635937"
OWNER_EL, OWNER_EN = "Κατερίνα Μαλτεζάκη", "Katerina Maltezaki"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def t(el, en):
    """Bilingual inline text: both languages ship in the HTML, CSS shows one."""
    return f'<span class="i-el" lang="el">{el}</span><span class="i-en" lang="en">{en}</span>'

# ── photos: (file stem, alt EL, alt EN) — order = display order ───────────
P = {
 "green": [
  ("Κουζίνα με λευκά ντουλάπια και ανοξείδωτο ψυγείο, πράσινοι τοίχοι","Kitchen with white cabinets and a steel fridge, green walls"),
  ("Σαλόνι-τραπεζαρία με καναπέ, τηλεόραση και κλιματιστικό","Living and dining area with sofa, TV and air conditioning"),
  ("Τραπεζαρία δίπλα στην κουζίνα, με λουλούδια στο τραπέζι","Dining table beside the kitchen, with flowers"),
  ("Κουζίνα με φούρνο, απορροφητήρα και βιτρίνα","Kitchen with oven, hood and glass-front cupboard"),
  ("Καμάρα προς τον διάδρομο και το μπάνιο","Archway to the hallway and bathroom"),
  ("Η κουζίνα από την πόρτα, με την καμάρα πίσω","The kitchen seen from the doorway, with the arch behind"),
  ("Διπλό υπνοδωμάτιο με κομοδίνα και πορτατίφ","Double bedroom with bedside tables and lamps"),
  ("Υπνοδωμάτιο με τουαλέτα, καθρέφτη και ντουλάπα","Bedroom with dressing table, mirror and wardrobe"),
  ("Βιτρίνα στον διάδρομο","Glass-front cabinet in the hallway")],
 "studio": [
  ("Μπαλκονόπορτα προς το μπαλκόνι με θέα στα πεύκα","Glass door onto the balcony and the pines"),
  ("Στούντιο με μονό κρεβάτι, τραπεζαρία και μπαλκονόπορτα","Studio with single bed, dining table and balcony door"),
  ("Μονά σιδερένια κρεβάτια και τηλεόραση στο στούντιο","Iron-frame single beds and TV in the studio"),
  ("Μονό κρεβάτι δίπλα στην μπαλκονόπορτα","Single bed by the balcony door"),
  ("Θέα από το μπαλκόνι προς το πευκοδάσος","View from the balcony towards the pine forest"),
  ("Διπλό κρεβάτι με τιρκουάζ μαξιλάρια","Double bed with turquoise cushions"),
  ("Διπλό κρεβάτι με πορτατίφ και κομοδίνο","Double bed with lamp and bedside table"),
  ("Κουζινούλα με εστίες και νεροχύτη","Kitchenette with hob and sink"),
  ("Ντουλάπα και κλιματιστικό στο υπνοδωμάτιο","Wardrobe and air conditioning in the bedroom"),
  ("Μπάνιο με ντους","Bathroom with shower")],
 "turquoise-loft": [
  ("Κουζίνα με τιρκουάζ ρετρό ψυγείο, πλυντήριο και την ανοιχτή σκάλα από πάνω","Kitchen with turquoise retro fridge, washing machine and the open-tread staircase above"),
  ("Σαλόνι με μπλε καναπέ, τηλεόραση, κλιματιστικό και πόρτα προς το μπαλκόνι","Living room with blue sofa, TV, air conditioning and door to the balcony"),
  ("Μεγάλο μπαλκόνι με τραπέζι, πάνω από το πευκοδάσος","Large balcony with a table, over the pine forest"),
  ("Ανοιχτή σκάλα με ξύλινα σκαλοπάτια προς τη σοφίτα","Open-tread staircase with wooden steps up to the loft"),
  ("Υπνοδωμάτιο σοφίτας με διπλό κρεβάτι και κλιματιστικό","Loft bedroom with double bed and air conditioning"),
  ("Διπλό υπνοδωμάτιο με λευκά σεντόνια","Double bedroom with white linen"),
  ("Θέα από το μπαλκόνι στα πεύκα","View from the balcony over the pines"),
  ("Το μπαλκόνι με το τραπέζι και τα πεύκα","The balcony table and the pines"),
  ("Σαλόνι με τη σκάλα και την μπαλκονόπορτα","Living room with the staircase and balcony door"),
  ("Κρεβάτι στη σοφίτα, κάτω από τη στέγη","Bed in the loft, under the roof"),
  ("Υπνοδωμάτιο με διπλό κρεβάτι δίπλα στο παράθυρο","Bedroom with a double bed by the window"),
  ("Μπάνιο με νιπτήρα και ντους","Bathroom with basin and shower")],
 "stone-maisonette": [
  ("Σαλόνι διπλού ύψους με πέτρινο τοίχο, από τη σοφίτα","Double-height living room with stone wall, seen from the loft"),
  ("Σαλόνι, κουζίνα και σκάλα προς τον όροφο","Living room, kitchen and staircase to the upper floor"),
  ("Γωνιακός καναπές μπροστά στον πέτρινο τοίχο","Corner sofa in front of the stone wall"),
  ("Ανοιχτή σκάλα δίπλα σε τοιχογραφία με ανθισμένα κλαδιά","Open-tread staircase beside a blossom-branch mural"),
  ("Διπλό υπνοδωμάτιο με πορτατίφ","Double bedroom with lamps"),
  ("Υπνοδωμάτιο με διπλό κρεβάτι και πέτρινη επένδυση","Bedroom with double bed and stone-clad wall"),
  ("Δωμάτιο σοφίτας με μονό κρεβάτι και βιβλιοθήκη","Loft room with single bed and bookshelves"),
  ("Μπάνιο με μάρμαρο και ντους-βροχή","Marble-tiled bathroom with rain shower"),
  ("Στρογγυλός καθρέφτης και νιπτήρας","Round mirror and basin"),
  ("Κουζίνα με μπλε ντουλάπια και τραπεζαρία κάτω από τη σκάλα","Kitchen with blue cabinets and dining table under the stairs"),
  ("Σαλόνι με τηλεόραση και κλιματιστικό","Living room with TV and air conditioning"),
  ("Το σαλόνι από ψηλά","The living room from above"),
  ("Πέτρινος τοίχος και ψηλά παράθυρα","Stone wall and tall windows"),
  ("Ντουλάπα με καθρέφτη","Wardrobe with mirror"),
  ("Υπνοδωμάτιο με ντουλάπα","Bedroom with wardrobe"),
  ("Δεύτερο μπάνιο","Second bathroom"),
  ("Λεπτομέρεια από την τοιχογραφία με τα ανθισμένα κλαδιά","Detail of the blossom-branch mural")],
}
PHOTOS = {k: [(f"{k}-{i:02d}", el, en) for i, (el, en) in enumerate(v, 1)] for k, v in P.items()}

AM = {  # icon id, EL, EN
 "ac": ("ac","Κλιματισμός","Air conditioning"),
 "kitchen": ("kitchen","Κουζίνα","Kitchen"),
 "kitchenette": ("kitchen","Κουζινούλα","Kitchenette"),
 "fridge": ("fridge","Ρετρό ψυγείο","Retro fridge"),
 "washer": ("washer","Πλυντήριο ρούχων","Washing machine"),
 "balcony": ("balcony","Μπαλκόνι","Balcony"),
 "bigbalcony": ("balcony","Μεγάλο μπαλκόνι","Large balcony"),
 "loft": ("stairs","Σοφίτα με σκάλα","Loft via staircase"),
 "tv": ("tv","Τηλεόραση","TV"),
 "single": ("bed","Μονά κρεβάτια","Single beds"),
 "double": ("bed","Διπλό κρεβάτι","Double bed"),
 "shower": ("shower","Μπάνιο με ντους","Shower"),
 "pines": ("pine","Θέα στα πεύκα","Pine-forest view"),
 "stone": ("home","Σαλόνι διπλού ύψους","Double-height living room"),
}

# NOTE: apartment names are working names drawn from the photos — confirm with Katerina.
APTS = [
 {"slug":"turquoise-loft","el":"Τιρκουάζ σοφίτα","en":"Turquoise Loft","page":True,
  "teaser":("Ρετρό τιρκουάζ ψυγείο, ανοιχτή σκάλα προς τη σοφίτα και μεγάλο μπαλκόνι πάνω από τα πεύκα.",
            "A turquoise retro fridge, an open-tread staircase to the loft and a big balcony over the pines."),
  "chips":["ac","washer","bigbalcony","loft"],
  "amen":["ac","kitchen","fridge","washer","bigbalcony","loft","tv","shower"],
  "body":[
   ("Ένα φωτεινό διαμέρισμα σε δύο επίπεδα. Στην ανοιχτή κουζίνα ξεχωρίζει το τιρκουάζ ρετρό ψυγείο, δίπλα σε εστίες, φούρνο και πλυντήριο ρούχων· από πάνω της, μια ανοιχτή σκάλα με ξύλινα σκαλοπάτια ανεβαίνει στο υπνοδωμάτιο της σοφίτας.",
    "A bright apartment on two levels. The open kitchen is built around a turquoise retro fridge, with a hob, oven and washing machine beside it; above it, an open-tread staircase with wooden steps climbs to the loft bedroom."),
   ("Το σαλόνι, με κλιματισμό και τηλεόραση, ανοίγει με μπαλκονόπορτα σε ένα μεγάλο μπαλκόνι με τραπέζι για φαγητό έξω, πάνω από το πευκοδάσος. Υπάρχει επίσης διπλό υπνοδωμάτιο και μπάνιο με ντους.",
    "The living room, with air conditioning and a TV, opens through glass doors onto a large balcony with a table for eating outside, looking over the pine forest. There is also a double bedroom and a bathroom with a shower.")],
  "spaces":[
   (1,"Κουζίνα","Kitchen","Τιρκουάζ ρετρό ψυγείο, εστίες, φούρνος, πλυντήριο.","Turquoise retro fridge, hob, oven, washing machine."),
   (4,"Σκάλα & σοφίτα","Staircase & loft","Ανοιχτή ξύλινη σκάλα προς το υπνοδωμάτιο της σοφίτας.","Open wooden staircase up to the loft bedroom."),
   (2,"Σαλόνι","Living room","Καναπές, τηλεόραση, κλιματισμός, έξοδος στο μπαλκόνι.","Sofa, TV, air conditioning, door to the balcony."),
   (3,"Μπαλκόνι","Balcony","Μεγάλο, με τραπέζι, πάνω από τα πεύκα.","Large, with a table, over the pines."),
   (6,"Υπνοδωμάτια","Bedrooms","Διπλό υπνοδωμάτιο και υπνοδωμάτιο σοφίτας.","A double bedroom and the loft bedroom."),
   (12,"Μπάνιο","Bathroom","Με ντους.","With shower.")],
  "og":"turquoise-loft.jpg"},
 {"slug":"stone-maisonette","el":"Μεζονέτα με πέτρα","en":"Stone-wall Maisonette","page":False,
  "teaser":("Σαλόνι διπλού ύψους με πέτρινο τοίχο, ζωγραφισμένη σκάλα και υπνοδωμάτια στη σοφίτα.",
            "A double-height living room with a stone wall, a painted staircase and loft bedrooms."),
  "chips":["stone","loft","ac","shower"],"og":"stone-maisonette.jpg"},
 {"slug":"studio","el":"Στούντιο με θέα στα πεύκα","en":"Pine-view Studio","page":False,
  "teaser":("Μονά κρεβάτια, κουζινούλα και μπαλκόνι που κοιτάζει κατευθείαν στα πεύκα.",
            "Single beds, a kitchenette and a balcony that looks straight into the pines."),
  "chips":["single","kitchenette","balcony","pines"],"og":"studio.jpg"},
 {"slug":"green","el":"Πράσινο διαμέρισμα","en":"Green Apartment","page":False,
  "teaser":("Κουζίνα-σαλόνι με πράσινους τοίχους και καμάρα, και ξεχωριστό διπλό υπνοδωμάτιο.",
            "A green-walled kitchen and living room under an arch, with a separate double bedroom."),
  "chips":["kitchen","double","ac","tv"],"og":"green.jpg"},
]

# ── icons ─────────────────────────────────────────────────────────────────
ICONS = {
 "phone":'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "wa":'<path d="M3.5 20.5l1.4-4.1A8.6 8.6 0 1 1 8 19.3z"/><path d="M9.3 8.4c.3-.5.8-.5 1.1 0l.6 1.3c.1.3 0 .6-.2.8l-.4.4c.5 1 1.3 1.8 2.3 2.3l.4-.4c.2-.2.5-.3.8-.2l1.3.6c.5.3.5.8 0 1.1-.8.5-1.8.6-2.7.2a8 8 0 0 1-3.5-3.5c-.4-.9-.3-1.9.3-2.6z"/>',
 "viber":'<path d="M12 3c5 0 8 2 8 7s-3 7-8 7l-4 3v-3.5C5 15.5 4 13 4 10c0-5 3-7 8-7z"/><path d="M12.5 6.5a3.5 3.5 0 0 1 3 3M12.5 8.5a1.5 1.5 0 0 1 1 1"/>',
 "fb":'<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/>',
 "link":'<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "share":'<path d="M12 3v12M7 8l5-5 5 5M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/>',
 "ac":'<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M9.5 4.5 12 6l2.5-1.5M9.5 19.5 12 18l2.5 1.5"/>',
 "kitchen":'<path d="M4 10h16v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4zM2 10h20M9 7c0-1 1-1 1-2.5M14 7c0-1 1-1 1-2.5"/>',
 "fridge":'<path d="M7 3h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zM6 10h12M9 6v2M9 13v3"/>',
 "washer":'<path d="M5 3h14v18H5zM5 7h14"/><circle cx="12" cy="14" r="4"/><path d="M8 5h1"/>',
 "balcony":'<path d="M3 12h18M5 12v8M9 12v8M13 12v8M17 12v8M3 20h18M7 12V4h10v8"/>',
 "stairs":'<path d="M3 20h5v-4h4v-4h4V8h5"/>',
 "tv":'<path d="M3 6h18v11H3zM8 21h8M12 17v4"/>',
 "bed":'<path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.6"/>',
 "shower":'<path d="M4 21V7a3 3 0 0 1 6 0M7 10h7M9 14v.5M12 14v.5M15 14v.5M10.5 17.5v.5M13.5 17.5v.5"/>',
 "pine":'<path d="M12 3l5 7h-3l4 6H6l4-6H7zM12 16v5"/>',
 "home":'<path d="M4 20V10l8-6 8 6v10zM9 20v-6h6v6"/>',
 "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
 "back":'<path d="M19 12H5M11 6l-6 6 6 6"/>',
 "prev":'<path d="M15 6l-6 6 6 6"/>',
 "next":'<path d="M9 6l6 6-6 6"/>',
 "close":'<path d="M6 6l12 12M18 6 6 18"/>',
 "grid":'<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/>',
 "mail":'<path d="M3 6h18v12H3zM3 7l9 6 9-6"/>',
 "pin":'<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
}
SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{v}</symbol>' for k, v in ICONS.items()) + "</defs></svg>"
def ic(name): return f'<svg aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>'

# ── images ────────────────────────────────────────────────────────────────
def pic(pre, stem, el, en, sizes="100vw", eager=False, w=1200, h=1600):
    ws = ",".join(f"{pre}assets/img/{stem}-{x}.webp {x}w" for x in (480, 800, 1200))
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    return (f'<picture><source type="image/webp" srcset="{ws}" sizes="{sizes}">'
            f'<img src="{pre}assets/img/{stem}-800.jpg" width="{w}" height="{h}" alt="{escape(el)}" '
            f'data-alt-el="{escape(el)}" data-alt-en="{escape(en)}" {load} decoding="async"></picture>')
def full(pre, stem): return f"{pre}assets/img/{stem}-1200.webp"

# ── shared chrome ─────────────────────────────────────────────────────────
def head(pre, canon, title_el, title_en, desc_el, desc_en, og, og_alt, extra=""):
    title = f"{title_el} · {title_en}"
    desc = f"{desc_el} · {desc_en}"
    img = BASE + "og/" + og
    return f"""<!doctype html>
<html lang="el" data-lang="el" data-title-el="{escape(title_el)}" data-title-en="{escape(title_en)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>(function(){{var d=document.documentElement,l=null;d.classList.add('js');try{{l=new URLSearchParams(location.search).get('lang')||localStorage.getItem('lang')}}catch(e){{}}if(l!=='el'&&l!=='en'){{l=/^el\\b/i.test(navigator.language||'el')?'el':'en'}}d.setAttribute('data-lang',l);d.lang=l;document.title=d.getAttribute('data-title-'+l)}})()</script>
<title>{escape(title_el)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="el" href="{canon}?lang=el">
<link rel="alternate" hreflang="en" href="{canon}?lang=en">
<link rel="alternate" hreflang="x-default" href="{canon}">
<meta name="theme-color" content="#17322A">
<link rel="icon" href="{pre}assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}assets/apple-touch-icon.png">
<link rel="preload" href="{pre}assets/fonts/noto-serif-display-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}assets/css/site.css">
<!-- Open Graph / sharing: absolute URLs only -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{img}">
<meta property="og:image:secure_url" content="{img}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{escape(og_alt)}">
<meta property="og:locale" content="el_GR">
<meta property="og:locale:alternate" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{escape(og_alt)}">
{extra}
</head>
<body>
<a class="skip" href="#main">{t("Μετάβαση στο περιεχόμενο","Skip to content")}</a>
{SPRITE}
"""

def header(pre, home=True):
    h = "" if home else f"{pre}"
    nav = [("apartments","Διαμερίσματα","Apartments"),("photos","Φωτογραφίες","Photos"),("keramoti","Κεραμωτή","Keramoti"),("contact","Επικοινωνία","Contact")]
    links = "".join(f'<a href="{h}#{a}">{t(el,en)}</a>' for a, el, en in nav)
    return f"""<header class="hdr">
 <div class="wrap">
  <a class="brand" href="{pre or './'}"><b>Katerina apartments</b><small>{t("Κεραμωτή","Keramoti")}</small></a>
  <nav class="nav" aria-label="Κύριο μενού" data-aria-el="Κύριο μενού" data-aria-en="Main menu">{links}</nav>
  <div class="lang" role="group" aria-label="Γλώσσα / Language">
   <button type="button" data-set-lang="el" aria-pressed="true"><span aria-hidden="true">EL</span><span class="sr-only">Ελληνικά</span></button>
   <button type="button" data-set-lang="en" aria-pressed="false"><span aria-hidden="true">EN</span><span class="sr-only">English</span></button>
  </div>
  {call_btn("btn-sm")}
 </div>
</header>"""

def call_btn(cls=""):
    return f'<a class="btn btn-call {cls}" href="tel:{TEL}">{ic("phone")}{t("Καλέστε για κράτηση","Call to book")}</a>'
def wa_btn(cls="", label=True):
    lab = t("WhatsApp","WhatsApp") if label else '<span class="sr-only">WhatsApp</span>'
    return f'<a class="btn btn-wa {cls}" href="{WA}" rel="noopener">{ic("wa")}{lab}</a>'

def footer(pre):
    return f"""<footer class="ftr">
 <div class="wrap">
  <span>© 2026 Katerina apartments · {t("Κεραμωτή, Καβάλα","Keramoti, Kavala")}</span>
  <span>{t("Κρατήσεις μόνο τηλεφωνικά","Bookings by phone only")} · <a href="tel:{TEL}">{PHONE}</a></span>
 </div>
</footer>
<div class="callbar" role="region" aria-label="Κράτηση" data-aria-el="Κράτηση" data-aria-en="Booking">
 {call_btn()}
 {wa_btn(label=False)}
</div>
<dialog class="lb" id="lb" aria-label="Φωτογραφίες" data-aria-el="Φωτογραφίες" data-aria-en="Photos">
 <div class="lb-top"><span class="lb-count" aria-live="polite"></span>
  <button class="lb-btn lb-close" type="button">{ic("close")}<span class="sr-only">{t("Κλείσιμο","Close")}</span></button></div>
 <div class="lb-stage">
  <button class="lb-btn lb-prev" type="button">{ic("prev")}<span class="sr-only">{t("Προηγούμενη","Previous")}</span></button>
  <img alt="">
  <button class="lb-btn lb-next" type="button">{ic("next")}<span class="sr-only">{t("Επόμενη","Next")}</span></button>
 </div>
 <p class="lb-cap"></p>
</dialog>
<script src="{pre}assets/js/site.js" defer></script>
</body>
</html>
"""

def tbc(el, en): return f'<span class="tbc">{t(el, en)}</span>'

def carousel(pre, slug, photos, sizes, lb=True, eager_first=False, label=("",""), count=True):
    slides = "".join(
        (f'<a href="{full(pre,s)}" data-lb="{slug}">' if lb else "<div>") + pic(pre, s, el, en, sizes, eager_first and i == 0) + ("</a>" if lb else "</div>")
        for i, (s, el, en) in enumerate(photos))
    return f"""<div class="car" data-car>
  <div class="car-track" tabindex="0" role="group" aria-roledescription="carousel" aria-label="{escape(label[0])}" data-aria-el="{escape(label[0])}" data-aria-en="{escape(label[1])}">{slides}</div>
  <button class="car-btn car-prev" type="button" tabindex="-1" aria-hidden="true">{ic("prev")}</button>
  <button class="car-btn car-next" type="button" tabindex="-1" aria-hidden="true">{ic("next")}</button>
  {'<span class="car-count" aria-hidden="true"></span>' if count else ''}
 </div>"""

# ── HOME ──────────────────────────────────────────────────────────────────
def home():
    pre = ""
    L = PHOTOS["turquoise-loft"]
    jsonld = {"@context":"https://schema.org","@type":"LodgingBusiness","name":SITE,"url":BASE,
              "telephone":"+30 697 763 5937","image":BASE+"og/home.jpg",
              "address":{"@type":"PostalAddress","addressLocality":"Keramoti","addressRegion":"Kavala","addressCountry":"GR"},
              "geo":{"@type":"GeoCoordinates","latitude":40.857,"longitude":24.702}}
    out = head(pre, BASE, "Katerina apartments · Διαμερίσματα στην Κεραμωτή", "Katerina apartments · Apartments in Keramoti",
               "Οικογενειακά διαμερίσματα στην Κεραμωτή Καβάλας, ανάμεσα στο πευκοδάσος και την αμμουδιά. Κρατήσεις τηλεφωνικά",
               "Family-run apartments in Keramoti, Kavala, between the pine forest and the sand. Book by phone",
               "home.jpg", "Katerina apartments, Keramoti: balcony over the pines, turquoise kitchen and stone-wall living room",
               f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>')
    out += header(pre)
    out += f"""<main id="main">
<section class="hero" aria-labelledby="h1">
 <div class="hero-media">{pic(pre, L[2][0], L[2][1], L[2][2], "(min-width:960px) 55vw, 100vw", eager=True)}</div>
 <div class="hero-aside" aria-hidden="true">{pic(pre, L[0][0], L[0][1], L[0][2], "200px")}</div>
 <div class="hero-copy on-photo">
  <p class="kicker">{t("Κεραμωτή · Καβάλα","Keramoti · Kavala · Greece")}</p>
  <h1 id="h1">Katerina apartments</h1>
  <p class="tagline">{t("Οικογενειακά διαμερίσματα ανάμεσα στο πευκοδάσος και την αμμουδιά.","Family-run apartments between the pine forest and the sand.")}</p>
  <div class="cta-row">{call_btn()}{wa_btn()}</div>
 </div>
</section>
<ul class="facts" aria-label="Αποστάσεις" data-aria-el="Αποστάσεις" data-aria-en="Distances">
 <li><b>10 km</b><small>{t("περίπου, από το αεροδρόμιο Καβάλας","approx., from Kavala airport")}</small></li>
 <li><b>35–40′</b><small>{t("με το φέρι για Θάσο","by ferry to Thassos")}</small></li>
 <li><b>40 km</b><small>{t("περίπου, ανατολικά της Καβάλας","approx., east of Kavala")}</small></li>
 <li><b>{t("Δίπλα","Next door")}</b><small>{t("στο Δέλτα του Νέστου","to the Nestos delta")}</small></li>
</ul>

<section class="sec">
 <div class="wrap intro reveal">
  <p class="big">{t("Ένα μικρό, οικογενειακό κατάλυμα στο χωριό. Κλείνετε απευθείας με την Κατερίνα, στο τηλέφωνο.","A small, family-run place in the village. You book directly with Katerina, by phone.")}</p>
  <div>
   <p class="lede">{t("Χωρίς φόρμες και χωρίς πλατφόρμες. Πάρτε τηλέφωνο ή στείλτε μήνυμα στο WhatsApp για διαθεσιμότητα και τιμές.","No forms, no booking platforms. Call or send a WhatsApp message to ask about availability and rates.")}</p>
   <p><a class="more" href="tel:{TEL}">{PHONE} {ic("arrow")}</a></p>
  </div>
 </div>
</section>

<section class="sec" id="apartments" aria-labelledby="h-apts" style="padding-top:0">
 <div class="wrap">
  <div class="sec-head reveal"><div><span class="kicker">{t("Τα διαμερίσματα","The apartments")}</span>
   <h2 id="h-apts">{t("Διαλέξτε τον χώρο σας","Choose your space")}</h2></div>
   <p class="lede">{t("Ο αριθμός ατόμων ανά διαμέρισμα θα συμπληρωθεί σύντομα.","Sleeping capacity per apartment will be added shortly.")}</p></div>
  <div class="cards">"""
    for a in APTS:
        ph = PHOTOS[a["slug"]][:6]
        href = f'apartments/{a["slug"]}/'
        name = t(a["el"], a["en"])
        alt = t(a["en"], a["el"])
        title = f'<a href="{href}">{name}</a>' if a["page"] else name
        chips = "".join(f'<li class="chip">{ic(AM[c][0])}{t(AM[c][1],AM[c][2])}</li>' for c in a["chips"])
        foot = (f'<a class="more" href="{href}" tabindex="-1" aria-hidden="true">{t("Δείτε το διαμέρισμα","View apartment")} {ic("arrow")}</a>'
                if a["page"] else f'<span class="soon">{t("Η σελίδα ετοιμάζεται","Page in progress")}</span>')
        out += f"""
   <article class="card reveal">
    {carousel(pre, a["slug"], ph, "(min-width:760px) 600px, 100vw", label=(a["el"]+": φωτογραφίες", a["en"]+": photos"))}
    <div class="card-body">
     <h3>{title}</h3>
     <p class="alt-name">{alt}</p>
     <p>{t(*a["teaser"])}</p>
     <ul class="chips">
      <li>{tbc("Άτομα: προς επιβεβαίωση","Sleeps: to be confirmed")}</li>{chips}</ul>
     <div class="card-foot">{foot}</div>
    </div>
   </article>"""
    out += "\n  </div>\n </div>\n</section>\n"

    # gallery
    curated = [("turquoise-loft",3),("stone-maisonette",1),("turquoise-loft",1),("studio",1),("green",1),("stone-maisonette",4),
               ("turquoise-loft",4),("studio",3),("stone-maisonette",8),("green",7),("turquoise-loft",5),("studio",5)]
    seen = set(); order = []
    for k, i in curated: order.append(PHOTOS[k][i-1]); seen.add(PHOTOS[k][i-1][0])
    for k in ("turquoise-loft","stone-maisonette","studio","green"):
        for p in PHOTOS[k]:
            if p[0] not in seen: order.append(p)
    hid = ' class="is-hidden"'
    items = "".join(f'<a href="{full(pre,s)}" data-lb="all"{hid if n >= 12 else ""}>{pic(pre,s,el,en,"(min-width:1100px) 300px, (min-width:720px) 33vw, 50vw")}</a>'
                    for n, (s, el, en) in enumerate(order))
    out += f"""<section class="sec" id="photos" aria-labelledby="h-photos" style="padding-top:0">
 <div class="wrap">
  <div class="sec-head reveal"><div><span class="kicker">{t("Φωτογραφίες","Gallery")}</span>
   <h2 id="h-photos">{t("Πραγματικές φωτογραφίες","Real photos")}</h2></div>
   <p class="lede">{t("Πατήστε μια φωτογραφία για μεγέθυνση. Βέλη ή σύρσιμο για την επόμενη.","Tap a photo to enlarge. Use the arrow keys or swipe for the next one.")}</p></div>
  <div class="grid" id="gal">{items}</div>
  <div class="grid-more"><button class="btn btn-ghost" type="button" data-show-all aria-controls="gal" aria-expanded="false">{ic("grid")}{t(f"Όλες οι φωτογραφίες ({len(order)})", f"All photos ({len(order)})")}</button></div>
 </div>
</section>
"""
    why = [
     ("Παραλία & Αμμόγλωσσα","Beach & Ammoglossa","Η αμμουδερή λωρίδα της Αμμόγλωσσας απλώνεται μπροστά στο χωριό.","The sandy Ammoglossa spit stretches out in front of the village.","~","beach"),
     ("Φέρι για Θάσο","Ferry to Thassos","Από το λιμάνι της Κεραμωτής, η διαδρομή για Θάσο κρατά 35 με 40 λεπτά.","From Keramoti harbour the crossing to Thassos takes 35 to 40 minutes.","35′","ferry"),
     ("Δέλτα του Νέστου","Nestos delta","Ο υγρότοπος του Δέλτα του Νέστου βρίσκεται ακριβώς δίπλα στο χωριό.","The Nestos delta wetland lies right next to the village.","","delta"),
     ("Αεροδρόμιο & Καβάλα","Airport & Kavala","Περίπου 10 km από το αεροδρόμιο της Καβάλας και περίπου 40 km από την πόλη.","About 10 km from Kavala airport and about 40 km from the city.","10 km","airport"),
    ]
    lis = "".join(f"""
   <li class="why-item reveal">
    <div class="ph" role="img" aria-label="{escape(el_t)}: θέση για πραγματική φωτογραφία" data-aria-el="{escape(el_t)}: θέση για πραγματική φωτογραφία" data-aria-en="{escape(en_t)}: real photo slot"><span>{t("Πραγματική φωτογραφία εδώ","Real photo here")}</span></div>
    {f'<span class="num" aria-hidden="true">{num}</span>' if num and num!='~' else ''}
    <h3>{t(el_t,en_t)}</h3><p>{t(el_d,en_d)}</p>
   </li>""" for el_t, en_t, el_d, en_d, num, _ in why)
    out += f"""<section class="sec why" id="keramoti" aria-labelledby="h-why">
 <div class="wrap">
  <div class="sec-head reveal"><div><span class="kicker">{t("Γιατί Κεραμωτή","Why Keramoti")}</span>
   <h2 id="h-why">{t("Θάλασσα, πεύκα και δέλτα","Sea, pines and a river delta")}</h2></div></div>
  <ul class="why-list">{lis}
  </ul>
 </div>
</section>

<section class="sec" id="location" aria-labelledby="h-map">
 <div class="wrap map-wrap">
  <div class="reveal"><span class="kicker" style="color:var(--terra);display:block;margin-bottom:10px">{t("Τοποθεσία","Location")}</span>
   <h2 id="h-map">{t("Κεραμωτή, Καβάλα","Keramoti, Kavala")}</h2>
   <p class="lede" style="margin-top:14px">{t("Το κατάλυμα βρίσκεται μέσα στο χωριό. Δεν υπάρχει όνομα οδού, οπότε καλέστε την Κατερίνα για οδηγίες.","The apartments are in the village itself. There is no street name, so call Katerina for directions.")}</p>
   <p><a class="more" href="https://www.openstreetmap.org/#map=14/40.857/24.702" rel="noopener">{t("Άνοιγμα σε μεγαλύτερο χάρτη","Open a larger map")} {ic("arrow")}</a></p>
  </div>
  <div>
   <div class="map"><iframe title="Χάρτης: Κεραμωτή, Καβάλα" src="https://www.openstreetmap.org/export/embed.html?bbox=24.655%2C40.835%2C24.750%2C40.880&amp;layer=mapnik" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
   <p class="map-credit">{t("Χάρτης","Map")} © <a href="https://www.openstreetmap.org/copyright" rel="noopener">OpenStreetMap contributors</a></p>
  </div>
 </div>
</section>
"""
    out += contact(pre) + "</main>\n" + footer(pre)
    return out

def contact(pre):
    return f"""<section class="sec contact" id="contact" aria-labelledby="h-contact">
 <div class="wrap contact-grid">
  <div>
   <span class="kicker" style="display:block;margin-bottom:10px">{t("Επικοινωνία & κρατήσεις","Contact & bookings")}</span>
   <h2 id="h-contact">{t("Καλέστε την Κατερίνα","Call Katerina")}</h2>
   <a class="phone-big" href="tel:{TEL}">{PHONE}</a>
   <div class="cta-row">{call_btn()}{wa_btn()}</div>
  </div>
  <dl class="dl">
   <div><dt>{t("Οικοδέσποινα","Host")}</dt><dd>{t(OWNER_EL, OWNER_EN)}</dd></div>
   <div><dt>{t("Τηλέφωνο","Phone")}</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd></div>
   <div><dt>WhatsApp</dt><dd><a href="{WA}" rel="noopener">{PHONE}</a></dd></div>
   <div><dt>Email</dt><dd>{tbc("Θα προστεθεί","To be added")}</dd></div>
   <div><dt>{t("Περιοχή","Area")}</dt><dd>{t("Κεραμωτή, Καβάλα, Ελλάδα","Keramoti, Kavala, Greece")}</dd></div>
  </dl>
 </div>
</section>
"""

# ── ROOM ──────────────────────────────────────────────────────────────────
def room(a):
    pre = "../../"
    ph = PHOTOS[a["slug"]]
    canon = f'{BASE}apartments/{a["slug"]}/'
    out = head(pre, canon, f'{a["el"]} · Katerina apartments, Κεραμωτή', f'{a["en"]} · Katerina apartments, Keramoti',
               t_strip(a["teaser"][0]) + " Κρατήσεις τηλεφωνικά", t_strip(a["teaser"][1]) + " Book by phone",
               a["og"], f'{a["en"]} at Katerina apartments, Keramoti: three real photos of the apartment')
    out += header(pre, home=False)
    bento = "".join(f'<a href="{full(pre,s)}" data-lb="room">{pic(pre,s,el,en,"(min-width:960px) 50vw, 100vw" if i==0 else "25vw", eager=(i==0))}</a>' for i,(s,el,en) in enumerate(ph[:5]))
    amen = "".join(f'<li>{ic(AM[k][0])}{t(AM[k][1],AM[k][2])}</li>' for k in a["amen"])
    spaces = "".join(f'<li><a href="{full(pre,ph[i-1][0])}" data-lb="room">{pic(pre,ph[i-1][0],ph[i-1][1],ph[i-1][2],"96px")}</a><div><b>{t(el,en)}</b><span>{t(del_,den)}</span></div></li>' for i,el,en,del_,den in a["spaces"])
    body = "".join(f"<p>{t(el,en)}</p>" for el,en in a["body"])
    allg = "".join(f'<a href="{full(pre,s)}" data-lb="room">{pic(pre,s,el,en,"(min-width:1100px) 300px, (min-width:720px) 33vw, 50vw")}</a>' for s,el,en in ph)
    others = [o for o in APTS if o["slug"] != a["slug"]]
    oth = "".join(f"""<article class="card"><div class="car"><div class="car-track" style="overflow:hidden">{pic(pre,PHOTOS[o['slug']][0][0],PHOTOS[o['slug']][0][1],PHOTOS[o['slug']][0][2],"(min-width:960px) 400px, 100vw")}</div></div>
     <div class="card-body"><h3>{(f'<a href="../{o["slug"]}/">' + t(o["el"],o["en"]) + '</a>') if o["page"] else t(o["el"],o["en"])}</h3><p>{t(*o["teaser"])}</p>{'' if o["page"] else '<span class="soon">'+t("Η σελίδα ετοιμάζεται","Page in progress")+'</span>'}</div></article>""" for o in others)
    out += f"""<main id="main">
<div class="wrap">
 <a class="crumb" href="../../#apartments">{ic("back")}{t("Όλα τα διαμερίσματα","All apartments")}</a>
 <section class="room-hero" aria-label="Φωτογραφίες" data-aria-el="Φωτογραφίες" data-aria-en="Photos">
  {carousel(pre, "room", ph, "100vw", eager_first=True, label=(a["el"]+": φωτογραφίες", a["en"]+": photos"))}
  <div class="bento">{bento}</div>
  <div class="showall"><a class="btn" href="#all-photos">{ic("grid")}{t(f"Όλες ({len(ph)})", f"All {len(ph)} photos")}</a></div>
 </section>

 <header class="room-head">
  <div><p class="kicker" style="color:var(--terra);margin:0 0 10px">{t("Διαμέρισμα · Κεραμωτή","Apartment · Keramoti")}</p>
   <h1>{t(a["el"], a["en"])}</h1><p class="alt-name">{t(a["en"], a["el"])}</p></div>
  <ul class="qf">
   <li>{tbc("Άτομα: προς επιβεβαίωση","Sleeps: to be confirmed")}</li>
   <li>{tbc("Υπνοδωμάτια: προς επιβεβαίωση","Bedrooms: to be confirmed")}</li>
   <li>{tbc("Τιμές: θα προστεθούν","Rates: to be added")}</li>
  </ul>
 </header>

 <div class="room-layout" style="padding-bottom:48px">
  <div>
   <div class="prose">{body}</div>
   <h2 class="h3">{t("Οι χώροι","The spaces")}</h2>
   <ul class="spaces">{spaces}</ul>
   <h2 class="h3">{t("Παροχές","Amenities")}</h2>
   <ul class="amen">{amen}</ul>
   <p style="margin-top:12px;font-size:.92rem;color:var(--ink-2)">{t("Ρωτήστε την Κατερίνα για ό,τι δεν βλέπετε εδώ.","Ask Katerina about anything not listed here.")}</p>
  </div>
  <aside class="book" aria-labelledby="h-book">
   <h2 id="h-book">{t("Κράτηση τηλεφωνικά","Book by phone")}</h2>
   <p class="note">{t("Καλέστε ή στείλτε μήνυμα στην Κατερίνα για διαθεσιμότητα και τιμές.","Call or message Katerina for availability and rates.")}</p>
   {call_btn()}
   {wa_btn()}
   <div class="share" data-share>
    <span class="share-label" id="share-l">{t("Κοινοποίηση","Share this apartment")}</span>
    <div class="share-row" role="group" aria-labelledby="share-l">
     <button type="button" class="share-native" data-native>{ic("share")}{t("Κοινοποίηση…","Share…")}</button>
     <a href="#" data-fb target="_blank" rel="noopener">{ic("fb")}Facebook</a>
     <a href="#" data-wa target="_blank" rel="noopener">{ic("wa")}WhatsApp</a>
     <a href="#" data-viber>{ic("viber")}Viber</a>
     <button type="button" data-copy>{ic("link")}{t("Αντιγραφή συνδέσμου","Copy link")}</button>
    </div>
    <p class="toast" role="status" aria-live="polite"></p>
   </div>
  </aside>
 </div>

 <section id="all-photos" class="sec" style="padding-top:0" aria-labelledby="h-all">
  <h2 id="h-all" class="h3">{t(f"Όλες οι φωτογραφίες ({len(ph)})", f"All photos ({len(ph)})")}</h2>
  <div class="grid">{allg}</div>
 </section>

 <section class="sec" style="padding-top:0" aria-labelledby="h-oth">
  <h2 id="h-oth" class="h3">{t("Τα άλλα διαμερίσματα","The other apartments")}</h2>
  <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{oth}</div>
 </section>
</div>
"""
    out += contact(pre) + "</main>\n" + footer(pre)
    return out

def t_strip(s): return s

if __name__ == "__main__":
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(home())
    for a in APTS:
        if a["page"]:
            d = os.path.join(ROOT, "apartments", a["slug"]); os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(room(a))
    print("built")
