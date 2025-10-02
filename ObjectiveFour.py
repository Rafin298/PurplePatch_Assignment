import os
import json
from bs4 import BeautifulSoup

PURPLEPATCH_ID = "123456"

def parse_ads_txt(file_path):
    purplepatch_found = False
    competitors = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 2:
                domain, pub_id = parts[0], parts[1]

                if PURPLEPATCH_ID not in pub_id:
                    competitors.append(domain)

    return list(set(competitors))


report = {}
ads_folder = "Ads.txt"
for fname in os.listdir(ads_folder):
    fpath = os.path.join(ads_folder, fname)
    competitors = parse_ads_txt(fpath)
    report[fname] = {
            "competitors": competitors,
        }
    
with open("ObjectFourReportCompetitors.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("Report saved to ObjectFourReportCompetitors.json")




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
            "id": ins.get("data-purplepatch-id"),
        }

        # i assumed if width >= 728 and height >= 90 then high viewability
        if int(slot["width"]) >= 728 and int(slot["height"]) >= 90:
            slot["viewability"] = "High"
        else:
            slot["viewability"] = "Medium/Low"
        if slot["id"] != "53126d71827fcba70ff68055b9a73ca1pdt":
            slots.append(slot)

    return slots


slots_folder = "Adslot Code"
report = {}
for fname in os.listdir(slots_folder):
    fpath = os.path.join(slots_folder, fname)
    slots = parse_adslot_code(fpath)
    publisher_name = slots[0]["publisher"] if slots else fname
    report[publisher_name] = {"adslots": slots}

with open("Objective_Four_Competitor_viewability_and_slots_position_Report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("Report saved to Objective_Four_Competitor_viewability_and_slots_position_Report.json")