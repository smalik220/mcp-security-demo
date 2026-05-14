# Secure vs Insecure MCP Server — Mini-Demo

**Duur:** 7 minuten  
**Werkvorm:** Demo  
**Thema:** Responsible AI / Secure AI 

---

## Doel

Laten zien hoe een slecht geconfigureerde MCP-server beveiligingsrisico's veroorzaakt binnen een AI-systeem, en hoe je dit concreet oplost en welke handelingen je als gebruiker kunt nemen om het MCP-server te beveiligen

---

## Context

AI-agents gebruiken steeds vaker MCP-servers om externe tools aan te sturen — zoals het lezen van bestanden, aanroepen van API's of uitvoeren van code.

Maar wat gebeurt er als de toegangscontrole verkeerd geïmplementeerd is?

---

## Architectuur

```
AI Agent
   ↓
MCP Server
   ↓ hier zit het beveiligingsprobleem
Repository Files
```

---

## Planning

| Minuut | Onderdeel | Werkvorm |
|---|---|---|
| 0 – 1 | Introductie: wat is een onveilige MCP-server en waarom is dit relevant? | Uitleg |
| 1 – 3 | Live demo: insecure MCP-server — bestand opvragen dat niet toegankelijk mag zijn | Demo |
| 3 – 4 | Interactief: vraag aan de klas — "Welke data kan een aanvaller hier bereiken?" | Discussie |
| 4 – 6 | Live demo: secure versie — zelfde aanval, nu geblokkeerd met logging | Demo |
| 6 – 7 | Conclusie: koppeling aan OWASP LLM07 en Responsible AI | Uitleg |

---

## Demo Detail

### 1 min Introductie

- Korte uitleg: MCP (Model Context Protocol) laat AI-agents tools gebruiken
- Een MCP-server bepaalt welke tools en bestanden een agent mag benaderen
- Zonder goede beveiliging kan een agent bij gevoelige informatie

### 2 min Live demo: insecure server

| Request | Insecure server |
|---|---|
| `/read_file?path=fake_repo/README.md` | 200 OK — bestandsinhoud |
| `/read_file?path=fake_repo/secret.env` | 200 OK — API keys zichtbaar |

- Server geeft elk bestand terug zonder controle

### 2 min — Discussie

> "Welke data kan een aanvaller hier bereiken?"

Verwacht antwoord: API-keys, wachtwoorden, configuratiebestanden — alles wat op het systeem staat.

### 2 min Live demo: secure server

| Request | Secure server |
|---|---|
| `/read_file?path=fake_repo/README.md` | 200 OK — bestandsinhoud |
| `/read_file?path=fake_repo/secret.env` | 403 Forbidden + logging |

```python
# Insecure
def read_file(path: str):
    return open(path).read()

# Secure
ALLOWED_PATHS = ["fake_repo/README.md"]

def read_file(path: str):
    if path not in ALLOWED_PATHS:
        raise PermissionError("Toegang geweigerd")
    return open(path).read()
```

### 1 min Conclusie

---

## OWASP Koppeling

| OWASP categorie | Verband met deze demo |
|---|---|
| LLM07 — Insecure Plugin Design | MCP-server zonder toegangscontrole |
| LLM08 — Excessive Agency | Agent heeft meer rechten dan nodig |
| LLM06 — Sensitive Information Disclosure | `secret.env` is leesbaar zonder authenticatie |

---

## Repository Structuur

```
mcp-security-demo/
├── app_insecure.py        # Onveilige MCP-server (geen toegangscontrole)
├── app_secure.py          # Beveiligde versie (allowlist + logging)
├── fake_repo/
│   ├── README.md          # Normaal bestand — mag worden gelezen
│   └── secret.env         # Gevoelig bestand — mag NIET worden gelezen
├── requirements.txt       # Dependencies (fastapi, uvicorn)
└── README.md              # Uitleg van het project + demo-instructies
```

---

## Vereisten

### Lesmateriaal
- FastAPI demo-code insecure + secure versie via GitHub repository
- Laptop met Python geïnstalleerd
- QR-code naar de GitHub repository voor de klas
- Scherm voor demonstratie

### Technische vereisten
- Python 3.10+
- pip install -r requirements.txt
- Terminal om de server te starten

### Server starten
```bash
# Insecure server
uvicorn app_insecure:app --reload

# Secure server
uvicorn app_secure:app --reload
```

### Demo requests
```
GET http://localhost:8000/read_file?path=fake_repo/README.md
GET http://localhost:8000/read_file?path=fake_repo/secret.env
```

---

## Bronnen

- [MCP Security & Authorization](https://modelcontextprotocol.io/docs/tutorials/security/authorization)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
