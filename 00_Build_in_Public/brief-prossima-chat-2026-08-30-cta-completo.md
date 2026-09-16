# Brief — follow-up ENTRY_001 (CTA data-driven parziale)

**Contesto:** ENTRY_001 (2026-08-30, journal `00_Build_in_Public/JOURNAL.md`) ha reso data-driven URL e testo del bottone CTA (`content/_cta.json` → `{{CTA_URL}}`/`{{CTA_TEXT_HEADER}}`/`{{CTA_TEXT_MAIN}}`), limitando deliberatamente lo scope a quello segnalato nel brief precedente ("l'URL/testo del CTA"). Un grep di verifica dopo il fix ha trovato che prezzo e nome prodotto restano hardcoded altrove negli stessi 4 template, fuori dallo scope diretto.

## MEDIA — Prezzo/nome prodotto ancora hardcoded fuori dal bottone CTA

Occorrenze non coperte da `content/_cta.json`:
- `template-g.html:443` — badge `[ whatsapp ai autopilot™ — €17 ]`
- `template-g.html:452` — testo `€17 una tantum. Nessun abbonamento, nessuna call obbligatoria.`
- `template-a.html:730`, `template-c.html:622`, `template-d.html:413`, `template-g.html:449` — corpo descrittivo che nomina "WhatsApp AI Autopilot™" in prosa (non in un placeholder)

Se il prezzo cambia di nuovo (es. da €17 a un altro valore), questi punti richiedono ancora modifica manuale su più file — lo stesso problema che l'ENTRY_001 ha risolto solo per il bottone.

**Istruzione:** valutare se estendere `content/_cta.json` con `cta_price` (es. `"€17"`) e `cta_product_name` (es. `"WhatsApp AI Autopilot™"`), aggiungere `{{CTA_PRICE}}` e `{{CTA_PRODUCT_NAME}}` a `load_cta()` in `build.py`, e sostituire le occorrenze sopra. Verificare con l'utente prima di implementare — è un'estensione dello stesso pattern già accettato, ma allarga lo scope di cosa viene sempre iniettato vs cosa resta prosa libera per-template (il body descrittivo ha toni diversi per categoria A/C/D/G, quindi solo nome e prezzo vanno estratti, non l'intera frase).
