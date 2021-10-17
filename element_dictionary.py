# Accept name or abbreviation of element and return its atomic number
# Database for program
element_name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium",
                "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

element_symb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "H", "He", "Li", "Be", "B", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr",
                "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

electron_shell = ["1s^1", "1s^2", "2s^1", "2s^2", "2p^1", "2p^2", "2p^3", "2p^4", "2p^5", "2p^6", "3s^1", "3s^2", "3p^1", "3p^2", "3p^3", "3p^4", "3p^5", "3p^6", "4s^1", "4s^2", "3d^1", "3d^2", "3d^3", "3d^4", "3d^5", "3d^6", "3d^7", "3d^8", "3d^9", "3d^10", "4p^1", "4p^2", "4p^3", "4p^4", "4p^5", "4p^6", "5s^1", "5s^2", "4d^1", "4d^2", "4d^3", "4d^4", "4d^5", "4d^6", "4d^7", "4d^8", "4d^9", "4d^10", "5p^1", "5p^2", "5p^3", "5p^4", "5p^5", "5p^6", "6s^1", "6s^2", "4f^1", "4f^2", "4f^3",
                  "4f^4", "4f^5", "4f^6", "4f^7", "4f^8", "4f^9", "4f^10", "4f^11", "4f^12", "4f^13", "4f^14", "5d^1", "5d^2", "5d^3", "5d^4", "5d^5", "5d^6", "5d^7", "5d^8", "5d^9", "5d^10", "6p^1", "6p^2", "6p^3", "6p^4", "6p^5", "6p^6", "7s^1", "7s^2", "5f^1", "5f^2", "5f^3", "5f^4", "5f^5", "5f^6", "5f^7", "5f^8", "5f^9", "5f^10", "5f^11", "5f^12", "5f^13", "5f^14", "6d^1", "6d^2", "6d^3", "6d^4", "6d^5", "6d^6", "6d^7", "6d^8", "6d^9", "6d^10", "7p^1", "7p^2", "7p^3", "7p^4", "7p^5", "7p^6"]


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
        else:
            break
    return atomic_num


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
