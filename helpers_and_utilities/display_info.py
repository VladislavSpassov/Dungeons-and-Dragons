from helpers_and_utilities.utils import clear_screen


class DisplayInfo:
    def __init__(self, hero):
        self.hero = hero

    def display_info(self, info_type):
        dicts = {'character_info': self.display_hero_information,
                 'help': self.display_help,
                 'lore': self.display_lore,
                 'map_keys': self.display_map_keys,
                 'credits': self.display_credits
                 }

        dicts[info_type]()

    def display_hero_information(self):
        FORMAT_SPACES = '      '
        print(
            f'{self.hero.name} the {self.hero.title}\n\n'
            f'Current health: {self.hero.health}\n'
            f'Current mana: {self.hero.mana}\n'
            f'Mana regeneration: {self.hero.mana_regeneration_rate}\n\n'
            f'Current Weapon:\n'
            f'{FORMAT_SPACES}Name: {self.hero.weapon.name}\n'
            f'{FORMAT_SPACES}Damage: {self.hero.weapon.damage}\n\n'
            f'Current Spell:\n'
            f'{FORMAT_SPACES}Name: {self.hero.spell.name}\n'
            f'{FORMAT_SPACES}Damage: {self.hero.spell.damage}\n'
            f'{FORMAT_SPACES}Mana Cost: {self.hero.spell.mana_cost}\n'
            f'{FORMAT_SPACES}Range: {self.hero.spell.cast_range}'
        )
        input('\nPress Enter to continue... ')

    def display_credits(self):
        with open('credits.txt', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    def display_help(self):
        with open('help.txt', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    def display_lore(self):
        with open('lore.txt', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    def display_map_keys(self):
        with open('map_keys.txt', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    @staticmethod
    def display_intro():
        clear_screen()
        with open('intro.txt', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    # TODO ADD DISPLAY LORE AND OTHER SHIT
