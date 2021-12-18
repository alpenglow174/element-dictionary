import PySimpleGUI as sg
from PySimpleGUI import TITLE_LOCATION_TOP, Frame

#  ______ _                           _          _____  _      _   _                              
#  |  ____| |                         | |        |  __ \(_)    | | (_)                             
#  | |__  | | ___ _ __ ___   ___ _ __ | |_ ______| |  | |_  ___| |_ _  ___  _ __   __ _ _ __ _   _ 
#  |  __| | |/ _ \ '_ ` _ \ / _ \ '_ \| __|______| |  | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
#  | |____| |  __/ | | | | |  __/ | | | |_       | |__| | | (__| |_| | (_) | | | | (_| | |  | |_| |
#  |______|_|\___|_| |_| |_|\___|_| |_|\__|      |_____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
#                                                                                             __/ |
#                                                                                            |___/  

'''
Database for program
'''
# Accept name or abbreviation of element and return its atomic number

element_name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium",
                "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

element_symb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr",
                "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

electron_shell = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p", "8s", "5g", "6f", "7d", "8p"]

superScript = [0, "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "¹⁰", "¹¹", "¹²", "¹³", "¹⁴"] 


'''
INPUT
'''
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

def validityChecker(inval,input_type):
    if input_type == 1 and (text_clean(inval).capitalize()) in element_name:
        return True
    elif input_type == 2 and (text_clean(inval).capitalize()) in element_symb:
        return True
    elif input_type == 3 and inval.isdigit() == True:
        if int(inval) > 0 and int(inval) < 119:
            return True
        else:
            return False
    else:
        return False

'''
Functions/ Calculations
'''
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
    i = 0 # variable to traverse shell list
    ec = '' # variable for final electronic configuration
    while atomic_num > 0:
        x = electron_shell[i]
        if atomic_num >= maxShellLimit(x):
            ec = ec + x + str(superScript[maxShellLimit(x)])
            atomic_num -= maxShellLimit(x)
        elif atomic_num < maxShellLimit(x):
            ec = ec + x + str(superScript[atomic_num])
            atomic_num = 0
        i += 1
    #Exceptions
    if atomic_num == 24: #Cr
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d⁵'
    elif atomic_num == 29: #Cu
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰'
    elif atomic_num == 41: #Nb
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁴'
    elif atomic_num == 46: #Pd
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s⁰ 4d¹⁰'
    elif atomic_num == 58: #Ce
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f²'
    elif atomic_num == 65: #Tb
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁹'
    elif atomic_num == 91: #Pa
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f² 6d¹'
    elif atomic_num == 97: #Bk
        ec = '1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁹'
    return ec

def atomic_Number(inval, input_type):
    # Component to input data and determine atomic number
    atomic_num = None
    if input_type == 1:
        element_nam_input = (text_clean(inval))
        atomic_num = element_name.index(element_nam_input.capitalize()) + 1
    elif input_type == 2:
        element_symb_input = (text_clean(inval))
        atomic_num = element_symb.index(element_symb_input.capitalize()) + 1
    elif input_type == 3:
        atomic_num = inval
    return atomic_num

period = 0
valence_e = 0
def bohrEc():
    # Find EC in Bohr model (KLMN)
    K, L, M, N, O, P, Q, R = 0, 0, 0, 0, 0, 0, 0, 0
    EC_var = atomicNumber

    # 2,8,8,16,16,32
    # Cr, Cu, Nb, Pd, Ce, Ce, Tb, Pa, Bk
    # 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p, 8s, 5g, 6f, 7d, 8p, and 9s


    while EC_var > 0: #Transition elements valency
        if K+1 < 3:  # +1 because base is 0 and it will run 3 times otherwise
            # fill 2 in K
            K += 1
            EC_var -= 1
        elif L+1 < 9:
            # fill 8 in L
            L += 1
            EC_var -= 1
        elif M+1 < 9:
            # fill 8 in M
            M += 1
            EC_var -= 1
        elif N+1 < 3:
            # fill 2 in N
            N += 1
            EC_var -= 1
    # Now we are filling based on Quantum Model
        elif M+1 < 19:
            # fill 18 in M
            M += 1
            EC_var -= 1
        elif N+1 < 9:
            # fill 8 in N
            N += 1
            EC_var -= 1
        elif O+1 < 3:
            # fill 2 in O
            O += 1
            EC_var -= 1
        elif N+1 < 19:
            # fill 18 in N
            N += 1
            EC_var -= 1
        elif O+1 < 9:
            # fill 8 in O
            O += 1
            EC_var -= 1
        elif P+1 < 3:
            # fill 2 in P
            P += 1
            EC_var -= 1
        elif N+1 < 33:
            # fill 32 in N
            N += 1
            EC_var -= 1
        elif O+1 < 19:
            # fill 18 in O
            O += 1
            EC_var -= 1
        elif P+1 < 9:
            # fill 8 in P
            P += 1
            EC_var -= 1
        elif Q+1 < 3:
            # fill 2 in Q
            Q += 1
            EC_var -= 1
        elif O+1 < 33:
            # fill 32 in O
            O += 1
            EC_var -= 1
        elif P+1 < 19:
            # fill 18 in P
            P += 1
            EC_var -= 1   
        elif Q+1 < 9:
            # fill 8 in Q
            Q += 1
            EC_var -= 1
        elif R+1 < 3:
            # fill 2 in R
            R += 1
            EC_var -= 1
        elif O+1 < 51:
            # fill 50 in O
            O += 1
            EC_var -= 1
        elif P+1 < 33:
            # fill 32 in P
            P += 1
            EC_var -= 1  
        elif Q+1 < 19:
            # fill 18 in Q
            Q += 1
            EC_var -= 1
        elif R+1 < 9:
            # fill 8 in R
            R += 1
            EC_var -= 1
        

    #the exceptions:
    if atomicNumber == 24:#Cr
        K = 2
        L = 8
        M = 13
        N = 1
        O = 0
        P = 0
        Q = 0
        R = 0
    elif atomicNumber == 29:#Cu
        K = 2
        L = 8
        M = 18
        N = 1
        O = 0
        P = 0
        Q = 0
        R = 0
    elif atomicNumber == 41:#Nb
        K = 2
        L = 8
        M = 18
        N = 12
        O = 1
        P = 0
        Q = 0
        R = 0
    elif atomicNumber == 46:#Pd
        K = 2
        L = 8
        M = 18
        N = 18
        O = 0
        P = 0
        Q = 0
        R = 0
    elif atomicNumber == 58:#Ce
        K = 2
        L = 8
        M = 18
        N = 20
        O = 8
        P = 2
        Q = 0
        R = 0
    elif atomicNumber == 65:#Tb
        K = 2
        L = 8
        M = 18
        N = 27
        O = 8
        P = 2
        Q = 0
        R = 0
    elif atomicNumber == 91:#Pa
        K = 2
        L = 8
        M = 18
        N = 32
        O = 20
        P = 9
        Q = 2
        R = 0
    elif atomicNumber == 97:#Bk
        K = 2
        L = 8
        M = 18
        N = 32
        O = 27
        P = 8
        Q = 2
        R = 0

    '''
    valenc electron
    '''

    global valence_e
    # setting no of valence electrons (KLMNOPQR)
    if R > 0:
        # no of valence electrons is no of electrons is N
        valence_e = R
    elif Q > 0:
        valence_e = N
    elif P > 0:
        valence_e = M
    elif O > 0:
        valence_e = M
    elif N > 0:
        valence_e = N
    elif M > 0:
        valence_e = M
    elif L > 0:
        valence_e = L
    elif K > 0:
        valence_e = K
    
    global period
    period_temp = 9 #temporary period
    SHELL = [R, Q, P, O, N,  M, L, K ] #list of shells
    for i in SHELL:
        period_temp-=1
        if i>0:
            period = period_temp
            break #to stop loop and not continue
    
    return K,L,M,N,O,P,Q,R


def bohrPrint(ec):
    ecString = ''
    for i in ec:
        if i == 0:
            continue
        ecString+=str(i)
        ecString+=', '
    return ecString.rstrip(', ')



'''
OUTPUT
'''
'''program_state = "r"'''
'''while program_state == "r":
    atomicNumber = atomic_Number()
    #For later formatting convenience
    print(">>",element_name[atomicNumber - 1], "<<") #Displays element for reference during testing
    print("  >> Atomic number            >> ",atomicNumber)
    print("  >> Electronic configuration >> ",electronic_configuration(atomicNumber))
    print("  >> Bohr Configuration       >> ",bohrPrint(bohrEc()))
    program_state = input(">> Press r to restart program and q to quit >> ")'''
    
sg.theme("DarkGrey5")

outputLayout = [[sg.Text(">> Element" + " <<\n  >> Element Symbol             >> " + "\n  >> Atomic Number               >> " + "\n  >> Electronic Configuration >> " + "\n  >> Bohr Configuration         >>  ",key='-OUTPUT-')]]
inputLayout = [[sg.Text("Please choose method of input :"),sg.Radio("Element Name",group_id="choice",enable_events=True,key=1),sg.Radio("Element Symbol",group_id="choice",enable_events=True,key=2),sg.Radio("Atomic Number",group_id="choice",default=True,enable_events=True,key=3)],
          [sg.Text("Enter your input : "),sg.Input(expand_x=True,pad=(10),enable_events=True, key='-IN-')]]
layout = [[Frame("Input parameters", inputLayout, title_location=TITLE_LOCATION_TOP,expand_x=True,expand_y=True)],
          [Frame("Element Description",outputLayout, title_location=TITLE_LOCATION_TOP, expand_x=True, expand_y=True)]]

window = sg.Window("Element dictionary", layout,margins=(10,10),scaling=1.8)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    input_type = 3
    if event == sg.WINDOW_CLOSED:
        break
    if values[1] == True:
        input_type = 1
    elif values[2] == True:
        input_type = 2
    elif values[3] == True:
        input_type = 3
    if validityChecker(values['-IN-'],input_type) == True:
        atomicNumber = int(atomic_Number(values['-IN-'], input_type))
        '''print(">>",element_name[atomicNumber - 1], "<<") #Displays element for reference during testing
        print("  >> Atomic number            >> ",atomicNumber)
        print("  >> Electronic configuration >> ",electronic_configuration(atomicNumber))
        print("  >> Bohr Configuration       >> ",)'''
        outputStr = ">> " + element_name[atomicNumber - 1] + " <<\n  >> Element Symbol             >> " + element_symb[atomicNumber - 1] + "\n  >> Atomic Number               >> " + str(atomicNumber) + "\n  >> Electronic Configuration >> " + electronic_configuration(atomicNumber) + "\n  >> Bohr Configuration         >>  " + bohrPrint(bohrEc()) + "\n  >> Valence Electrons         >>  " + str(valence_e) + "\n  >> Period         >>  " + str(period)
        window['-OUTPUT-'].update(outputStr)
    else: window['-OUTPUT-'].update("\n\n\n\n")

window.close()