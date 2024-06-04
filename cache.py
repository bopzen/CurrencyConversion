# Dictionary variable used for saving the cached rates
cache = {}


# Getting Historical Rate from cache if existing
def get_rate_from_cache(date, base_currency, target_currency):
    if base_currency in cache and date in cache[base_currency] and target_currency in cache[base_currency][date]:
        return cache[base_currency][date][target_currency]
    return None


# Saving rate to cache
def save_cache(date, base_currency, target_currency, rate):
    if base_currency not in cache:
        cache[base_currency] = {}
        if date not in cache[base_currency]:
            cache[base_currency][date] = {}
    cache[base_currency][date][target_currency] = rate
