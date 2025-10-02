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
            "category": ins.get("data-publisher-category"),
            "width": ins.get("data-publisher-width"),
            "height": ins.get("data-publisher-height"),
        }

        slots.append(slot)

    return slots


slots_folder = "Adslot Code"
report = {}
for fname in os.listdir(slots_folder):
    fpath = os.path.join(slots_folder, fname)
    slots = parse_adslot_code(fpath)
    publisher_name = slots[0]["publisher"] if slots else fname
    if publisher_name in report:
        report[publisher_name]["adslots"].extend(slots)
    else:
        report[publisher_name] = {"adslots": slots}
        
with open("ObjectTwoReport.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("Report saved to ObjectTwoReport.json")