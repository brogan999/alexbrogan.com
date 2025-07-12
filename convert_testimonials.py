import csv
import os
from datetime import datetime

csv_file = "../testimonials.csv"
output_dir = "converted_testimonials"
os.makedirs(output_dir, exist_ok=True)

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row.get("Person's Name", "Untitled Testimonial").strip()
        slug = row.get("Slug", title.lower().replace(" ", "-"))
        body = row.get("Testimonial Text", "").strip()

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

