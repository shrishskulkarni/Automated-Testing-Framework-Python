"""
logger.py
---------
Handles writing test execution results to results.txt with timestamps.
"""

from datetime import datetime
from pathlib import Path


RESULTS_FILE = Path(__file__).parent / "results.txt"


def log_message(message: str) -> None:
    """Append a single timestamped log line to results.txt."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with RESULTS_FILE.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def log_run_header() -> None:
    """Write a readable section header for each test run."""
    separator = "-" * 60
    log_message(separator)
    log_message("Starting test run")


def log_run_footer(total: int, passed: int, failed: int) -> None:
    """Write test run summary details."""
    log_message(f"Summary -> Total: {total}, Passed: {passed}, Failed: {failed}")
    log_message("Test run completed")
