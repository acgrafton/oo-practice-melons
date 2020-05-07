############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                 is_bestseller):
        """Initialize a melon type."""

        self.pairings = []

        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    #Create default melon types and adds pairings.
    musk = MelonType('musk','Muskmelon',1998,'green',True,True)
    musk.add_pairing('mint')
    casaba = MelonType('cas','Casaba',2003,'orange',False,False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    crenshaw = MelonType('cren','Crenshaw',1996,'green',False,False)
    crenshaw.add_pairing('prosciutto')
    yellow_watermelon = MelonType('yw','Yellow Watermelon',2013,'yellow',False,True)
    yellow_watermelon.add_pairing('ice_cream')

    #Add melon types to list of all melons.
    all_melon_types.extend([musk,casaba,crenshaw,yellow_watermelon])

    #Return list of all melon types.
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    #Loop through list of melon types
    for melon in melon_types:
        #Print melon name and 'pairs with' verbiage
        print(f'{melon.name} pairs with')
        #Iterate through melon.pairings list and print each pairing
        for pairing in melon.pairings:
            print("-", pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #Return a dictionary by iterating through melon_types and setting the melon
    #as key and melon name as the value.
    return {melon.code : melon.name for melon in melon_types}


original_melons_types = make_melon_types()
print_pairing_info(original_melons_types)
melon_by_melon_code_dict = make_melon_type_lookup(original_melons_types)


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""


    def __init__(self, melon_type_code, shape_rating, color_rating,
                 harvested_from_field, harvested_by):
        """Initialize a melon"""

        self.type = melon_type_code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Return True if shape rating and color rating are both greater than 5 
        and if the melon was not harvested from Field 3."""

        return True if (self.shape_rating >5 and self.color_rating > 5 
                              and self.harvested_from_field != 3) else False


def make_melons():
    """Returns a list of Melon objects."""

    list_of_melons = []

    melon_1 = Melon('yw',8,7,2,'Sheila')
    melon_2 = Melon('yw',3,4,2,'Sheila')
    melon_3 = Melon('yw',9,8,3,'Sheila')
    melon_4 = Melon('cas',10,6,35,'Sheila')
    melon_5 = Melon('cren',8,9,35,'Michael')
    melon_6 = Melon('cren',8,2,35,'Michael')
    melon_7 = Melon('cren',2,3,4,'Michael')
    melon_8 = Melon('musk',6,7,4,'Michael')
    melon_9 = Melon('yw',7,10,3,'Sheila')

    return [melon_1, melon_2, melon_3, melon_4, melon_5, 
            melon_6, melon_7, melon_8, melon_9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    #Iterate through melons list and print harvested by, harvested from, 
    #and sellability.
    for melon in melons:
        sellable = "(CAN BE SOLD)" if melon.is_sellable() else "(NOT SELLABLE)"
        print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_from_field}", sellable)

harvested_melons = make_melons()

get_sellability_report(harvested_melons)





