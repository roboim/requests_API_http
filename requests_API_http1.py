import requests


class Superhero_Api:

    def get_statistics(self):
        url = "https://akabab.github.io/superhero-api/api/all.json"
        response = requests.get(url, headers={'User-agent': 'netology'})
        return response.json()


def get_heroes_powerstats(heroes_list, stat_name) -> dict:
    superhero_api = Superhero_Api()
    data_all = superhero_api.get_statistics()
    heroes_stat = {}
    for superhero in heroes_list:
        [heroes_stat.setdefault(hero['name'], hero['powerstats'][stat_name]) for hero in data_all if hero['name'] == superhero]
    return heroes_stat


if __name__ == '__main__':
    heroes = ['Hulk', 'Captain America', 'Thanos']
    stat = 'intelligence'

    heroes_dict = get_heroes_powerstats(heroes, stat)
    res = sorted(heroes_dict.items(), key=lambda item: item[1], reverse=True)
    print(res[0][0])
