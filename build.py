#!/usr/bin/env python3
"""
Programmatic SEO page builder for FutureLens.
Usage: python build.py <slug>
Example: python build.py agente-whatsapp-avvocati
"""
import html
import json
import os
import re
import sys
from datetime import date


# ── Render helpers ──────────────────────────────────────────────────────────

def render_trust_items(items):
    parts = []
    for item in items:
        parts.append(
            f'      <div class="trust-item">\n'
            f'        <div class="trust-val">{item["value"]}</div>\n'
            f'        <div class="trust-lbl">{item["label"]}</div>\n'
            f'      </div>'
        )
    return '\n'.join(parts)


def render_data_box(stats):
    parts = []
    for stat in stats:
        parts.append(
            f'        <div class="stat-item">\n'
            f'          <div class="stat-num">{stat["value"]}</div>\n'
            f'          <div>\n'
            f'            <div class="stat-desc">{stat["label"]}</div>\n'
            f'            <div class="stat-src">{stat["source"]}</div>\n'
            f'          </div>\n'
            f'        </div>'
        )
    return '\n'.join(parts)


def render_steps(steps):
    parts = []
    for i, step in enumerate(steps, 1):
        num = f'{i:02d}'
        parts.append(
            f'      <div class="step-item">\n'
            f'        <div class="step-num">{num}</div>\n'
            f'        <div class="step-body">\n'
            f'          <div class="step-title">{step["title"]}</div>\n'
            f'          <div class="step-desc">{step["body"]}</div>\n'
            f'          <div class="step-output">→ output: {step["output"]}</div>\n'
            f'        </div>\n'
            f'      </div>'
        )
    return '\n'.join(parts)


def render_checklist(items, variant='yes'):
    parts = []
    for item in items:
        if variant == 'yes':
            parts.append(f'      <li><span class="ck">✓</span> <span>{item}</span></li>')
        else:
            parts.append(f'      <li><span class="cx">✗</span> <span style="color:var(--cmut);">{item}</span></li>')
    return '\n'.join(parts)


def render_confronto_table(rows):
    parts = []
    for row in rows:
        parts.append(
            f'        <tr>\n'
            f'          <td>{row["criteria"]}</td>\n'
            f'          <td>{row["col2"]}</td>\n'
            f'          <td>{row["col3"]}</td>\n'
            f'          <td class="hl">{row["agent"]}</td>\n'
            f'        </tr>'
        )
    return '\n'.join(parts)


def render_results_table(rows):
    parts = []
    for row in rows:
        parts.append(
            f'        <tr>\n'
            f'          <td>{row["metric"]}</td>\n'
            f'          <td>{row["baseline"]}</td>\n'
            f'          <td class="hl">{row["with_agent"]}</td>\n'
            f'          <td>{row["delta"]}</td>\n'
            f'        </tr>'
        )
    return '\n'.join(parts)


def render_faq_html(faqs):
    parts = []
    for faq in faqs:
        parts.append(
            f'      <div class="faq-item">\n'
            f'        <div class="faq-q">{faq["q"]}</div>\n'
            f'        <div class="faq-a">{faq["a"]}</div>\n'
            f'      </div>'
        )
    return '\n'.join(parts)


# ── Cat. C render helpers ────────────────────────────────────────────────────

def render_nav_box(items):
    parts = []
    for item in items:
        parts.append(
            f'        <li style="font-size:13px; color:var(--csec);">→ {item}</li>'
        )
    return '\n'.join(parts)


def render_calcolo_html(c):
    h3 = c.get('calcolo_h3', 'Calcola il Tuo Impatto')
    formula = c.get('calcolo_formula', '')
    esempio = c.get('calcolo_esempio', '')
    return (
        f'      <h3 style="font-size:14px; font-weight:600; color:var(--ctxt); margin-bottom:12px;">{h3}</h3>\n'
        f'      <p style="font-size:13px; color:var(--csec); line-height:1.65; margin-bottom:12px;">{formula}</p>\n'
        f'      <p style="font-family:\'JetBrains Mono\',monospace; font-size:11px; color:var(--cgrn); '
        f'background:var(--cterm); padding:10px 14px;">{esempio}</p>'
    )


