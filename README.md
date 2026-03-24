# Automated Testing Framework (Python)

## Overview

This project is a simple automated testing framework built using Python. It is designed to execute multiple test cases, detect failures, and log results in a structured manner.

The project demonstrates core concepts of test automation, including test execution, failure handling, and logging—similar to basic workflows used in real-world software testing environments.

---

## Features

* Executes multiple test cases automatically
* Detects and reports pass/fail status using assertions
* Continues execution even if some tests fail
* Logs test results with timestamps for debugging
* Simple and modular structure for easy understanding

---

## Project Structure

```
main.py         # Executes all test cases
test_cases.py   # Contains test functions
logger.py       # Handles logging of results
```

---

## How It Works

* Test cases are defined using Python functions and assertions
* The main script runs all test cases sequentially
* Each test result is captured and logged
* Failures are recorded without stopping the execution of other tests

---

## Example Test

```python
def test_addition():
    assert 2 + 2 == 4
```

---

## How to Run

1. Make sure Python is installed
2. Run the following command:

```
python main.py
```

3. View results in the terminal and in `results.txt`

---

## Skills Demonstrated

* Python programming
* Test automation fundamentals
* Debugging and failure handling
* File handling and logging
* Modular code design

---

## Limitations

This is a basic framework intended for learning purposes. It can be extended to support:

* API testing
* File validation
* Integration with CI/CD pipelines
* Advanced reporting

---

## Conclusion

This project demonstrates a foundational understanding of automated testing and provides a base that can be extended for more complex testing scenarios.
