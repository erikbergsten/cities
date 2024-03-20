import json
import sys

# Read JSON from stdin
input_json = sys.stdin.read()

# Convert the input JSON string to a Python dictionary
cities_data = json.loads(input_json)

# Prepare the GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Loop through each city in the original JSON and convert it to a GeoJSON feature
for city in cities_data:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": city["location"]
        },
        "properties": {
            "name": city["name"],
            "description": city.get("description", "")  # Use .get() to avoid KeyError if 'description' is missing
        }
    }
    # Append the feature to the feature list in the GeoJSON
    geojson["features"].append(feature)

# Write the GeoJSON to stdout
sys.stdout.write(json.dumps(geojson))
