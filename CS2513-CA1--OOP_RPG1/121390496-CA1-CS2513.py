from typing import ClassVar


class InputError(ValueError):
    pass


class Character:
    __hp_current = ClassVar[int]
    __hp_full = ClassVar[int]
    __att = ClassVar[int]
    __spd = ClassVar[int]
    __def = ClassVar[int]
    __lvl = 1
    _DEMON = {"Health": 15, "Attack": 10, "Defence": 5, "Speed": 10}  # demon level 1 stats
    _DEMON_SLAYERS = {
        "Water": [{"Health": 70, "Attack": 70, "Defence": 70, "Speed": 70, "Name": "Tanjiro Kamado", "Master": [1, 2, 3, 4]},
                  ["First Form: Water Surface Slash", "Second Form: Water Wheel", "Third Form: Flowing Dance",
                   "Fourth Form: Striking Tide"],
                  #Character Info
                  '''Tanjiro Kamado (竈門かまど 炭たん治じ郎ろう Kamado Tanjirō) is the main protagonist of Demon Slayer: 
Kimetsu no Yaiba. He is a Demon Slayer in the Demon Slayer Corps, who joined to find a remedy to 
turn his sister, Nezuko Kamado, back into a human and to hunt down and kill demons,
and later swore to defeat Muzan Kibutsuji, the King of Demons, in order to prevent others from 
suffering the same fate as him. Before he became a Demon Slayer, Tanjiro was a coal burner before 
his entire family was slaughtered by Muzan while his younger sister, Nezuko, was turned into a demon.
Source: 
    https://kimetsu-no-yaiba.fandom.com/wiki/Tanjiro_Kamado#cite_note-auto-a9600c9ab30126f57705f16465c4bc6e-3
                  '''],
        "Beast": [{"Health": 70, "Attack": 70, "Defence": 50, "Speed": 80, "Name": "Inosuke Hashibira", "Master": [1, 2, 3, 4]},
                  ["First Fang: Pierce", "Second Fang: Slice ", "Third Fang: Devour ", "Fourth Fang: Slice 'n' Dice"],
                  # Character Info
                  '''Inosuke Hashibira (嘴はし平びら 伊い之の助すけ Hashibira Inosuke) is one of the main protagonists of Demon Slayer: 
Kimetsu no Yaiba and along with Zenitsu Agatsuma, a traveling companion of Tanjiro Kamado and Nezuko Kamado.
He is also a Demon Slayer in the Demon Slayer Corps.
Source: 
    https://kimetsu-no-yaiba.fandom.com/wiki/Inosuke_Hashibira
                  '''
                  ],
        "Thunder": [{"Health": 40, "Attack": 90, "Defence": 40, "Speed": 80, "Name": "Zenitsu Agatsuma", "Master": [1]},
                    ["First Form: Thunderclap and Flash", "Second Form: Rice Spirit", "Third Form: Thunder Form", "Fourth Form: Distant Thunder"],
                    # Character Info
                    '''Zenitsu Agatsuma (我あが妻つま 善ぜん逸いつ Agatsuma Zen'itsu) is one of the main protagonists of Demon Slayer: 
Kimetsu no Yaiba and along with Inosuke Hashibira, a travelling companion of Tanjiro Kamado and Nezuko Kamado.
He is also a Demon Slayer in the Demon Slayer Corps.
Source: 
    https://kimetsu-no-yaiba.fandom.com/wiki/Zenitsu_Agatsuma 
                    '''
                    ]}  # demon slayer preset characters level 1 stats

    def __str__(self):
        return f"HEALTH = {self.__hp_current}/{self.__hp_full}\n" \
               f"ATTACK = {self.__att}\n" \
               f"SPEED = {self.__spd}\n" \
               f"DEFENCE = {self.__def}\n" \
               f"LEVEL = {self.__lvl}\n"

    # assign values to attributes after instantiation
    def _assign_attributes(self, type_char, breathing_type=None):
        if type_char == "Demon":
            self.type_char = self._DEMON
        else:
            self.type_char = self._DEMON_SLAYERS[breathing_type][0]
        self.__hp_current = self.type_char["Health"]
        self.__hp_full = self.__hp_current
        self.__att = self.type_char["Attack"]
        self.__spd = self.type_char["Speed"]
        self.__def = self.type_char["Defence"]

    ''' Getters & Setters (Common Attributes) '''
    @property
    def _level(self):
        return self.__lvl

    @_level.setter
    def _level(self, new_level):
        self.__lvl = new_level

    @property
    def _health_current(self):
        return self.__hp_current

    @_health_current.setter
    def _health_current(self, new_health_current):
        self.__hp_current = new_health_current

    @property
    def _health_full(self):
        return self.__hp_full

    @_health_full.setter
    def _health_full(self, new_health_full):
        self.__hp_full = new_health_full

    @property
    def _attack(self):
        return self.__att

    @_attack.setter
    def _attack(self, new_attack):
        self.__att = new_attack

    @property
    def _speed(self):
        return self.__spd

    @_speed.setter
    def _speed(self, new_speed):
        self.__spd = new_speed

    @property
    def _defence(self):
        return self.__def

    @_defence.setter
    def _defence(self, new_defence):
        self.__def = new_defence


