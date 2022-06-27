# # Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render


import random
import pprint
import requests as HTTP_Client
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("""<h1>Welcome to the HomePage<br>
    Click the Random Button to Get Started!<br><h1>
    <form action="/random">
        <button type="submit">Random Starter</button>
    </form>""")


# -=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# working code from session with michael
# needed to install requests to make work: python -m pip install requests


# import os
# import json

pp = pprint.PrettyPrinter(indent=2, depth=2)

# # Create your views here.

# change to random_team when adding functions
def random_team(request):
    # Holds our team
    poke_team = []

    # used to prevent duplicates
    used_names = []

    # Get our starting pokemon
    # rand_num = str(random.randrange(899) + 1)
    rand_num = str(random.randint(1, 898))

    # url + ?pokemon=1 returns Bulbosaur Team
    # Allows user to specify the first pokemon
    if request.GET.get('pokemon'):
        if int(request.GET.get('pokemon')) > 0 and int(request.GET.get('pokemon')) < 899:
            poke_id = request.GET.get('pokemon')
        else:
            # Generates a random pokemon if they input an invalid ID
            poke_id = rand_num
    else:
        # Generates a random pokemon if none are specified
        poke_id = rand_num

    # Set our endpoint with the starting pokemon
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"

    API_response = HTTP_Client.get(endpoint)
    responseJSON = API_response.json()

    # Add that pokemon to our team
    poke_team.append(responseJSON)

    # Add that pokemon to our used names list
    used_names.append(responseJSON['name'])

    # New endpoint for specific type
    poke_type = responseJSON['types'][0]['type']['url']

    # Getting data for that pokemon type using the new endpoint
    new_API_response = HTTP_Client.get(poke_type)
    new_responseJSON = new_API_response.json()

    # Find out how many pokemon share this type
    num_of_type = len(new_responseJSON['pokemon'])

    # Fill out rest of team
    while len(used_names) < 6:
        new_id = random.randrange(num_of_type)
        new_pokemon = new_responseJSON['pokemon'][new_id]['pokemon']

        # Grab a new pokemon's url so we can grab it's name and sprite
        new_url = new_pokemon['url']
        API_response = HTTP_Client.get(new_url)
        responseJSON = API_response.json()

        # Add pokemon to our team if it is not a duplicate
        if responseJSON['name'] not in used_names:
            poke_team.append(responseJSON)
            used_names.append(responseJSON['name'])

    pp.pprint(poke_team)

    response = render(request, 'pokemon/index.html',
                      {'poke_team': poke_team})
    return response

# -=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# def random_team(request):
#     return index(request)

# makes button work

# -===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# create a type based button
# endpoint + type/0-18
# order of types on api site
# type shadow and unknown type/10001, 10002 refer to just two pokemon, kinda new, not super important
# def type_team(request):

#     types = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
#     # need top figure out how to get button to pass number variable to function or internally desginate which item in types list to add to api call
#     endpoint = f"https://pokeapi.co/api/v2/type/{poke_id}"

#     API_response = HTTP_Client.get(endpoint)
#     responseJSON = API_response.json()

#     # Add that pokemon to our team
#     poke_team.append(responseJSON)

#     # Add that pokemon to our used names list
#     used_names.append(responseJSON['name'])

#     # New endpoint for specific type
#     poke_type = responseJSON['types'][0]['type']['url']

#     # Getting data for that pokemon type using the new endpoint
#     new_API_response = HTTP_Client.get(poke_type)
#     new_responseJSON = new_API_response.json()

#     # Find out how many pokemon share this type
#     num_of_type = len(new_responseJSON['pokemon'])

#     # Fill out rest of team
#     while len(used_names) < 6:
#         new_id = random.randrange(num_of_type)
#         new_pokemon = new_responseJSON['pokemon'][new_id]['pokemon']

#         # Grab a new pokemon's url so we can grab it's name and sprite
#         new_url = new_pokemon['url']
#         API_response = HTTP_Client.get(new_url)
#         responseJSON = API_response.json()

#         # Add pokemon to our team if it is not a duplicate
#         if responseJSON['name'] not in used_names:
#             poke_team.append(responseJSON)
#             used_names.append(responseJSON['name'])

#     pp.pprint(poke_team)

#     response = render(request, 'pokemon/index.html',
#                       {'poke_team': poke_team})
#     return response


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# learning how to use search template
# https://learndjango.com/tutorials/django-search-tutorial

# def search(request):
#     # Holds our team
#     poke_team = []

#     # used to prevent duplicates
#     used_names = []

#     # Get our starting pokemon
#     # rand_num = str(random.randrange(899) + 1)
#     # rand_num = str(random.randint(1, 898))

#     # url + ?pokemon=1 returns Bulbosaur Team
#     # Allows user to specify the first pokemon
#     # if request.GET.get('pokemon'):
#     #     if int(request.GET.get('pokemon')) > 0 and int(request.GET.get('pokemon')) < 899:
#     #         poke_id = request.GET.get('pokemon')
#     #     else:
#     #         # Generates a random pokemon if they input an invalid ID
#     #         poke_id = rand_num
#     # else:
#     #     # Generates a random pokemon if none are specified
#     #     poke_id = rand_num

#     poke_id = f"pokemon/{text}"
#     # Set our endpoint with the starting pokemon
#     endpoint = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"

#     API_response = HTTP_Client.get(endpoint)
#     responseJSON = API_response.json()

#     # Add that pokemon to our team
#     poke_team.append(responseJSON)

#     # Add that pokemon to our used names list
#     used_names.append(responseJSON['name'])

#     # New endpoint for specific type
#     poke_type = responseJSON['types'][0]['type']['url']

#     # Getting data for that pokemon type using the new endpoint
#     new_API_response = HTTP_Client.get(poke_type)
#     new_responseJSON = new_API_response.json()

#     # Find out how many pokemon share this type
#     num_of_type = len(new_responseJSON['pokemon'])

#     # Fill out rest of team
#     while len(used_names) < 6:
#         new_id = random.randrange(num_of_type)
#         new_pokemon = new_responseJSON['pokemon'][new_id]['pokemon']

#         # Grab a new pokemon's url so we can grab it's name and sprite
#         new_url = new_pokemon['url']
#         API_response = HTTP_Client.get(new_url)
#         responseJSON = API_response.json()

#         # Add pokemon to our team if it is not a duplicate
#         if responseJSON['name'] not in used_names:
#             poke_team.append(responseJSON)
#             used_names.append(responseJSON['name'])

#     pp.pprint(poke_team)

#     response = render(request, 'pokemon/index.html',
#                       {'poke_team': poke_team})
#     return response

# -=--=-=-=-=-=-=-=--=-=-=-=-=-==-=-=-=-=-=-=-=-=-===-

# def home(request):
#     return HttpResponse("""<h1>Welcome to the HomePage<br>
#     Click the Random Button to Get Started!<br><h1>
#     <form action="/random">
#         <button type="submit">Random Starter</button>
#     </form>""")

# works!!!

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-