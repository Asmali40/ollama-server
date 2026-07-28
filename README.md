# Local Ollama Server 🤖

Ein eigener lokaler KI-Server mit **FastAPI** und **Ollama**.

Dieses Projekt stellt eine REST API bereit, über die lokale Large Language Models (LLMs) angesprochen werden können.  
Der Server läuft lokal und kommuniziert mit einer laufenden Ollama-Instanz.

Ziel des Projekts ist es, eine eigene kleine KI-Infrastruktur aufzubauen, die später um eine Weboberfläche, Streaming, Datenbanken und Docker erweitert werden kann.

---

## ✨ Features

- 🚀 FastAPI Backend
- 🤖 Lokale KI-Modelle mit Ollama
- 🔌 REST API Schnittstelle
- ⚡ Eigener CLI Startbefehl
- 🧩 Modulare Projektstruktur
- ⚙️ Zentrale Konfiguration
- 📚 Automatische API-Dokumentation mit Swagger

---

# Voraussetzungen

Folgende Software wird benötigt:

- Python 3.12+
- uv
- Ollama

Versionen prüfen:

```bash
python --version
uv --version
ollama --version
```

---

# Installation

## Repository klonen

```bash
git clone <repository-url>

cd ollama
```

---

## Abhängigkeiten installieren

Mit `uv`:

```bash
uv sync
```

Danach das Projekt installieren:

```bash
uv pip install -e .
```

---

# Ollama Setup

## Ollama Server starten

Ollama muss lokal laufen:

```bash
ollama serve
```

Standardmäßig läuft Ollama unter:

```
http://localhost:11434
```

---

## Modell installieren

Beispiel:

```bash
ollama pull qwen2.5:1.5b
```

Installierte Modelle anzeigen:

```bash
ollama list
```

---

# Server starten

Der eigene FastAPI Server kann über den eigenen CLI-Befehl gestartet werden:

```bash
uv run ollama
```

Danach läuft die API unter:

```
http://localhost:8000
```

---

# API Dokumentation

FastAPI stellt automatisch eine Swagger Oberfläche bereit:

```
http://localhost:8000/docs
```

Dort können alle Endpunkte getestet werden.

---

# API Nutzung

## Chat Anfrage

Endpoint:

```
POST /chat
```

Request:

```json
{
  "prompt": "Erkläre mir Python"
}
```

Response:

```json
{
  "answer": "Python ist eine Programmiersprache..."
}
```

---

# Projektstruktur

```
src/
└── app/
    │
    ├── main.py
    │   └── FastAPI Anwendung
    │
    ├── cli.py
    │   └── Eigener Startbefehl
    │
    ├── constants.py
    │   └── Globale Konfiguration
    │
    ├── schemas.py
    │   └── API Datenmodelle
    │
    ├── ollama.py
    │   └── Verbindung zu Ollama
    │
    └── router/
        │
        └── chat.py
            └── Chat API Endpunkt
```

---

# Architektur

```
                 User
                  |
                  |
                  v
              FastAPI
                  |
                  |
                  v
             Router Layer
                  |
                  |
                  v
             Schemas
          (Datenvalidierung)
                  |
                  |
                  v
             Ollama Client
                  |
                  |
                  v
              Ollama
                  |
                  |
                  v
              LLM Model
```

---

# Konfiguration

Die wichtigsten Einstellungen befinden sich in:

```
constants.py
```

Beispiel:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"

DEFAULT_MODEL = "qwen2.5:1.5b"

REQUEST_TIMEOUT = 120
```

---

# Entwicklung

Server mit automatischem Reload starten:

```bash
uv run ollama
```

Bei Änderungen am Code startet der Server automatisch neu.

---

# Fehlerbehebung

## Ollama nicht erreichbar

Fehler:

```
Connection refused localhost:11434
```

Lösung:

```bash
ollama serve
```

---

## Modell nicht gefunden

Fehler:

```
model not found
```

Lösung:

```bash
ollama pull qwen2.5:1.5b
```

---

## API startet nicht

Projekt neu installieren:

```bash
uv pip install -e .
```

Danach:

```bash
uv run ollama
```

---

# Roadmap

Geplante Erweiterungen:

- [ ] Eigene Chat-Weboberfläche
- [ ] Streaming Antworten wie ChatGPT
- [ ] Chat-Verlauf speichern
- [ ] Mehrere Modelle unterstützen
- [ ] Docker Container
- [ ] Docker Compose Setup
- [ ] Benutzerverwaltung
- [ ] Datei-Upload
- [ ] RAG Dokumentensuche
- [ ] Authentifizierung

---

# Technologie Stack

| Technologie | Verwendung |
|---|---|
| Python | Programmiersprache |
| FastAPI | Backend Framework |
| Uvicorn | ASGI Server |
| Ollama | Lokale KI Modelle |
| Pydantic | Datenvalidierung |
| uv | Paketverwaltung |

---

# Lizenz

Dieses Projekt ist ein Lernprojekt und dient dazu, eine eigene lokale KI-Anwendung aufzubauen.