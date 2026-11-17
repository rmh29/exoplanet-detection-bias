"""
Download confirmed-planet data from the NASA Exoplanet Archive.

Queries the planetary systems composite parameters table via the 
TAP service and saves it as a CSV.
Column definitions: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
"""

from pathlib import Path
import requests

URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
OUT_PATH = Path("data/raw/exoplanets.csv")

COLUMNS = [
    "pl_name", "hostname", "discoverymethod", "disc_year", "disc_facility",
    "pl_orbper", # orbital period, days
    "pl_orbsmax", # semi major axis, AU
    "pl_rade", # radius, earth radii
    "pl_radeerr1", "pl_radeerr2", # upper/lower radius uncertainty
    "pl_bmasse", # mass, earth masses
    "pl_bmassprov", #mass type: true or minimum (M sin i)
    "sy_dist", # distance, parsecs
]

def download_exoplanets() -> None:
    query = f"select {','.join(COLUMNS)} from pscomppars"
    response = requests.get(URL, params={"query": query, "format": "csv"}, timeout=60)
    response.raise_for_status() #error catch

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(response.text)
    n_planets = len(response.text.splitlines()) - 1 #minus header row
    print(f"Saved {n_planets} planets to {OUT_PATH}")


if __name__ == "__main__":
    download_exoplanets()