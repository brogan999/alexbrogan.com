import csv
import os
from datetime import datetime

csv_file = "../Articles.csv"
output_dir = "converted_articles"
os.makedirs(output_dir, exist_ok=True)

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row.get("Name", "Untitled Article").strip()
        slug = row.get("Slug", title.lower().replace(" ", "-"))
        date_raw = row.get("Published On", "")
        body = row.get("Post Body", "").strip()

        try:
            date = datetime.strptime(date_raw[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
        except:
            date = datetime.today().strftime('%Y-%m-%d')

        filename = f"{date}-{slug}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as out:
            out.write("---\n")
            out.write(f'title: "{title}"\n')
            out.write(f'date: {date}\n')
            out.write(f'draft: false\n')
            out.write("---\n\n")
            out.write(body)

