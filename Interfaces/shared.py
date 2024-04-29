import numpy as np

file_paths = [
    'data/VPC1-KOH-3M-50.txt',
    'data/VPC1-KOH-3M-100.txt',
    'data/VPC1-KOH-3M-250.txt',
    'data/VPC1-KOH-3M-500.txt',
    'data/VPC1-KOH-3M-1000.txt'
]

file_paths = [
    'data\ME8-KOH-3M-50.txt',
    'data\ME8-KOH-3M-100.txt',
    'data\ME8-KOH-3M-250.txt',
    'data\ME8-KOH-3M-500.txt',
    'data\ME8-KOH-3M-1000.txt'
]

CONSTANT_CHARGES = 3.6                        # CONSTANTE
REFERENCE_ELECTRODE = 'E (V vs Hg/HgO)'       # USER (Reference electrode)                               YA
DENSIDAD_DE_CORRIENTE = 'j(Ag\u207B\u00B9)'   # Cuando se de el Area: I (mAcm-2)                         
name = '_'
MASS_UG = 'mass (mg)'                         # * m de micrometro 

active_mass = 1                               # USER (Mass of active material / Geometry Surface Area)   YA
speeds = np.array([5, 10, 25, 50, 100])       # USER (archivos)
reduced_speeds = speeds * 0.001               # CALCULADA
div_win = 100                                 # USER (Potential steps)                                   YA
DLC = 7.3  # C/g                              # USER (Double layer capacitance)                          YA
Mmol = 39  # g/mol                            # USER (Molar mass of active ion (g/mol))
mass_elec = 0.00112  # Massogram  # g         # USER (Mass of active material (g))
mol_weight = 197.94247  # g/mol               # USER (Molar mass of active material (g/mol))
density = 2.3  # g/cm3                        # USER (Active material density)
electrons = 1                                 # USER (Number of electrons)
surface_area = 14  # cm^2/g                   # USER (Specific surface area)

#mass_elec2 = 0.0034 * 0.7  # Insertogram
# Load -> Charge
# C&D, Percentage, Barrido, Positive Current

CONSTANT_CHARGES = 3.6                        # CONSTANTE
REFERENCE_ELECTRODE = 'E (V vs Hg/HgO)'       # USER (Reference electrode)                               YA
DENSIDAD_DE_CORRIENTE = 'j(Ag\u207B\u00B9)'   # Cuando se de el Area: I (mAcm-2)                         
name = '_'
MASS_UG = 'mass (mg)'                         # * m de micrometro 

active_mass = 1                               # USER (Mass of active material / Geometry Surface Area)   YA
speeds = np.array([5, 10, 25, 50, 100])       # USER (archivos)
reduced_speeds = speeds * 0.001               # CALCULADA
div_win = 100                                 # USER (Potential steps)                                   YA
DLC = 27.19  # C/g                              # USER (Double layer capacitance)                          YA
Mmol = 7  # g/mol                            # USER (Molar mass of active ion (g/mol))
mass_elec = 0.00238  # Massogram  # g         # USER (Mass of active material (g))
mol_weight = 728.596  # g/mol               # USER (Molar mass of active material (g/mol))
density = 3.178  # g/cm3                        # USER (Active material density)
electrons = 1                                 # USER (Number of electrons)
surface_area = 4  # cm^2/g                   # USER (Specific surface area)