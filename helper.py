# Imports
import sys, json

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
def element(name):
    for element in elementdata:
        if elementdata[element]['name'] == name or elementdata[element]['small'] == name:
            print(elementdata[element])

# Dictionary of commands
commands = {
    'elements' : {
        'long' : 'elements',
        'short' : 'none',
        'syntax' : 'helper.py elements',
        'command' : elements,
        'description' : 'Prints all element names, symbols, and atomic weights. To see all information for a specific element use the element (-e) feature.'
    },
    'element' : {
        'long' : 'element',
        'short' : '-e',
        'syntax' : 'helper.py element (ELEMENT_NAME or ELEMENT_SYMBOL) || helper.py -e (ELEMENT_NAME or ELEMENT_SYMBOL)',
        'command' : element,
        'description' : 'Prints all information for a specific element'
    }
}
# Main Loop
for command in commands:
    if sys.argv[1] == commands[command]['long'] or sys.argv[1] == commands[command]['short']:
        if len(sys.argv) == 3:
            commands[command]['command'](sys.argv[2])
        else: 
            commands[command]['command']()
        print('\n' + commands[command]['description'])