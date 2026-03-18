from script import MedianCoffeeReport, read_files
import pytest

def test_calculate_median():
    data = {
        "Иван": [10.0, 20.0, 15.0],
        "Маша": [5.0, 30.0]
    }
    report = MedianCoffeeReport()
    result = report.calculate(data)
    assert result["Иван"] == 15.0
    assert result["Маша"] == 17.5

def test_read_files(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("student,coffee_spent\nИван,10\nИван,20\nМаша,5\n")
    result = read_files([str(file)])
    assert result["Иван"] == [10.0, 20.0]
    assert result["Маша"] == [5.0]

def test_invalid_file():
    with pytest.raises(SystemExit):
        read_files(["несуществующий_файл.csv"])




