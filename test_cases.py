def test_addition():
    assert 2 + 3 == 5, "Addition failed"

def test_uppercase():
    assert "python".upper() == "PYTHON", "Uppercase conversion failed"

def test_file_write_read():
    with open("sample.txt", "w") as f:
        f.write("hello")

    with open("sample.txt", "r") as f:
        content = f.read()

    assert content == "hello", "File read/write failed"

def test_intentional_failure():
    assert 10 * 2 == 25, "Intentional failure"

def get_test_cases():
    return [
        test_addition,
        test_uppercase,
        test_file_write_read,
        test_intentional_failure
    ]
