from test_cases import get_test_cases
from logger import log_result

def main():
    tests = get_test_cases()
    total = len(tests)
    passed = 0

    print("Running Tests...\n")

    for test in tests:
        name = test.__name__
        try:
            test()
            print(f"[PASS] {name}")
            log_result(name, "PASS")
            passed += 1
        except Exception as e:
            print(f"[FAIL] {name} - {e}")
            log_result(name, "FAIL", str(e))

    print("\nSummary:")
    print(f"Total: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")

if __name__ == "__main__":
    main()
