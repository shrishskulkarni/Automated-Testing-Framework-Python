# Automated Testing Framework (Python)

A beginner-friendly yet professional Python project that demonstrates core testing and automation concepts:
assertions, modular test execution, resilient failure handling, timestamped logging, CLI options, and report exports.

## Why This Project

This project is designed to showcase practical QA/Automation fundamentals in a clean codebase suitable for a resume or portfolio.

## Features

- Modular structure with dedicated files for test cases, logging, and execution
- Assertion-based test cases (2 pass + 1 intentional fail demo)
- Graceful exception handling (one failure does not stop the test run)
- Clear terminal output with optional color and verbose mode
- End-of-run summary (total, passed, failed)
- Persistent timestamped log file (`results.txt`)
- Export reports to JSON and CSV with timestamped filenames
- Custom report directory support via CLI

## Project Structure

```text
Automated-Testing-Framework-Python/
├── main.py
├── test_cases.py
├── logger.py
├── results.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10+ (works on Windows/macOS/Linux)

No external libraries are required.

## How To Run

From the project root:

```bash
python main.py
```

### Useful CLI Options

```bash
# Detailed per-test messages
python main.py --verbose

# Disable terminal colors
python main.py --no-color

# Save JSON/CSV reports to a custom folder
python main.py --output-dir custom_reports
```

## Example Output

```text
Running automated test suite...

[PASS] test_addition
[PASS] test_string_uppercase
[FAIL] test_intentional_failure

=============================================
Test Execution Summary
=============================================
Total tests : 3
Passed      : 2
Failed      : 1
Overall     : SOME TESTS FAILED
=============================================
```

## Output Files

- `results.txt` -> timestamped execution logs
- `reports/results_<timestamp>.json` -> structured report data
- `reports/results_<timestamp>.csv` -> tabular report data

## Screenshots / Demo

Add terminal screenshots or a short GIF here for your portfolio:

- `assets/demo-terminal-output.png`
- `assets/demo-run.gif`

> Tip: You can record a short GIF showing `--verbose` and summary output.

## Resume Talking Points

- Built a custom Python test framework with modular architecture and CLI controls
- Implemented robust pass/fail tracking and non-blocking exception handling
- Added automated log and multi-format report generation (TXT/JSON/CSV)
- Improved usability with colorized terminal output and clear test summaries

## Future Improvements

- Add support for test discovery from multiple files
- Add tags or categories for selective test execution
- Integrate with CI (GitHub Actions) to run tests on every push
- Generate HTML report output
