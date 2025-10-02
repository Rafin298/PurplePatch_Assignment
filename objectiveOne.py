## Check a publisher’s/ads.txt file and verify whether PurplePatch’s seller ID is included.

import os
import json
PURPLEPATCH_ID = "purplepatch.online"

def parse_ads_txt(file_path):
    purplepatch_found = False
    competitors = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 2:
                pub_id =  parts[1]

                if PURPLEPATCH_ID in pub_id:
                    purplepatch_found = True

    return purplepatch_found, list(set(competitors))


report = {}
ads_folder = "Ads.txt"
for fname in os.listdir(ads_folder):
    fpath = os.path.join(ads_folder, fname)
    purplepatch_found, competitors = parse_ads_txt(fpath)
    report[fname] = {
        "purplepatch_present": purplepatch_found,
    }
    
with open("ObjectOneReport.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("Report saved to ObjectOneReport.json")