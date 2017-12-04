# Creates the Help List, Add all new functions to it
help_list = ['mol_to_mass', 'mass_to_mol', 'periodic_table', 'list_periodic_table']

# Create Variable for Avogadros Number
avogadros_number = 6.022 * 10 ** 23

# Dictionary for the Periodic Table
periodic_elements = {
    'H' : {
        'Element Name' : 'Hydrogen',
        'Atomic Number' : '1'
    },
    'He' : {
        'Element Name' : 'Helium',
        'Atomic Number' : '2'
    },
    'Li' : {
        'Element Name' : 'Lithium',
        'Atomic Number' : '3'
    },
    'Be' : {
        'Element Name' : 'Beryllium',
        'Atomic Number' : '4'
    },
    'B' : {
        'Element Name' : 'Boron',
        'Atomic Number' : '5'
    },
    'C' : {
        'Element Name' : 'Carbon',
        'Atomic Number' : '6'
    },
    'N' : {
        'Element Name' : 'Nitrogen',
        'Atomic Number' : '7'
    },
    'O' : {
        'Element Name' : 'Oxygen',
        'Atomic Number' : '8'
    },
    'F' : {
        'Element Name' : 'Fluorine',
        'Atomic Number' : '9'
    },
    'Ne' : {
        'Element Name' : 'Neon',
        'Atomic Number' : '10'
    },
    'Na' : {
        'Element Name' : 'Sodium',
        'Atomic Number' : '11'
    },
    'Mg' : {
        'Element Name' : 'Magnesium',
        'Atomic Number' : '12'
    },
    'Al' : {
        'Element Name' : 'Aluminum',
        'Atomic Number' : '13'
    },
    'Si' : {
        'Element Name' : 'Silicon',
        'Atomic Number' : '14'
    },
    'P' : {
        'Element Name' : 'Phosphorus',
        'Atomic Number' : '15'
    },
    'S' : {
        'Element Name' : 'Sulfur',
        'Atomic Number' : '16'
    },
    'Cl' : {
        'Element Name' : 'Chlorine',
        'Atomic Number' : '17'
    },
    'Ar' : {
        'Element Name' : 'Argon',
        'Atomic Number' : '18'
    },
    'K' : {
        'Element Name' : 'Potassium',
        'Atomic Number' : '19'
    },
    'Ca' : {
        'Element Name' : 'Calcium',
        'Atomic Number' : '20'
    },
}


# Function for doing mol to mass
def mol_to_mass(x):
    mol = float(x)
    mass = mol / avogadros_number 
    print mass 
    con_check = raw_input('Would you like to continue?')
    if con_check == 'y':
        conversation()
    else:
        print 'Goodbye'
    
# Function for doing mass to mol
def mass_to_mol(x):
    mass = float(x)
    mol = mass * avogadros_number 
    print mol 
    con_check = raw_input('Would you like to continue?')
    if con_check == 'y':
        conversation()
    else:
        print 'Goodbye'
        
# Function which gives information for a specific element
def periodic_table(which_element):
    for elements in which_element:
        print periodic_elements[which_element]
    con_check = raw_input('Would you like to continue?')
    if con_check == 'y':
        conversation()
    else:
        print 'Goodbye'
        
# Function that prints out the entire list of elements
def list_periodic_table():
    for elements in periodic_elements:
        print elements
    con_check = raw_input('Would you like to continue?')
    if con_check == 'y':
        conversation()
    else:
        print 'Goodbye'
    
    

# Function that lets the program and conversation loop run 
def conversation():    
    text = raw_input('What do you need help with?')
    if text == 'mol_to_mass':
        x = raw_input('How many mols are there?')
        if x > 0:
            mol_to_mass(x)
    elif text == 'mass_to_mol':
        x = raw_input('how much mass is there?')
        if x > 0:
            mass_to_mol(x)
    elif text == 'periodic_table':
        which_element = raw_input('what element?')
        if which_element > 0:
            periodic_table(which_element)
    elif text == 'list_periodic_table':
        list_periodic_table()
    else:
        print 'The command you gave is not valid, try:'
        for each in help_list:
            print each
            
start = raw_input('Would you like to start the program?')
if start == 'y':
    conversation()
else:
    print 'Goodbye'

