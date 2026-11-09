# Periodic Table Information Finder
from pyscript import display, document


def countries_capital(e):
    document.getElementById('output').innerHTML = ' '
    user_input = document.getElementById('input1').value

    periodic_table = {
    "H": {"name": "Hydrogen", "number": 1, "mass": 1.008},
    "He": {"name": "Helium", "number": 2, "mass": 4.0026},
    "C": {"name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"name": "Oxygen", "number": 8, "mass": 15.999},
    "F": {"name": "Fluorine", "number": 9, "mass": 18.998},
    "Ne": {"name": "Neon", "number": 10, "mass": 20.180},
    "P": {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S": {"name": "Sulfur", "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine", "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon", "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium", "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine", "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton", "number": 36, "mass": 83.798},
    "I": {"name": "Iodine", "number": 53, "mass": 126.90},
    "Xe": {"name": "Xenon", "number": 54, "mass": 131.29},
    "Rn": {"name": "Radon", "number": 86, "mass": 222},

  }   

    periodic_checker = user_input in periodic_table

    display_message = ( f"sorry, this {user_input} non-metal is nawt in this lista", f"Symbol: {user_input}, Name: {periodic_table.get(user_input, {}).get('name')}, Atomic Number: {periodic_table.get(user_input, {}).get('number')}, Atomic Mass: {periodic_table.get(user_input, {}).get('mass')}" )

    final_output = display_message[periodic_checker]

    display(final_output, target="output")