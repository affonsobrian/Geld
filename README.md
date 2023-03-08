# Geld

A library to easily handle currency conversions.


## Official documentation
- We do not have an official documentation yet, we are working on this.

## Data origin
Currently the API uses the https://theforexapi.com/api to get the values. (If the forex API the default client will not work)
We are working to make it extensable so you can pick info from different sources in the future.


## How to install

```
pip install geld
```

## How to use the Sync Client

```
from geld.clients import sync_client as client
result = client.convert_currency("USD", "BRL", 25, "2021-12-05")
```