# Imports
import sys, json
from constants import *

# Load Periodic Table JSON - Saves data as elementdata
with open('periodictable.json') as f:
    elementdata = json.load(f)

# Elements Function
# Lists general information for all the elements
def elements():
    for elements in elementdata:
        print(elementdata[elements]['name'] + ' (' + elementdata[elements]['small'] + '):')
        print('\tMolar Mass: ', elementdata[elements]['molar'])

# Element Function
# Lists the in depth information for a specific element
def element():
    for element in elementdata:
        if elementdata[element]['name'] == sys.argv[2] or elementdata[element]['small'] == sys.argv[2]:
            print(elementdata[element])

# Mol to Mass and Mass to Mol Conversion
# Prompts user for if they are using mass or mol conversion
# and then does the conversion for them
def molMass():
    number = input("What is the number that you wish to convert?")
    while True:
        conversion = input("Is this mols or mass? (mol/mass)")
        if conversion == "mol":
            mass = float(number) / AVOGADRO_CONSTANT
            string = "Mass: " + str(mass)
            break
        elif conversion == "mass":
            mol = float(number) * AVOGADRO_CONSTANT
            string = "Mols: " + str(mol)
            break
        else:
            print("Please respond with either mol or mass")     
    print(string)


# Load Commands JSON - Saves commands as commands
with open('commands.json') as t:
    commands = json.load(t)


# Main Loop
for command in commands:
    if sys.argv[1] == commands[command]['long'] or sys.argv[1] == commands[command]['short']:
        eval(commands[command]['command'])
        print('\n' + commands[command]['description'])