# Spister Backend

Das Backend für die Spister-Anwendung, entwickelt mit Django und Django REST Framework. Es bietet APIs für Benutzerverwaltung, Profilbilder, Restaurant und andere Funktionen. Für die Authentifizierung wird JWT (JSON Web Token) verwendet.

## Voraussetzungen

Stelle sicher, dass die folgenden Tools auf deinem System installiert sind:

- Python 3.10 oder höher
- pip (Python Package Installer)
- virtualenv 

## Installation

1. **Repository klonen:**

   ```bash
   git clone https://github.com/SunnyDevZH/Sipster-Backend
   
2. **Odner öffnen**

    ```bash
    cd Sipster-Backend

3. **Virtuele Umgebung erstelle und aktivieren**

    ```bash
    python3 -m venv venv
    source venv/bin/activate    für Mac
    venv\Scripts\activate       für Windows

4. **Abhängigkeiten installieren:**

    ```bash
    pip3 install -r requirements.txt

5. **Datenbank migrieren**

    ```bash
    python3 manage.py migrate

6. **Superuser erstellen**

    ```bash
    python3 manage.py createsuperuser

7. **Entwicklungsserver starten**

    ```bash
    python3 manage.py runserver

8.  **Für das Testen mit Testdaten**
    ```bash
    python3 manage.py loaddata fixtures/testdaten.json

## Doku Projekt FFHS:

**Meilenstein 1 Freitag, 14. Februar 2025**

PDF mit:

- Beschreibung der Applikation und ihres Funktionsumfangs
- Funktionale und nichtfunktionale Anforderungen
- Projektstruktur: Roadmap und grobe Aufgaben
- Bewertung der Applikation hinsichtlich allgemeiner Projektanforderungen
- Design-Grundbausteine
- Wireframes für das Frontend
- Die Tools und Technologien

**Meilenstein 2 Freitag, 28. März 2025**

Video: Loom 

Erledigt:
- Login funktion mit JWT
- Frontend soweit mit React geschrieben
- Backend mit Django eingerichtet
- API-Daten bereit stellen (Restaurants, User usw.)
- Frontend mit Backend verknüpfen

**Meilenstein 3 Donnerstag 2. Mai 2025**

Video: Loom 

Erledigt:
- Profilbild hochladen
- Daten per PUT vom User auf dem Backend ändern
- Magic funktion implementieren
- Display Mode update
- Logout

**Meilenstein 4 Freitag 6. Juni 2025**

Video: Loom 

Erledigt:
- Fixtures mit Testdaten
- Bugfix
- Kategorien auch im Backend 
- Feedback Button
- Code Doku
- Anpassung Readme
