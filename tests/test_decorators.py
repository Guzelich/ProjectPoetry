from fileinput import filename
import pytest
from src.decorators import log
import os


# Вспомогательная функция для очистки файла лога после тестов
@pytest.fixture
def log_file(tmp_path):
    log_path = tmp_path / "test_log.txt"
    yield str(log_path)
    # Файл будет автоматически удалён после завершения теста (подсказка Германа, если что на удаление)


def test_successful_function_call(log_file):
    @log(filename=log_file)
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

    with open(log_file, "r") as f:
        content = f.read()
    assert "add ok" in content
    assert "result:" in content


def test_function_with_exception(log_file):
    @log(filename=log_file)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open(log_file, "r") as f:
        content = f.read()
    assert "divide error: ZeroDivisionError" in content
    assert "args=(1, 0)" in content


def test_function_with_kwargs(log_file):
    @log(filename=log_file)
    def greet(name="World"):
        return f"Hello, {name}!"

    result = greet(name="German")
    assert result == "Hello, German!"

    with open(log_file, "r") as f:
        content = f.read()
    assert "greet ok" in content
    assert "kwargs={'name': 'German'}" not in content  # kwargs не выводятся при успехе


def test_function_with_exception_and_kwargs(log_file):
    @log(filename=log_file)
    def risky_func(value, should_fail=False):
        if should_fail:
            raise ValueError("Something went wrong")
        return value

    with pytest.raises(ValueError):
        risky_func(42, should_fail=True)

    with open(log_file, "r") as f:
        content = f.read()
    assert "risky_func error: ValueError: Something went wrong" in content
    assert "kwargs={'should_fail': True}" in content


def test_multiple_calls_append_to_log(log_file):
    @log(filename=log_file)
    def echo(x):
        return x

    echo(1)
    echo(2)

    with open(log_file, "r") as f:
        lines = f.readlines()
    assert len(lines) == 2
    assert "echo ok" in lines[0]
    assert "echo ok" in lines[1]