def render_cause_items(items):
    parts = []
    for item in items:
        parts.append(
            f'      <div class="causa-item">\n'
            f'        <div class="causa-title">{item["titolo"]}</div>\n'
            f'        <p class="causa-text">{item["testo"]}</p>\n'
            f'      </div>'
        )
    return '\n'.join(parts)


def render_cause_sintesi(items):
    parts = []
    for item in items:
        parts.append(
            f'        <li style="font-size:13px; color:var(--csec); display:flex; gap:10px;">'
            f'<span style="color:var(--cacc); flex-shrink:0;">▸</span> <span>{item}</span></li>'
        )
    return '\n'.join(parts)


def render_soluzioni(soluzioni):
    parts = []
    for sol in soluzioni:
        parts.append(
            f'      <div class="sol-card">\n'
            f'        <div class="sol-nome">{sol["nome"]}</div>\n'
            f'        <div class="sol-grid">\n'
            f'          <div><div class="sol-field-label">Cosa promette</div>'
            f'<div class="sol-field-val">{sol["promette"]}</div></div>\n'
            f'          <div><div class="sol-field-label">Perché non basta</div>'
            f'<div class="sol-field-val neg">{sol["limite"]}</div></div>\n'
            f'          <div><div class="sol-field-label">Per chi funziona</div>'
            f'<div class="sol-field-val">{sol["per_chi"]}</div></div>\n'
            f'          <div><div class="sol-field-label">Costo reale</div>'
            f'<div class="sol-field-val">{sol["costo"]}</div></div>\n'
            f'        </div>\n'
            f'      </div>'
        )
    return '\n'.join(parts)


def render_risultati_main(c):
    before = c.get('risultati_main_before', '')
    after = c.get('risultati_main_after', '')
    time_ = c.get('risultati_main_time', '')
    return (
        f'      <div style="display:flex; align-items:center; gap:24px; flex-wrap:wrap;">\n'
        f'        <div>\n'
        f'          <div style="font-family:\'JetBrains Mono\',monospace; font-size:11px; '
        f'color:var(--cmut); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">prima</div>\n'
        f'          <div style="font-family:\'JetBrains Mono\',monospace; font-size:1.4rem; '
        f'color:var(--csec);">{before}</div>\n'
        f'        </div>\n'
        f'        <div style="font-family:\'JetBrains Mono\',monospace; font-size:1.8rem; color:var(--cacc);">→</div>\n'
        f'        <div>\n'
        f'          <div style="font-family:\'JetBrains Mono\',monospace; font-size:11px; '
        f'color:var(--cmut); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">con protocollo</div>\n'
        f'          <div style="font-family:\'JetBrains Mono\',monospace; font-size:1.8rem; '
        f'font-weight:600; color:var(--ctxt);">{after}</div>\n'
        f'        </div>\n'
        f'        <div style="font-family:\'JetBrains Mono\',monospace; font-size:10px; '
        f'color:var(--cmut); text-transform:uppercase; letter-spacing:0.1em; margin-left:auto;">in {time_}</div>\n'
        f'      </div>'
    )


