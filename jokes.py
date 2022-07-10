from jokeapi import Jokes


def print_joke():
    j = await Jokes()
    joke = await j.get_joke()
    if joke["type"] == "single":
        return joke["joke"]
    else:
        output = f'''{joke["setup"]}\n{joke["delivery"]}'''
        return output
