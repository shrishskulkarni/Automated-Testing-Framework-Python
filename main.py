"""
main.py
-------
Entry point for running all test cases in this mini testing framework.

Features:
- Runs all tests from test_cases.py
- Handles pass/fail without stopping the full run
- Logs detailed results with timestamps to results.txt
- Prints clear terminal output with optional verbose mode
- Shows final execution summary
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

from colorama import just_fix_windows_console
from logger import log_message, log_run_footer, log_run_header
from test_cases import get_test_cases


class Colors:
    """ANSI color codes for terminal output."""

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"


def color_text(text: str, color: str, use_color: bool) -> str:
    """Return colored text if color output is enabled."""
    if not use_color:
        return text
    return f"{color}{text}{Colors.RESET}"


def export_results(
    results, passed: int, failed: int, output_dir: Path | None = None
) -> tuple[Path, Path]:
    """
    Export test results to JSON and CSV files.

    Returns:
        tuple[Path, Path]: (json_file_path, csv_file_path)
    """
    if output_dir is None:
        output_dir = Path(__file__).parent / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = output_dir / f"results_{timestamp}.json"
    csv_path = output_dir / f"results_{timestamp}.csv"

    payload = {
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": failed,
        },
        "results": results,
    }

    with json_path.open("w", encoding="utf-8") as json_file:
        json.dump(payload, json_file, indent=2)

    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "status", "details"])
        writer.writeheader()
        writer.writerows(results)

    return json_path, csv_path


def run_all_tests(
    verbose: bool = False,
    use_color: bool = True,
    include_intentional_fail: bool = False,
):
    """
    Execute all tests and collect a detailed result for each one.

    Returns:
        tuple: (results, passed_count, failed_count)
    """
    tests = get_test_cases(include_intentional_failure=include_intentional_fail)
    results = []
    passed_count = 0
    failed_count = 0

    log_run_header()

    for test_func in tests:
        test_name = test_func.__name__
        try:
            test_func()
            status = "PASS"
            details = "Test executed successfully."
            passed_count += 1
        except AssertionError as error:
            status = "FAIL"
            details = str(error)
            failed_count += 1
        except Exception as error:  # Catch unexpected runtime exceptions gracefully.
            status = "ERROR"
            details = f"Unexpected exception: {error}"
            failed_count += 1

        results.append(
            {
                "name": test_name,
                "status": status,
                "details": details,
            }
        )

        # Log each test result to file.
        log_message(f"{test_name} -> {status}: {details}")

        # Print each test result to terminal.
        if status == "PASS":
            status_text = color_text("[PASS]", Colors.GREEN, use_color)
        else:
            status_text = color_text(f"[{status}]", Colors.RED, use_color)

        if verbose:
            print(f"{status_text} {test_name} - {details}")
        else:
            print(f"{status_text} {test_name}")

    log_run_footer(total=len(tests), passed=passed_count, failed=failed_count)
    return results, passed_count, failed_count


def print_summary(total: int, passed: int, failed: int, use_color: bool = True) -> None:
    """Display end-of-run summary in terminal."""
    print("\n" + "=" * 45)
    print("Test Execution Summary")
    print("=" * 45)
    print(f"Total tests : {total}")
    print(color_text(f"Passed      : {passed}", Colors.GREEN, use_color))
    print(
        color_text(
            f"Failed      : {failed}",
            Colors.RED if failed > 0 else Colors.GREEN,
            use_color,
        )
    )
    if failed > 0:
        print(color_text("Overall     : SOME TESTS FAILED", Colors.YELLOW, use_color))
    else:
        print(color_text("Overall     : ALL TESTS PASSED", Colors.GREEN, use_color))
    print("=" * 45)


def parse_args():
    """Parse command-line arguments for runner options."""
    parser = argparse.ArgumentParser(description="Run the automated testing framework.")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed reason/message for each test case.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output in terminal.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="Directory to save JSON/CSV reports (default: reports).",
    )
    parser.add_argument(
        "--include-intentional-fail",
        action="store_true",
        help="Include the intentional failure test for demo purposes.",
    )
    return parser.parse_args()


def main() -> int:
    """Program entry point."""
    args = parse_args()
    just_fix_windows_console()
    use_color = not args.no_color
    output_dir = Path(args.output_dir)

    print("Running automated test suite...\n")
    results, passed, failed = run_all_tests(
        verbose=args.verbose,
        use_color=use_color,
        include_intentional_fail=args.include_intentional_fail,
    )
    total = len(results)
    print_summary(total=total, passed=passed, failed=failed, use_color=use_color)
    json_file, csv_file = export_results(
        results=results,
        passed=passed,
        failed=failed,
        output_dir=output_dir,
    )

    print("\nDetailed logs saved to results.txt")
    print(f"JSON report saved to {json_file}")
    print(f"CSV report saved to {csv_file}")
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
