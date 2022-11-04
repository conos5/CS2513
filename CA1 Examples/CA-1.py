# J - remember it is 6:45am on Sunday when I decided to do this :)

# My initial CA-1 thoughts on code
# create a very simple Pokédex, using Python Classes...
# starting with Pokemon Black/White 2 - Oshawatt, Snivy and Tepig

# let's begin with the Pokemon Class:
# so based on these links, what do I add to my base parent class:
# https://www.pokemon.com/us/pokedex/oshawott
# https://www.pokemon.com/us/pokedex/snivy

# is it type, waeaknesses, details, stats?  where do I start.

# let's start with all 3, so first decision what is the type of these inputs:

from typing import ClassVar

class Pokemon:
    '''
    very simple Pokédex, using Python Classes...
    '''

    # instance private attributes
    # Encapsulation - the idea of restricting access to methods 
    # and attributes in a class
    __pokemon_name: ClassVar[str] # string name
    __pokemon_type: ClassVar[dict[list]] # dictionary of types in a list
    __pokemon_weaknesses: ClassVar[dict[list]] # dictionary of weaknesses in a list
    __pokemon_details: ClassVar[dict] # dictionary of details
    # new attribute
    __pokemon_stats: ClassVar[dict[int]] # dictionary of stats, as ints


    # create my default constructor, using *args and *kwargs - remember to add hints
    def __init__(self, class_name, *args:str, **kwargs:str) -> None:

        # I set the first param as the class name, or the Pokemon Name
        self.__pokemon_name = class_name

        # I then use the **kwargs to pass in a dictionary of details, so I can build my parent class
        # small bit of logic needed here - to stop crashes
        if len(kwargs) != 0:
            if "type" in kwargs.keys():
                self.__pokemon_type = kwargs["type"]
            else:
                raise PokemonExceptionError("Seems to be a problem with constructor type for "+str(self.__class__.__name__))

            if "weaknesses" in kwargs.keys():
                self.__pokemon_weaknesses = kwargs["weaknesses"]
            else:
                raise PokemonExceptionError("Seems to be a problem with constructor weaknesses for "+str(self.__class__.__name__))

            if "details" in kwargs.keys():
                self.__pokemon_details = kwargs["details"]
            else:
                raise PokemonExceptionError("Seems to be a problem with constructor details for "+str(self.__class__.__name__))

            # new attributes added after some thought on the pokedex
            # these are the values that change during battle
            if "stats" in kwargs.keys():
                self.__pokemon_stats = kwargs["stats"]
            else:
                raise PokemonExceptionError("Seems to be a problem with constructor stats for "+str(self.__class__.__name__))


    # I now have some simple attributes, so lets add some getter/setters
    # let's use both types of properties - version 1
    # so I added an option to change the Pokemon Name
    # but is this right?  do I change the class/type if a pokemon evolves or just all of its details?
    # lets leave for now...  but this might be changed
    @property
    # get the pokemon name
    def pokemon_name(self):
        return self.__pokemon_name

    @pokemon_name.setter
    # set the pokemon name
    def pokemon_name(self, toa: str):
        self.__pokemon_name = toa

    # setters and getters - properties - version 2
    # get the pokemon type
    def get_pokemon_type(self) -> dict:
        return self.__pokemon_type

    # set the pokemon type
    def set_pokemon_type(self, top: dict) -> None:
        # lets call the new private method
        self.__check_pokemon_dict_values(self.__pokemon_type, top)

    # how I access the attributes just using it's name
    pokemon_type = property(get_pokemon_type, set_pokemon_type)

    # I don't add the getters/setters for the other attributes, as I feel 
    # I don't need to, as these should not change

    # but I will add a new attribute called "Stats", as these can change, as the pokemon grows...
    # get the pokemon stats
    def get_pokemon_stats(self) -> dict:
        return self.__pokemon_stats

    # set the pokemon stats
    def set_pokemon_stats(self, sop: dict) -> None:
        # lets call the new private method
        self.__check_pokemon_dict_values(self.__pokemon_stats, sop)
        
    # how I access the attributes just using it's name
    pokemon_stats = property(get_pokemon_stats, set_pokemon_stats)

    # the code in set_pokemon_stats and get_pokemon_type is very similar, so I created a private function
    # for code similarity
    def __check_pokemon_dict_values(self, original_dict: dict, input_dict: dict) -> dict:
        '''
        check the contents of input_dict for keys in original_dict\n
        if all okay, update original_dict and return it
        '''
        # small bit of logic here.
        # if a key does not exist in stats, then do not add it and return an error
        for key in input_dict.keys():
            # if the key is in stats
            if key in original_dict.keys():
                # then change the value for the stats key
                original_dict[key] = input_dict[key]
            # otherwise issue a Pokemon Exception Error message
            else:
                raise PokemonExceptionError("Seems to be a problem with the input key: \""+str(key)+"\" for "+str(self.__class__.__name__))

        return original_dict


    def __str__(self) -> str:
        '''
        return a  string of this class
        '''
        # just incase the pokemon has multiple input types
        type_string = ""
        for val in self.__pokemon_type["type"]:
            type_string += val+"/"

        return "\nMy name is "+ self.__class__.__name__ +\
            " and I am a " + type_string[:-1] +\
                 " type. "+self.__pokemon_details["title"]

    # so now I have name, type and stats as inputs to this parent class