# Demon Slayer; child class of character... Demon Slayer = Playable character
class DemonSlayer(Character):
    __exp_current = 0
    __exp_full = 15  # make all characters 15 exp for level 1
    __name = ClassVar[str]
    __forms_mastered = ClassVar[list]

    def __init__(self, breathing=None, **kwargs):
        self.__breathing_type = breathing
        if len(kwargs) == 0:
            self._assign_attributes()
            self.__name = self._get_name(self.__breathing_type)
        else:
            self.__name = kwargs['Name']
            self.__master = kwargs['Master']
            self._master_of_setter = self.__master
            self._assign_attributes()
        #   exception

    def __str__(self):
        return "CLASS = Demon Slayer\n" \
               f"NAME = {self.__name}\n" \
               f"BREATHING TYPE = {self.__breathing_type}\n" \
               f"FORMS MASTERED = {self.__forms_mastered}\n" \
               + super().__str__() + \
               f"EXP = {self.__exp_current}/{self.__exp_full}\n"

    def _assign_attributes(self):
        super()._assign_attributes("Demon Slayer", self.__breathing_type)
        self.__forms_mastered = self._master_of

    @property
    def _character_info(self):
        return self._DEMON_SLAYERS[self.__breathing_type][2]

    @_character_info.setter
    def _character_info(self, new_char_info: str):
        self._DEMON_SLAYERS[self.__breathing_type][2] = new_char_info
        # ^ set character_info for self created character to something new, so it is not one for preset character

    def _demon_slayer_forms(self, char_type):
        print(f"{char_type} Type Breathing Forms")
        for form in enumerate(self._DEMON_SLAYERS[char_type][1], 1):
            print("-" + str(form[0]), form[1])

    def _get_name(self, char_type):
        return self._DEMON_SLAYERS[char_type][0]["Name"]

    @property
    def _master_of(self):
        forms = self._DEMON_SLAYERS[self.__breathing_type][0]["Master"]
        if forms == [0]:
            self.__forms_mastered = "Master of None"
        else:
            forms_mastered_list = []
            for form in forms:
                forms_mastered_list.append(self._DEMON_SLAYERS[self.__breathing_type][1][form-1])
                self.__forms_mastered = forms_mastered_list
        print(self._DEMON_SLAYERS[self.__breathing_type][0]["Master"])
        return self.__forms_mastered

    @_master_of.setter
    def _master_of(self, masters: list):
        self._DEMON_SLAYERS[self.__breathing_type][0]["Master"] = masters
        print(self._DEMON_SLAYERS[self.__breathing_type][0]["Master"])
        forms = self._DEMON_SLAYERS[self.__breathing_type][0]["Master"]
        if forms == [0]:
            self.__forms_mastered = "Master of None"
        else:
            forms_mastered_list = []
            for form in forms:
                forms_mastered_list.append(self._DEMON_SLAYERS[self.__breathing_type][1][form - 1])
                self.__forms_mastered = forms_mastered_list

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

