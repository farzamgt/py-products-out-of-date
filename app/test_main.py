import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products_with_mocked_date():
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        },
    ]

    class MockDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2022, 2, 5)

    with patch("app.main.datetime.date", MockDate):
        result = outdated_products(products)

    assert result == ["duck"]
