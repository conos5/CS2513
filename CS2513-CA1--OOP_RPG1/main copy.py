from typing import ClassVar


# character can also have horse and name what they'd like...
# you can encounter horses of varying degrees of intelligence, speed and health

class Character:
    __TYPES = {"Demon Slayer": DEMON_SLAYERS, "Hashira": HASHIRA}
    # TYPES
    __DEMON_SLAYERS = {"Tanjiro Kamado": TANJIRO, "Inosuke Hashibira": INOSUKE, "Zenitsu Agatsuma": ZENITSU}
    # DEMON SLAYERS
    __TANJIRO = {"Health": 70, "Attack": 70, "Speed": 70}
    __INOSUKE = {"Health": 70, "Attack": 60, "Speed": 80}
    __ZENITSU = {"Health": 40, "Attack": 90, "Speed": 80}

    __hp_current = ClassVar[int]
    __att = ClassVar[int]
    __spd = ClassVar[int]
    __exp_current = 0
    __exp_full = ClassVar[int]
    __level = 1

    __attack_multiplier = 0.15 #affected by swords and sometimes horses/
    __hp_multiplier = 1 #affected by armor and sometimes horses
    __spd_multiplier = 0.5 #affected by horses and sometimes armor

    def __init__(self, char_type, char_name):
        self.char_type = char_type.capitalize()
        self._char_name = char_name.capitalize()
        self._assign_attributes()
        # self.hp = max_hp
        # self.max_hp = max_hp
        # if self._char_name not in CHARACTERS:
        #     raise Exception("This character does not exist")

    def __str__(self):
        return f"{self._char_name}\n"\
               f"CURRENT HEALTH = {self.__hp_current} / FULL HEALTH = {self.__hp_full}\n" \
               f"ATTACK = {self.__att}\n" \
               f"SPEED = {self.__spd}\n" \
               f"LEVEL = {self.__level}" \
               f"CURRENT EXP = "

    def _assign_attributes(self):
        char_name_dict = CHARACTERS[self._char_name]
        self.__hp_current = char_name_dict["health"]
        self.__hp_full = self__hp_current
        self.__att = char_name_dict["attack"]
        self.__spd = char_name_dict["speed"]

    # def _assign_type(self):
    #     char_type_dict = TYPES[self._char_name]

    # def equip_armor(self, armor):
    #     armor_name_dict = ARMORS[self.armor]

    # def heal(self):
    #     if self.hp < self.max_hp:
    #         self.hp += 1
    #     else:
    #         print(f"{self._char_name} is already at full health!")
    '''
    armor to increase health and modify baseline speed
    mutations to adapt varying attributes
        can increase max attack, speed and health
        whilst decreasing another
    weapons to increase attack and or speed
    '''



class Merchant(NonPlayerCharacter):
    '''
    types
        armorer
        horse merchant
        craftsman
        alchemist
        healer
    '''
    pass


class Beast():
    pass

def main():
    witcher_character1 = Character("Tanjiro")
    print(witcher_character1, '\n')

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
    print("prints info")
class Menu:
    MAIN_MENU = ["Play", "Info", "Quit"]
    TYPE_OPTIONS = ["Demon Slayer", "Self-Creation"]
    BREATHING_TYPE_OPTIONS = ["Water", "Lightning", "Earth", "Sound", "Fire"]
    CHARACTER_OPTIONS = []
    def __init__(self, type):
        display_menu(type)

    def display_menu(self, menu_type):
        print(f"{menu_type}")
        for item in enumerate(menu_type, 1):
            print("-"+item[0],item[1])

    def menu_input(self, player_input: str):
        pass

if __name__ == "__main__":
    main()
    ''' put below into function '''
    GAME_ONGOING = False
    while not GAME_ONGOING:
        print(display_main_menu())
        main_menu_input = get_input("Select Option: ")

        for item in MAIN_MENU_OPTIONS:
            # raise exception
            print("invalid input, try again")
            pass
        else:
            print("valid input")
            if main_menu_input == MAIN_MENU_OPTIONS[0]:
                start_game()
            elif main_menu_input == MAIN_MENU_OPTIONS[1]:
                display_info()
            break



# KINGDOM LIST
'''
    REDANIA
    KAEDWEN
    TEMERIA
    AEDIRN
    SKELLIGE
'''
# ARMOR LIST
'''
    WITCHER UNDERSHIRT
    WITCHER JACKET
    WITCHER ARMOR
    HEAVY LEATHER JACKET
    ELVEN ARMOR
    LEATHER JACKET
    RAVEN'S AMOR
    WILD HUNT ARMOR
    ZIREAEL'S ARMOR
    WITCH HUNTER'S COAT
    ARMOR OF TIR NA LIA
    ARMOR OF LOCH GARMAN
    ARMOR D'AN RI CONCUBHAR
    ARMOR OF THE WOLF -- GERALT
    ARMOR OF THE BEAR -- VESEMIR
    ARMOR OF THE FOX -- CIRI
    SAMURAI'S KIMONO
    STOLEN PEASANTS UNDERSHIRT --- WHEN YOU DIE
'''
# TROUSERS LIST
'''
    WITCHER TROUSERS
    WITCHER LEATHER TROUSERS
    WITCHER HEAVY TROUSERS
    LEATHER TROUSERS
    HEAVY LEATHER TROUSERS
    ELVEN TROUSERS
    RAVEN'S TROUSERS
    WILD HUNT TROUSERS
    TROUSER D'AN RI CONCUBHAR
    TROUSER OF LOCH GARMAN
    WEE SCOTTISH KILT
    WORN PEASANTS TROUSERS --- WHEN YOU DIE
'''
# BOOTS LIST
'''
    LEATHER BOOTS
    HARDENED LEATHER BOOTS
    WITCHER BOOTS
    REINFORCED WITCHER BOOTS
    ELVEN BOOTS
    WILD HUNT BOOTS
    RAVEN'S BOOTS
    AN RI CONCUBHAR'S TRUSTY BOOTS
    LOCH GARMAN LEATHER BOOTS
    SOAKED PEASANTS BOOTS --- WHEN YOU DIE
'''
# GLOVES LIST
'''
    LEATHER GAUNTLETS
    WITCHERS GAUNTLETS
    THANOS' GAUNTLETS
    WILD HUNT GAUNTLETS
    ELVEN GAUNTLETS
    RAVEN'S GAUNTLETS
    AN RI CONCUBHAR'S GAUNTLETS
    LOCH GARMAN LEATHER GLOVES
    LOCH GARMAN STEEL GAUNTLETS
    WORN LEATHER GLOVES
'''
# WEAPONS LIST
'''
  WITCHER'S STEEL SWORD
  AXE
  RUSTY SWORD
  NUNCHOKS
  LIGHT CLUB
  SAMURAI SWORD
  ELVEN SWORD
  MASTER-CRAFTED WITCHER BLADE
  SWORD OF AN RI CONCUBHAR
  GWALHIR
  MOONBLADE
  ASSASSIN'S DAGGER
  D'YAEBYL
  WITCH-HUNTER'S SWORD
'''
# BEASTIARY
'''

'''

# exception throwing