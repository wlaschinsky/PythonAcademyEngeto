# imports
import math
import os # clear screen

# Main function

def main_calculator():
    """Main function of calculator. Display options and select operation."""
    operations = (
    '+', '-', '*', '/', 'power', 'average', 
    'area_circle', 'volume_cylinder', 'quit'
    )

    while True:
        # TODO display options 
        display_options(operations)
        
        # TODO select operations
        choice = input('Choose an operation: ')
        
        # TODO clear screen
        clear_screen()

        # TODO if QUIT
        if choice == 'quit':
            print('Goodbye!')
            break
        
        # TODO elif basic operations
        elif choice in ('+', '-', '*', '/'):
            calculate_basic_operations()

        # # TODO elif power

        # # TODO elif average

        # # TODO elif area_circle
        # if choice == 'area_circle':
        #     calculate_area_circle()

        # # TODO elif volume_cylinder
        # if choice == 'volume_cylinder':
        #     calculate_volume_cylinder()


   
def calculate_basic_operations():
    """
    Description:
    Input values one by one, numbers and operators.
    After input "=", eval() function will be applied.

    Example:
    expression = 5+5+4-3

    Result:
    11
    """
    expression = ''
    while True:
        entry = input('Enter number or operator, "=" to calculate: ')

        if entry.isdigit() or entry in ('+', '-', '*', '/'):
            expression += entry
        elif entry == '=':
            print(f'{expression} = {eval(expression)}')
            break

# def calculate_area_circle():
#     """Calculate area of circle."""
#     radius = float(input('Enter radius: '))
#     area = math.pi * radius ** 2    # pow(radius, 2)
#     print(f'Area of circle with radius {radius} is {area:.2f}')  # 2f - 2 desetinna mista - protoze pouzivam f-string
    
def display_options(tuple_of_operations: tuple) -> None:
    """
    Description:
    Connects values from *args with .join method.
    Then adds separator before and after arguments.
    
    Example: 
    args = ("a", "b", "C")

    Result:
    ---------
    a | b | C
    ---------
    """    
    joined_operations = ' | '.join(tuple_of_operations)
    separator = '=' * len(joined_operations)
    print(separator, joined_operations, separator, sep='\n')

# def calculate_volume_cylinder():
    """Calculate volume of cylinder."""
    radius = float(input('Enter radius: '))
    height = float(input('Enter height: '))
    volume = math.pi * radius ** 2 * height
    print(f'Volume of cylinder with radius {radius} and height {height} is {volume:.2f}')

def clear_screen():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # pro windows je 'cls', pro ostatni 'clear'

# po importu se spusti jen tyhle nadefinovane funkce
if __name__ == '__main__':
    main_calculator()