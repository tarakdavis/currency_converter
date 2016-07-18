class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code
