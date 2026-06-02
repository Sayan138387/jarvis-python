import requests

def get_joke():

    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    data = response.json()

    return f"{data['setup']} ... {data['punchline']}"


def get_quote():

    url = "https://api.quotable.io/random"

    response = requests.get(url)

    data = response.json()

    return f"{data['content']} By {data['author']}"


def get_fact():

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)

    data = response.json()

    return data['text']