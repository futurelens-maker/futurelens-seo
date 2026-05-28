# futurelens-seo

Pagine programmatic SEO per FutureLens. HTML statico deployato su Vercel.

## Struttura

```
futurelens-seo/
├── agente-whatsapp-coach-high-ticket/
│   └── index.html      → /agente-whatsapp-coach-high-ticket
├── robots.txt          → /robots.txt
├── sitemap.xml         → /sitemap.xml
└── vercel.json         → configurazione Vercel
```

## Deploy

1. Push su GitHub (repo: futurelens-seo)
2. Import su Vercel → deploy automatico
3. Aggiungere custom domain: seo.futurelens.xyz
   - Namecheap DNS: CNAME `seo` → `cname.vercel-dns.com`
   - Vercel dashboard: Add Domain

## Aggiungere una pagina

1. Crea cartella con nome = URL slug (es. `agente-whatsapp-consulenti/`)
2. Copia `agente-whatsapp-coach-high-ticket/index.html` nella nuova cartella
3. Aggiorna: H1, meta title/description, canonical URL, descriptor, segmento, contenuti
4. Aggiungi l'URL in `sitemap.xml`
5. Commit + push → Vercel rideploya automaticamente

## Checklist SEO pre-pubblicazione

- [ ] Keyword in H1, prime 100 parole, almeno 1 H2, meta title
- [ ] Canonical URL corretto e coerente con sitemap
- [ ] Schema WebPage + FAQPage + Service compilati
- [ ] Lista "cosa non fa" presente
- [ ] CTA Blueprint €27 primaria + Substack secondaria
- [ ] Nessun placeholder rimasto ([N], [URL], etc.)
- [ ] Rich Results Test: search.google.com/test/rich-results
