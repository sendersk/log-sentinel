import json
import csv
from pathlib import Path
from models import LogEntry


def export_json(data: dict, path: str):
    Path(path).write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )


def export_csv(entries: list[LogEntry], path: str):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["level", "ip", "message"])

        for e in entries:
            writer.writerow([e.level, e.ip, e.message])