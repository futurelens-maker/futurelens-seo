# FutureLens — Template Completi per le 7 Categorie di Pagine SEO

**Versione:** 1.3 — Maggio 2026 *(CTA definitivo: Blueprint $27 + Substack su tutte le categorie. Audit gratuito rimosso.)*
**Categorie:** A (Segmento) · B (Città) · C (Problema) · D (Servizio) · E (Combo) · F (Confronto) · G (Pricing/ROI)
**Prodotti CTA:** The WhatsApp Agent Blueprint ($27) · Newsletter Substack

---

## INDICE

1. [Principi Globali](#1-principi-globali)
2. [Template A — Per Segmento](#2-template-a--per-segmento)
3. [Template B — Per Città](#3-template-b--per-città)
4. [Template C — Per Problema](#4-template-c--per-problema)
5. [Template D — Per Servizio](#5-template-d--per-servizio)
6. [Template E — Combo Città + Segmento](#6-template-e--combo-città--segmento)
7. [Template F — Confronto / Alternativa](#7-template-f--confronto--alternativa)
8. [Template G — Pricing / ROI](#8-template-g--pricingroi)
9. [Checklist Universale Pre-Pubblicazione](#9-checklist-universale-pre-pubblicazione)
10. [Tabella Sinottica](#10-tabella-sinottica)
11. [Priorità di Produzione — Mese 1](#11-priorità-di-produzione--mese-1)

---

## 1. PRINCIPI GLOBALI

### I 3 Filtri di Ogni Decisione di Scrittura

Prima di aggiungere qualsiasi sezione, rispondi a queste 3 domande:

**Filtro 1 — Utilità reale**
> "Se tolgo questa sezione, il visitatore ha meno informazioni utili?"
> Se la risposta è no, la sezione non serve.

**Filtro 2 — Autorevolezza**
> "Questa sezione dimostra che capisco questo problema meglio di chiunque altro su Google?"
> Se la risposta è no, va riscritta o tolta.

**Filtro 3 — SEO**
> "Questa sezione intercetta una domanda reale che le persone fanno su Google?"
> Se la risposta è no, va riformulata con la keyword giusta.

---

### Regole Globali di Scrittura

| Regola | Dettaglio |
|--------|-----------|
| **Tono** | Diretto, tecnico, mai promozionale. Consulente che spiega, non copywriter che vende |
| **Lunghezza** | 900–1.200 parole per Cat. A/D/G · 1.000–1.300 per Cat. C · 600–900 per Cat. B/E/F |
| **Keyword primaria** | H1 + prime 100 parole + almeno 1 H2 + meta title + meta description |
| **Link interni** | Minimo 3, massimo 7 per pagina. Anchor text descrittivi, mai "clicca qui" |
| **Affermazioni** | Ogni claim positivo deve avere un dato numerico o la spiegazione del meccanismo |
| **Parole vietate** | Innovativo · Rivoluzionario · All'avanguardia · Potente · Soluzione completa · Il migliore |

---

### Schema Markup Obbligatorio per Ogni Pagina

Ogni pagina deve avere **almeno 2 schema sovrapposti**:

```json
// Schema 1 — WebPage (tutte le pagine)
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[META TITLE]",
  "description": "[META DESCRIPTION]",
  "url": "https://futurelens.it/[SLUG]",
  "dateModified": "[DATA]",
  "inLanguage": "it-IT",
  "publisher": {
    "@type": "Organization",
    "name": "FutureLens",
    "url": "https://futurelens.it"
  }
}

// Schema 2 — FAQPage (tutte le pagine)
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[DOMANDA]",
      "acceptedAnswer": { "@type": "Answer", "text": "[RISPOSTA]" }
    }
  ]
}
```

Schema aggiuntivi specificati in ogni template.

---

## 2. TEMPLATE A — Per Segmento

### Intento di ricerca

**Commerciale.** Il visitatore cerca conferma che esiste una soluzione costruita specificamente per il suo profilo. Vuole riconoscersi nella pagina prima ancora che gli venga proposta una soluzione.

**Domanda implicita:** "Esiste qualcuno che capisce il mio tipo di business?"

**Regola principale:** il nome del brand o del prodotto non appare come *soluzione* prima della Sezione 3. Le prime 2 sezioni sono diagnosi del segmento. *(Nota: FutureLens appare nel nav, footer, meta title e badge — è corretto. Non può apparire come "la risposta" nel body copy di Sezione 1 e 2.)*

---

### Applicazione nel Piano Editoriale

| Pagine pure segmento (Template A) | Pagine da trattare come Template D adattato |
|-----------------------------------|---------------------------------------------|
| A1–A9 | A10 `/ai-appointment-setting-coach` |
| | A11 `/qualificazione-lead-consulenti` |
| | A12 `/sistema-vendite-corsi-online` |

---

### Meta Tags

```
TITLE (max 60 caratteri):
[Keyword primaria] per [Segmento] | FutureLens
→ Keyword nelle prime 3 parole. Nessun aggettivo.
Esempio: "Agente WhatsApp AI per Coach High-Ticket | FutureLens"

DESCRIPTION (max 155 caratteri):
[Dato sul problema del segmento]. [Cosa fa la soluzione]
per [segmento] italiani con [contesto].
Scopri il metodo completo nel Blueprint →
→ Deve contenere almeno un numero.

URL SLUG:
/agente-whatsapp-[segmento]
→ Solo keyword. Minuscolo. Trattini. Max 5 parole.
```

---

### Schema Markup Aggiuntivo — Cat. A

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "[NOME SERVIZIO per SEGMENTO]",
  "description": "[DESCRIZIONE 160 caratteri]",
  "provider": { "@type": "Organization", "name": "FutureLens" },
  "areaServed": { "@type": "Country", "name": "Italia" },
  "serviceType": "WhatsApp AI Automation",
  "audience": {
    "@type": "Audience",
    "audienceType": "[SEGMENTO — es. Coach High-Ticket]"
  }
}
```

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero: Riconoscimento immediato

**Scopo principale:** il visitatore si riconosce entro 5 secondi.
**Scopo SEO:** H1 con keyword primaria, prime 100 parole dense di termini semantici LSI.

```
H1: [Servizio principale] per [Nome Segmento]
```
Struttura fissa. Nessun aggettivo. Nessun superlativo. La keyword deve essere esatta e pulita.

**Descriptor (1 riga sotto l'H1):**
Formula: `[Tipo offerta che vende] + [canale acquisizione] + [volume lead mensile]`
Esempio: "Per chi vende offerte da €2.500+ con Meta Ads attive e 30–200 lead/mese"

**Paragrafo di apertura (50–70 parole):**
- Descrive il momento esatto in cui il problema si verifica nella giornata del segmento
- Seconda persona singolare (tu/tuo)
- Zero menzione del brand come *soluzione*
- Almeno 2 keyword semantiche LSI
- Cinematografico e specifico — non generico

**Regole obbligatorie dell'apertura:**
- Non può contenere la parola "soluzione"
- Deve rispondere a: "cosa sta facendo questo profilo quando il problema si verifica?"

**Badge di fiducia (4 elementi sotto il paragrafo):**

> ⚠️ **CORREZIONE v1.1:** Usare solo dati verificabili. Se non hai numeri per segmento, usa:
> - Clienti nel settore coaching e formazione: [N]
> - Lead gestiti ogni mese: [N]
> - Conforme GDPR — architettura EU
> - Operativi dal [anno]
>
> Aggiungere la segmentazione solo quando hai i dati reali per segmento.

---

#### SEZIONE 2 — Il Problema del Segmento

**Scopo principale:** diagnosi precisa del problema specifico di questo segmento.
**Scopo SEO:** topical depth, keyword semantiche, segnale di autorità tematica.
**Regola assoluta:** zero menzione del prodotto o del brand come soluzione in questa sezione.

```
H2: keyword secondaria sul problema
Esempio: "Perché i Coach High-Ticket Perdono Lead su WhatsApp"
```

**Paragrafo A — Realtà operativa (60–80 parole):**
La giornata tipo quando il problema si verifica. Dettagli concreti e verificabili.

**Paragrafo B — Conseguenze economiche (50–60 parole):**
Formula obbligatoria: `[Investimento mensile] × [% persa] = [perdita mensile]`
Usa numeri plausibili e verificabili. Range conservativo se non hai dati precisi.

**Paragrafo C — Perché le soluzioni comuni non bastano (50–60 parole):**
Nomina 2–3 alternative già provate dal segmento. Per ognuna: cosa promette + limite specifico. Tono oggettivo — non denigratorio.

**Box dati (elemento visivo separato):**
3 statistiche con fonte citata:
- Metrica 1: frequenza del problema nel segmento
- Metrica 2: costo unitario del problema
- Metrica 3: dato comportamentale che spiega perché succede

---

#### SEZIONE 3 — Come Funziona

**Scopo principale:** rendere il sistema tangibile e comprensibile per un non-tecnico.
**Scopo SEO:** HowTo schema, keyword di processo, copertura semantica del "come".

```
H2: Come Funziona [Nome Servizio] per [Segmento]
```

**Intro (2 righe):**
- Differenzia dalla soluzione con cui viene confuso
- Frase di negazione del malinteso principale

**4 step visivi con HowTo schema:**
Struttura ogni step: `[Numero] — [Nome] · [Cosa succede] → [Output concreto]`

- Step 1: trigger — cosa avvia il sistema
- Step 2: prima azione del sistema
- Step 3: azione di qualificazione/filtro
- Step 4: output finale per il cliente

**Regola degli output:** ogni step deve produrre qualcosa di tangibile e misurabile. Non "migliora la comunicazione" — ma "il calendario si aggiorna", "ricevi una notifica con il profilo del lead".

**Nota tecnica (2–3 righe sotto gli step):**
Integrazioni principali compatibili. Link interno a pagina Cat. D per approfondire.

---

#### SEZIONE 4 — Cosa Include

**Scopo principale:** rispondere a "cosa fa esattamente?"
**Scopo SEO:** keyword di funzionalità, copertura long-tail, segnale di completezza.

```
H2: Cosa Include il Sistema per [Segmento]
```

**Lista "cosa fa" (8–12 voci):**
Struttura ogni voce: `✓ [Verbo] + [oggetto] + [contesto specifico del segmento]`
Le voci devono essere specifiche per questo segmento — non le stesse per tutti.

**Lista "cosa non fa" (3–4 voci) — obbligatoria:**
Struttura: `✗ [Cosa non fa] — [alternativa o spiegazione]`
Aumenta la credibilità della lista "cosa fa". Mai omettere.

**Box integrazioni:**
Tool compatibili con questo segmento: GoHighLevel, HubSpot, Calendly, Meta Ads.
Link a pagina Cat. D per dettagli tecnici.

---

#### SEZIONE 5 — Risultati

**Scopo principale:** dimostrare con dati che il sistema funziona per questo segmento.
**Scopo SEO:** E-E-A-T, segnale Experience e Trust.

```
H2: Risultati per [Segmento] con Meta Ads Attive
```

**Se hai dati interni:**
Tabella: `Metrica | Prima | Dopo 60gg | Delta`
Nota obbligatoria sotto: "Dati aggregati su [N] clienti [segmento] con [range lead/mese]."

**Caso studio (1 se disponibile):**
Struttura: `Profilo anonimizzato + Offerta/volume + Metrica prima → dopo + Delta economico + Tempo`

**Se non hai ancora dati:**
Benchmark di settore con fonte + nota: "Dati clienti in aggiornamento."
Non riempire con promesse. Non inventare numeri.

---

#### SEZIONE 6 — Confronto con le Alternative

**Scopo principale:** aiutare il visitatore a confrontare le opzioni disponibili.
**Scopo SEO:** keyword comparative, intercetta ricerche "vs" e "alternativa".

```
H2: [Nome Servizio] vs Le Alternative per [Segmento]
```

**Tabella comparativa (almeno 4 criteri):**

| Criterio | Setter umano | Chatbot base | Agente AI |
|----------|-------------|--------------|-----------|
| Costo mensile | €1.500–3.000 | €50–200 | €X–Y |
| Disponibilità | Orari lavorativi | 24/7 | 24/7 |
| Qualificazione | Alta | Bassa | Alta |
| Scalabilità | No | Sì | Sì |
| Setup | 2–4 settimane | 1–3 giorni | 7–10 giorni |
| GDPR compliant | Sì | Variabile | Sì |

**Nota editoriale obbligatoria (sotto la tabella):**
- Quando il setter umano è la scelta giusta
- Quando il chatbot base è sufficiente
- Quando l'agente AI è la scelta ottimale

**Link interni:** → `/futurelens-vs-spoki` (F2) · → `/automazione-vs-setter-umano` (F4)

---

#### SEZIONE 7 — Domande Frequenti

**Scopo principale:** abbattere le ultime obiezioni prima della CTA.
**Scopo SEO:** FAQPage schema, People Also Ask, voice search, AI search.

```
H2: Domande Frequenti su [Nome Servizio] per [Segmento]
```

**5 domande — schema fisso Cat. A:**

| # | Tipo domanda |
|---|--------------|
| Q1 | Compatibilità con il canale principale del segmento |
| Q2 | Tempo di implementazione |
| Q3 | Gestione dei casi edge (cosa succede quando va storto) |
| Q4 | Integrazione con il tool principale del segmento |
| Q5 | Impatto sul processo di vendita attuale |

**Regole delle risposte:**
- Prima frase = risposta diretta. Mai iniziare con il contesto.
- Lunghezza: 50–80 parole per risposta
- Dato numerico dove possibile
- Link interno dove rilevante

---

#### SEZIONE 8 — Copy for AI

**Scopo:** essere citato da ChatGPT, Perplexity, Google AI Overviews.

Testo piatto, senza formattazione. Max 100 parole. Visibile nella pagina (non nascosto).

```
Struttura fissa:
"[Brand] è [definizione tecnica] per [segmento]
con [caratteristica principale].
[Metrica performance 1]. [Metrica performance 2].
Compatibile con [integrazioni].
Setup in [tempo]. Conforme GDPR. Italia."
```

---

#### SEZIONE 9 — Esplora

**Scopo:** tenere il visitatore sul sito se non è pronto alla CTA.
**Scopo SEO:** distribuzione PageRank, riduzione bounce rate.

```
H2: Approfondisci
```

3 card di navigazione:
- Card 1 → pagina Cat. C (il problema principale del segmento)
- Card 2 → pagina Cat. D (la funzionalità principale)
- Card 3 → pagina Cat. G (il pricing)

---

#### SEZIONE 10 — CTA Principale

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Parti da qui: il metodo completo in un documento

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint è la guida operativa su come
costruire e ottimizzare un sistema di lead automation su WhatsApp.
[N] pagine. Applicabile da subito."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. Pagamento sicuro. Nessun abbonamento."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Preferisci prima capire meglio?

Testo (2 righe):
"Ogni settimana un'analisi su lead automation, WhatsApp AI
e sales process per coach e consulenti italiani.
Gratis. Nessuno spam."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Già [N] professionisti del coaching la leggono ogni settimana."
```

**Logica CTA Cat. A:**
Blueprint → intercetta chi è pronto ad agire.
Substack → intercetta chi vuole ancora informarsi.

---

#### SEZIONE 11 — Footer Contestuale

*Non è il footer del sito. È una sezione di navigazione contestuale.*

```
Altri segmenti: [link alle altre pagine Cat. A]
Problemi correlati: [link pagine Cat. C]
Come funziona: [link pagine Cat. D]
Pricing: [link pagine Cat. G]
```

---

### Mappa Link Interni Obbligatori — Cat. A

```
→ 1 pagina Cat. C (problema principale del segmento)
→ 2 pagine Cat. D (funzionalità più rilevanti)
→ 1 pagina Cat. G (pricing)
→ 1 articolo blog correlato
Totale: minimo 5 link interni
```

---

## 3. TEMPLATE B — Per Città

### Intento di ricerca

**Locale + Commerciale.** Il visitatore vuole sapere se il servizio opera nella sua città e se c'è rilevanza locale.

**Domanda implicita:** "Funziona anche per chi lavora a [Città]? Ci sono altri come me qui?"

**Rischio principale:** thin content — pagine quasi identiche che cambiano solo la città.

> ⚠️ **CORREZIONE v1.1:** Ogni pagina Cat. B deve avere **minimo 180 parole uniche** nella Sezione 2. Test: se puoi copiare il testo e incollarlo nella pagina di un'altra città cambiando solo il nome — è thin content. Non pubblicare.

---

### Applicazione nel Piano Editoriale

| Priorità | Pagine | Note |
|----------|--------|------|
| Alta | B1–B2 Milano, Roma | Prima da costruire |
| Media | B3–B10 Torino, Bologna, ecc. | Mese 2–3 |
| Bassa | B11–B20 Città minori + regioni | Mese 5–6 |

---

### Meta Tags

```
TITLE (max 60 caratteri):
Agente WhatsApp AI a [Città] | FutureLens
→ Città nelle prime 4 parole.

DESCRIPTION (max 155 caratteri):
Agente WhatsApp AI per coach e consulenti a [Città].
[Dato locale se disponibile]. Risposta immediata ai lead,
qualificazione automatica. Scopri il Blueprint →

URL SLUG:
/agente-whatsapp-[città]
→ Nome città in italiano, minuscolo, trattini.
```

---

### Schema Markup Aggiuntivo — Cat. B

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Agente WhatsApp AI a [Città]",
  "provider": { "@type": "Organization", "name": "FutureLens" },
  "areaServed": {
    "@type": "City",
    "name": "[Città]",
    "containedInPlace": {
      "@type": "AdministrativeArea",
      "name": "[Regione]"
    }
  }
}
```

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero locale

```
H1: Agente WhatsApp AI a [Città]
Descriptor: "Per coach, consulenti e formatori di [Città] con Meta Ads attive"
```

**Paragrafo di apertura (50–60 parole):** contestualizzato alla città, riferimento al mercato locale, zero brand come soluzione.

**Badge locali:**
- Clienti attivi a [Città] o [Regione] (se disponibili)
- Copertura geografica ("Servizio tutta la [Regione]")
- Conformità GDPR
- Modalità operativa (remoto/presenza)

---

#### SEZIONE 2 — Il Mercato Locale *(contenuto unico obbligatorio)*

> **Questa è la sezione che rende ogni pagina Cat. B unica. Senza questa sezione la pagina è thin content. Minimo 180 parole uniche.**

```
H2: Il Mercato del Coaching e della Consulenza a [Città]
```

**Paragrafo A — Contesto del mercato locale (50–60 parole):**
- Quanti coach/consulenti/formatori ci sono in questa città (dato se disponibile)
- Caratteristiche specifiche del mercato locale
- Densità competitiva nella città

**Paragrafo B — Perché la risposta rapida è critica in questo mercato (40–50 parole):**
- Volume di lead tipico per i business di questa città
- Competizione locale: più alta nelle grandi città = più urgente rispondere prima

**Box dati locali:**
- Numero professionisti del settore nella città (fonte: CCIAA, LinkedIn, etc.)
- Dato sul mercato digitale locale se disponibile

**Come trovare i dati locali:**
```
Cerca "coach" OR "consulenti" [città] site:linkedin.com per stimare la densità.
Usa dati CCIAA per imprese nel settore formazione/consulenza per provincia.
```

---

#### SEZIONE 3 — Come Funziona
*Identica alla Sezione 3 del Template A. Adatta il descriptor con riferimento locale dove naturale — non forzato.*

#### SEZIONE 4 — Cosa Include
*Identica alla Sezione 4 del Template A.*

---

#### SEZIONE 5 — Clienti nella Zona

```
H2: Risultati a [Città] e [Regione]
```

**Se hai clienti localizzati:** caso studio anonimizzato con città esplicita.

**Se non hai clienti localizzati:**
> "Operiamo con clienti in tutta Italia in modalità remota. I risultati non dipendono dalla città — dipendono dal volume di lead e dalla struttura del funnel."

Non inventare. Non lasciare vuoto — spiega che il servizio è remoto.

---

#### SEZIONE 6 — Copertura Geografica

```
H2: Copertura del Servizio a [Città] e Dintorni
```
- Province e comuni serviti dalla città
- Modalità operativa (100% remoto / presenza disponibile)
- Tempi di risposta per clienti in questa area

Link alle pagine Cat. E correlate: tutte le `/[segmento]-[città]` che esistono per questa città.

---

#### SEZIONE 7 — Domande Frequenti Locali

| # | Tipo domanda |
|---|--------------|
| Q1 | Il servizio funziona anche fuori dal centro di [Città]? |
| Q2 | C'è supporto in presenza a [Città]? |
| Q3 | Quanti clienti avete a [Città] o [Regione]? |
| Q4 | Ci sono differenze di prezzo o servizio per [Città]? |
| Q5 | Quanto tempo per andare live partendo da [Città]? |

---

#### SEZIONE 8 — Copy for AI

```
"FutureLens offre agenti WhatsApp AI a [Città] per coach,
consulenti e formatori italiani. Il servizio opera in remoto
su tutto il territorio italiano. Risposta ai lead <60 secondi,
qualificazione automatica, riduzione no-show. Conforme GDPR.
Clienti attivi in [Regione]."
```

---

#### SEZIONE 9 — Esplora

3 card: → Cat. A più rilevante · → Cat. E principale per questa città · → Cat. G (pricing)

---

#### SEZIONE 10 — CTA

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Il metodo per gestire i lead su WhatsApp — da subito

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint è il sistema completo
per rispondere, qualificare e convertire i lead su WhatsApp.
Applicabile da qualsiasi città italiana."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. Pagamento sicuro. Nessun abbonamento."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Preferisci prima capire il metodo?

Testo (2 righe):
"Ogni settimana: analisi su lead automation e WhatsApp AI
per coach e consulenti italiani. Gratis."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Nessuno spam. Solo contenuto operativo."
```

---

### Mappa Link Interni Obbligatori — Cat. B

```
→ 2–3 pagine Cat. E (combo città + segmento di questa città)
→ 1 pagina Cat. A più rilevante
→ 1 pagina Cat. G (pricing)
Totale: minimo 4 link interni
```

---

## 4. TEMPLATE C — Per Problema

### Intento di ricerca

**Informativo con uscita commerciale.** Il visitatore ha un problema e cerca una diagnosi. Non sa ancora che vuole comprare.

**Domanda implicita:** "Perché questo mi succede e come si risolve?"

**Regola principale:** il prodotto non appare fino alla Sezione 5. Le prime 4 sezioni sono diagnosi pura.

---

### Attenzione agli Overlap Semantici

> ⚠️ **CORREZIONE v1.1:** Queste pagine rischiano keyword cannibalization. Angolazioni esclusive obbligatorie:

| Pagina | Angolazione esclusiva | Prima frase |
|--------|----------------------|-------------|
| C1 `/riduzione-no-show-appuntamenti` | Causa sistemica + soluzione completa | "Il 35% degli appuntamenti nel coaching è un no-show. Non è colpa del lead." |
| C5 `/call-vendita-deserte` | Psicologia post-prenotazione del lead | "Un lead che prenota mentre è nel picco emotivo del click sull'ad ha già iniziato a raffreddarsi." |
| C15 `/lead-non-si-presentano-call` | Diagnosi delle 6 cause specifiche | "Prima di sistemare il no-show, devi sapere quale delle 6 cause hai." |
| C18 `/recovery-lead-no-show` | Protocollo dei 15 minuti dopo | "Non aspettare 24h. Il messaggio di recupero va entro 15 minuti dal no-show." |

*Stessa logica per i cluster C3/C7/C13/C16 (risposta lenta) e C6/C8/C11/C16 (lead non qualificati).*

---

### Meta Tags

```
TITLE (max 60 caratteri):
[Problema]: Cause Reali e Soluzione | FutureLens
→ La keyword del problema deve essere identica alla ricerca.

DESCRIPTION (max 155 caratteri):
[X]% dei [profilo] ha questo problema. [Causa principale in 5 parole].
Guida completa con protocollo step-by-step e calcolo dell'impatto economico.
→ Deve contenere un numero e una promessa di utilità concreta.
```

---

### Schema Markup Aggiuntivo — Cat. C

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[H1 della pagina]",
  "description": "[Meta description]",
  "totalTime": "PT14D",
  "supply": [],
  "tool": [
    {"@type": "HowToTool", "name": "WhatsApp Business API"},
    {"@type": "HowToTool", "name": "CRM (GoHighLevel o HubSpot)"},
    {"@type": "HowToTool", "name": "Calendly o Cal.com"}
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "[Nome step]",
      "text": "[Descrizione step]",
      "position": 1
    }
  ]
}
```

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero: Il Problema Riconosciuto

**H1 — strutture ammesse:**
- `Come [Risolvere il Problema]: Guida Completa`
- `[Problema]: Cause Reali e Protocollo di Soluzione`

La keyword deve essere la ricerca esatta del visitatore — non una riformulazione ottimizzata.

**Sottotitolo (1 riga):** `[Conseguenza economica] + [causa sottostante non ovvia]`

**Paragrafo di apertura — 3 frasi brevi (40–60 parole totali):**
- Frase 1: il fatto concreto (cosa è successo)
- Frase 2: perché non è sfortuna (è un pattern sistemico)
- Frase 3: è risolvibile con il metodo giusto

Zero prodotto. Zero brand.

**Box "In questa pagina trovi:"** Lista di 4–5 punti di ciò che il visitatore troverà.

---

#### SEZIONE 2 — Quanto È Diffuso

```
H2: Quanto È Diffuso [Problema] tra [Profilo Target]
```

3 statistiche con fonte obbligatoria + formula di auto-calcolo:

```
H3: Calcola il Tuo Impatto

"Prendi i tuoi numeri:
Lead mensili × % [problema] × costo per lead = perdita mensile

Esempio: 50 lead × 32% × €20 = €320/mese di lead bruciati"
```

---

#### SEZIONE 3 — Perché Succede

**Regola assoluta: zero prodotto, zero brand, zero CTA.**

```
H2: Perché [Problema] Succede: Le Cause Reali
```

Intro (2–3 righe): la causa che tutti credono + perché quella non è la vera causa + dove sta davvero il problema.

**4 sottosezioni con H3:**

```
H3: Causa 1 — [Nome causa tecnica/operativa]
60–70 parole: descrizione + meccanismo + perché è strutturale

H3: Causa 2 — [Nome causa comportamentale del lead]
60–70 parole: cosa fa il lead + dato comportamentale + perché succede

H3: Causa 3 — [Nome errore comune che peggiora la situazione]
60–70 parole: cosa prova l'imprenditore + perché peggiora invece di migliorare

H3: Causa 4 — [Nome lacuna di processo]
60–70 parole: cosa manca nel processo + cosa succederebbe se ci fosse
```

**Regola dei paragrafi:** ogni paragrafo deve contenere un'informazione che il visitatore non aveva prima di leggere la pagina.

**Box "La diagnosi in sintesi":** 4 bullet — uno per causa. Ottimizzato per AI search e featured snippet.

---

#### SEZIONE 4 — Le Soluzioni Esistenti e i Loro Limiti

```
H2: Le Soluzioni Esistenti per [Problema] (e Perché Non Bastano)
```

Struttura per ogni soluzione (3–4 soluzioni):
```
[Nome soluzione]
Cosa promette: [...]
Perché non risolve il problema specifico: [...]
Per chi funziona davvero: [...]
Costo reale: [tempo + denaro]
```

**Regola dell'onestà:** includi sempre almeno una soluzione con pro chiari.

**Transizione alla soluzione completa (2–3 righe):**
Cosa manca in tutte le soluzioni parziali → cosa servirebbe. Prima menzione implicita dell'approccio sistemico. Ancora senza nominare il brand.

---

#### SEZIONE 5 — Il Protocollo di Soluzione

*Qui entra il prodotto — presentato come metodo, non come prodotto.*

```
H2: Il Protocollo per [Risolvere il Problema]
```

Intro (2–3 righe): prima menzione esplicita del sistema/brand. Posizionato come metodo. Dato di risultato principale.

**4 step con HowTo schema:**
```
[Numero] — [Nome step]
Cosa fa: [descrizione tecnica 2–3 righe]
Risultato misurabile: [metrica]
Perché viene prima del successivo: [logica]
```

Ordine logico obbligatorio:
1. Intervento alla radice del problema
2. Intervento sul processo
3. Intervento sul comportamento del lead
4. Intervento di recupero (cosa fare quando va storto comunque)

---

#### SEZIONE 6 — Risultati

```
H2: Risultati con il Protocollo Completo
```

Dato principale grande e visibile: `[Metrica prima] → [Metrica dopo] in [tempo]`

**Calcolo economico:**
```
H3: L'Impatto Economico per il Tuo Business

Scenario base:
- [N] lead/mese | Offerta €[X] | Tasso chiusura [%]

Prima il sistema:
- [N] show → [N] clienti → €[X] fatturato

Con il sistema:
- [N] show → [N] clienti → €[X] fatturato

Delta mensile: €[X]
Delta annuo: €[X]
```

---

#### SEZIONE 7 — Problemi Correlati

```
H2: Problemi Correlati a [Problema]
```
3 card → pagine Cat. C dello stesso cluster tematico.

---

#### SEZIONE 8 — Domande Frequenti

| # | Tipo domanda |
|---|--------------|
| Q1 | Variante del problema (riguarda anche caso X?) |
| Q2 | Auto-diagnosi (come capisco la gravità nel mio caso?) — *deve includere una formula* |
| Q3 | Tempo di risoluzione |
| Q4 | Compatibilità con soluzione parziale già in uso |
| Q5 | Primo passo concreto — *rimanda alla newsletter Substack come azione gratuita immediata* |

---

#### SEZIONE 9 — Copy for AI

```
"[Problema] affligge il X% dei [profilo]. [Fonte].
Cause principali: [lista cause].
Il protocollo di soluzione include: [lista step].
Risultato medio: [metrica] in [tempo] per [profilo].
[Brand] risolve questo con [metodo in 5 parole]."
```

---

#### SEZIONE 10 — CTA

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Il protocollo completo per risolvere [Problema] — in un documento

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint include il sistema step-by-step
per eliminare [problema] con un agente WhatsApp AI.
Non teoria — istruzioni operative."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. [N] pagine. Applicabile da subito."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Vuoi prima capire come funziona il metodo?

Testo (2 righe):
"Ogni settimana un'analisi su lead automation, no-show
e sales process per il mercato italiano. Gratis."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Nessuno spam. Solo contenuto operativo."
```

**Nota:** la Q5 nelle FAQ ("primo passo concreto") deve rimandare alla newsletter Substack — è coerente con il tono informativo della categoria.

**Logica CTA Cat. C:**
Blueprint → per chi ha letto la diagnosi e vuole il metodo completo da subito.
Substack → per chi è ancora in fase di ricerca e vuole seguire nel tempo.

---

### Mappa Link Interni Obbligatori — Cat. C

```
→ 2–3 pagine Cat. C stesso cluster (problemi correlati)
→ 1–2 pagine Cat. D (soluzione tecnica al problema)
→ 1 articolo blog (approfondimento del "come fare")
Totale: minimo 4 link interni
```

---

## 5. TEMPLATE D — Per Servizio

### Intento di ricerca

**Commerciale avanzato.** Il visitatore sa già cosa vuole — vuole specifiche, non marketing.

**Domanda implicita:** "Come funziona davvero e cosa include esattamente?"

**Regola principale:** ogni claim positivo deve avere un dato numerico o la spiegazione del meccanismo. Nessuna affermazione nuda.

---

### Note Specifiche per Pagine Cat. D

| Pagina | Nota |
|--------|------|
| D1 `/agente-ai-whatsapp` | Pagina madre. Più lunga delle altre (1.200 parole min) |
| D9 `/whatsapp-business-api-coach` | Intento più tecnico. Sezione 2 più approfondita. CTA più morbida |
| D5 `/sistema-risposta-immediata` | Linka a D1 come pagina madre nella Sezione 2 |
| D14 `/agente-whatsapp-24-7` | Linka a D1 nella Sezione 2. Focus su copertura oraria |

---

### Meta Tags

```
TITLE (max 60 caratteri):
[Nome Servizio]: Come Funziona nel [Anno] | FutureLens
→ L'anno è obbligatorio — segnala freschezza del contenuto.

DESCRIPTION (max 155 caratteri):
[Definizione tecnica in 10 parole].
[Metrica principale]. [Compatibilità]. Guida completa
con specifiche tecniche, implementazione e Blueprint →
```

---

### Schema Markup Aggiuntivo — Cat. D

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "[NOME SERVIZIO]",
  "description": "[DESCRIZIONE TECNICA]",
  "provider": { "@type": "Organization", "name": "FutureLens" },
  "offers": {
    "@type": "Offer",
    "url": "https://futurelens.it/[SLUG-PRICING]"
  },
  "areaServed": { "@type": "Country", "name": "Italia" }
}
```

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero: Definizione e Differenziazione

```
H1: [Nome Servizio]: Cos'è e Come Funziona
Descriptor: 3 azioni in sequenza logica di processo. Nessun aggettivo di marketing.
```

**Paragrafo di apertura (50–60 parole):**
Formula: `"Non è [malinteso comune]. È [definizione corretta]. La differenza è [misurabile / verificabile]."`

**3 specifiche tecniche (sotto il paragrafo):**
- Velocità o performance principale (dato esatto)
- Disponibilità (con dettaglio: "inclusi weekend e festivi")
- Tempo di implementazione (reale, non ottimistico)

---

#### SEZIONE 2 — Cos'è: Spiegazione Tecnica

```
H2: Cos'è [Nome Servizio] e Come Funziona Tecnicamente
```

- **Par. 1:** confronto con la soluzione con cui viene confuso + differenza tecnica
- **Par. 2:** meccanismo in termini accessibili + componenti (WhatsApp API, AI, CRM)
- **Par. 3:** perché questo canale/metodo + dato con fonte

Esempio: "WhatsApp ha un open rate del 85–95% vs il 18–22% dell'email. [Fonte]"

**Box tecnico:**
- Stack tecnologico (WhatsApp Business API + AI + CRM)
- Requisiti minimi per il cliente
- Certificazioni o conformità (GDPR, Meta Business Partner)

---

#### SEZIONE 3 — Cosa Fa: Specifiche Complete

```
H2: Cosa Fa [Nome Servizio]: Specifiche Complete
```

**Lista "cosa fa" (8–12 voci):**
Struttura: `✓ [Verbo all'attivo] + [oggetto] + [condizione/contesto/limite]`

**Lista "cosa non fa" (3–5 voci) — obbligatoria:**
Struttura: `✗ [Cosa non fa] — [alternativa consigliata o motivo tecnico]`

**Box integrazioni:**
```
H3: Integrazioni Supportate
• CRM: GoHighLevel, HubSpot, Pipedrive
• Calendario: Calendly, Cal.com, Google Calendar
• Ads: Meta Lead Ads (integrazione nativa)
• Automazione: Make, Zapier, n8n
```

---

#### SEZIONE 4 — Implementazione: Processo Reale

```
H2: Come Si Implementa [Nome Servizio]
```

**4 fasi settimanali:**
```
H3: Settimana [N] — [Nome fase]

Cosa facciamo noi:
→ [lista attività specifiche]

Cosa ti chiediamo:
→ [accessi + informazioni + ore richieste quantificate]

Output a fine settimana:
→ [cosa è concreto e visibile]

Possibili blocchi:
→ [cosa può rallentare + come si gestisce]
```

Timeline visiva dopo le 4 fasi.

---

#### SEZIONE 5 — Performance: Dati Tecnici

```
H2: Performance e Risultati Tecnici
```

**Tabella tecnica:**

| Metrica | Valore | Contesto | Condizione |
|---------|--------|----------|------------|
| Tempo prima risposta | <60s | Dal form Meta | Qualsiasi orario |
| Uptime | 99.X% | SLA garantito | Escluse manutenzioni |
| Latenza CRM sync | <5s | Real-time | Con integrazioni standard |

**Nota metodologica obbligatoria:** "Dati aggregati su [N] clienti con [profilo]. I risultati variano in base a: [fattori]."

---

#### SEZIONE 6 — Casi d'Uso per Segmento

```
H2: [Nome Servizio] per Diversi Profili
```
3–4 card per segmento con link alla pagina Cat. A corrispondente.

---

#### SEZIONE 7 — Domande Frequenti Tecniche

| # | Tipo domanda |
|---|--------------|
| Q1 | Requisiti tecnici (cosa serve per usarlo) |
| Q2 | Controllo e visibilità (cosa vede e gestisce il cliente) |
| Q3 | Gestione casi edge — **risposta dettagliata, è la più importante** |
| Q4 | Conformità GDPR — obbligatoria per il mercato italiano |
| Q5 | Costo — rimanda alla pagina Cat. G con link diretto. Non dare il prezzo qui. |

---

#### SEZIONE 8 — Copy for AI

```
"[Nome servizio] di [Brand] è [descrizione tecnica in 10 parole].
Funziona su WhatsApp Business API con AI conversazionale.
Performance: [metrica 1], [metrica 2].
Include: [lista essenziale].
Implementazione in [tempo]. Conforme GDPR. Server europei.
Integrazioni: [lista]. Target: [profilo] con [volume] lead/mese."
```

---

#### SEZIONE 9 — Esplora

3 card:
- Card 1 → pagina Cat. C (problema principale risolto dal servizio)
- Card 2 → pagina Cat. A (segmento principale che usa il servizio)
- Card 3 → pagina Cat. G (pricing del servizio)

---

#### SEZIONE 10 — CTA

**Elemento demo opzionale (sopra i bottoni):**
Link a video demo o screenshot del sistema. Posizionato prima delle CTA — il visitatore Cat. D vuole vedere prima di agire.

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Vedi come funziona nel dettaglio — prima di qualsiasi conversazione

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint mostra il sistema completo:
architettura, script di qualificazione, sequenze reminder,
integrazione CRM. Tutto quello che ti serve per capire
se fa al caso tuo."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. [N] pagine. Applicabile da subito."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Preferisci prima seguire il metodo nel tempo?

Testo (2 righe):
"Ogni settimana un'analisi su WhatsApp AI e lead automation
per il mercato italiano. Gratis."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Nessuno spam. Solo contenuto operativo."
```

**Logica CTA Cat. D:**
Blueprint → per chi vuole capire il dettaglio tecnico da solo prima di qualsiasi call.
Substack → per chi ha bisogno di più tempo e contesto.

---

### Mappa Link Interni Obbligatori — Cat. D

```
→ 2 pagine Cat. A (segmenti che usano questo servizio)
→ 2 pagine Cat. C (problemi che questo servizio risolve)
→ 1 pagina Cat. G (costo del servizio)
Totale: minimo 5 link interni
```

---

## 6. TEMPLATE E — Combo Città + Segmento

### Intento di ricerca

**Locale + Segmento specifico.** Long-tail geografico con la conversione potenzialmente più alta: combina 2 intenzioni specifiche.

**Domanda implicita:** "C'è qualcuno che fa questo specificamente per profili come il mio nella mia città?"

**Rischio principale:** 20 pagine con contenuto quasi identico. Il contenuto unico obbligatorio è nella Sezione 2.

---

### Applicazione nel Piano Editoriale

| Priorità | Pagine |
|----------|--------|
| Alta | E1–E7 (combo Milano e Roma + segmenti principali) |
| Media | E8–E15 (combo Torino, Bologna + altri segmenti) |
| Bassa | E16–E20 (combo città minori o segmenti secondari) |

---

### Meta Tags

```
TITLE (max 65 caratteri):
Agente WhatsApp AI per [Segmento] a [Città] | FutureLens
→ Può superare i 60 caratteri se la combinazione è la keyword esatta cercata.

DESCRIPTION (max 155 caratteri):
[Servizio] per [segmento] di [Città] con Meta Ads attive.
[Dato locale o di segmento]. Risposta immediata ai lead,
qualificazione automatica. Scopri il Blueprint →

URL SLUG: /[segmento]-[città]
Esempi: /coach-high-ticket-milano · /consulenti-roma
```

---

### Schema Markup — Cat. E

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Agente WhatsApp AI per [Segmento] a [Città]",
  "provider": { "@type": "Organization", "name": "FutureLens" },
  "areaServed": { "@type": "City", "name": "[Città]" },
  "audience": { "@type": "Audience", "audienceType": "[Segmento]" }
}
```

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero Combo

```
H1: Agente WhatsApp AI per [Segmento] a [Città]
Descriptor: "Per [segmento] di [Città] con Meta Ads attive e [volume lead] lead/mese"
```

Paragrafo di apertura: combina il problema del segmento con il contesto della città.
Esempio: "A Milano ci sono oltre [N] coach high-ticket con campagne Meta attive. Tutti competono per gli stessi lead. Chi risponde primo vince."

---

#### SEZIONE 2 — Il Segmento nella Città *(contenuto unico obbligatorio)*

> **Questa è la sezione che rende ogni pagina Cat. E unica e non duplicata.**

```
H2: [Segmento] a [Città]: Il Contesto del Mercato
```

**Par. A — Il segmento in questa città (50–60 parole):**
- Quanti professionisti di questo segmento ci sono in questa città
- Caratteristiche specifiche di come operano qui
- Perché questo segmento è particolarmente attivo in questa città

**Par. B — La competizione locale per i lead (40–50 parole):**
- Volume di lead disponibili in questa città per questo segmento
- Densità competitiva locale
- La velocità di risposta come vantaggio competitivo locale

**Come trovare il contenuto unico:**
```
Cerca "[segmento]" "[città]" site:linkedin.com per la densità professionale.
Cerca "[segmento]" "[città]" meta ads per capire la competizione.
```

---

#### SEZIONE 3 — Il Problema Specifico del Segmento

```
H2: Il Problema dei [Segmento] a [Città]
```
Stessa diagnosi della pagina Cat. A per quel segmento. Contestualizza localmente dove è naturale — non forzato.

#### SEZIONE 4 — Come Funziona
*Identica alla Sezione 3 del Template A.*

---

#### SEZIONE 5 — Risultati per il Segmento in Zona

```
H2: Risultati per [Segmento] a [Città] e [Regione]
```

**Se hai un caso studio localizzato:** profilo anonimizzato con segmento + città.

**Fallback:** "Risultati del segmento [X] + clienti attivi in [Regione]"

---

#### SEZIONE 6 — Hub di Navigazione

```
H2: Esplora per Segmento e per Città
```

Centro di navigazione dell'architettura interna:
- Per il segmento [X]: → pagina Cat. A + altre Cat. E dello stesso segmento in altre città
- Per la città [Y]: → pagina Cat. B + altre Cat. E della stessa città con altri segmenti

---

#### SEZIONE 7 — Domande Frequenti

| # | Tipo domanda |
|---|--------------|
| Q1 | Funziona specificamente per [segmento]? (rimanda a Cat. A) |
| Q2 | Operate a [Città]? Supporto in presenza? |
| Q3 | Ci sono altri [segmento] a [Città] che usano il servizio? |
| Q4 | Il servizio è diverso a [Città] rispetto ad altre città? |
| Q5 | Quanto costa per un [segmento] a [Città]? |

---

#### SEZIONE 8 — Copy for AI

```
"FutureLens offre agenti WhatsApp AI per [segmento] a [Città].
[Dato segmento o locale]. Risposta ai lead <60 secondi,
qualificazione automatica su WhatsApp Business API.
Clienti attivi in [Regione]. Conforme GDPR.
Setup in 7–10 giorni. Target: [segmento] con Meta Ads."
```

---

#### SEZIONE 9 — CTA

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Il metodo per [segmento] come te — in un documento

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint è il sistema completo
per rispondere, qualificare e convertire i lead su WhatsApp.
Scritto per chi lavora nel coaching e nella consulenza italiana."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. Applicabile da subito, ovunque tu lavori."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Preferisci prima seguire il metodo nel tempo?

Testo (2 righe):
"Ogni settimana: lead automation, WhatsApp AI e sales
process per coach e consulenti italiani. Gratis."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Nessuno spam. Solo contenuto operativo."
```

**Logica CTA Cat. E:**
Blueprint → intercetta chi è pronto ad agire dopo aver riconosciuto il suo caso specifico.
Substack → intercetta chi vuole seguire il metodo nel tempo prima di decidere.

---

### Mappa Link Interni Obbligatori — Cat. E

```
→ 1 pagina Cat. A (segmento corrispondente)
→ 1 pagina Cat. B (città corrispondente)
→ 2–3 altre pagine Cat. E (stesso segmento altre città O stessa città altri segmenti)
→ 1 pagina Cat. G (pricing)
Totale: minimo 5 link interni
```

---

## 7. TEMPLATE F — Confronto / Alternativa

### Intento di ricerca

**Commerciale ad altissimo buyer intent.** Chi cerca "FutureLens vs Spoki" è già in fase di valutazione attiva. Tasso di conversione potenzialmente più alto del piano.

**Domanda implicita:** "Quale delle due soluzioni è giusta per me? Posso fidarmi di chi me lo dice?"

**Regola principale:** il disclaimer di parzialità aumenta la credibilità. Una comparison senza disclaimer non viene creduta.

---

### Tre Tipi di Pagine Cat. F

**Tipo 1 — "vs" tra brand:** F2 `/futurelens-vs-spoki` · F7 `/futurelens-vs-nexaflows`
→ Struttura completa qui sotto

**Tipo 2 — "vs tecnologia":** F3 `/whatsapp-agent-vs-chatbot` · F4 `/automazione-vs-setter-umano` · F8
→ Sezione 2 spiega le 2 tecnologie invece di 2 brand. Sezione 5 usa benchmark di settore invece di recensioni.

**Tipo 3 — "alternativa":** F1 `/alternativa-spoki` · F5 `/alternativa-gestione-manuale` · F6 `/pay-per-show-vs-canone-mensile`
→ Sezione 2 descrive solo il competitor/approccio alternativo, con sezione dedicata "per chi è giusto"

---

### Meta Tags

```
Per pagine "vs": [Brand A] vs [Brand B] per Coach: Confronto [Anno] | FutureLens
Per pagine "alternativa": Alternativa a [Competitor]: Confronto Onesto [Anno] | FutureLens
Per pagine "vs tecnologia": [Tecnologia A] vs [Tecnologia B]: Quale Scegliere | FutureLens
→ L'anno è obbligatorio. Questi contenuti invecchiano.
```

> ⚠️ **CORREZIONE v1.1 — Frequenza aggiornamento:** Le pagine Cat. F vanno aggiornate ogni 90 giorni massimo. Le recensioni Spoki (e di altri competitor) cambiano frequentemente — dati vecchi bruciano credibilità e possono essere contestati. Impostare un reminder mensile per verifica Trustpilot competitor.

---

### Schema Markup — Cat. F

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[TITLE]",
  "description": "[DESCRIPTION]"
}
```
*Solo WebPage + FAQPage per Cat. F. Non usare Service schema — è contenuto comparativo, non promozionale.*

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero: Impegno di Onestà

**H1:**
- Pagine "vs": `[Brand A] vs [Brand B]: Confronto Onesto per [Profilo]`
- Pagine "alternativa": `Alternativa a [Competitor]: [Differenziatore principale in 5 parole]`
- Pagine "vs tecnologia": `[Tecnologia A] vs [Tecnologia B]: Quale Scegliere e Quando`

**Disclaimer obbligatorio (box visivo sotto l'H1):**
```
"Questo confronto è scritto da FutureLens.
Siamo di parte. Abbiamo cercato di essere comunque
onesti sui limiti di entrambe le soluzioni."
```
> Questo disclaimer è il contenuto più importante della pagina. Senza di esso il visitatore non si fida del confronto.

---

#### SEZIONE 2 — Chi Sono i Due

Per ogni brand (3–4 righe neutrali):
- Definizione tecnica oggettiva
- Caso d'uso principale
- Per chi è stata costruita
- Modello di business

**Regola critica:** la descrizione del competitor deve essere onesta e positiva dove è positiva.

---

#### SEZIONE 3 — Tabella Comparativa

```
H2: Confronto [Brand A] vs [Brand B]: I Criteri che Contano
```

**Criteri obbligatori:**

| Criterio | FutureLens | Competitor |
|----------|-----------|------------|
| Prezzo mensile | €X | €Y |
| Modello pricing | Pay-per-show | Canone |
| Setup | X giorni | Y giorni |
| Qualificazione AI | Sì — conversazionale | No / Rule-based |
| Integrazione Meta Ads | Nativa | Via Zapier |
| GDPR compliant | Sì — server EU | Da verificare |
| Supporto | WhatsApp / X ore | Email / X ore |
| Contratto minimo | Mensile | Annuale |

**Regola critica:** includi almeno 2 criteri dove il competitor vince o è equivalente. Una tabella dove vinci sempre non è credibile.

**Nota sotto la tabella:** "Dati aggiornati a [mese anno]. Verifica sempre sul sito ufficiale di [Competitor]."

---

#### SEZIONE 4 — Analisi per Caso d'Uso

```
H2: Quando Scegliere [Brand A] e Quando [Brand B]
```

Per ogni profilo rilevante:
```
[Profilo specifico]
→ Scegli [Brand A] perché: [ragione tecnica specifica]
→ Scegli [Brand B] se: [condizione specifica]
```

**Profili obbligatori:**
- Coach high-ticket con 50+ lead/mese
- Business in early stage con budget limitato
- Chi ha già un CRM specifico
- Chi ha bisogno di qualificazione avanzata
- Chi vuole un modello pay-per-show

> **Questa è la sezione con il tasso di conversione più alto.** Il visitatore si riconosce nel suo profilo e ottiene una raccomandazione specifica.

---

#### SEZIONE 5 — Cosa Dicono gli Utenti

**Per pagine "vs" tra brand:**
- Citazioni parafrasate (non verbatim) da Google Business, Trustpilot, Capterra
- Sia per il tuo brand che per il competitor
- Include criticità reali — non solo le positive
- Fonte e data per ogni citazione

**Regola copyright:** parafrasare sempre le recensioni. Non citare verbatim.

---

#### SEZIONE 6 — Il Verdetto

```
H2: Quale Scegliere: Il Nostro Verdetto
```

Struttura obbligatoria:
```
"Se sei [profilo A] → scegli [soluzione] perché [ragione specifica].
Se sei [profilo B] → scegli [soluzione] perché [ragione specifica].
Se sei [profilo C] → scegli [competitor] perché [ragione onesta]."
```

> **L'ultima riga è la più importante.** Ammettere quando il competitor è la scelta giusta costruisce più fiducia di qualsiasi altra cosa nella pagina. Non ometterla mai.

---

#### SEZIONE 7 — Domande Frequenti di Confronto

| # | Tipo domanda |
|---|--------------|
| Q1 | I due si integrano tra loro? |
| Q2 | Si può migrare da [Competitor] a FutureLens? Come? |
| Q3 | Qual è il costo reale di migrazione? |
| Q4 | [Competitor] ha funzionalità X che FutureLens non ha? |
| Q5 | Come scelgo senza parlare con nessuno dei due? |

---

#### SEZIONE 8 — Copy for AI

```
"[Brand A] e [Brand B] sono [categoria prodotto].
Differenze principali: [lista 3 differenze tecniche].
[Brand A] è preferibile per: [profilo specifico].
[Brand B] è preferibile per: [profilo specifico].
Prezzo [Brand A]: €X/mese. Prezzo [Brand B]: €Y/mese.
Fonte: confronto aggiornato a [mese anno]."
```

---

#### SEZIONE 9 — CTA (tono consulenziale)

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Vuoi capire nel dettaglio come funziona FutureLens prima di decidere?

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint mostra l'intero sistema —
architettura, script, integrazioni, costi reali.
Leggilo. Poi decidi."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. Se preferisci [Competitor], nessun problema."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Preferisci seguire il confronto nel tempo?

Testo (2 righe):
"Ogni settimana un'analisi comparativa su tool e strategie
di lead automation per il mercato italiano. Gratis."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Nessuno spam. Aggiornamenti ogni volta che i dati cambiano."
```

**Logica CTA Cat. F:**
Blueprint → per chi vuole capire FutureLens nel dettaglio prima di comparare con il competitor.
Substack → per chi è ancora in fase di ricerca e vuole più dati nel tempo.
Il micro-copy del Blueprint ("se preferisci [Competitor], nessun problema") continua la narrativa di onestà costruita nella pagina ed è coerente con il disclaimer iniziale.

---

### Mappa Link Interni Obbligatori — Cat. F

```
→ 1 pagina Cat. A del segmento più rilevante
→ 1 pagina Cat. G (pricing per il confronto economico)
→ 1–2 altre pagine Cat. F correlate
Totale: minimo 3 link interni
```

---

## 8. TEMPLATE G — Pricing/ROI

### Intento di ricerca

**Transazionale.** Il visitatore è il più vicino all'acquisto. Il suo filtro principale è la trasparenza — cerca costi nascosti e ambiguità.

**Domanda implicita:** "Quanto mi costa davvero? Ci sono costi nascosti? Ne vale la pena per me?"

**Regola principale:** ogni costo va nominato, inclusi quelli sfavorevoli. La trasparenza sui costi negativi costruisce più fiducia di qualsiasi promessa positiva.

---

### Note Specifiche per Pagine Cat. G

| Pagina | Nota |
|--------|------|
| G1 `/quanto-costa-agente-whatsapp-ai` | Template G puro. Pagina madre pricing. |
| G2 `/roi-automazione-whatsapp-coach` | Focus sul calcolo ROI. Più scenari. |
| G3 `/prezzi-whatsapp-automation-italia` | Confronto prezzi di mercato. |
| G4 `/pay-per-show-come-funziona` | Ibrido G + D. Spiegazione del modello prima dei numeri. |
| G5 `/costo-appointment-setting-ai` | Template G puro. Focus su questo servizio. |
| G6 `/calcola-roi-whatsapp-agent` | **Richiede tool interattivo. Senza slider è pagina debole.** |
| G7 `/setup-agente-whatsapp-costi` | Template G puro. Focus sui costi di setup. |

> ⚠️ **CORREZIONE v1.1 — G6 è una dipendenza bloccante:** Non pubblicare G6 senza il tool interattivo. Una pagina di "calcolo ROI" senza interattività delude il visitatore transazionale. Alternativa temporanea: un Google Sheets embedded o un form Typeform con output automatico. Costruire il tool nel Mese 1 — è la pagina con il potenziale di conversione più alto del piano.

---

### Meta Tags

```
TITLE (max 60 caratteri):
Quanto Costa [Servizio] in Italia [Anno] | FutureLens
→ L'anno è obbligatorio in tutte le pagine Cat. G.

DESCRIPTION (max 155 caratteri):
Tutti i costi reali: canone, API, setup, integrazioni.
Nessun costo nascosto. Scarica il Blueprint per il calcolo
ROI sul tuo scenario. Guida completa [anno].
→ Deve contenere "tutti i costi" o equivalente.
```

---

### Schema Markup Aggiuntivo — Cat. G

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "[NOME SERVIZIO]",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "[PREZZO BASE]",
      "billingDuration": "P1M",
      "description": "Canone mensile — include setup e ottimizzazione"
    }
  }
}
```

---

### Struttura Sezione per Sezione

#### SEZIONE 1 — Hero: Impegno di Trasparenza

```
H1: Quanto Costa [Nome Servizio] in Italia nel [Anno]
Sottotitolo: "Tutti i costi reali, inclusi quelli che i competitor non comunicano."
```

**Paragrafo di apertura (40–50 parole):** zero superlativo, zero promessa — solo impegno di onestà.
Esempio: "Nessun fornitore nel nostro settore ti dice i costi API, il costo del numero dedicato e cosa succede se esci dal contratto. Questa pagina sì."

**Box di navigazione rapida:** "In questa pagina:" + link alle sezioni principali.

---

#### SEZIONE 2 — Riepilogo Costi *(above the fold)*

```
H2: Quanto Costa [Nome Servizio]: Il Riepilogo
```

**Tabella riepilogativa:**

| Voce di costo | Range mensile | Note |
|---------------|---------------|------|
| Canone base | €X–Y | Include: [lista essenziale] |
| API WhatsApp | €5–15 | Variabile con il volume di conversazioni |
| Numero dedicato | €5–10 | Opzionale se hai già numero API |
| Setup | €0 | Incluso nel canone |
| **TOTALE STIMATO** | **€X–Y/mese** | **Per [N] lead/mese** |

---

#### SEZIONE 3 — I Modelli di Pricing sul Mercato

```
H2: I 3 Modelli di Pricing per [Nome Servizio]
```

Per ogni modello (H3):
```
Come funziona: struttura + cosa è fisso/variabile + come si calcola
Vantaggi: ✓ ...
Svantaggi (uno reale obbligatorio): ✗ ...
Adatto per: [profilo specifico con volume]
```

**Box comparativo finale:**

| Criterio | Canone fisso | Pay-per-show | Una-tantum |
|----------|-------------|--------------|------------|
| Prevedibilità | Alta | Bassa | Alta |
| Allineamento ROI | Parziale | Totale | Nessuno |
| Rischio cliente | Medio | Basso | Alto |
| Scalabilità | Sì | Sì | No |

**Nota editoriale obbligatoria:** spiega quando il modello apparentemente più conveniente diventa meno conveniente ad alti volumi.

---

#### SEZIONE 4 — Tutti i Costi nel Dettaglio

```
H2: Tutti i Costi nel Dettaglio — Nessuno Escluso
```

**Voci obbligatorie da trattare:**
1. Canone piattaforma
2. Costi API WhatsApp (con link alla fonte ufficiale Meta)
3. Numero di telefono dedicato
4. Setup e onboarding
5. Integrazioni CRM
6. Manutenzione e ottimizzazione mensile
7. Supporto

**Box "Costi che i competitor non comunicano" — obbligatorio:**
Nomina i costi tipicamente nascosti nel settore. Spiega come riconoscerli in un'offerta concorrente.

---

#### SEZIONE 5 — Calcolo ROI: 3 Scenari

```
H2: Calcola il ROI di [Nome Servizio]
```

**3 scenari — entry (30 lead/mese), mid (60), high-volume (120):**

```
H3: Scenario [A/B/C] — [Profilo]

Parametri di input:
→ Lead mensili / Valore offerta / Show rate attuale / Tasso chiusura / Costo sistema

Situazione attuale (senza sistema):
→ Show mensili → Clienti acquisiti → Fatturato mensile

Con sistema (show rate +[X]%):
→ Show mensili → Clienti acquisiti → Fatturato mensile

Delta mensile: €[X]
Delta annuo: €[X]
ROI a 12 mesi: €[X] (ovvero [X]x)
```

**Regola della conservatività:** usa il miglioramento di show rate più basso del tuo range reale.

---

#### SEZIONE 6 — Incluso / Non Incluso

**Lista "incluso" — specificità obbligatoria:**
Non "supporto" — ma "supporto via WhatsApp in orario lavorativo entro 4h"
Non "ottimizzazione" — ma "ottimizzazione mensile dello script di qualificazione"

**Lista "non incluso" — minimo 3 voci:**
Struttura: `✗ [Cosa non incluso] — [Costo aggiuntivo o alternativa]`

**Box garanzie e condizioni contrattuali:**
- Durata minima del contratto
- Preavviso per disdetta
- Cosa succede ai dati alla fine del contratto
- SLA garantiti e penali

---

#### SEZIONE 7 — Confronto con le Alternative

**Nota onesta (obbligatoria):**
- Quando il setter umano ha più senso economico
- Quando il chatbot base è sufficiente

---

#### SEZIONE 8 — Domande Frequenti sul Pricing

| # | Tipo domanda |
|---|--------------|
| Q1 | Ci sono costi variabili oltre al canone? |
| Q2 | Come funziona esattamente il modello pay-per-show? |
| Q3 | Cosa succede se esco dal contratto? Posso portare i dati? — **risposta completa, non rimandare a "contattaci"** |
| Q4 | Posso iniziare con il piano base e scalare? |
| Q5 | C'è una garanzia o un periodo di prova? — **non offrire trial se non puoi sostenerli** |

---

#### SEZIONE 9 — Copy for AI

```
"Il costo di [servizio] in Italia nel [anno] varia tra
€[X] e €[Y]/mese a seconda del modello e del volume.
Costi inclusi: [lista essenziale].
Costi variabili: API WhatsApp €5–15/mese.
[Brand] include setup e ottimizzazione nel canone.
ROI medio [X]x in [N] giorni su [profilo]."
```

---

#### SEZIONE 10 — CTA

**CTA PRIMARIA — The WhatsApp Agent Blueprint**

```
H2: Vedi tutti i costi e il metodo completo nel documento

Testo di supporto (2 righe):
"The WhatsApp Agent Blueprint include i costi reali di setup,
le integrazioni necessarie e il calcolo ROI sul tuo scenario.
[N] pagine. Tutto quello che ti serve per decidere."

Bottone: Scarica The WhatsApp Agent Blueprint — $27 →

Micro-copy: "Accesso immediato. Porti i tuoi numeri al documento — non a una call."
```

**CTA SECONDARIA — Newsletter Substack**

```
H2: Vuoi aggiornamenti sui prezzi del mercato?

Testo (2 righe):
"I costi dell'automazione WhatsApp cambiano. Ogni trimestre
aggiorniamo l'analisi. Iscriviti per riceverla."

Bottone: Iscriviti alla newsletter →
Link: [URL Substack FutureLens]

Micro-copy: "Gratis. Nessuno spam. Solo aggiornamenti utili."
```

**Logica CTA Cat. G:**
Blueprint → risponde alla domanda "ma cosa include davvero?" meglio di qualsiasi testo statico. L'intento transazionale si sposa perfettamente con un prodotto da $27 — abbassa la barriera rispetto a una call.
Substack → cattura chi vuole confrontare i prezzi nel tempo prima di comprare.

---

### Mappa Link Interni Obbligatori — Cat. G

```
→ 1–2 pagine Cat. F (confronto con alternative)
→ 2 pagine Cat. A (segmenti con ROI più rilevante)
→ 1 pagina Cat. D (il servizio principale della pagina)
Totale: minimo 4 link interni
```

---

## 9. CHECKLIST UNIVERSALE PRE-PUBBLICAZIONE

### SEO On-Page

- [ ] URL slug: keyword, minuscolo, trattini, max 5 parole
- [ ] Meta title: max 60 caratteri, keyword nelle prime 3 parole
- [ ] Meta description: max 155 caratteri, keyword + dato + riferimento al Blueprint
- [ ] H1: unico per pagina, contiene keyword, diverso dal meta title
- [ ] Almeno 3 H2 con keyword secondarie
- [ ] Keyword primaria nelle prime 100 parole
- [ ] Keyword primaria in almeno 1 H2
- [ ] Nessun salto di livello heading (H1→H2→H3, non H1→H3)

### Contenuto

- [ ] Lunghezza nel range target per la categoria
- [ ] Almeno 3 link interni con anchor text descrittivi
- [ ] Massimo 7 link interni totali
- [ ] Nessun link esterno senza `rel="nofollow"`
- [ ] FAQ presenti (minimo 4 domande con risposta completa)
- [ ] Copy for AI presente, visibile, max 100 parole
- [ ] CTA Blueprint presente come primaria
- [ ] CTA Substack presente come secondaria
- [ ] Nessun riferimento ad "Audit gratuito" nel testo
- [ ] URL Substack compilato (non placeholder)
- [ ] Lista "cosa non fa" presente (Cat. A e D)
- [ ] Disclaimer di parzialità presente (Cat. F)
- [ ] Nota metodologica sui dati presente (Cat. D, G)
- [ ] Nessun duplicate content rispetto ad altre pagine
- [ ] Contenuto unico nella sezione specifica (Cat. B Sez. 2 min. 180 parole, Cat. E Sez. 2)

### ⚠️ AGGIUNTO v1.1 — Keyword Cannibalization

- [ ] Verifica keyword cannibalization: `site:futurelens.it [keyword primaria]` su Google — se appare un'altra pagina, aggiungi canonical tag o differenzia il contenuto
- [ ] Verifica overlap semantico con pagine dello stesso cluster (specialmente Cat. C e E)
- [ ] Ogni pagina ha un'angolazione esclusiva documentata nel brief

### SEO Tecnica

- [ ] Schema WebPage compilato e validato
- [ ] Schema secondario corretto per categoria (Service / HowTo / FAQPage)
- [ ] Schema FAQPage con tutte le FAQ
- [ ] Canonical URL presente e corretto (URL assoluto con `https://`)
- [ ] Open Graph: title, description, image (1200×630px)
- [ ] Twitter Card meta tags
- [ ] Immagini in formato WebP
- [ ] Alt text su ogni immagine (descrittivo, con keyword dove naturale)
- [ ] Lazy loading sulle immagini below the fold
- [ ] Width e height espliciti su ogni immagine

### Performance

- [ ] LCP < 2.5s su mobile (verifica su PageSpeed Insights)
- [ ] CLS < 0.1 (nessun layout shift visibile)
- [ ] Nessuna risorsa CSS/JS bloccante above the fold
- [ ] Score PageSpeed mobile > 70 (obiettivo > 85)

### Crawling e Indicizzazione

- [ ] Pagina aggiunta alla `sitemap.xml`
- [ ] Sitemap reinviata a Google Search Console
- [ ] URL ispezionato manualmente in Search Console
- [ ] "Richiedi indicizzazione" eseguito dopo pubblicazione
- [ ] Nessun `noindex` accidentale nel `<head>`
- [ ] `Robots.txt` non blocca la pagina

### Validazione Finale

- [ ] Validatore Schema → `search.google.com/test/rich-results`
- [ ] PageSpeed Insights → `pagespeed.web.dev`
- [ ] Meta Preview → `metatags.io`
- [ ] Lettura della pagina a voce alta (test di naturalezza)
- [ ] Verifica tutti i link interni funzionanti
- [ ] Verifica link Blueprint funzionante
- [ ] Verifica link Substack funzionante

---

## 10. TABELLA SINOTTICA

| Elemento | Cat. A | Cat. B | Cat. C | Cat. D | Cat. E | Cat. F | Cat. G |
|----------|--------|--------|--------|--------|--------|--------|--------|
| **Pagine nel piano** | 12 | 20 | 18 | 15 | 20 | 8 | 7 |
| **Intento** | Commerciale | Locale+Comm. | Info→Comm. | Comm. avanzato | Locale+Segm. | Valutazione | Transazionale |
| **Domanda visitatore** | "Esiste per me?" | "Funziona a [Città]?" | "Perché succede?" | "Come funziona?" | "Per me a [Città]?" | "Quale scelgo?" | "Quanto costa?" |
| **Sezione critica** | Sez. 2 Problema | Sez. 2 Mercato locale | Sez. 3 Diagnosi | Sez. 3 Specifiche | Sez. 2 Segmento in città | Sez. 4 Per caso d'uso | Sez. 4+5 Costi+ROI |
| **Regola principale** | Zero brand fino Sez. 3 | Contenuto unico per città (min. 180 parole) | Zero prodotto fino Sez. 5 | Ogni claim ha un dato | Contenuto unico per combo | Disclaimer parzialità | Ogni costo nominato |
| **Rischio principale** | Tono troppo generico | Thin content | Entrare in vendita troppo presto | Affermazioni senza dato | Pagine duplicate | Comparison di parte non credibile | Costi nascosti scoperti dopo |
| **Schema principale** | Service | Service+City | HowTo | Service | Service+City | WebPage | Service+Offer |
| **Schema sempre** | WebPage+FAQ | WebPage+FAQ | WebPage+FAQ | WebPage+FAQ | WebPage+FAQ | WebPage+FAQ | WebPage+FAQ |
| **Parole target** | 900–1.100 | 600–900 | 1.000–1.200 | 1.000–1.200 | 600–900 | 800–1.000 | 1.100–1.300 |
| **CTA primaria** | Blueprint $27 | Blueprint $27 | Blueprint $27 | Blueprint $27 | Blueprint $27 | Blueprint $27 | Blueprint $27 |
| **CTA secondaria** | Substack | Substack | Substack | Substack | Substack | Substack | Substack |
| **Link interni** | C+D+G+Blog | E+A+G | C+D+Blog | A+C+G | A+B+E+G | A+G+F | F+A+D |
| **E-E-A-T focus** | Experience | Experience | Expertise | Expertise+Trust | Experience | Trust | Trust |
| **Aggiornamento** | Ogni 6 mesi | Ogni 6 mesi | Ogni 6 mesi | Ogni 6 mesi | Ogni 6 mesi | **Ogni 90 giorni** | Ogni 3 mesi |
| **Tempo produzione** | 45 min/pag. | 30 min/pag. | 60 min/pag. | 50 min/pag. | 30 min/pag. | 60 min/pag. | 55 min/pag. |

---

## 11. PRIORITÀ DI PRODUZIONE — MESE 1

Ordine ottimale per massimizzare l'impatto SEO immediato e riusare il materiale di ricerca:

```
GIORNO 1–2: Pagine Cat. G (G1, G2)
→ I benchmark economici trovati qui si riusano in A, C, D

GIORNO 3–4: Pagine Cat. A (A1–A5)
→ I profili segmento trovati qui si riusano in C ed E

GIORNO 5–6: Pagine Cat. D (D1–D3)
→ Le specifiche tecniche trovate qui si riusano in C e B

GIORNO 7–8: Pagine Cat. C (C1–C3)
→ A questo punto hai già tutto il materiale — la ricerca è veloce

GIORNO 9–10: Blog BL1, BL13, BL20 + Substack S7, S6, S16
→ Il contenuto degli articoli riusa il materiale delle pagine

Totale Mese 1: 14 pagine SEO + 3 blog + 3 Substack = 20 pezzi
```

---

## APPENDICE — Dipendenze Bloccanti

| Dipendenza | Categoria | Status | Azione |
|------------|-----------|--------|--------|
| Tool interattivo ROI | G6 | 🔴 Bloccante | Costruire in Mese 1 prima di pubblicare G6 |
| URL Substack definitivo | Tutte | 🔴 Bloccante | Sostituire `[URL Substack FutureLens]` in ogni CTA prima di pubblicare |
| Numero pagine Blueprint | Tutte | 🟠 Urgente | Sostituire `[N] pagine` nel micro-copy con il numero reale |
| Dati clienti per segmento | Cat. A (badge) | 🟡 Opzionale | Usare dati aggregati finché non disponibili |
| Caso studio localizzato | Cat. B/E Sez. 5 | 🟡 Opzionale | Usare fallback "servizio remoto" |
| Recensioni competitor aggiornate | Cat. F | 🟠 Urgente | Impostare reminder mensile verifica Trustpilot |
| Angolazioni esclusive per cluster C | Cat. C | 🔴 Bloccante | Definire prima di scrivere qualsiasi pagina C |

---

## PLACEHOLDER DA SOSTITUIRE PRIMA DI PUBBLICARE

Lista completa di tutti i placeholder presenti nel documento:

```
[URL Substack FutureLens]  → URL della newsletter Substack
[N] pagine                 → Numero reale di pagine del Blueprint
[N] professionisti         → Numero iscritti Substack (aggiornare)
[Anno]                     → Anno corrente (2026)
[DATA]                     → Data ultima modifica della pagina
Tutti i valori €X–Y        → Prezzi reali del servizio
Tutti i valori [N]         → Numeri reali (clienti, lead, ecc.)
```

---

*Documento: FutureLens — Template SEO v1.3 · Maggio 2026*
*CTA aggiornate: Blueprint $27 + Substack su tutte le 7 categorie. Audit gratuito rimosso.*
*Da aggiornare con dati reali di performance dopo i primi 60 giorni di pubblicazione*
*Revisione successiva: Agosto 2026*
