from geopy.geocoders import Nominatim
import pandas as pd
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("geocode_logger")

# Initialize geolocator
geolocator = Nominatim(user_agent="gurgaon_sector_locator")

# Your list of sectors
sectors = [
    'sector 36', 'sector 89', 'sohna road', 'sector 92', 'sector 102',
    'gwal pahari', 'sector 108', 'sector 105', 'sector 26', 'sector 109',
    'sector 28', 'sector 65', 'sector 12', 'sector 85', 'sector 70a',
    'sector 30', 'sector 107', 'sector 3', 'sector 2', 'sector 41',
    'sector 4', 'sector 62', 'sector 49', 'sector 81', 'sector 66',
    'sector 86', 'sector 48', 'sector 51', 'sector 37', 'sector 111',
    'sector 67', 'sector 113', 'sector 13', 'sector 61', 'sector 69',
    'sector 67a', 'sector 37d', 'sector 82', 'sector 53', 'sector 74',
    'sector 52', 'sector 43', 'sector 14', 'sector 25', 'sector 95',
    'sector 56', 'sector 83', 'sector 104', 'sector 88a', 'sector 55',
    'sector 50', 'sector 84', 'sector 91', 'sector 76', 'sector 82a',
    'sector 78', 'manesar', 'sector 93', 'sector 7', 'sector 71',
    'sector 110', 'sector 33', 'sector 70', 'sector 103', 'sector 90',
    'sector 38', 'sector 79', 'sector 112', 'sector 22', 'sector 59',
    'sector 99', 'sector 9', 'sector 58', 'sector 77', 'sector 1',
    'sector 57', 'sector 106', 'dwarka expressway', 'sector 63',
    'sector 5', 'sector 40', 'sector 23', 'sector 6', 'sector 72',
    'sector 47', 'sector 45', 'sector 68', 'sector 11', 'sector 60',
    'sector 39', 'sector 63a', 'sector 24', 'sector 46', 'sector 17',
    'sector 15', 'sector 10', 'sector 31', 'sector 21', 'sector 80',
    'sector 73', 'sector 54', 'sector 8', 'sector 88', 'sector 27'
]

# Initialize result list
sector_coords = []

# Function to get lat/long with retries
def fetch_coordinates(place, retries=3, delay=1):
    for attempt in range(retries):
        try:
            location = geolocator.geocode(f"{place}, Gurgaon, India")
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except Exception as e:
            logger.warning(f"Attempt {attempt+1}: Error fetching {place}: {e}")
            time.sleep(delay)
    return None, None

# Main loop with logging and delay
for sector in sectors:
    sector_clean = sector.strip().title()
    lat, lon = fetch_coordinates(sector_clean)
    logger.info(f"{sector_clean} => Latitude: {lat}, Longitude: {lon}")
    sector_coords.append({
        "sector": sector_clean,
        "latitude": lat,
        "longitude": lon
    })
    time.sleep(1)  

# Convert to DataFrame
df_coords = pd.DataFrame(sector_coords)

# Save as CSV
df_coords.to_csv("gurgaon_sector_coordinates.csv", index=False)
print(df_coords)
