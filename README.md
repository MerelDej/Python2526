# To Do Lijst
Een **Python-gebaseerde command-line To-Do-Lijst applicatie** waarmee je **gebruikers, projecten en taken** kunt beheren via een SQLite-database.  
Het systeem ondersteunt volledige **CRUD-functionaliteit**, taakstatussen en het **genereren van rapporten in CSV en Excel**.

## Technologieën

- **Python 3**
- **SQLite** (lokale database)
- **Pandas** (rapport generatie)
- **Command-Line Interface (CLI)**

## Functionaliteiten
- **Gebruikersbeheer**
  - Gebruikers toevoegen, bekijken, aanpassen en verwijderen
- **Projectbeheer**
- **Gebruikersbeheer**
    - Gebruikers toevoegen, bekijken, aanpassen en verwijderen
- **Projectbeheer**
    - Projecten koppelen aan gebruikers
    - Projecten toevoegen, bekijken, aanpassen en verwijderen
- **Taakbeheer**
    - Taken koppelen aan gebruikers en projecten
    - Taakstatus bijhouden (`pending` / `completed`)
    - Vervaldatums instellen
- **Rapportage**
    - Volledig overzicht van alle taken
    - Gefilterde rapporten op project, gebruiker en/of status
    - Export naar **CSV of Excel**
- **Interactief CLI-menu**
    - Gebruiksvriendelijk menu
    - Veilig annuleren (`q`) vanuit elk invoerveld

## Projectstructuur
```
.

├── Main.py # Startpunt van de CLI & menu

├── DbOperations.py # Database CRUD-operaties

├── Report.py # Rapportgeneratie (CSV / Excel)

├── Enums.py # Enums voor taakstatus en rapporttypes

├── Quit.py # Veilig afsluiten van invoer

├── Database/

│ ├── Settings.py # Databasepad

│ └── CreateDatabase.py # Databaseschema & testdata

└── reports/ # Gegenereerde rapporten (automatisch aangemaakt)
```

## Installatie en setup

### Linux of MacOS

```bash
git clone https://github.com/MerelDej/Python2526.git
cd Python2526
python -m venv .venv
source .venv/bin/activate
# installeer de packages
pip install -r requirements.txt
```

### Windows

```powershell
git clone https://github.com/MerelDej/Python2526.git
cd Python2526
python -m venv .venv
# Windows cmd
.venv/Scripts/activate.ps1
# Windows Powershell
.venv/Scripts/activate.ps1
# installeer de packages
pip install -r requirements.txt
```

## Database aanmaken

```bash
python CreateDatabase.py
```

## Applicatie starten

```bash
python Main.py
```

Je ziet nu een interactief menu.

```
=== To Do List Command Menu ===
1. List all users
2. List all tasks
3. List all projects
4. Add user
5. Add task
6. Add project
7. Update user
8. Update task
9. Update project
10. Delete user
11. Delete task
12. Delete project
13. Generate full report
14. Generate filtered report
0. Exit
```

upAdd project
7. Update user
8. Update task
9. Update project
10. Delete user
11. Delete task
12. Delete project
13. Generate full report
14. Generate filtered report
0. Exit
```