# futurelens-seo — Build in Public Journal

Questo journal documenta ogni milestone, pivot architetturale e lezione appresa nella costruzione delle pagine SEO programmatiche di **futurelens-seo** (`seo.futurelens.xyz`).

Ha due livelli per ogni entry: **(A) cosa è stato costruito** e **(B) come è stato usato Claude Code per costruirlo**.

---

## INDICE DELLE ENTRY

| # | Data | Tipo | Titolo |
|---|------|------|--------|
| [001](#entry-001) | 2026-08-30 | Pivot Architetturale + Infrastruttura | Chiusura propagazione rename prodotto low-ticket: 9 file residui, CTA data-driven, Rename Verification Gate |

---

<a name="entry-001"></a>
## ENTRY_001 — 2026-08-30 — Chiusura propagazione rename prodotto low-ticket: 9 file residui, CTA data-driven, Rename Verification Gate

**Tipo:** Pivot Architetturale + Infrastruttura
**Fase:** Contenuto | Infrastruttura

---

### Il Problema Ingegneristico Affrontato

Una sessione precedente (ENTRY_004 del journal a livello ecosistema) aveva propagato il rename del prodotto low-ticket (da "The WhatsApp Agent Blueprint €27" stack Dify+n8n+2Chat/90min a "WhatsApp AI Autopilot™ €17" stack n8n+Evolution API+Claude Code/75min) solo su 4 template HTML e 4 JSON di contenuto, lasciando fuori scope 9 file `content/*.json` con la stessa incoerenza tecnica e il lavoro completato ma non pushato. Un grep esaustivo lanciato per verificare la chiusura ha inoltre scoperto un residuo non previsto dal brief: un box "stack tecnico" (Dify/2Chat) hardcoded direttamente in `template-a.html` e `template-c.html`, quindi presente su tutte le pagine Cat. A/C generate — non solo sui 9 file segnalati.

### Il Pivot Architetturale (Root Cause Analysis)

- **Prima:** il rename di prodotto richiedeva editare a mano 4 template HTML (CTA URL/testo duplicato 4 volte) più un numero di JSON per-pagina non tracciato in modo esaustivo — nessun controllo strutturale garantiva che un grep negativo sul vecchio nome fosse davvero a zero occorrenze.
- **Dopo:** il CTA (URL + due varianti di testo) vive in un'unica fonte, `content/_cta.json`, iniettata da `build.py` in ogni pagina; e `futurelens-seo/CLAUDE.md` ha ora un Rename Verification Gate esplicito che impone un grep su **entrambe** le categorie di file (JSON per-pagina e HTML template condiviso) prima di dichiarare un rename chiuso.
- **Perché funziona:** il gate stesso, applicato subito dopo averlo scritto, ha trovato in tempo reale il residuo nei template che il brief precedente non aveva previsto — la regola non è teorica, si è validata nella stessa sessione in cui è stata introdotta.

### Il Meccanismo Cambiato

- **Prima:** CTA hardcoded in 4 punti per template × 4 template = 8 stringhe da mantenere sincronizzate a mano ad ogni cambio di prezzo/nome/URL.
- **Dopo:** `build.py` carica `content/_cta.json` e lo fonde nel dizionario di replacements comune a tutti i tipi di template (`{{CTA_URL}}`, `{{CTA_TEXT_HEADER}}`, `{{CTA_TEXT_MAIN}}`) — un cambio futuro tocca un solo file di config, zero righe di HTML.
- **Perché funziona:** separa dato (prodotto/prezzo/URL) da presentazione (markup del bottone), lo stesso principio già in uso per tutto il resto del contenuto per-pagina via placeholder — il CTA era l'unica eccezione rimasta hardcoded.

### Come è Stato Usato Claude Code

Il lavoro meccanico e ben specificato (leggere 9 JSON per intero e riscrivere le sezioni tecniche mantenendo stile e struttura, poi validare con `build.py`) è stato delegato a un agente in background con un prompt che includeva il pattern di riferimento esatto (i due file già corretti in ENTRY_004) e il criterio di validazione (build senza warning). L'agente ha fatto un secondo giro di grep per beccare stringhe residue mancate al primo passaggio — comportamento non richiesto esplicitamente nel prompt ma coerente con l'istruzione di verificare zero warning. Il lavoro architetturale (design del pattern CTA, scrittura del gate, applicazione del gate che ha trovato il gap nei template) è stato fatto in sessione principale, non delegato — richiedeva di leggere `build.py` per capire dove agganciare l'injection e di decidere lo schema dei placeholder insieme all'utente prima di implementare.

### Session Quality

- **Task nella sessione:** 5 (push lavoro pregresso, riscrittura 9 JSON via agente, refactor CTA data-driven, scrittura Rename Verification Gate, fix del residuo template-a/c trovato applicando il gate) + setup di questo journal come coda
- **Qualità output:** Buona — ogni passaggio è stato chiuso con una verifica esplicita (grep esaustivo a zero occorrenze, build senza warning su tutte le pagine, diff review prima del commit) invece di fidarsi del completamento dichiarato
- **Note:** nessun sacrificio di qualità percepito, ma la sessione ha toccato più aree indipendenti (contenuto, build system, governance CLAUDE.md) in sequenza — la delega in background del task 2 ha tenuto la sessione principale libera per il lavoro architetturale invece di sovrapporli
- **Raccomandazione:** pattern valido da ripetere — quando un brief ha un task meccanico ben specificato (leggi N file, riscrivi con pattern noto, valida con un comando) e uno o più task di design che richiedono conferma dell'utente, delegarli in parallelo invece che in sequenza

**Regola operativa:** sessioni con 3+ task complessi simultanei degradano la qualità dell'output. Preferire sessioni focalizzate: 1-2 task complessi per sessione. Se la sessione aveva sovraccarico — pianificare una sessione di review per verificare la qualità dei file prodotti.

### Ottimizzazione Architettura Claude

Il Rename Verification Gate aggiunto a `futurelens-seo/CLAUDE.md` è un guardrail testato nella stessa sessione: applicato subito dopo la scrittura, ha trovato un gap reale (stack tecnico hardcoded nei template) che sarebbe rimasto silenzioso fino al prossimo cambio di prodotto. Regola generale per progetti con contenuto ibrido (dati per-pagina + template condiviso): un grep di verifica rename deve sempre coprire entrambe le categorie di file, mai fermarsi al primo gruppo che restituisce risultati.

### Il "Takeaway" per il Mercato

> "Un rename di prodotto sembra chiuso quando il grep sul contenuto torna pulito — finché non controlli anche il template che genera quel contenuto, e trovi che il vecchio nome viveva lì da mesi, invisibile a ogni verifica precedente."

### Il "Takeaway" per Chi Usa Claude Code

> "Scrivere una regola di verifica (il gate) e applicarla subito nella stessa sessione, invece di lasciarla come promessa per la prossima volta, è l'unico modo per sapere se funziona davvero — in questo caso ha trovato un gap reale al primo utilizzo."

### Artefatti Prodotti

- `content/agente-ai-whatsapp.json`, `agente-whatsapp-accademie-digitali.json`, `agente-whatsapp-coach-high-ticket.json`, `agente-whatsapp-consulenti.json`, `agente-whatsapp-formatori.json`, `appointment-setting-ai-italia.json`, `lead-whatsapp-senza-risposta.json`, `perdo-clienti-whatsapp.json`, `riduzione-no-show-appuntamenti.json` — stack tecnico riscritto
- `content/_cta.json` — nuova fonte unica per URL/testo CTA
- `build.py` — funzione `load_cta()` + injection nei replacements
- `template-a.html`, `template-c.html`, `template-d.html`, `template-g.html` — CTA convertito a placeholder; `template-a.html`/`template-c.html` anche fix box "stack tecnico"
- `CLAUDE.md` — sezione Rename Verification Gate + doc pattern CTA data-driven + blocco config `log-milestone`
- Tutte le 13 pagine in `Pagine/*/index.html` + `sitemap.xml` rigenerate
- 2 commit pushati su `main` (`396596a`, `4ef19f2`)
- Questo journal (`00_Build_in_Public/JOURNAL.md`), creato da zero per il progetto
