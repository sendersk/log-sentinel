from collections import Counter
from models import LogEntry


def analyze(entries: list[LogEntry]) -> dict:
    levels = Counter(e.level for e in entries)
    ips = Counter(e.ip for e in entries if e.ip)

    errors = [e for e in entries if e.level == "ERROR"]

    return {
        "total_logs": len(entries),
        "levels": dict(levels),
        "top_ips": ips.most_common(5),
        "error_count": len(errors)
    }