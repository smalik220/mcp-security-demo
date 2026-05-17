# MCP Security Demo

Demo die laat zien hoe een slecht geconfigureerde MCP-server beveiligingsrisico's veroorzaakt, en hoe je dit oplost.

---

## Repository structuur

```
mcp-security-demo/
├── mcp_insecure.py        # Onveilige MCP-server (geen toegangscontrole)
├── mcp_secure.py          # Beveiligde MCP-server (allowlist + logging)
├── bestanden/
│   ├── leesbaar-bestand.md    # Toegestaan bestand
│   └── secret.env             # Gevoelig bestand — mag NIET worden gelezen
├── tests/
│   └── test_security.py       # Tests voor beide servers
├── requirements.txt
└── README.md
```

---

## Installatie

```bash
pip3 install -r requirements.txt
```

---

## Server starten

**Insecure server:**
```bash
mcp dev mcp_insecure.py
```

**Secure server:**
```bash
mcp dev mcp_secure.py
```

De MCP Inspector opent automatisch in de browser.

## Testen

Start een van de servers en volg de onderstaande stappen om de demo te testen via de MCP Inspector.

1. Open de MCP Inspector via de link die automatisch in de terminal verschijnt na het starten van de server
2. Navigeer naar het tabblad *Tools* en selecteer *read_file*
3. Voer een pad in bij het veld *path* en klik op *Run Tool*

*Voorbeeldpaden om te testen:*

| Pad | Verwacht resultaat |
|---|---|
| `bestanden/leesbaar-bestand.md` | Bestandsinhoud zichtbaar |
| `bestanden/secret.env` | Insecure: API key zichtbaar — Secure: Access denied |


---

## Demo

| Pad | Insecure server | Secure server |
|---|---|---|
| `bestanden/leesbaar-bestand.md` | Bestandsinhoud zichtbaar | Bestandsinhoud zichtbaar |
| `bestanden/secret.env` | API key zichtbaar | Access denied |

---

## Tests draaien

```bash
python3 -m pytest tests/ -v
```

---

## OWASP koppeling

| Categorie | Verband |
|---|---|
| LLM07 — Insecure Plugin Design | MCP-server zonder toegangscontrole |
| LLM08 — Excessive Agency | Agent heeft meer rechten dan nodig |
| LLM06 — Sensitive Information Disclosure | `secret.env` leesbaar zonder authenticatie |

---

## Bronnen

- [MCP Security & Authorization](https://modelcontextprotocol.io/docs/tutorials/security/authorization)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

