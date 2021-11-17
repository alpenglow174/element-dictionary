# Accept name or abbreviation of element and return its atomic number
# Database for program
element_name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium",
                "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

element_symb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "H", "He", "Li", "Be", "B", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr",
                "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

electron_shell = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p", "8s", "5g", "6f", "7d", "8p"]

# Code to format all input text to lowercase and spaceless
def text_clean(textout):
    textout = textout.lower().strip().split()
    textout = "".join(textout)
    return textout

def input_checker():
    while True:
        try:
            atomic_num = int(input(">> Please enter the atomic number - "))
        except ValueError:
            print(">> Sorry that is the incorrect input try again")
            continue
        if atomic_num < 1:
            print(">> Sorry that is the incorrect input try again")
            continue
        elif atomic_num > 118:
            print(">> Sorry that is the incorrect input try again")
        else:
            break
    return atomic_num

# Function to find the maxshell capacity of an orbital
def maxShellLimit(shell):
    if shell[1] == 's':
        return 2    
    elif shell[1] == 'p':
        return 6
    elif shell[1] == 'd':
        return 10
    elif shell[1] == 'f':
        return 14

# Function to calculate the electronic configuration of the element
def electronic_configuration(atomic_num):
    i = 0
    ec = ''
    while atomic_num > 0:
        x = electron_shell[i]
        if atomic_num >= maxShellLimit(x):
            ec = ec + x + str(maxShellLimit(x)) + ' '
            atomic_num -= maxShellLimit(x)
        elif atomic_num < maxShellLimit(x):
            ec = ec + x + str(atomic_num) + ' '
            atomic_num = 0
        i += 1
    return ec

# Component to input data and determine atomic number
atomic_num = None
input_type = int(input(
    ">> Choose your method of input(1,2,3) <<\n 1 - Element name\n 2 - Element symbol\n 3 - Atomic number\n>> Input choice - "))
if input_type == 1:
    element_nam_input = (text_clean(input(">> Enter the element name - ")))
    atomic_num = element_name.index(element_nam_input.capitalize()) + 1
elif input_type == 2:
    element_symb_input = (text_clean(input(">> Enter the element Symbol - ")))
    atomic_num = element_symb.index(element_symb_input.capitalize()) + 1
elif input_type == 3:
    atomic_num = input_checker()

#For later formatting convenience
print(element_name[atomic_num - 1], "-")#Displays element for reference during testing
print(atomic_num)
print(electronic_configuration(atomic_num))