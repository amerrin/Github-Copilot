import datetime


def parse_expenses(expenses_string):
    """Parse the list of expenses and return the list of triples (date, value, currency).
    Ignore lines starting with #.
    Parse the date using datetime
    """

    expenses = []
    for line in expenses_string.splitlines():
        if not line.startswith("#"):
            date, value, currency = line.split()
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            value = float(value)
            expenses.append((date, value, currency))
    return expenses

"""write a unit test for this function parse_expenses()"""
def test_parse_expense():
    assert parse_expenses("# test") == []
    assert parse_expenses("") == []
    assert parse_expenses("2019-09-01 100 USD") == [(datetime.datetime(2019, 9, 1), 100, "USD")]
    assert parse_expenses("2019-09-01 100 USD\n2019-09-03 200 EUR\n2019-09-10 300 JPY") == [
        (datetime.datetime(2019, 9, 1), 100, "USD"),
        (datetime.datetime(2019, 9, 3), 200, "EUR"),
        (datetime.datetime(2019, 9, 10), 300, "JPY"),
    ]
    assert parse_expenses("2019-09-01 100 USD\n2019-09-03 200 EUR\n2019-09-10 300 JPY\n# test") == [
        (datetime.datetime(2019, 9, 1), 100, "USD"),
        (datetime.datetime(2019, 9, 3), 200, "EUR"),
        (datetime.datetime(2019, 9, 10), 300, "JPY"),
    ]
    assert parse_expenses("2019-09-01 100 USD\n2019-09-03 200 EUR\n2019-09-10 300 JPY\n# test\n") == [
        (datetime.datetime(2019, 9, 1), 100, "USD"),
        (datetime.datetime(2019, 9, 3), 200, "EUR"),
        (datetime.datetime(2019, 9, 10), 300, "JPY"),
    ]

"""run the unit test that was created"""

if __name__ == "__main__":
    test_parse_expense()
    print("Everything passed")

