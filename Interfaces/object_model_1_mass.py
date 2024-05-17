from archivos import file_paths, veloc

class Object_Model_1_Mass_():

    def __init__(self, reference_electrode=None, active_mass=None, speeds=None, div_win=None, DLC=None, Mmol=None, mol_weight = None, density=None, electrons=None, surface_area=None):

        # Constantes
        self.CONSTANT_CHARGES = 3.6
        self.DENSIDAD_DE_CORRIENTE = 'j(Ag\u207B\u00B9)'
        self.MASS_UG = 'mass (mg)'

        # Variables
        self.file_paths = file_paths
        self.speeds = veloc

        self.active_mass = active_mass # USER (Mass of active material (g))
        self.density = density  # g/cm3 USER (Active material density)
        self.mol_weight = mol_weight # g/mol USER (Molar mass of active material (g/mol))
        self.div_win = div_win # USER (Potential steps)
        self.electrons = electrons # USER (Number of electrons)
        self.DLC = DLC  # C/g USER (Electric Double layer capacitance) 
        self.reference_electrode = reference_electrode #'E (V vs Hg/HgO)' Reference Electrode
        self.Mmol = Mmol  # g/mol USER (Molar mass of active ion (g/mol))
        self.surface_area = surface_area  # cm^2/g USER (Specific surface area)

        # Derivadas
        self.reduced_speeds = speeds * 0.001