'''
But you are still returning some stuff from your pokemon function which you aren't using anywhere because you are
maintaining some state (pokemon_moves and pokemon_name lists) outside of the function so you could change this
slightly to:
'''

def pokemon():
    pokemon_name = []
    pokemon_moves = []

    for id in pokemon_list:
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id)
        response = requests.get(url)
        pokemon = response.json()
        pokemon_name.append(pokemon['name'])
        pokemon_moves.append(pokemon['moves'])
    return pokemon_name, pokemon_moves

'''
Then where you use it,
'''

pokemon_name, pokemon_moves = pokemon()

'''
also, you might want to process the moves some more and just pick the name of the moves
'''