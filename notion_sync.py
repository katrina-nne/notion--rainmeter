import json
from notion_client import Client
from config import NOTION_TOKEN, DATA_SOURCE_ID

notion = Client(auth=NOTION_TOKEN)

response = notion.data_sources.query(
    data_source_id=DATA_SOURCE_ID
)

events = []

for page in response["results"]:

    props = page["properties"]

    def get_title(name):
        t = props[name]["title"]
        return t[0]["plain_text"] if t else ""

    def get_date(name):
        d = props[name]["date"]
        return d["start"] if d else ""

    def get_select(name):
        s = props[name]["select"]
        return s["name"] if s else ""

    def get_status(name):
        s = props[name]["status"]
        return s["name"] if s else ""

    def get_rich(name):
        r = props[name]["rich_text"]
        return r[0]["plain_text"] if r else ""

    events.append({
        "task": get_title("Task"),
        "class": get_select("Class"),
        "due": get_date("Due"),
        "time": get_rich("Time"),
        "status": get_status("Status"),
        "type": get_select("Type"),
        "notes": get_rich("Notes")
    })

events.sort(key=lambda x: x["due"] or "9999")

with open("data/events.json","w",encoding="utf-8") as f:
    json.dump(events,f,indent=4)

print("Done!")