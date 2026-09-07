# Notion x Rainmeter Dashboard
A Rainmeter widget that uses my notion database to display upcoming tasks on my desktop

---

## Features 
- Connects to notion DB
- Python retrieves and processes task data
- Displays tasks using Rainmeter
- Converts due dates into friendly descriptions such as:
  - `Due Today`
  - `Tomorrow`
  - `In 3 days`
  - `12 Sep`
- Hides completed tasks
- Displays time-base greeting
- Displays todays date

---

## Preview 
<img width="628" height="740" alt="image" src="https://github.com/user-attachments/assets/90fbc2a5-8e11-4041-bb4d-5b75803c7e1c" />

---

## Tech used
- Python
- Notion API
- Rainmeter
- Rainmeter INI
- Python JSON

---
## How It Works

The project is divided into three main stages:
```text
┌──────────────┐
│    Notion    │
│   Database   │
└──────┬───────┘
       │
       │ Notion API
       ▼
┌──────────────┐
│    Python    │
│              │
│ Fetch data   │
│ Process data │
│ Format data  │
└──────┬───────┘
       │
       │ Rainmeter variables
       ▼
┌──────────────┐
│   Rainmeter  │
│   Dashboard  │
└──────────────┘
```
## Important files
- **notion_sync.py**
    - Handles communication with the Notion API and retrieves the task data.

- **export_rainmeter.py**
    - Processes the retrieved data and converts it into variables that Rainmeter can display.

- **Dashboard.ini**
    - Defines the main Rainmeter dashboard layout and meters.

-  **@Resources/Variables.inc**
    - Contains reusable dashboard settings such as:
      Dimensions
      Colours
      Fonts
      Text sizes
      Border radius
      Dashboard spacing
    
- **Styles.inc**
    - Contains shared Rainmeter styling.

- **main.py**
    - Acts as the entry point for running the Python workflow.

 > [!NOTE]
> Notion API credentials are not included in this repo.
> sensitive🤫 and generated files are excluded using .gitignore, including:
>```text
>config.py
>data/events.json
>@Resources/Data/dashboard_variables.inc
>data/dashboard_variables.inc
>__pycache__/
>```
> You will need to use your own Notion API credentials and database configuration.

## Requirements
- Windows
- Rainmeter
- Python 3.x
- A Notion account
- A Notion integration/API key
- A Notion database containing your tasks

## Setup 
### 1. Clone the repository

``` git clone https://github.com/katrina-nne/notion--rainmeter.git```

***Then enter the project directory:***

```cd notion--rainmeter```
### 2. Install the Python dependencies

Install the required Python packages for the project.

```pip install -r requirements.txt```

> A requirements file will be added to the project as the dependency setup is finalised.

### 3. Configure Notion

Create a Notion integration and connect it to the database containing your tasks.
Add your credentials to the local configuration file.

***Do not commit the configuration file to GitHub.***

### 4. Run the Python workflow

Run:
```python main.py```

This retrieves and processes the task information and generates the Rainmeter variables.

### 5. Load the Rainmeter skin

Open Rainmeter and load:

```NotionDashboard```

The dashboard should then display your upcoming tasks 🤩

## Customising
To change how the dashboard looks, you can do this through:

``` @Resources/Variables.inc ```

eg. 
```
Background=24,24,27,248
CardBackground=40,42,46,252

PrimaryText=255,255,255
SecondaryText=185,185,190

Accent=0,120,255
```
***Other settings control:***
- Dashboard width
- Card size
- Card radius
- Fonts
- Font sizes
- Spacing
- Colours

## Future Improvements

**Planned improvements include:**
- Automatic background synchronisation
- Dynamic Fluent Icons for task types
- Clickable tasks that open the corresponding Notion page
- Improved task sorting
- Progress/completion indicators
 - Installation/setup documentation
