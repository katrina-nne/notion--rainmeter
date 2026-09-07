import json
from datetime import datetime, date


#Configuration
# ==========================================================

USER_NAME = "Katrina"
MAX_VISIBLE_CARDS = 5

COURSE_COLOURS = {
    "CSC2042S": "255,196,0",      #Gold
    "CSC2002S": "255,140,0",      #Orange
    "INF2011S": "0,120,255",      #Blue
    "MAM1032S": "40,167,69",      #Green
    "STA1000S": "156,39,176",     #Purple
}

TYPE_ICONS = {
    "Assignment": r"[\xE8A5]",   #document
    "Quiz": r"[\xE8FD]",         #clipboard
    "Test": r"[\xE9D9]",         #notebook
    "Exam": r"[\xE814]",         #incidentTriangle
    "Project": r"[\xE8c9]",      #importance
}


DEFAULT_COLOUR = "200,200,200"
DEFAULT_ICON = r"[\xE7C3]"

#Helper Functions
# ==========================================================

def format_time(time_str):
    """Convert 23H55 -> 23:55"""

    if not time_str:
        return ""

    return time_str.replace("H", ":").replace("h", ":")

def get_greeting():
    """Return greeting based on current time"""

    hour = datetime.now().hour

    if 5 <= hour < 12:
        return f"Good morning, {USER_NAME}."

    elif 12 <= hour < 17:
        return f"Good afternoon, {USER_NAME}."

    elif 17 <= hour < 22:
        return f"Good evening, {USER_NAME}."

    else:
        return f"Good night, {USER_NAME}."

def get_today():
    """Return today's date"""

    today = datetime.now()

    return f"{today.strftime('%A')} - {today.day} {today.strftime('%B')}"


def get_summary(events):
    """Return dashboard summary"""

    count = len(events)

    if count == 0:
        return "You're all caught up."

    elif count == 1:
        return "1 upcoming task"

    return f"{count} upcoming tasks"



#Load Events
# ==========================================================

with open("data/events.json", encoding="utf-8") as f:
    events = json.load(f)

today = date.today()

visible_events = []

#Process Events
# ==========================================================

for event in events:

    if event["status"].lower() == "done":
        continue

    due_text = ""

    if event["due"]:

        due_date = datetime.fromisoformat(event["due"]).date()
        diff = (due_date - today).days

        if diff < 0:
            due_text = f"Overdue by {-diff} day(s)"

        elif diff == 0:
            due_text = "Due Today"

        elif diff == 1:
            due_text = "Tomorrow"

        elif diff <= 7:
            due_text = f"In {diff} days"

        else:
            due_text = due_date.strftime("%d %b")

    event["friendly_due"] = due_text

    event["colour"] = COURSE_COLOURS.get(
        event["class"],
        DEFAULT_COLOUR
    )

    event["icon"] = TYPE_ICONS.get(
        event["type"],
        DEFAULT_ICON
    )

    visible_events.append(event)

#Export Variables
# ==========================================================

lines = [
    "[Variables]",
    "",
    f"Greeting={get_greeting()}",
    f"Today={get_today()}",
    f"Summary={get_summary(visible_events)}",
    ""
]

for i, event in enumerate(visible_events[:MAX_VISIBLE_CARDS], start=1):

    lines.extend([
        f"Card{i}Title={event['task']}",
        f"Card{i}Course={event['class']}",
        f"Card{i}Due={event['friendly_due']}",
        f"Card{i}Time={format_time(event['time'])}",
        f"Card{i}Colour={event['colour']}",
        f"Card{i}Icon={event['icon']}",
        ""
    ])

with open(
    "@Resources/Data/dashboard_variables.inc",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(lines))

print("Rainmeter variables exported.")