# futurelens-seo — Programmatic SEO

`/log-milestone` è una skill globale (`~/.claude/skills/log-milestone/`). Il blocco sotto è la sua configurazione per questo progetto — non rimuoverlo.

<!-- log-milestone: config -->
journal_path: 00_Build_in_Public/JOURNAL.md
journal_tipo_extra: []
journal_fase_vocab: [Contenuto, SEO, Template, Infrastruttura, Sistema, "Claude Architecture"]
journal_campi_extra: []
<!-- /log-milestone: config -->

## Stack

HTML statico → GitHub → Vercel → `https://seo.futurelens.xyz` (deploy ~60 secondi dopo push)

## Skill disponibile

| Comando | Descrizione |
|---|---|
| `/crea-pagina-seo` | Genera una nuova pagina da un file MD con i contenuti del segmento → build.py → git push |

## Come aggiungere una pagina (flusso automatico)

1. Prepara un file MD con i contenuti del segmento
2. Usa `/crea-pagina-seo` — la skill gestisce tutto il resto

## Come aggiungere una pagina (flusso manuale)

1. Crea `content/[slug].json` usando `content/_schema.json` come riferimento
2. `python build.py [slug]` → genera `[slug]/index.html` + aggiorna `sitemap.xml`
3. `git add [slug]/index.html sitemap.xml content/[slug].json`
4. `git commit -m "feat: pagina [slug]" && git push origin main`

## Struttura

```
futurelens-seo/
├── template.html          ← HTML con {{MARKER}} — non modificare manualmente
├── build.py               ← generatore: python build.py <slug>
├── content/
│   ├── _schema.json       ← template vuoto per nuove pagine
│   └── [slug].json        ← contenuto variabile per ogni pagina
├── [slug]/index.html      ← output generato da build.py
├── sitemap.xml            ← aggiornato automaticamente da build.py
├── robots.txt
└── vercel.json
```

## Regole tecniche obbligatorie

- `canonical_url`: sempre `https://seo.futurelens.xyz/[slug]`
- `date_modified`: data odierna (YYYY-MM-DD)
- Prodotto/prezzo da citare come CTA: WhatsApp AI Autopilot™, €17 (non più "The WhatsApp Agent Blueprint" €27 — deprecato 2026-08-28, vedi `~/.claude/kb/04_offerte/offerta-whatsapp-autopilot.md`). CTA URL: `https://futurelens.xyz/whatsapp-autopilot`. Dal 2026-08-30 URL e testo del CTA sono **data-driven**: unica fonte `content/_cta.json` (`cta_url`, `cta_text_header`, `cta_text_main`), iniettato da `build.py` in ogni pagina via `{{CTA_URL}}` / `{{CTA_TEXT_HEADER}}` / `{{CTA_TEXT_MAIN}}` — per cambiare prodotto/prezzo/URL del CTA basta editare `content/_cta.json` e rilanciare `build.py` su tutte le pagine, senza toccare i 4 template
- Substack URL: `https://thesystemlog.substack.com/`
- Sezione 8 (Copy for AI): `style="display:none;"` — già in template, non toccare
- Zero placeholder: nessun campo vuoto nei JSON prima del build

## Pagine live

| Slug | Segmento |
|---|---|
| agente-whatsapp-coach-high-ticket | Coach High-Ticket |
| agente-whatsapp-consulenti | Consulenti B2B |
| agente-whatsapp-accademie-digitali | Accademie Digitali |
| agente-whatsapp-infoproduttori | Infoproduttori |
| agente-whatsapp-formatori | Formatori |
| agente-ai-whatsapp | Definizione tecnica agente AI WhatsApp |
| appointment-setting-ai-italia | AI Appointment Setting Italia |
| riduzione-no-show-appuntamenti | Riduzione No-Show Appuntamenti |
| perdo-clienti-whatsapp | Perdo Clienti su WhatsApp |
| lead-whatsapp-senza-risposta | Lead WhatsApp Senza Risposta |
| roi-automazione-whatsapp-coach | ROI Automazione WhatsApp per Coach |
| quanto-costa-agente-whatsapp-ai | Quanto Costa un Agente WhatsApp AI |
| qualificazione-lead-automatica | Qualificazione Lead Automatica |

Nota: questa tabella va tenuta sincronizzata con `content/*.json` (fonte di verità sulle pagine esistenti) — ogni nuovo `content/[slug].json` corrisponde a una pagina in `Pagine/[slug]/`.

## Checklist SEO pre-push

- [ ] Nessun `{{` rimasto nel file generato
- [ ] H1 contiene il nome del segmento
- [ ] Canonical URL corretto
- [ ] Schema WebPage + Service + FAQPage nel `<head>`
- [ ] `dateModified` = data odierna
- [ ] Sitemap aggiornata con `<lastmod>` odierno

## Risparmio token vs approccio manuale

Claude genera solo il JSON (~3–5KB) invece dell'HTML completo (~50KB). Risparmio ~80% di token per pagina.

## Rename Verification Gate

Obbligatorio ogni volta che un nome prodotto, prezzo o dettaglio tecnico dello stack (es. componenti del funnel low-ticket) cambia. In questo progetto il contenuto vive in **due posti distinti** che vanno controllati entrambi, non solo uno:

1. `content/*.json` — contenuto per-pagina (hero, FAQ, tabelle, ai_copy_text)
2. `template-a/c/d/g.html` — HTML sorgente condiviso da tutte le pagine di quel tipo (CTA, header, badge)

Prima di dichiarare un rename "completo" in una entry del journal o in un brief, esegui `grep -rn "<vecchio-termine>"` su **entrambe** le categorie di file (`content/*.json` E `template-*.html`), non fermarti al primo gruppo che dà risultati. Un rename non è considerato chiuso finché questo grep esaustivo non restituisce zero occorrenze fuori scope (escluse note storiche che spiegano il rename stesso). Ricorda che le pagine in `Pagine/[slug]/index.html` sono generate da `build.py` — non editarle a mano, correggi sempre la fonte (JSON o template) e rilancia il build.
