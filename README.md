# exoplanet-detection-bias
How has the kind of exoplanet we can detect changed over time, and how much of the population we see is just detection bias?  


## Getting the data

The data comes from the [Nasa Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) and isn't stored in this repo. To download it and set it up, clone the repo and then in a virtual environment use python src/download_data.py and python src/load_db.py. This creates 'data/raw/exoplanets.csv' and an SQLite database at 'data/exoplanets.db'

## Data  

The data cleaning process removes duplicates, converts types (numerical to integer), and removes physically impossible values. Rows with missing values are deliberately kept.

## Limitations

The archive's composite table reports a mass for almost every planet, but about 47% of all masses (and 63% for transit planets) are estimated from radius rather than measured. I treat these as missing in all mass-based analysis. The radii of planets not detected by transits are mostly obtained from an empirical mass-radius relationship and are not measurements. Therefore for radius-based analysis, I look at only transit-detected planets.