# class Create(DemonSlayer):
#     __name = ClassVar[str]
#     __breathing_style = ClassVar[str]
#     def __init__(self, *args:str, **kwargs:str) -> None:
#         character_name = self.__name


# Demon; child class of character... Demon = Non-Playable character
class Demon(Character):
    def __init__(self):
        self._assign_attributes()

    def __str__(self):
        return "CLASS = Demon\n"\
               + super().__str__()

    def _assign_attributes(self):
        super()._assign_attributes("Demon")


# simple function for user input processing
def get_input(input_query):
    player_input = input(input_query)
    return player_input.capitalize()


# menu types
menu_types = {"MAIN MENU": ["Play", "Info"], "PLAYER OPTIONS": ["Demon Slayer", "Self-Creation"],
              "BREATHING TYPE OPTIONS": ["Water", "Thunder", "Beast"], "DEMON SLAYER OPTIONS": ["Tanjiro Kamado", "Inosuke Hashibira", "Zenitsu Agatsuma"],
              "CHARACTER OPTIONS": ["Player Info", "Player Stats"]}

player_variable = ClassVar[dict]
player_description = ClassVar[str]


def display_menu(menu_type, *args):  # args are for using player character specific instance methods etc
    print(f"{menu_type}")
    for menu_item in enumerate(menu_types[menu_type], 1):
        print("-" + str(menu_item[0]), menu_item[1])
    option_chosen = get_input("Select an option: ")
    if len(args) == 0:
        if menu_type == "MAIN MENU":
            if option_chosen == "1":  # Play
                display_menu("PLAYER OPTIONS")
            elif option_chosen == "2":  # Info
                game_info()
            else:
                raise InputError("Value must be 1 or 2")

        elif menu_type == "PLAYER OPTIONS":
            if option_chosen == "1":  # DEMON SLAYER
                display_menu("DEMON SLAYER OPTIONS")
            elif option_chosen == "2":  # CREATE
                display_menu("BREATHING TYPE OPTIONS")
            else:
                raise InputError("Value must be 1 or 2")

        elif menu_type == "DEMON SLAYER OPTIONS":
            if option_chosen == "1":  # Tanjiro
                tanjiro = DemonSlayer("Water")
                display_menu("CHARACTER OPTIONS", tanjiro)
            elif option_chosen == "2":  # Inosuke
                inosuke = DemonSlayer("Beast")
                display_menu("CHARACTER OPTIONS", inosuke)
            elif option_chosen == "3":  # Zenitsu
                zenitsu = DemonSlayer("Thunder")
                display_menu("CHARACTER OPTIONS", zenitsu)
            else:
                raise InputError("Value must be 1, 2 or 3")
        # create
        elif menu_type == "BREATHING TYPE OPTIONS":
            if option_chosen == "1":  # Water
                create_player_details("Water")
            elif option_chosen == "2":  # Beast
                create_player_details("Beast")
            elif option_chosen == "3":  # Thunder
                create_player_details("Thunder")
            else:
                raise InputError("Value must be 1, 2 or 3")
    elif len(args) == 1:
        instance_name = args[0]
        # menu_type == "CHARACTER_OPTIONS"
        if option_chosen == "1":  # Player Info
            print(instance_name._character_info)
        elif option_chosen == "2":  # Player Stats
            print(instance_name)
        else:
            raise InputError("Value must be 1 or 2")
    else:
        raise InputError("Too many arguments provided")


