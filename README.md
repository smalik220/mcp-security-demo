# MCP Security Demo

Demo die laat zien hoe een slecht geconfigureerde MCP-server beveiligingsrisico's veroorzaakt, en hoe je dit oplost.

---

## Repository structuur

```
mcp-security-demo/
├── app_insecure.py        # Onveilige MCP-server 
├── app_secure.py          # Beveiligde versie 
├── bestanden/
│   ├── leesbaar-bestand.md          # toegestaan bestand mag worden gelezen
│   └── secret.env         # environment bestand mag NIET worden gelezen
├── requirements.txt       # Dependencies
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
uvicorn app_insecure:app --reload
```

**Secure server:**
```bash
uvicorn app_secure:app --reload
```

---

## Demo requests

```bash
# Normaal bestand — beide servers geven dit terug
curl "http://localhost:8000/read_file?path=bestanden/leesbaar-bestand.md"

# Gevoelig bestand — insecure geeft het terug, secure geeft 403
curl "http://localhost:8000/read_file?path=bestanden/secret.env"
```

| Request | Insecure server | Secure server |
|---|---|---|
| `bestanden/leesbaar-bestand.md` | 200 OK | 200 OK |
| `bestanden/secret.env` | 200 OK — API keys zichtbaar | 403 Forbidden + logging |

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
