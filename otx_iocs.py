#!/usr/bin/env python3
import requests, csv, os
from datetime import datetime

# Use environment variable (never hardcode)
API_KEY = os.getenv("OTX_API_KEY")
if not API_KEY:
    print("Error: Set OTX_API_KEY in ~/.bashrc or .env")
    exit(1)

url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
headers = {"X-OTX-API-KEY": API_KEY}
r = requests.get(url, headers=headers)

if r.status_code != 200:
    print(f"API Error: {r.status_code}")
    exit(1)

iocs = []
for pulse in r.json().get("results", [])[:10]:
    for ind in pulse.get("indicators", []):
        iocs.append({
            "IOC": ind["indicator"],
            "Type": ind["type"],
            "Threat": pulse["name"],
            "Date": datetime.now().strftime("%Y-%m-%d")
        })

filename = f"otx_iocs_{datetime.now():%Y%m%d}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["IOC", "Type", "Threat", "Date"])
    writer.writeheader()
    writer.writerows(iocs)

print(f"Success: {len(iocs)} IOCs → {filename}")
