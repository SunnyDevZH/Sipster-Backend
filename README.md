# Spister Backend

Das Backend für die Spister-Anwendung, entwickelt mit Django und Django REST Framework. Es bietet APIs für Benutzerverwaltung, Profilbilder, Restaurant und andere Funktionen.

## Voraussetzungen

Stelle sicher, dass die folgenden Tools auf deinem System installiert sind:

- Python 3.10 oder höher
- pip (Python Package Installer)
- virtualenv (optional, aber empfohlen)

## Installation

1. **Repository klonen:**

   ```bash
   git clone <repository-url>
   cd Spister-Backend

2. **Virtuele Umgebung erstelle und aktivieren**

    python3 -m venv venv
    source venv/bin/activate    für Mac
    venv\Scripts\activate       für Windows

3. **Abhängigkeiten installieren:**

    pip3 install -r requirements.txt

4. **Datenbank migrieren**

    python3 manage.py migrate

5. **Superuser erstellen**

    python3 manage.py createsuperuser

6. **Entwicklungsserver starten**

    python3 manage.py runserver

## Doku Projekt FFHS:

**Meilenstein 1 Freitag, 14. Februar 2025**

PDF mit:

- BESCHREIBUNG DER APPLIKATION UND IHRES FUNKTIONSUMFANGS
- FUNKTIONALE UND NICHTFUNKTIONALE ANFORDERUNGEN
- PROJEKTSTRUKTUR: ROADMAP UND GROBE AUFGABEN
- BEWERTUNG DER APPLIKATION HINSICHTLICH ALLGEMEINER PROJEKTANFORDERUNGEN
- DESIGN-GRUNDBAUSTEINE
- WIREFRAMES FÜR DAS FRONTEND
- DIE TOOLS UND TECHNOLOGIEN

**Meilenstein 2 Freitag, 28. März 2025**

Video: Loom 

Erledigt:
- Login funktion mit JWT
- Frontend soweit mit React geschrieben
- Backend mit Django eingerichtet
- API-Daten bereit stellen (Restaurants, User usw.)
- Frontend mit Backend verknüpfen

**Meilenstein 3  2025**

Video: Loom 

Erledigt:
- Profilbild hochladen
- Daten per PUT vom User auf dem Backend ändern
- Magic funktion implementieren
- Display Mode update
- Logout

**Meilenstein 4  2025**

Video: Loom 

Erledigt:
- Code aufräumen
- Code Doku erstellen
- Testen
- 
- 
