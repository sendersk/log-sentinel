from parser import parse_file
from analyzer import analyze
from exporter import export_json, export_csv


def main():
    entries = parse_file("logs/app.log")

    report = analyze(entries)

    export_json(report, "output/report.json")
    export_csv(entries, "output/report.csv")

    print("Log analysis completed")


if __name__ == "__main__":
    main()