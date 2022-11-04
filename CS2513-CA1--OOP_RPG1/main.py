from typing import ClassVar
# character can also have horse and name what they'd like...
# you can encounter horses of varying degrees of intelligence, speed and health

class Character:
    # __DEMON_SLAYERS = {"Tanjiro Kamado": {"Health": 70, "Attack": 70, "Speed": 70, "Breathing Type": "Water"},
    #                    "Inosuke Hashibira": {"Health": 70, "Attack": 60, "Speed": 80, "Breathing Type": "Beast"},
    #                    "Zenitsu Agatsuma": {"Health": 40, "Attack": 90, "Speed": 80, "Breathing Type": "Lightning"}}

    # __DEMONS = {""}
    __hp_current = ClassVar[int]
    __hp_full = ClassVar[int]
    __att = ClassVar[int]
    __spd = ClassVar[int]
    __def = ClassVar[int]
    __lvl = 1
    # __exp_current = 0
    # __exp_full = 15 #make all characters 15 exp for level 1
    # __breathing_type = ClassVar[str]
    ''''''
        # __attack_multiplier = 0.15 #affected by swords and sometimes horses/
        # __hp_multiplier = 1 #affected by armor and sometimes horses
        # __spd_multiplier = 0.5 #affected by horses and sometimes armor
    ''''''
        # def __init__(self, char_name):
        #     # self.char_type = char_type.capitalize()
        #     self._char_name = char_name.capitalize()
        #     self._assign_attributes()
        #     # self.hp = max_hp
        #     # self.max_hp = max_hp
        #     # if self._char_name not in CHARACTERS:
        #     #     raise Exception("This character does not exist")
    '''^old init'''


    ''' ^init v3'''
    # def __str__(self):
    #     return f"{self._char_name}\n"\
    #            f"CURRENT HEALTH = {self.__hp_current} / FULL HEALTH = {self.__hp_full}\n" \
    #            f"ATTACK = {self.__att}\n" \
    #            f"SPEED = {self.__spd}\n" \
    #            f"CURRENT EXP = {self.__exp_current} / FULL EXP = {self.__exp_full}\n"\
    #            f"LEVEL = {self.__lvl}\n" \
    #            f"BREATHING TYPE = {self.__breathing_type}\n"
    # for presets and latter half of character creation

    # def _assign_type(self):
    #     char_type_dict = TYPES[self._char_name]

    # def heal(self):
    #     if self.hp < self.max_hp:
    #         self.hp += 1
    #     else:
    #         print(f"{self._char_name} is already at full health!")
    @property
    def _level(self):
        return self.__lvl
    @_level.setter
    def _level(self, new_level):
        self.__lvl = new_level

class DemonSlayer(Character):
    # __DEMON_SLAYERS = {"Tanjiro Kamado": {"Health": 70, "Attack": 70, "Defence": 70, "Speed": 70, "Breathing Type": "Water"},
    #                    "Inosuke Hashibira": {"Health": 70, "Attack": 70, "Defence": 50, "Speed": 80, "Breathing Type": "Beast"},
    #                    "Zenitsu Agatsuma": {"Health": 40, "Attack": 90, "Defence": 40, "Speed": 80, "Breathing Type": "Lightning"}}



    __DEMON_SLAYERS = {"Water": [{"Health": 70, "Attack": 70, "Defence": 70, "Speed": 70, "Name": "Tanjiro Kamado", "Master": 1},
                                 ["First Form: Water Surface Slash", "Second Form: Water Wheel", "Third Form: Flowing Dance", "Eighth Form: Waterfall Basin", "Tenth Form: Constant Flux"]],
                       "Beast": [{"Health": 70, "Attack": 70, "Defence": 50, "Speed": 80, "Name": "Inosuke Hashibira", "Master": 1},
                                 ["First Fang: Pierce", "Second Fang: Slice ", "Third Fang: Devour ", "Fourth Fang: Slice 'n' Dice", "Fifth Fang: Crazy Cutting"]],
                       "Thunder": [{"Health": 40, "Attack": 90, "Defence": 40, "Speed": 80, "Name": "Zenitsu Agatsuma", "Master": 1},
                                     ["First Form: Thunderclap and Flash", "Third Form: Thunder Form", "Fourth Form: Distant Thunder", "Fifth Form: Heat Lightning"]]}
    '''now demon slayers sorted by breathing, not player name'''
    # TODO: amend master for each character
    __exp_current = 0
    __exp_full = 15     #make all characters 15 exp for level 1

    def __init__(self, breathing=None, **kwargs):
        self.__breathing_type = breathing
        if len(kwargs) == 0:
            self._assign_attributes()
            self.__breathing_type = str(self.__DEMON_SLAYERS[self.__breathing_type]["Name"])
        else:
            self.__name = kwargs['Name']
            self.__master = kwargs['Master']
        #   exception
    def _assign_attributes(self):
        self.__hp_current = self.__DEMON_SLAYERS[self.__breathing_type]["Health"]
        self.__hp_full = self.__hp_current
        self.__att = self.__DEMON_SLAYERS[self.__breathing_type]["Attack"]
        self.__spd = self.__DEMON_SLAYERS[self.__breathing_type]["Speed"]
        self.__def = self.__DEMON_SLAYERS[self.__breathing_type]["Defence"]

    @property
    def _master_of(self):
        form_ints = self.__DEMON_SLAYERS[self.__breathing_type][0]["Master"] #returns integer eg. 127 -> meaning they are master of forms 1,2&7
        master_of_list = []
        for form in form_ints:
            form -= 1 #to adjust indexing appropriately
            master_of_list.append(self.__DEMON_SLAYERS[self.__breathing_type][1][form])
        return master_of_list

    @_master_of.setter
    def _master_of(self, masters):
        self.__DEMON_SLAYERS[self.__breathing_type][0]["Master"].append(masters) #appends form to

    @property
    def _experience_current(self):
        return self.__exp_current

    @_experience_current.setter
    def _experience_current(self, new_exp_current):
        self.__exp_current = new_exp_current

    @property
    def _experience_full(self):
        return self.__exp_full

    @_experience_full.setter
    def _experience_full(self, new_exp_full):
        self.__exp_full = new_exp_full

    def __str__(self):
        return f"{self._char_name}\n"\
               f"CURRENT HEALTH = {self.__hp_current} / FULL HEALTH = {self.__hp_full}\n" \
               f"ATTACK = {self.__att}\n" \
               f"SPEED = {self.__spd}\n" \
               f"DEFENCE = {self.__def}\n" \
               f"CURRENT EXP = {self.__exp_current} / FULL EXP = {self.__exp_full}\n"\
               f"LEVEL = {self.__level}\n" \
               f"BREATHING TYPE = {self.__breathing_type}\n"

    def _assign_attributes(self):
        self.__hp_current = self.__DEMON_SLAYERS[self._char_name]["Health"]
        self.__hp_full = self.__hp_current
        self.__att = self.__DEMON_SLAYERS[self._char_name]["Attack"]
        self.__spd = self.__DEMON_SLAYERS[self._char_name]["Speed"]
        self.__breathing_type = str(self.__DEMON_SLAYERS[self._char_name]["Breathing Type"])
        _assign_types(self.__breathing_type)

