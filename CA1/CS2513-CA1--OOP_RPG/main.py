
intro_text = '''
    This is a very simplified character customisable take on The Witcher game
    by CD Projekt Red based on the books by Polish author Andrzej Sapkowski.
    
    You can select 2 types of characters to play as; a Witcher or a Mage.
    Witcher's are the front-of-the-line, all action style characters that rely on brute force 
    and the steel of their blade to defeat monsters.
    Mage's on the other hand typically keep their distance by using spells to take down their foes.
    Choose wisely.
    
    There are 3 Witchers you can choose from:
        Geralt
        Ciri
        Vesemir
    
            STATS
            
            Geralt: 70 Health, 70 Attack and 70 Speed
                - Geralt of Rivia is a true all-rounder and the main character of the Witcher series.
                    
                  To read more about Geralt, follow this link: https://witcher.fandom.com/wiki/Geralt_of_Rivia
                
            Ciri: 50 Health, 60 Attack and 100 Speed
                - Ciri is the daughter..... she relys on her speed to dodge and attack
                
            Vesemir: 70 Health, 90 Attack and 40 Speed
                - The old-timer may not be the quickest, but makes up for it in his Strength and Wisdom having seen it all.
'''
    # There are 2 Mages you can choose from:
    #     Yennefer
    #     Triss
    #
    #         STATS
    



# TYPES = {"Witcher": WITCHER, "Mage": MAGE}

GERALT = {"health": 70, "attack": 70, "speed": 70}
CIRI = {"health": 50, "attack": 60, "speed": 100}
VESEMIR = {"health": 70, "attack": 90, "speed": 40}

CHARACTERS = {"Geralt": GERALT, "Ciri": CIRI, "Vesemir": VESEMIR}
# can only be one witcher named Geralt of Rivia
# CHARACTER LIST

# character can also have horse and name what they'd like...
# you can encounter horses of varying degrees of intelligence, speed and health

class Character:
    _hp = 0
    _att = 0
    _spd = 0
    # use ^ ClassVar

    __attack_multiplier = 0.15 #affected by swords and sometimes horses/
    __hp_multiplier = 1 #affected by armor and sometimes horses
    __spd_multiplier = 0.5 #affected by horses and sometimes armor
    #for armor
    # _chest =
    # _trousers =
    # _boots =
    # _gloves =

    # _has_horse = False #unless...
    def __init__(self, char_name):
        self._char_name = char_name.capitalize()
        self._assign_attributes()
        # self.hp = max_hp
        # self.max_hp = max_hp
        # if self._char_name not in CHARACTERS:
        #     raise Exception("This character does not exist")

    def __str__(self):
        return f"{self._char_name}\n"\
               f"HEALTH = {self._hp}\n" \
               f"ATTACK = {self._att}\n" \
               f"SPEED = {self._spd}\n" \
               f"ARMOR = ..."

    def _assign_attributes(self):
        char_name_dict = CHARACTERS[self._char_name]
        self._hp = char_name_dict["health"]
        self._att = char_name_dict["attack"]
        self._spd = char_name_dict["speed"]

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

class NonPlayerCharacter:
    pass

class Witcher(Character):
    pass
# def intro_text():
#     intro_text = '''
#     This is a very simplified character customisable take on The Witcher game
#     by CD Projekt Red based on the books by Polish author Andrzej Sapkowski.
#     '''
#     print(intro_text)

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
    witcher_character1 = Character("Ciri")
    witcher_character2 = Character("geralt")
    witcher_character3 = Character("vesemir")
    print(witcher_character1, '\n')
    print(witcher_character2, '\n')
    print(witcher_character3)

def get_input(input_query):
    player_input = input(input_query)
    return player_input.capitalize()
# class Menu:
#     MAIN_MENU_OPTIONS = ["Play", "Info", "Quit"]
#     CHARACTER_MENU_OPTIONS = []
#     def __init__(self,type):


def display_main_menu():
    return "MAIN MENU\n" \
           "Play\n"\
           "Info\n"\
           "Quit\n"

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

if __name__ == "__main__":
    main()
    ''' put below into function '''
#     GAME_ONGOING = False
#     MAIN_MENU_OPTIONS = ["Play", "Info", "Quit"]
#
#     while not GAME_ONGOING:
#         print(display_main_menu())
#         main_menu_input = get_input("Select Option: ")
#
#         if main_menu_input not in MAIN_MENU_OPTIONS:
# #           raise exception
#             print("invalid input")
#             break
#         else:
#             print("valid input")
#             if main_menu_input == MAIN_MENU_OPTIONS[0]:
#                 start_game()
#             elif main_menu_input == MAIN_MENU_OPTIONS[1]:
#                 display_info()
#             break



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