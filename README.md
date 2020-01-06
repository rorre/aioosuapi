# aioosuapi

Asynchronous osu! api wrapper

Not recommended for use. This module scrapes non-api pages. It's a temporary solution until osu-web api becomes public.

### To install type this in terminal: 

`pip3 install git+https://github.com/Kyuunex/aioosuapi.git@v2-parsed`


# Quick example:
```python
from aioosuwebapi import aioosuwebapi

osuweb = aioosuwebapi()

result = await osuweb.get_user("1623405") 

print(result['name'])
# Okoratu
```
