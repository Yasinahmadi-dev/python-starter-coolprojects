# Python Automation Starter Kit

Three foundational Python automation scripts built on Windows 11 covering local file routing, hardware telemetry, and REST API ingestion.

## Scripts Included

1. **`organizer.py`** — Scans a target directory using `pathlib` and `shutil`, automatically sorting files by extension into categorized subfolders (`PDFs/`, `Documents/`, `Images/`, `Spreadsheets/`).
2. **`monitor.py`** — Polls CPU, RAM, and disk utilization via `psutil` and logs timestamped threshold alerts to `system_alerts.log`.
3. **`price_tracker.py`** — Queries live cryptocurrency market data from the CoinGecko REST API using `requests`, evaluates target price thresholds, and handles network timeouts/HTTP errors gracefully.

## Setup & Usage

```bash
pip install -r requirements.txt
python price_tracker.py