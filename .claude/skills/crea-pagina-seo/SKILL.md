# Skill: /crea-pagina-seo

Genera una nuova pagina programmatic SEO da un file MD con i contenuti del segmento, aggiorna sitemap.xml e fa git push su Vercel.

## Input atteso

L'utente incolla o riferisce un file `.md` con i contenuti per il nuovo segmento. Il file contiene tutte le informazioni necessarie: pain point specifici, dati con fonti, checklist, FAQ, copy AI.

## Flusso

### Step 0 — Leggi lo schema
Leggi `content/_schema.json` per conoscere la struttura dati completa. Usa questo file come riferimento per compilare il JSON del nuovo segmento.

### Step 1 — Leggi il brief
Leggi il file MD fornito dall'utente (o il contenuto incollato). Estrai:
- Slug (es. `agente-whatsapp-avvocati`)
- Titolo segmento, subtitle, hero pain
- Trust items specifici per il segmento
- Dati con fonte per il data box
- 4 step con output
- 10 checklist ✓ e 3 checklist ✗
- Tabella risultati (5 righe)
- Tipo di confronto (setter umano / chatbot / Spoki / VA / ecc.)
- 5 FAQ segmento-specifiche
- Copy AI summary

### Step 2 — Genera content/[slug].json
Compila il file JSON con tutte le chiavi dello schema. **Regole obbligatorie:**
- `date_modified` = data odierna (formato YYYY-MM-DD)
- `canonical_url` = `https://seo.futurelens.xyz/[slug]`
- Zero placeholder: nessun campo vuoto, `[N]`, `€X–Y` non compilato
- `confronto_col2` e `confronto_col3` = i nomi reali dei competitor per questo segmento
- Tutte le `checklist_yes` devono avere 10 voci, `checklist_no` 3 voci
- `faqs` = esattamente 5 domande, specifiche per il segmento (non generiche)

Scrivi il file in `content/[slug].json`.

### Step 3 — Esegui build.py
```
python build.py [slug]
```
Dal progetto root `c:\Users\user\claude-ecosystem\futurelens-seo`.

Verifica output: nessun WARNING su "unreplaced markers".

### Step 4 — Verifica assenza placeholder
Leggi `[slug]/index.html` e controlla:
- Nessun testo `{{` nel file
- H1 contiene il nome del segmento corretto
- `<link rel="canonical"` punta all'URL corretto
- `dateModified` è la data odierna
- Sezione 8 (Copy for AI) ha `style="display:none;"`

### Step 5 — Git commit e push
```bash
git add [slug]/index.html sitemap.xml content/[slug].json
git commit -m "feat: pagina [slug]"
git push origin main
```

Riporta all'utente:
- URL live: `https://seo.futurelens.xyz/[slug]` (live in ~60 secondi)
- Conferma sitemap aggiornata
- Eventuale Rich Results Test: `https://search.google.com/test/rich-results?url=https://seo.futurelens.xyz/[slug]`

## Regole fisse (non modificare)
- WhatsApp AI Autopilot™ URL: `https://futurelens.xyz/whatsapp-autopilot`
- Substack URL: `https://thesystemlog.substack.com/`
- Prezzo WhatsApp AI Autopilot™: `€17` (una tantum, setup guidato in 75 minuti)
- Stack tecnico: `n8n / Evolution API (self-host) / Claude Code (Metodo AI-Guidato™) / GoHighLevel / HubSpot / Calendly / Meta Lead Ads` (invariante)
- `schema_service_type`: sempre `WhatsApp AI Automation`
