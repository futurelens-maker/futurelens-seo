# futurelens-seo — Programmatic SEO

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
- Blueprint URL: `https://futurelens.xyz/whatsapp-agent-blueprint` · Prezzo: `€27`
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

## Checklist SEO pre-push

- [ ] Nessun `{{` rimasto nel file generato
- [ ] H1 contiene il nome del segmento
- [ ] Canonical URL corretto
- [ ] Schema WebPage + Service + FAQPage nel `<head>`
- [ ] `dateModified` = data odierna
- [ ] Sitemap aggiornata con `<lastmod>` odierno

## Risparmio token vs approccio manuale

Claude genera solo il JSON (~3–5KB) invece dell'HTML completo (~50KB). Risparmio ~80% di token per pagina.
