import tkinter as tk
from tkinter import messagebox

# Data for the periodic table: (symbol, atomic number, name, atomic mass, electronic configuration)
elements = [
    ("H", 1, "Hydrogen", 1.008, "1s¹"),
    ("He", 2, "Helium", 4.0026, "1s²"),
    ("Li", 3, "Lithium", 6.94, "[He] 2s¹"),
    ("Be", 4, "Beryllium", 9.0122, "[He] 2s²"),
    ("B", 5, "Boron", 10.81, "[He] 2s² 2p¹"),
    ("C", 6, "Carbon", 12.011, "[He] 2s² 2p²"),
    ("N", 7, "Nitrogen", 14.007, "[He] 2s² 2p³"),
    ("O", 8, "Oxygen", 15.999, "[He] 2s² 2p⁴"),
    ("F", 9, "Fluorine", 18.998, "[He] 2s² 2p⁵"),
    ("Ne", 10, "Neon", 20.180, "[He] 2s² 2p⁶"),
    ("Na", 11, "Sodium", 22.990, "[Ne] 3s¹"),
    ("Mg", 12, "Magnesium", 24.305, "[Ne] 3s²"),
    ("Al", 13, "Aluminium", 26.982, "[Ne] 3s² 3p¹"),
    ("Si", 14, "Silicon", 28.085, "[Ne] 3s² 3p²"),
    ("P", 15, "Phosphorus", 30.974, "[Ne] 3s² 3p³"),
    ("S", 16, "Sulfur", 32.06, "[Ne] 3s² 3p⁴"),
    ("Cl", 17, "Chlorine", 35.45, "[Ne] 3s² 3p⁵"),
    ("Ar", 18, "Argon", 39.948, "[Ne] 3s² 3p⁶"),
    ("K", 19, "Potassium", 39.098, "[Ar] 4s¹"),
    ("Ca", 20, "Calcium", 40.078, "[Ar] 4s²"),
    ("Sc", 21, "Scandium", 44.956, "[Ar] 3d¹ 4s²"),
    ("Ti", 22, "Titanium", 47.867, "[Ar] 3d² 4s²"),
    ("V", 23, "Vanadium", 50.942, "[Ar] 3d³ 4s²"),
    ("Cr", 24, "Chromium", 51.996, "[Ar] 3d⁵ 4s¹"),
    ("Mn", 25, "Manganese", 54.938, "[Ar] 3d⁵ 4s²"),
    ("Fe", 26, "Iron", 55.845, "[Ar] 3d⁶ 4s²"),
    ("Co", 27, "Cobalt", 58.933, "[Ar] 3d⁷ 4s²"),
    ("Ni", 28, "Nickel", 58.693, "[Ar] 3d⁸ 4s²"),
    ("Cu", 29, "Copper", 63.546, "[Ar] 3d¹⁰ 4s¹"),
    ("Zn", 30, "Zinc", 65.38, "[Ar] 3d¹⁰ 4s²"),
    ("Ga", 31, "Gallium", 69.723, "[Ar] 3d¹⁰ 4s² 4p¹"),
    ("Ge", 32, "Germanium", 72.63, "[Ar] 3d¹⁰ 4s² 4p²"),
    ("As", 33, "Arsenic", 74.922, "[Ar] 3d¹⁰ 4s² 4p³"),
    ("Se", 34, "Selenium", 78.971, "[Ar] 3d¹⁰ 4s² 4p⁴"),
    ("Br", 35, "Bromine", 79.904, "[Ar] 3d¹⁰ 4s² 4p⁵"),
    ("Kr", 36, "Krypton", 83.798, "[Ar] 3d¹⁰ 4s² 4p⁶"),
    ("Rb", 37, "Rubidium", 85.468, "[Kr] 5s¹"),
    ("Sr", 38, "Strontium", 87.62, "[Kr] 5s²"),
    ("Y", 39, "Yttrium", 88.906, "[Kr] 4d¹ 5s²"),
    ("Zr", 40, "Zirconium", 91.224, "[Kr] 4d² 5s²"),
    ("Nb", 41, "Niobium", 92.906, "[Kr] 4d⁴ 5s¹"),
    ("Mo", 42, "Molybdenum", 95.95, "[Kr] 4d⁵ 5s¹"),
    ("Tc", 43, "Technetium", 98, "[Kr] 4d⁵ 5s²"),
    ("Ru", 44, "Ruthenium", 101.07, "[Kr] 4d⁷ 5s¹"),
    ("Rh", 45, "Rhodium", 102.91, "[Kr] 4d⁸ 5s¹"),
    ("Pd", 46, "Palladium", 106.42, "[Kr] 4d¹⁰"),
    ("Ag", 47, "Silver", 107.87, "[Kr] 4d¹⁰ 5s¹"),
    ("Cd", 48, "Cadmium", 112.41, "[Kr] 4d¹⁰ 5s²"),
    ("In", 49, "Indium", 114.82, "[Kr] 4d¹⁰ 5s² 5p¹"),
    ("Sn", 50, "Tin", 118.71, "[Kr] 4d¹⁰ 5s² 5p²"),
    ("Sb", 51, "Antimony", 121.76, "[Kr] 4d¹⁰ 5s² 5p³"),
    ("Te", 52, "Tellurium", 127.60, "[Kr] 4d¹⁰ 5s² 5p⁴"),
    ("I", 53, "Iodine", 126.90, "[Kr] 4d¹⁰ 5s² 5p⁵"),
    ("Xe", 54, "Xenon", 131.29, "[Kr] 4d¹⁰ 5s² 5p⁶"),
    ("Cs", 55, "Cesium", 132.91, "[Xe] 6s¹"),
    ("Ba", 56, "Barium", 137.33, "[Xe] 6s²"),
    ("La", 57, "Lanthanum", 138.91, "[Xe] 5d¹ 6s²"),
    ("Ce", 58, "Cerium", 140.12, "[Xe] 4f¹ 5d¹ 6s²"),
    ("Pr", 59, "Praseodymium", 140.91, "[Xe] 4f³ 6s²"),
    ("Nd", 60, "Neodymium", 144.24, "[Xe] 4f⁴ 6s²"),
    ("Pm", 61, "Promethium", 145, "[Xe] 4f⁵ 6s²"),
    ("Sm", 62, "Samarium", 150.36, "[Xe] 4f⁶ 6s²"),
    ("Eu", 63, "Europium", 151.96, "[Xe] 4f⁷ 6s²"),
    ("Gd", 64, "Gadolinium", 157.25, "[Xe] 4f⁷ 5d¹ 6s²"),
    ("Tb", 65, "Terbium", 158.93, "[Xe] 4f⁹ 6s²"),
    ("Dy", 66, "Dysprosium", 162.50, "[Xe] 4f¹⁰ 6s²"),
    ("Ho", 67, "Holmium", 164.93, "[Xe] 4f¹¹ 6s²"),
    ("Er", 68, "Erbium", 167.26, "[Xe] 4f¹² 6s²"),
    ("Tm", 69, "Thulium", 168.93, "[Xe] 4f¹³ 6s²"),
    ("Yb", 70, "Ytterbium", 173.05, "[Xe] 4f¹⁴ 6s²"),
    ("Lu", 71, "Lutetium", 174.97, "[Xe] 4f¹⁴ 5d¹ 6s²"),
    ("Hf", 72, "Hafnium", 178.49, "[Xe] 4f¹⁴ 5d² 6s²"),
    ("Ta", 73, "Tantalum", 180.95, "[Xe] 4f¹⁴ 5d³ 6s²"),
    ("W", 74, "Tungsten", 183.84, "[Xe] 4f¹⁴ 5d⁴ 6s²"),
    ("Re", 75, "Rhenium", 186.21, "[Xe] 4f¹⁴ 5d⁵ 6s²"),
    ("Os", 76, "Osmium", 190.23, "[Xe] 4f¹⁴ 5d⁶ 6s²"),
    ("Ir", 77, "Iridium", 192.22, "[Xe] 4f¹⁴ 5d⁷ 6s²"),
    ("Pt", 78, "Platinum", 195.08, "[Xe] 4f¹⁴ 5d⁹ 6s¹"),
    ("Au", 79, "Gold", 196.97, "[Xe] 4f¹⁴ 5d¹⁰ 6s¹"),
    ("Hg", 80, "Mercury", 200.59, "[Xe] 4f¹⁴ 5d¹⁰ 6s²"),
    ("Tl", 81, "Thallium", 204.38, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹"),
    ("Pb", 82, "Lead", 207.2, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²"),
    ("Bi", 83, "Bismuth", 208.98, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³"),
    ("Po", 84, "Polonium", 209, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴"),
    ("At", 85, "Astatine", 210, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵"),
    ("Rn", 86, "Radon", 222, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶"),
    ("Fr", 87, "Francium", 223, "[Rn] 7s¹"),
    ("Ra", 88, "Radium", 226, "[Rn] 7s²"),
    ("Ac", 89, "Actinium", 227, "[Rn] 6d¹ 7s²"),
    ("Th", 90, "Thorium", 232.04, "[Rn] 6d² 7s²"),
    ("Pa", 91, "Protactinium", 231.04, "[Rn] 5f² 6d¹ 7s²"),
    ("U", 92, "Uranium", 238.03, "[Rn] 5f³ 6d¹ 7s²"),
    ("Np", 93, "Neptunium", 237, "[Rn] 5f⁴ 6d¹ 7s²"),
    ("Pu", 94, "Plutonium", 244, "[Rn] 5f⁶ 7s²"),
    ("Am", 95, "Americium", 243, "[Rn] 5f⁷ 7s²"),
    ("Cm", 96, "Curium", 247, "[Rn] 5f⁷ 6d¹ 7s²"),
    ("Bk", 97, "Berkelium", 247, "[Rn] 5f⁹ 7s²"),
    ("Cf", 98, "Californium", 251, "[Rn] 5f¹⁰ 7s²"),
    ("Es", 99, "Einsteinium", 252, "[Rn] 5f¹¹ 7s²"),
    ("Fm", 100, "Fermium", 257, "[Rn] 5f¹² 7s²"),
    ("Md", 101, "Mendelevium", 258, "[Rn] 5f¹³ 7s²"),
    ("No", 102, "Nobelium", 259, "[Rn] 5f¹⁴ 7s²"),
    ("Lr", 103, "Lawrencium", 262, "[Rn] 5f¹⁴ 7s² 7p¹"),
    ("Rf", 104, "Rutherfordium", 267, "[Rn] 5f¹⁴ 6d² 7s²"),
    ("Db", 105, "Dubnium", 270, "[Rn] 5f¹⁴ 6d³ 7s²"),
    ("Sg", 106, "Seaborgium", 271, "[Rn] 5f¹⁴ 6d⁴ 7s²"),
    ("Bh", 107, "Bohrium", 270, "[Rn] 5f¹⁴ 6d⁵ 7s²"),
    ("Hs", 108, "Hassium", 277, "[Rn] 5f¹⁴ 6d⁶ 7s²"),
    ("Mt", 109, "Meitnerium", 278, "[Rn] 5f¹⁴ 6d⁷ 7s²"),
    ("Ds", 110, "Darmstadtium", 281, "[Rn] 5f¹⁴ 6d⁸ 7s²"),
    ("Rg", 111, "Roentgenium", 282, "[Rn] 5f¹⁴ 6d⁹ 7s²"),
    ("Cn", 112, "Copernicium", 285, "[Rn] 5f¹⁴ 6d¹⁰ 7s²"),
    ("Nh", 113, "Nihonium", 286, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹"),
    ("Fl", 114, "Flerovium", 289, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²"),
    ("Mc", 115, "Moscovium", 290, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³"),
    ("Lv", 116, "Livermorium", 293, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴"),
    ("Ts", 117, "Tennessine", 294, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵"),
    ("Og", 118, "Oganesson", 294, "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶"),
]

# Function to show element details
def show_element_details(symbol, atomic_number, name, atomic_mass, electron_config):
    messagebox.showinfo(f"Element: {name}",
                        f"Symbol: {symbol}\nAtomic Number: {atomic_number}\nAtomic Mass: {atomic_mass}\n"
                        f"Electronic Configuration: {electron_config}")

# Create the main application window
root = tk.Tk()
root.title("Periodic Table")

# Create a frame for the periodic table
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Add elements to the grid
row, col = 0, 0
for element in elements:
    symbol, atomic_number, name, atomic_mass, electron_config = element
    button = tk.Button(frame, text=f"{symbol}\n{atomic_number}", width=5, height=2,
                       command=lambda s=symbol, a=atomic_number, n=name, m=atomic_mass, e=electron_config:
                       show_element_details(s, a, n, m, e))
    button.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 17:
        col = 0
        row += 1

# Start the application
root.mainloop()


