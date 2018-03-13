# altiMether - Altcoin Autotrading

# Description
AltiMether uses the CCXT python API bindings for various cryptocurrency exchanges
to automatically perform cross-currency trades based on market trends and other
user-defined parameters.

Initially, altiMether will be implemented for the Bleutrade Exchange.

# Requirements
ccxt
python >= 3.3

# Installation

1)
```
pip install ccxt
```
2)
```
git clone https://github.com/aloerch/altiMether.git
```
3)
Edit the altiMether.py to include your Bleutrade API key info.

4)
Run it
```
python3 altiMether.py
```

# Notes
This pre-alpha version currently only provides information about market values
of coins and user balances on Bleutrade.

When automated trading is implemented, it will account for a number of variables,
including the value and trends of various altcoins compared to other altcoins,
bitcoin, and US Dollars; it will also take into consideration trading fees,
account balance thresholds, and provide for trading of profits while safeguarding
principle investments. 
