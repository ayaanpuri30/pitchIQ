from sports.configs.soccer import SoccerPitchConfiguration
import cv2
import os
import numpy as np
import openai


CONFIG = SoccerPitchConfiguration()
openai.api_key = os.getenv("OPEN_API_KEY")
if not openai.api_key:
    raise RuntimeError("Missing OPENAI_API_KEY env var")


def compute_zone_from_image(img_path, CONFIG):
    img = cv2.imread(img_path)                 # BGR
    red = img[:,:,2]                           # take red channel only
    h, w = red.shape

    # mask out pitch lines and background
    mask = (red > 50) & (red < 240)
    heat_img = red * mask

    # define pixel zones
    def row(x): return int((x/CONFIG.length)*h)
    def col(y): return int((y/CONFIG.width)*w)

    zones_px = {
      "left_att_third":   (row(2/3*CONFIG.length), row(CONFIG.length), col(0), col(CONFIG.width/2)),
      "right_att_third":  (row(2/3*CONFIG.length), row(CONFIG.length), col(CONFIG.width/2), col(CONFIG.width)),
      "central_midfield": (row(CONFIG.length/3), row(2/3*CONFIG.length), col(0), col(CONFIG.width)),
      "defensive_third":  (row(0), row(CONFIG.length/3), col(0), col(CONFIG.width)),
    }

    total = heat_img.sum()
    stats = {}
    for name, (r0,r1,c0,c1) in zones_px.items():
        stats[name] = float(heat_img[r0:r1, c0:c1].sum()) / float(total) if total else 0
    return stats

def compute_zone_coverage(coordinates, CONFIG):
    """
    coordinates: list of (x, y) positions
    CONFIG: pitch dimensions (length, width)
    returns: dictionary of percentages for each zone
    """
  
    zones = {
        "left_attacking_third": {
            "x_min": CONFIG.length * (2/3), 
            "x_max": CONFIG.length,
            "y_min": 0.0,
            "y_max": CONFIG.width * 0.5,  # left half if y=0 is bottom and y=width is top
        },
        "right_attacking_third": {
            "x_min": CONFIG.length * (2/3),
            "x_max": CONFIG.length,
            "y_min": CONFIG.width * 0.5,
            "y_max": CONFIG.width,
        },
        "central_midfield": {
            "x_min": CONFIG.length * (1/3),
            "x_max": CONFIG.length * (2/3),
            "y_min": 0.0,
            "y_max": CONFIG.width,
        },
        "defensive_third": {
            "x_min": 0.0,
            "x_max": CONFIG.length * (1/3),
            "y_min": 0.0,
            "y_max": CONFIG.width,
        },
    }

    zone_counts = {z: 0 for z in zones}
    total_count = 0
    
    # Flatten list of lists, if needed
    all_positions = [pos for coords_set in coordinates for pos in coords_set]
    
    for (x, y) in all_positions:
        total_count += 1
        for zone_name, bounds in zones.items():
            if (bounds['x_min'] <= x < bounds['x_max'] and
                bounds['y_min'] <= y < bounds['y_max']):
                zone_counts[zone_name] += 1
                break

    zone_percentages = {}
    for z in zones:
        zone_percentages[z] = zone_counts[z] / total_count if total_count else 0

    return zone_percentages

def get_playstyle_description(team_data):
    # Convert the dictionary to a JSON-like string
    data_str = str(team_data)

    system_prompt = "You are a soccer tactics analyst."
    user_prompt = (
        f"Here is the zone coverage data for Atletico Madrid in their soccer match:\n"
        f"{data_str}\n\n"
        "Based on these percentages, what can you infer about their playstyle? "
        "Give a concise summary."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]