# class Water(DemonSlayer):
#     __special_move = [{"Name": "Water Surface Slash", "No.": "1st Form", "Attack Multiplier": 2},
#                       {"Name": "Water Wheel", "No.": "2nd Form", "Attack Multiplier": 2},
#                       {"Name": "Whirlpool", "No.": "6th Form", "Attack Multiplier": 2}]
#     def __init__(self, **kwargs):
#
#     # def _special_move(self):
#     #     return __special_move
#
# class Beast(DemonSlayer):
#     __special_move = [{"Name": "Pierce", "No.": "1st Fang", "Attack Multiplier": 2},
#                       {"Name": "Water Wheel", "No.": "2nd Fang", "Attack Multiplier": 2}]
#     pass
#
# class Thunder(DemonSlayer):
#     __special_move = [{"Name": "Thunderclap and Flash", "No.": "1st Form", "Attack Multiplier": 2}]
#     pass

class Create(DemonSlayer):
    __name = ClassVar[str]
    __breathing_style = ClassVar[str]
    def __init__(self, *args:str, **kwargs:str) -> None:
        character_name = self.__name

class Demon(Character):
    pass

    # args for demons can be... level.. name
    #   if name not specified we generate a basic demon based on level
    #   elif name is provided just go to demon preset
    def __init__(self, *args):
        pass
def main():
    ds_character1 = DemonSlayer("Tanjiro Kamado")
    sample_input = {"Name": "Conor", "Breathing Type": "Water", "Master":"Water Wheel"}
    if sample_input["Breathing Type"] == "Water":
        created_character = DemonSlayer({"Name" = sample_input["Name"], ""})

    print(ds_character1, '\n', ds_character2)

def get_input(input_query):
    player_input = input(input_query)
    return player_input.capitalize()

def start_game():
    print("start game")
    '''
    display player options
    player names to select
    player info on each
    '''
    choice_of_player = get_input("")


def display_info():
    print('''Demon Slayer is placed in a fictional world set in early 20th century Taishō-era Japan, in which man-eating demons roam the land each night. 
    13-year-old Tanjiro Kamado’s world is turned upside down when he returns home one morning to find his entire family murdered, save for his sister Nezuko—who has turned into a demon. 
    Determined to avenge their deaths and find a cure that would transform Nezuko back into a human, Tanjiro sets out on a journey to train for the Demon Slayer Corps. 
    The story follows him as he joins this underground organization of skilled fighters who dedicate their lives to protecting humans from the vicious creatures.
    \n Source: https://time.com/5941594/what-is-demon-slayer-about/''')
class Menu:
    MAIN_MENU = ["Play", "Info", "Quit"]
    TYPE_OPTIONS = ["Demon Slayer", "Self-Creation"]
    BREATHING_TYPE_OPTIONS = ["Water", "Lightning", "Earth", "Sound", "Fire"]
    CHARACTER_OPTIONS = []
    def __init__(self, type_opt):
        display_menu(type_opt)

    def display_menu(self, menu_type):
        print(f"{menu_type}")
        for menu_item in enumerate(menu_type, 1):
            print("-"+menu_item[0], menu_item[1])

    def menu_input(self, player_input: str):
        pass

if __name__ == "__main__":
    main()
    # ''' put below into function '''
    # GAME_ONGOING = False
    # while not GAME_ONGOING:
    #     print(display_main_menu())
    #     main_menu_input = get_input("Select Option: ")
    #
    #     for item in MAIN_MENU_OPTIONS:
    #         # raise exception
    #         print("invalid input, try again")
    #         pass
    #     else:
    #         print("valid input")
    #         if main_menu_input == MAIN_MENU_OPTIONS[0]:
    #             start_game()
    #         elif main_menu_input == MAIN_MENU_OPTIONS[1]:
    #             display_info()
    #         break

# exception throwing
# class Breathing_Style:
#     __special_move = ClassVar[str]
#     def __init__(self, breathing_style):
#         pass
