# exoplanet-detection-bias
How has the kind of exoplanet we can detect changed over time, and how much of the population we see is just detection bias?  


## Getting the data

The data comes from the [Nasa Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) and isn't stored in this repo. To download it and set it up, clone the repo and then in a virtual environment use python src/download_data.py and python src/load_db.py. This creates 'data/raw/exoplanets.csv' and an SQLite database at 'data/exoplanets.db'

## Data  

The data cleaning process removes duplicates, converts types (numerical to integer), and removes physically impossible values. Rows with missing values are deliberately kept.