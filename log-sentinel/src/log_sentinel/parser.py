import re
from models import LogEntry


LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)?\s*'
    r'\[(?P<timestamp>.*?)\]\s*'
    r'"(?P<message>.*?)"\s*'
    r'(?P<level>ERROR|INFO|WARN|WARNING|DEBUG)?'
)


def parse_line(line: str) -> LogEntry:
    match = LOG_PATTERN.search(line)

    if match:
        data = match.groupdict()

        return LogEntry(
            timestamp=None,
            level=data.get("level") or "INFO",
            ip=data.get("ip"),
            message=data.get("message") or line,
            raw=line,
        )

    return LogEntry(
        timestamp=None,
        level="UNKNOWN",
        ip=None,
        message=line,
        raw=line,
    )


def parse_file(path: str) -> list[LogEntry]:
    entries = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            entries.append(parse_line(line.strip()))

    return entries