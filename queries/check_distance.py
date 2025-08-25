from haversine import haversine, Unit
import pandas as pd
import json
import re

def extract_ip_loc_tuple(raw_string):
    try:
        cleaned = re.sub(r'\s+', ' ', raw_string.strip())
        fragments = re.split(r'}\s*,\s*{', cleaned)
        simplified = []

        for frag in fragments:
            if not frag.startswith('{'):
                frag = '{' + frag
            if not frag.endswith('}'):
                frag = frag + '}'

            obj = json.loads(frag)

            # Convert loc string to tuple of floats
            loc_str = obj.get('loc', '')
            try:
                lat, lon = map(float, loc_str.split(','))
                loc_tuple = (lat, lon)
            except:
                loc_tuple = None  # fallback if loc is malformed

            simplified.append({
                'ip': obj.get('ip'),
                'loc': loc_tuple
            })

        return simplified

    except Exception as e:
        print("⚠️ Error parsing row:", e)
        return []

def check_distance(coord1, coord2):
    distance = haversine(coord1, coord2, unit=Unit.KILOMETERS)
    # print(f"Distance: {distance:.2f} km")
    return distance

file_name = input("Enter the CSV file name (with .csv extension): ")

df_to_check = pd.read_csv(file_name)
df_windfarms = pd.read_csv('windfarm_data.csv')

df_to_check['ip_loc_list'] = df_to_check['notes'].apply(extract_ip_loc_tuple)

rows = []

for index, row in df_to_check.iterrows():
    query = row['query']
    protocol = row['protocol']

    ip_loc_list = row['ip_loc_list']
    for obj in ip_loc_list:
        ip = obj['ip']
        loc = obj['loc']
        long = loc[1]
        lat = loc[0]

        closest_farms_3 = []

        for _, farm in df_windfarms.iterrows():
            farm_name = farm['properties.name']
            farm_country = farm['properties.country']
            farm_loc_lat = farm['geometry.coordinates.latitude']
            farm_loc_long = farm['geometry.coordinates.longitude']

            distance = check_distance((lat, long), (farm_loc_lat, farm_loc_long))

            if len(closest_farms_3) < 3:
                closest_farms_3.append((farm_name, farm_loc_lat, farm_loc_long, distance, farm_country))
            else:
                max_distance = max(closest_farms_3, key=lambda x: x[3])[3]
                if distance < max_distance:
                    max_index = next(i for i, v in enumerate(closest_farms_3) if v[3] == max_distance)
                    closest_farms_3[max_index] = (farm_name, farm_loc_lat, farm_loc_long, distance, farm_country)
        for farm in closest_farms_3:
            rows.append({
                'protocol': protocol,
                'query': query,
                'ip': ip,
                'long': long,
                'lat': lat,
                'distance': farm[3],
                'windfarm': farm[0],
                'farm_country': farm[4],
                'farm_long': farm[1],
                'farm_lat': farm[2]
            })

df_closest_windfarms = pd.DataFrame(rows)
output_file_name = f"{file_name.split('.')[0]}_windfarms.csv"
df_closest_windfarms.to_csv(output_file_name, index=False)