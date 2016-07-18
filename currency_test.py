from currency import Currency,
import nose.tools import assert_raises

def test_create_currency_with_amount_and_code():
    one_dollar = Currency(1, 'USD')

    assert one_dollar.amount == 1
    assert one_dollar.currency_code == 'USD'

def test_currencys_can_be_equal():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 == curr2

def test_currencys_with_different_amounts_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 != curr2

def test_currencys_with_different_currency_codes_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')

    assert curr1 != curr2

def test_currencys_with_same_currency_codes_can_be_added():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 + curr2 == (100, 'USD')

def test_currencys_with_same_currency_codes_can_be_subtracted():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(1, 'USD')

    assert curr1 - curr2 == (98, 'USD')

def test_raise_error_when_currencys_are_added():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')

    assert_raises(DifferentCurrencyCodeError, Currency, __add__, curr1, curr2)

def test_raise_error_when_currencys_are_subtracted():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')

    assert_raises(DifferentCurrencyCodeError, Currency, __sub__, curr1, curr2)
