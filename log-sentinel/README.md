# Log Sentinel

> Lightweight log analysis and incident detection tool

Log Sentinel is a Python-based log processing and analysis utility designed to help developers and DevOps engineers quickly identify issues, detect anomalies, and generate structured reports from application and server logs.

The project focuses on practical backend automation, file processing, incident investigation, and observability fundamentals.

---

## ✨ Features

- 📄 Parse application and server logs
- ⚠️ Detect errors and warnings
- 📊 Generate incident statistics
- 📁 Export reports to JSON
- 📑 Export parsed entries to CSV
- 🐳 Docker support
- 🧪 Unit testing with Pytest
- 🔍 Static analysis with MyPy
- ⚡ Linting and formatting with Ruff
- 🏗️ Modular project architecture

---

## 🎯 Project Goals

This project was created to practice:

- File operations in Python
- Log processing and parsing
- Regular expressions
- Data analysis
- Backend automation
- DevOps workflows
- Structured data export
- Modern Python project architecture

---

## 📂 Project Structure

```text
log-sentinel/
│
├── logs/
│   └── app.log
│
├── output/
│   ├── report.json
│   └── report.csv
│
├── src/
│   └── log_sentinel/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── config.py
│       ├── exporter.py
│       ├── main.py
│       ├── models.py
│       └── parser.py
│
├── tests/
│
├── Dockerfile
├── compose.yaml
├── pyproject.toml
└── README.md
```

---

## ⚙️ How It Works

The application performs four main steps:

### 1. Parse Logs

Reads log files line by line and converts each entry into a structured Python object.

### 2. Analyze Data

Collects useful statistics, including:

- Total number of log entries
- Error count
- Warning count
- Distribution of log levels
- Most active IP addresses

### 3. Export Results

Generates reports in:

- JSON
- CSV

### 4. Incident Reporting

Creates structured output suitable for troubleshooting and further automation.

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone <repository-url>

cd log-sentinel
```

### Install dependencies

Using **uv**:

```bash
uv sync
```

---

## 📄 Example Log File

Place your log files inside the `logs/` directory.

Example:

```text
127.0.0.1 [2025-01-01 10:00:00] "GET /api/users" INFO
127.0.0.1 [2025-01-01 10:00:05] "GET /api/orders" ERROR
192.168.1.10 [2025-01-01 10:01:00] "POST /login" WARNING
```

---

## ▶️ Running the Application

Run locally:

```bash
uv run python src/log_sentinel/main.py
```

Generated output:

```text
output/
├── report.json
└── report.csv
```

---

## 📊 Example JSON Report

```json
{
  "total_logs": 1250,
  "error_count": 12,
  "levels": {
    "INFO": 1180,
    "WARNING": 58,
    "ERROR": 12
  },
  "top_ips": [
    [
      "127.0.0.1",
      840
    ],
    [
      "192.168.1.10",
      410
    ]
  ]
}
```

---

## 🐳 Docker

### Build image

```bash
docker build -t log-sentinel .
```

### Run container

```bash
docker run --rm log-sentinel
```

---

## 🐳 Docker Compose

Start the application:

```bash
docker compose up --build
```

Stop the application:

```bash
docker compose down
```

---

## 🧪 Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=log_sentinel
```

---

## 🔍 Code Quality

Run Ruff linter:

```bash
uv run ruff check .
```

Format source code:

```bash
uv run ruff format .
```

Run static type checking:

```bash
uv run mypy src
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python 3.13 | Programming Language |
| Pydantic | Data Validation |
| Pytest | Testing |
| Ruff | Linting & Formatting |
| MyPy | Static Type Checking |
| Docker | Containerization |
| uv | Dependency Management |

---

## 📈 Roadmap

Future improvements:

- Support for Apache logs
- Support for Nginx logs
- Linux system log parser
- Real-time log monitoring
- HTML report generation
- Slack notifications
- Discord notifications
- Email alerts
- Prometheus metrics export
- Grafana dashboard integration

---

## 💼 Example Use Cases

- Backend application monitoring
- Incident investigation
- Log analytics
- Security event analysis
- DevOps automation
- Daily operational reporting
- CI/CD pipeline validation

---

## 🛡️ Reliability

- Processes logs line by line
- Handles malformed log entries gracefully
- Structured output for further automation
- Lightweight and easy to extend

---

## 👨‍💻 Author

Created by Przemysław Senderski