def render_roi_html(c):
    h3 = c.get('roi_h3', "L'Impatto Economico per il Tuo Business")
    scenario = c.get('roi_scenario', '')
    prima = c.get('roi_prima', '')
    con_sistema = c.get('roi_con_sistema', '')
    delta_mensile = c.get('roi_delta_mensile', '')
    delta_annuo = c.get('roi_delta_annuo', '')
    return (
        f'      <h3 style="font-size:14px; font-weight:600; color:var(--ctxt); margin-bottom:16px;">{h3}</h3>\n'
        f'      <p style="font-family:\'JetBrains Mono\',monospace; font-size:10px; color:var(--cmut); '
        f'text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">scenario base</p>\n'
        f'      <p style="font-size:13px; color:var(--csec); margin-bottom:16px;">{scenario}</p>\n'
        f'      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">\n'
        f'        <div style="background:var(--c2); padding:14px 16px;">\n'
        f'          <div style="font-family:\'JetBrains Mono\',monospace; font-size:9px; color:var(--cmut); '
        f'text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">prima</div>\n'
        f'          <div style="font-size:13px; color:var(--csec);">{prima}</div>\n'
        f'        </div>\n'
        f'        <div style="background:var(--c2); padding:14px 16px; border-left:2px solid var(--cacc);">\n'
        f'          <div style="font-family:\'JetBrains Mono\',monospace; font-size:9px; color:var(--cacc); '
        f'text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">con sistema</div>\n'
        f'          <div style="font-size:13px; color:var(--csec);">{con_sistema}</div>\n'
        f'        </div>\n'
        f'      </div>\n'
        f'      <div style="display:flex; gap:24px; flex-wrap:wrap;">\n'
        f'        <div><span style="font-family:\'JetBrains Mono\',monospace; font-size:9px; '
        f'color:var(--cmut); text-transform:uppercase; letter-spacing:0.1em;">Delta mensile: </span>'
        f'<strong style="color:var(--cgrn);">{delta_mensile}</strong></div>\n'
        f'        <div><span style="font-family:\'JetBrains Mono\',monospace; font-size:9px; '
        f'color:var(--cmut); text-transform:uppercase; letter-spacing:0.1em;">Delta annuo: </span>'
        f'<strong style="color:var(--cgrn);">{delta_annuo}</strong></div>\n'
        f'      </div>'
    )


def render_correlati(correlati):
    parts = []
    for item in correlati:
        parts.append(
            f'      <a href="{item["url"]}" class="exp-card">\n'
            f'        <div class="exp-cat">{item["cat"]}</div>\n'
            f'        <div class="exp-title">{item["titolo"]}</div>\n'
            f'        <div class="exp-footer">\n'
            f'          <span>{item["note"]}</span>\n'
            f'          <span class="exp-arrow">→</span>\n'
            f'        </div>\n'
            f'      </a>'
        )
    return '\n'.join(parts)


def render_schema(c, page_title, date_modified):
    """Generate the full schema.org JSON-LD array using json.dumps for safety."""
    template_type = c.get('template_type', 'A')

    webpage = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": c['meta_title'],
        "description": c['meta_description'],
        "url": c['canonical_url'],
        "dateModified": date_modified,
        "inLanguage": "it-IT",
        "publisher": {
            "@type": "Organization",
            "name": "FutureLens",
            "url": "https://futurelens.xyz"
        }
    }

    faqpage = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq['q'],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq['a']
                }
            }
            for faq in c['faqs']
        ]
    }

    if template_type == 'C':
        howto = {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": page_title,
            "description": c['meta_description'],
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
                    "name": step['title'],
                    "text": step['body'],
                    "position": i + 1
                }
                for i, step in enumerate(c.get('steps', []))
            ]
        }
        schema = [webpage, howto, faqpage]
    else:
        service = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": page_title,
            "description": c['schema_service_desc'],
            "provider": {
                "@type": "Organization",
                "name": "FutureLens",
                "url": "https://futurelens.xyz"
            },
            "areaServed": {
                "@type": "Country",
                "name": "Italia"
            },
            "serviceType": "WhatsApp AI Automation",
            "audience": {
                "@type": "Audience",
                "audienceType": c['schema_audience']
            }
        }
        schema = [webpage, service, faqpage]

    return json.dumps(schema, ensure_ascii=False, indent=2)


# ── Core builder ────────────────────────────────────────────────────────────

