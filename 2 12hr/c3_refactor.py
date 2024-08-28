def calculate_tip(price: float, tip_percentage=20):
    return price * (tip_percentage / 100)


print(calculate_tip(100, 10))
print(calculate_tip(tip_percentage=25, price=100))
print(calculate_tip(100))


def weather_to_emoji(weather: str):
    """
    Takes in a string and retruns an emoji showing what you should do in that weather.
    Expected inputs: 'rain', 'thunderstorm', 'cloudy', 'sunny',

    >>> weather_to_emoji('rain')
    '☂️'

    >>> weather_to_emoji('cloudy')
    '🧥'

    >>> weather_to_emoji('thunderstorm')
    '🏠'

    >>> weather_to_emoji('sunny')
    '😎'
    """
    if weather == "rain":
        return "☂️"
    elif weather == "cloudy":
        return "🧥"
    elif weather == "thunderstorm":
        return "🏠"
    elif weather == "sunny":
        return "😎"
    else:
        raise BaseException(f"Unknown weather: {weather}")
    # I am still INSIDE weather_to_emoji


# I an OUTSIDE


print(weather_to_emoji("rain"))
print(weather_to_emoji("cloudy"))
print(weather_to_emoji("thunderstorm"))
print(weather_to_emoji("sunny"))
# print(weather_to_emoji('hailing'))


def sum(a: int, b: int) -> int:
    """
    Takes 2 integers, retruns their sum
    >>> sum(1, 2)
    3
    """

    return a + b
