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

# Load Commands JSON - Saves commands as commands
with open('commands.json') as t:
    commands = json.load(t)


# Main Loop
for command in commands:
    if sys.argv[1] == commands[command]['long'] or sys.argv[1] == commands[command]['short']:
        if len(sys.argv) == 3:
            eval(commands[command]['command'] + "('" + sys.argv[2] + "')")
        else: 
            eval(commands[command]['command'] + '()')
        print('\n' + commands[command]['description'])