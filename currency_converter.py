from currency import Currency


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, currency, convert_to_code):
        if currency.currency_code == convert_to_code:
            return currency
        else:
            if convert_to_code in self.rates:
                conversion_rate = self.rates[convert_to_code]
                amount = currency.amount * conversion_rate
                return Currency(amount, convert_to_code)
            else:
                raise UnknownCurrencyCodeError


class UnknownCurrencyCodeError(Exception):
    pass
