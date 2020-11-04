import requests

def get_starships_with_pilots():
    r = requests.get("https://swapi.dev/api/starships")
    next_page = r.json().get("next", None)
    pilot_cache = dict()
    while True:
        results = r.json().get("results")
        for starship in results:
            print(starship.get("name"))
            pilot_names = []
            for pilot_url in starship.get("pilots"):
                if pilot_url in pilot_cache.keys():
                    pilot = pilot_cache[pilot_url]
                else:
                    pilot = requests.get(pilot_url).json()
                    pilot_cache[pilot_url] = pilot
                pilot_names.append(pilot.get("name"))
            print(f"\tPilots: {', '.join(pilot_names) if pilot_names else None}")
        if next_page:
            r = requests.get(next_page)
            next_page = r.json().get("next", None)
        else:
            break


if __name__ == '__main__':
    get_starships_with_pilots()