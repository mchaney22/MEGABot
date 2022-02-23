import os




class NetRun():
    def __init__(self):
        self.netrunning_deck = {
            "Image Filepath": '.\\docs\\netrunning\\Individual Cards JPG\\',
            "Card Names" : ['Armor', 'Asp', 'Balron', 'Banhammer', 'CardBack', 'ControlNode', 'Deckkrash', 
                            'Dragon', 'Efreet', 'Eraser', 'File', 'Flak', 'Giant', 'Hellbolt', 'Hellhound', 
                            'Imp', 'Killer', 'Kraken', 'Liche', 'Nervescrub', 'Password', 'PoisonFlatline', 
                            'Raven', 'Sabertooth', 'Scorpion', 'SeeYa', 'Shield', 'Skunk', 'SpeedyGonzalvez', 
                            'Superglue', 'Sword', 'Vrizzbolt', 'Wisp', 'Worm'],
            "Interface Abilities" : ['Scanner', 'Backdoor', 'Cloak', 'Control', 
                                    'Eye Dee', 'Pathfinder', 'Slide', 'Virus', 'Zap']
            }

    def get_all_cards(self):
        return self.netrunning_deck["Card Names"]

    def get_all_file_paths(self):
        all_cards = self.get_all_cards()
        all_file_paths = []
        for card in all_cards:
            all_file_paths.append(self.netrunning_deck["Image Filepath"] + card + ".jpg")
        return all_file_paths 
    def hello(self):
        print("hello")
            


class Card():
    def __init__(self):
        pass
    def load_cards(self):
        pass
    def get_filesnames_in_dir(path):
        #returns a list of filenames in a directory
        return os.listdir(path)

class InitiativeQueue:
    def __init__(self):
        pass
    def add_to_queue(self):
        pass
    def remove_from_queue(self):
        pass
    def get_next_initiative(self):
        pass