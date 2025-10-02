import os
import json
from bs4 import BeautifulSoup

def parse_adslot_code(file_path):
    slots = []
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    for ins in soup.find_all("ins"):
        slot = {
            "publisher": ins.get("data-publisher-name"),
            "width": ins.get("data-publisher-width"),
            "height": ins.get("data-publisher-height"),
        }

        # i assumed if width >= 728 and height >= 90 then high viewability
        if int(slot["width"]) >= 728 and int(slot["height"]) >= 90:
            slot["viewability"] = "High"
        else:
            slot["viewability"] = "Medium/Low"

        slots.append(slot)

    return slots


slots_folder = "Adslot Code"
report = {}
for fname in os.listdir(slots_folder):
    fpath = os.path.join(slots_folder, fname)
    slots = parse_adslot_code(fpath)
    publisher_name = slots[0]["publisher"] if slots else fname
    report[publisher_name] = {"adslots": slots}
        
with open("ObjectThreeReport.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("Report saved to ObjectThreeReport.json")