def build_page(slug):
    content_file = os.path.join('content', f'{slug}.json')
    if not os.path.exists(content_file):
        print(f'ERROR: {content_file} not found')
        sys.exit(1)

    with open(content_file, 'r', encoding='utf-8') as f:
        c = json.load(f)

    template_type = c.get('template_type', 'A')
    template_file = 'template-c.html' if template_type == 'C' else 'template.html'

    if not os.path.exists(template_file):
        print(f'ERROR: {template_file} not found — run from project root')
        sys.exit(1)

    with open(template_file, 'r', encoding='utf-8') as f:
        tmpl = f.read()

    # Derived values
    date_modified = c.get('date_modified') or date.today().isoformat()
    page_title = re.sub(r'<br\s*/?>', ' ', c['h1_title']).strip()

    if template_type == 'C':
        replacements = {
            '{{META_TITLE}}':             c['meta_title'],
            '{{META_DESCRIPTION_ESC}}':   html.escape(c['meta_description']),
            '{{TWITTER_DESCRIPTION_ESC}}': html.escape(c['twitter_description']),
            '{{CANONICAL_URL}}':          c['canonical_url'],
            '{{SCHEMA_JSON_LD}}':         render_schema(c, page_title, date_modified),
            '{{HERO_BADGE_LABEL}}':       c['hero_badge_label'],
            '{{H1_TITLE}}':               c['h1_title'],
            '{{HERO_SUBTITLE}}':          c['hero_subtitle'],
            '{{HERO_PAIN_P1}}':           c['hero_pain_p1'],
            '{{NAV_BOX_HTML}}':           render_nav_box(c['nav_items']),
            '{{DIFFUSIONE_H2}}':          c['diffusione_h2'],
            '{{DIFFUSIONE_P1}}':          c['diffusione_p1'],
            '{{DATA_BOX_HTML}}':          render_data_box(c['data_box']),
            '{{CALCOLO_HTML}}':           render_calcolo_html(c),
            '{{CAUSE_H2}}':               c['cause_h2'],
            '{{CAUSE_INTRO}}':            c['cause_intro'],
            '{{CAUSE_ITEMS_HTML}}':       render_cause_items(c['cause_items']),
            '{{CAUSE_SINTESI_HTML}}':     render_cause_sintesi(c['cause_sintesi']),
            '{{SOLUZIONI_H2}}':           c['soluzioni_h2'],
            '{{SOLUZIONI_HTML}}':         render_soluzioni(c['soluzioni']),
            '{{SOLUZIONI_TRANSIZIONE}}':  c['soluzioni_transizione'],
            '{{PROTOCOLLO_H2}}':          c['protocollo_h2'],
            '{{PROTOCOLLO_INTRO}}':       c['protocollo_intro'],
            '{{STEPS_HTML}}':             render_steps(c['steps']),
            '{{RISULTATI_H2}}':           c['risultati_h2'],
            '{{RISULTATI_MAIN}}':         render_risultati_main(c),
            '{{RISULTATI_TABLE_HTML}}':   render_results_table(c['risultati_table']),
            '{{RISULTATI_NOTE}}':         c['risultati_note'],
            '{{ROI_HTML}}':               render_roi_html(c),
            '{{CORRELATI_H2}}':           c['correlati_h2'],
            '{{CORRELATI_HTML}}':         render_correlati(c['correlati']),
            '{{FAQ_H2}}':                 c['faq_h2'],
            '{{FAQ_HTML}}':               render_faq_html(c['faqs']),
            '{{AI_COPY_TEXT}}':           c['ai_copy_text'],
        }
    else:
        # Original Cat. A replacements (unchanged)
        replacements = {
            '{{META_TITLE}}':          c['meta_title'],
            '{{META_DESCRIPTION_ESC}}': html.escape(c['meta_description']),
            '{{TWITTER_DESCRIPTION_ESC}}': html.escape(c['twitter_description']),
            '{{CANONICAL_URL}}':       c['canonical_url'],
            '{{SCHEMA_JSON_LD}}':      render_schema(c, page_title, date_modified),
            '{{HERO_BADGE_LABEL}}':    c['hero_badge_label'],
            '{{H1_TITLE}}':            c['h1_title'],
            '{{HERO_SUBTITLE}}':       c['hero_subtitle'],
            '{{HERO_PAIN_P1}}':        c['hero_pain_p1'],
            '{{HERO_PAIN_P2}}':        c['hero_pain_p2'],
            '{{TRUST_ITEMS_HTML}}':    render_trust_items(c['trust_items']),
            '{{PROBLEMA_H2}}':         c['problema_h2'],
            '{{PROBLEMA_P1}}':         c['problema_p1'],
            '{{PROBLEMA_P2}}':         c['problema_p2'],
            '{{PROBLEMA_P3}}':         c['problema_p3'],
            '{{DATA_BOX_HTML}}':       render_data_box(c['data_box']),
            '{{COME_FUNZIONA_H2}}':    c['come_funziona_h2'],
            '{{COME_FUNZIONA_INTRO}}': c['come_funziona_intro'],
            '{{STEPS_HTML}}':          render_steps(c['steps']),
            '{{COSA_INCLUDE_H2}}':     c['cosa_include_h2'],
            '{{CHECKLIST_YES_HTML}}':  render_checklist(c['checklist_yes'], 'yes'),
            '{{CHECKLIST_NO_HTML}}':   render_checklist(c['checklist_no'], 'no'),
            '{{RISULTATI_H2}}':        c['risultati_h2'],
            '{{RISULTATI_TABLE_HTML}}': render_results_table(c['risultati_table']),
            '{{RISULTATI_NOTE}}':      c['risultati_note'],
            '{{CONFRONTO_H2}}':          c['confronto_h2'],
            '{{CONFRONTO_COL2}}':        c['confronto_col2'],
            '{{CONFRONTO_COL3}}':        c['confronto_col3'],
            '{{CONFRONTO_TABLE_BODY}}':  render_confronto_table(c['confronto_rows']),
            '{{CONFRONTO_NOTE}}':        c['confronto_note'],
            '{{FAQ_H2}}':              c['faq_h2'],
            '{{FAQ_HTML}}':            render_faq_html(c['faqs']),
            '{{AI_COPY_TEXT}}':        c['ai_copy_text'],
        }

    output = tmpl
    for marker, value in replacements.items():
        output = output.replace(marker, value)

    # Warn on unreplaced markers
    remaining = re.findall(r'\{\{[A-Z_]+\}\}', output)
    if remaining:
        print(f'WARNING: unreplaced markers: {sorted(set(remaining))}')

    # Write page
    os.makedirs(slug, exist_ok=True)
    out_path = os.path.join(slug, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f'OK {out_path}')

    # Update sitemap
    update_sitemap(slug, date_modified)


def update_sitemap(slug, date_modified):
    url = f'https://seo.futurelens.xyz/{slug}'
    sitemap_path = 'sitemap.xml'

    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if f'<loc>{url}</loc>' in content:
        content = re.sub(
            rf'(<loc>{re.escape(url)}</loc>\s*<lastmod>)[^<]*(</lastmod>)',
            rf'\g<1>{date_modified}\g<2>',
            content
        )
        print(f'OK sitemap: updated lastmod for {slug}')
    else:
        entry = (
            f'  <url>\n'
            f'    <loc>{url}</loc>\n'
            f'    <lastmod>{date_modified}</lastmod>\n'
            f'    <changefreq>monthly</changefreq>\n'
            f'    <priority>0.9</priority>\n'
            f'  </url>'
        )
        content = content.replace('</urlset>', f'{entry}\n</urlset>')
        print(f'OK sitemap: added {slug}')

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python build.py <slug>')
        print('Example: python build.py agente-whatsapp-avvocati')
        sys.exit(1)
    build_page(sys.argv[1])
