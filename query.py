from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
from astropy.table import Table
from datetime import date
from pathlib import Path

filename = f'archivedata/{date.today()}.csv'

if Path(filename).is_file():
    print(f"NASA Exoplanet Archive data current to {date.today()} exists at /{filename}")
else:
    print(f"Starting query of the NASA Exoplanet Archive current to today, {date.today()}")
    query = NasaExoplanetArchive.query_criteria(table="pscomppars", select="*")#,where="disc_facility like '%TESS%'")
    data = query.to_pandas()
    reduced_data = data[['hostname', 'pl_name', 'pl_msinie', 'pl_rade', 'disc_year', 'disc_refname', 'discoverymethod', 'disc_facility', 'ra', 'dec','gaia_dr3_id']]
    reduced_data.to_csv(filename)
    print(f"Saved query results to /{filename}")