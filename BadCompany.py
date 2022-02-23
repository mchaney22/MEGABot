import json
class BadCompany:
    def __init__(self, name, symbol, strength, influence, resources, strategy, security, company_head, hq, background):
        self.name = name
        self.symbol = symbol
        stats = {
            'strength' : strength,
            'influence': influence,
            'resources': resources,
            'strategy' : strategy,
            'security' : security,
        }
        self.company_head = company_head
        self.hq = hq
        self.background = background

def all_companies():
    companies = {}
    cw = CW()
    return cw.companies()
    # companies['ARA'] = BadCompany(name='Arasaka',symbol='ARA', strength=7, influence=6, resources=6, strategy=5, security=4,
    #                               company_head='Hanako Arasaka', hq='Tokyo, Japan', background='')
    # companies['MTEC'] = BadCompany(name='Militech International',symbol='MTEC', strength=6, influence=7, resources=4, strategy=5, security=6,
    #                               company_head='General Sammy Lee Young', hq='Washington D.C., NUSA', background='')
    # companies['CINO'] = BadCompany(name='Corporation Internationale Nauticale et Oceanique',symbol='CINO', strength=4, influence=5, resources=6, strategy=7, security=6,
    #                                 company_head='Peter Nicholas', hq='Le Havre, France', 
    #                                 background='Originally a British shipping firm, CINO deals mainly in the construction of shipping vessels and related navigation and shipping equipment. This is done at their huge dry-dock facility in Le Havre, or at Marseilles. They have modest krill processing centers, a few sea farms, and dozens of undersea research labs. For 10 years they\'ve been unsuccessfully struggling to break into nautitech.')    
    # companies['OTEC'] = BadCompany(name='Ocean Technology & Energy Corporation',symbol='OTEC', strength=5, influence=6, resources=7, strategy=6, security=4,
    #                                 company_head='Amanda Russell', hq='AquaDelphi, Hawaiian Islands', background='')
    # companies['ESA'] = BadCompany(name='European Space Agency',symbol='ESA', strength=6, influence=4, resources=7, strategy=7, security=4,
    #                                 company_head='Dr. John Glenn', hq='Tromsø, Norway', background='')
    # companies['NuNasa'] = BadCompany(name='NuNasa',symbol='NuNasa', strength=5, influence=6, resources=6, strategy=6, security=7,
    #                                 company_head='James W. Paine', hq='Dallas, NUSA', background='')
    # companies['BTEC'] = BadCompany(name='Biotechnica',symbol='BTEC', strength=6, influence=4, resources=4, strategy=7, security=7,
    #                                 company_head='Nicolo Loggagia', hq='Night City, Night City', background='')
    # companies['CBRAND'] = BadCompany(name='Continental Brands',symbol='CBRAND', strength=6, influence=6, resources=7, strategy=6, security=7,
    #                                 company_head='Olivia Forsyth', hq='Paris, Free Texas', background='')
    # return companies

# imports the 4CW json file, and creates a dictionary of all the companies
class CW:
    def __init__(self):
        self.json_name = "docs\\4CW.json"
        self.CW_dict = self.get_CW_dict_from_file()

    def get_CW_dict_from_file(self):
        return json.load(open(self.json_name))

    def companies(self):
        companies = {}
        for company in self.CW_dict['corps']:
            # turn the compnay into a BadCompany object
            company = json.loads(company)
            name = company['name']
            symbol = company['symbol']
            strength = company['strength']
            influence = company['influence']
            resources = company['resources']
            strategy = company['strategy']
            security = company['security']
            company_head = company['company_head']
            hq = company['hq']
            background = company['background']
            new_company = BadCompany(name, symbol, strength, influence, resources, strategy, security, company_head, hq, background)
            companies[symbol] = new_company
        return companies

    def save_players(self, player_to_corp):
        self.CW_dict['players'] = player_to_corp
        self.save_json()

    def get_players(self):
        return self.CW_dict['players']

    def get_corps(self):
        corps = self.CW_dict['corps']
        corp_list = corps['corp_list']
        for corp in corp_list:
            yield corps[corp]

    def get_corp_by_symbol(self, symbol):
        for corp in self.get_corps():
            if corp['symbol'] == symbol:
                return corp
        return None

    def player_to_corp(self, player):
        return self.CW_dict['players'][player]

    def corp_to_stats(self, corp):
        stats = self.CW_dict['corps'][corp]
        return stats

    def get_stock_history(self):
        return self.CW_dict['stock history'] 

    def save_stock_history(self, stock_history):
        self.CW_dict['stock history'] = stock_history
        self.save_json()

    def get_all_stocks(self):
        player_corps = self.CW_dict['players']
        stocks = []
        for player in player_corps:
            corp = player_corps[player]
            stock_value = self.CW_dict["corps"][corp]["stock_value"]
            stocks.append({corp: stock_value})
        return stocks
    
    def update_stocks(self, msg):
        pass

    def player_to_moves(self, player):
        # get the player's corp
        corp = self.player_to_corp(player)
        # get the corp's moves
        moves = self.CW_dict['moves'][corp + ' moves']
        # get the basic moves
        basic_moves = self.CW_dict['moves']['basic moves']
        # combine the two
        basic_moves.update(moves)
        ultimates_enabled = self.CW_dict['moves']['ults enabled']
        if ultimates_enabled:
            ultimate = self.CW_dict['moves']['ultimate products'][corp]
            basic_moves.update(ultimate)
        # turn the dict into a list with tuples containing 'name', 'description', and 'stat'
        for move in basic_moves:
            name = basic_moves[move]['name']
            description = basic_moves[move]['description']
            stat = basic_moves[move]['stat']
            yield (name, description, stat)

    def corp_to_sxx(self, corp):
        aliases = self.CW_dict['Sxx']['aliases'][corp]
        for partner in aliases:
            alias = self.CW_dict['Sxx']['aliases'][corp][partner]
            yield (partner, self.CW_dict['Sxx'][alias])

    def corp_to_voice(self, corp):
        voice = self.CW_dict['voices'][corp]
        return voice
        
    def enable_ultimate_products(self):
        self.CW_dict['moves']['ultimates enabled'] = True
        self.save_json()

    def save_json(self):
        with open(self.json_name, 'w') as outfile:
            json.dump(self.CW_dict, outfile, indent=4)



