# currency_converter
One of class will represent an amount of currency (a real-world thing you can point to), and the second will represent a currency converter (arguably a real-world person, but actually a set of procedures).

Currency objects

Created with an amount and a currency code.
Equal to another Currency object with the same amount and currency code.
NOT equal another Currency object with different amount or currency code.
Able to be added to another Currency object with the same currency code.
Able to be subtracted by another Currency object with the same currency code.
Raises a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
Able to be multiplied by an int or float and return a Currency object.
Currency() able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.

CurrencyConverter objects

Initialized with a dictionary of currency codes to conversion rates.
Able to take a Currency object and a requested currency code that is the same currency code as the Currency object's and return a Currency object equal to the one passed in. That is, currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD').
Able to take a Currency object that has one currency code it knows and a requested currency code and return a new Currency object with the right amount in the new currency code.
Able to be created with a dictionary of three or more currency codes and conversion rates. An example would be this: {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}, which implies that a dollar is worth 0.74 euros and that a dollar is worth 120 yen, but also that a euro is worth 120/0.74 = 162.2 yen.
Able to convert Currency in any currency code it knows about to Currency in any other currency code it knows about.
Raises an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.