def create_player_details(character_type):
    # player_dict = {"Name": "", "Master": None}
    player_name_unchecked = get_input("What would you like your character to be called? (less than 16 characters): ")
    if len(player_name_unchecked) < 16:
        player_name = player_name_unchecked
    else:
        raise InputError("Input must be below 16 characters")
    player_details = get_input("Give a brief description of your character: ")
    player_character = DemonSlayer(character_type, Name=player_name, Master=[0])

    player_character._character_info = player_details

    player_character._demon_slayer_forms(character_type)
    option_chosen = get_input(f"Using the corresponding number value for the form, "
                              f"select the breathing form you would like {player_name} to be a master of: ")
    if option_chosen == "1":  # master of form 1
        player_character._master_of = [1]
    elif option_chosen == "2":  # master of form 2
        player_character._master_of = [2]
    elif option_chosen == "3":  # master of form 3
        player_character._master_of = [3]
    elif option_chosen == "4":  # master of form 4
        player_character._master_of = [4]
    else:
        raise InputError("Value must be 1, 2, 3, or 4")

    '''
    format for creating player = 
        player_create = DemonSlayer("Beast", Name = "Conor", Master=[1])
        ie. DemonSlayer(BREATHING_TYPE, Name = ____, Master = [_])
    '''
        #     must get list of forms to be able to master
    print(player_character)


def game_info():
    print('''The world of Demon Slayer is set in early 20th century Taishō-era Japan, in which man-eating demons roam the land each night. 
13-year-old Tanjiro Kamado’s world is turned upside down when he returns home one morning to find his entire family murdered, save for his sister Nezuko—who has turned into a demon. 
Determined to avenge their deaths and find a cure that would transform Nezuko back into a human, Tanjiro sets out on a journey to train for the Demon Slayer Corps. 
The story follows him as he joins this underground organization of skilled fighters who dedicate their lives to protecting humans from the vicious creatures.
Source: 
    https://time.com/5941594/what-is-demon-slayer-about/

This project is intended to be a rudimentary form of an RPG of sorts based on Demon Slayer. In Demon Slayer the demon slayers
each have a breathing style. These breathing styles give specific attributes to that demon slayers' fighting style.
I chose to simply work with the 3 main characters and protagonists for this project: Tanjiro, Inosuke and Zenitsu; and 
therefore had only to work with 3 different breathing styles. However in a fully fleshed out game the idea would be that 
there would be all breathing styles included and all core demon slayers seen in the story would be a potential option to choose.
Game functionality would be something along the lines of a standard RPG in which you must fight demons to gain experience 
and therefore level up. Levelling up boosts the characters stats and so on. Character stats would include: Attack, Speed,
Defence and Health at the minimum. In a fully-fleshed out game it would likely be far more nuanced to include the likes of
endurance and intelligence etc. to make gameplay more interesting.
In this project I have set the foundations for a game similar to what I have outlined above:
I have created a class for Characters - this is the parent class for all characters ; hence would include Non-Playable Characters
(Demons in this case) and Playable Characters (Demon Slayers in the case). The parent class gives us the attributes that all characters
would have: eg. health, attack, defence, speed etc. However there are some attributes that are specific to playable characters
such as experience to level up, breathing forms, and a name attribute.
For playable characters I allowed the player to choose whether to be one of the 3 aforementioned Demon Slayers or to be a 
self-created character in which you give the demon slayer their name, choose which breathing style they possess and which
forms or techniques of this breathing styles they have mastered.
To support this functionality and make user interaction easier I created a simplistic menu interacted with through the console.
''')


def main():  # for demonstration
    tanjiro = DemonSlayer("Water")
    print(tanjiro)
    print(tanjiro._character_info)

    player_create = DemonSlayer("Beast", Name="Conor", Master=[1, 2])
    print(player_create)

    demon_instance = Demon()
    print(demon_instance)
    display_menu("MAIN MENU")


if __name__ == "__main__":
    main()




