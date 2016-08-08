from currency_converter import CurrencyConverter
from currency_converter import UnknownCurrencyCodeError
from currency import Currency
from nose.tools import assert_raises

conversion_rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}


def test_create_converter_with_conversion_rates():
    converter = CurrencyConverter(conversion_rates)
    assert converter.rates == conversion_rates


def test_convert_with_same_code_returns_itself():
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'USD'
    result = converter.convert(currency, convert_to_code)
    assert result == Currency(1, 'USD')


def test_convert_with_diff_code_converted_currency():
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'JPY'
    result = converter.convert(currency, convert_to_code)
    assert result == Currency(120, 'JPY')


def test_convert_with_unknown_code_raises_error():
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'LOL'

    with assert_raises(UnknownCurrencyCodeError):
        converter.convert(currency, convert_to_code)