# just added this for a bit of fun :)
class PokemonExceptionError(Exception):
    pass

# create some empty child classes
# one item I can add here is the pokedex number, as this is specific to the child, not the parent
class Oshawott(Pokemon):
    '''
    Oshawatt - # 501
    '''
    # create the pokedex number for this pokemon
    __pokemon_number: ClassVar[int] # int pokedex number

    # create my default constructor, using *args and *kwargs - remember to add hints
    # no need for class name here, as I can get it from the class
    def __init__(self, *args:str, **kwargs:str) -> None:
        super().__init__(str(self.__class__.__name__), *args, **kwargs)

        # if the number does not exist, raise an exception
        if "number" in kwargs.keys():
            self.__pokemon_number = kwargs["number"]
        else:
            raise PokemonExceptionError("Pokemon Number is missing for "+str(self.__class__.__name__))

    # I do not add getters/setters, as I do not want to change the pokedex number

class Snivy(Pokemon):
    pass

class Tepig(Pokemon):
    pass

# lets now add some calls and create some Pokemon
oshawatt_number=501
oshawatt_type = {"type": ["Water"]}
oshawatt_weaknesses = {"weaknesses": ["Grass", "Electric"]}
oshawatt_details = {"Height": "1:08", "Weight": 13.0, "Gender": "Male", \
    "Category": "Sea Otter", "Abilities": "Torrent", \
        "title": "The scalchop on my stomach isn’t just used for battle , it "+\
                    "can be used to break open hard berries as well...."}
oshawatt_stats = {"HP": 4, "Attack": 4, "Defense": 3,"Special Attack": 4, "Special Defense": 3, "Speed": 3}

# let's create Oshawatt
oshawatt = Oshawott(number=oshawatt_number, type=oshawatt_type, weaknesses=oshawatt_weaknesses, details=oshawatt_details, stats=oshawatt_stats)

# lets see what I can print, change or break?
# oshawatt2 with no type 
# uncomment to create an error
# oshawatt2 = Oshawott(number=oshawatt_number, weaknesses=oshawatt_weaknesses, details=oshawatt_details, stats=oshawatt_stats)
# __main__.PokemonExceptionError: Seems to be a problem with constructor type for Oshawott

# get some of the class attributes
print(oshawatt.pokemon_type)
print(oshawatt.pokemon_name)
print(oshawatt.pokemon_stats)

# update the stats
print(oshawatt.set_pokemon_stats({"Attack": 5})) # update Attack
print(oshawatt.pokemon_stats)

# update stats, but with the wrong key
# uncomment to create an error
# print(oshawatt.set_pokemon_stats({"Attacker": 5})) # update Attacker - should not work
# __main__.PokemonExceptionError: Seems to be a problem with these Stats for Oshawott - perfect
print(oshawatt.pokemon_stats)

# let's print "Oshawatt"
print(oshawatt)