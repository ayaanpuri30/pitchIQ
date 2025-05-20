import os
import json
# used this script originally to convert to tsx
def valid_name(s : str):
    if s[0] in digits or "&" in s or "\'" in s or "(" in s or "/" in s or "\\" in s:
        return False
    return True
# Path to your JSON of team names and their IDs
with open("team_ids.json", "r") as f:
    team_map_big = json.load(f)
digits = "0123456789"
team_names = [item['name'] for item in team_map_big["data"] if valid_name(item['name'])]

output_folder = "pitchiq/src/clubData"
os.makedirs(output_folder, exist_ok=True)

def make_valid_identifier(name):
    # Remove spaces and special chars for clean TS variable names
    return name.replace(" ", "").replace("-", "").replace(".", "")

def main():
    lines = []
    
    # Import lines
    for name in team_names:
        valid_name = make_valid_identifier(name)
        lines.append(f"import {valid_name}Data from './{name.replace(' ', '_')}';")

    lines.append("\nconst teamMap: Record<string, any> = {")
    # Map lines
    for name in team_names:
        valid_name = make_valid_identifier(name)
        lines.append(f'  "{name}": {valid_name}Data,')
    lines.append("};\n\nexport default teamMap;")

    # Save
    filename = os.path.join(output_folder, "teamMap.ts")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Saved {filename}")

if __name__ == "__main__":
    main()
