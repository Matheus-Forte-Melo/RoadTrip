from src import gui, logic

while True:
    gui.menu('  Road Trip   ', ['Car controls'])
    user_input = int(input('Choose one option: '))

    if user_input == 1:
        gui.menu('  Car Controls  ', ['Accelerate', 'Brake', 'Turn right', 'Turn left', 'Get speed', 'Get direction'])
        logic.car_controls()



