import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.ticker as mticker
from matplotlib.ticker import AutoMinorLocator
from get_mass_variables import obtener_valores
from settings_model_1 import obtener_archivos_y_velocidades

active_mass, density, mol_weight, div_win, electrons, DLC, REFERENCE_ELECTRODE, Mmol, surface_area = obtener_valores()
file_paths, speeds = obtener_archivos_y_velocidades()
reduced_speeds = speeds * 0.001

def obtener_tamaño(lista):
    tamaño = []
    while isinstance(lista, list):
        tamaño.append(len(lista))
        lista = lista[0]  # Suponiendo que todas las dimensiones tengan la misma longitud
    return tamaño

def correct_values(coordenadas_x, coordenadas_y, window_size = 5, std_dev_threshold = 1):
    # Take the absolute values of the x and y coordinates
    coordenadas_x = np.abs(coordenadas_x)
    coordenadas_y = np.abs(coordenadas_y)

    # Set the window size and standard deviation threshold
    #window_size = 5  # adjust this value to change the window size
    #std_dev_threshold = 1  # adjust this value to change the threshold Original: 2

    # Create a copy of the original y coordinates to store the corrected values
    corrected_y = coordenadas_y.copy()

    # Iterate over each point in the y coordinates
    for i in range(len(coordenadas_y)):
        # Calculate the start and end indices of the window
        window_start = max(0, i - window_size)
        window_end = min(len(coordenadas_y), i + window_size + 1)

        # Extract the y values within the window
        window_y = coordenadas_y[window_start:window_end]

        # Calculate the mean and standard deviation of the y values within the window
        window_avg = np.mean(window_y)
        window_std = np.std(window_y)

        # Check if the current y value is more than 2 standard deviations away from the mean
        if np.abs(coordenadas_y[i] - window_avg) > std_dev_threshold * window_std:
            # If it is, replace the current y value with the mean of the window
            corrected_y[i] = window_avg

    # Return the corrected y coordinates
    return corrected_y

def correct_values_bars(coordenadas_y, window_size=6):
    # Take the absolute values of the y coordinates
    coordenadas_y = np.abs(coordenadas_y)

    # Create a copy of the original y coordinates to store the corrected values
    corrected_y = coordenadas_y.copy()

    # Iterate over each point in the y coordinates
    for i in range(len(coordenadas_y)):
        # Calculate the start and end indices of the window
        window_start = max(0, i - window_size)
        window_end = min(len(coordenadas_y), i + window_size + 1)

        # Extract the y values within the window
        window_y = coordenadas_y[window_start:window_end]

        # Calculate the mean of the y values within the window
        window_avg = np.mean(window_y)

        # Replace the current y value with the mean of the window
        corrected_y[i] = window_avg

    # Return the corrected y coordinates
    return corrected_y

# Initialization of Ipos and Ineg matrices with zeros
Ipos = np.zeros((div_win, len(speeds)))
Ineg = np.zeros((div_win, len(speeds)))

class Normalizacion():

    def __init__(self):

        self.UExp_results = []
        self.IExp_results = []

        for i in range(len(file_paths)):
            Vbal = reduced_speeds[i]
            print(f'Etapa n={i}       Vbal={Vbal} mV/s')

            # Separate measurement file
            df_FichExp = pd.read_csv(file_paths[i], delimiter='\t', header=None, names=['Voltage', 'Current'])
            self.UExp = df_FichExp['Voltage']
            self.IExp = df_FichExp['Current'] / active_mass

            UExp_max_value = df_FichExp['Voltage'].max()
            UExp_min_value = df_FichExp['Voltage'].min()
            self.U = np.linspace(UExp_min_value, UExp_max_value, div_win)  # Modify N. of values
            self.Win = UExp_max_value - UExp_min_value  # Window Size
            print(f'Min: {UExp_min_value}, Max: {UExp_max_value}, div_win: {div_win}')
            print(f'Win: {self.Win}')

            # Separation of oxidation and reduction
            # Cathodic Current
            indice_positivo = np.where(np.diff(self.UExp) > 0)[0]
            UExppos = self.UExp[indice_positivo]
            IExppos = self.IExp[indice_positivo]
            # Anodic Current
            indice_negativo = np.where(np.diff(self.UExp) < 0)[0]
            UExpneg = self.UExp[indice_negativo]
            IExpneg = self.IExp[indice_negativo]

            # Interpolate
            # Create interpolation for Cathodic Current
            interp_func_pos = interp1d(UExppos, IExppos, kind='linear', fill_value="extrapolate")
            Ipos[:, i] = interp_func_pos(self.U)

            # Create interpolation for Anodic Current
            interp_func_neg = interp1d(UExpneg, IExpneg, kind='linear', fill_value="extrapolate")
            Ineg[:, i] = interp_func_neg(self.U)
            # # Interpolation for Cathodic Current
            # Ipos[:, i] = np.interp(U, UExppos, IExppos)
            # # Interpolation for Anodic Current
            # Ineg[:, i] = np.interp(U, UExppos, IExppos)

            self.UExp_results.append(self.UExp)
            self.IExp_results.append(self.IExp)

normalizacion_instance = Normalizacion()

class Oxidation():
    def __init__(self):
        self.IKpos = Ipos / np.sqrt(reduced_speeds)
        self.UKpos = np.sqrt(reduced_speeds)
        self.U = normalizacion_instance.U

oxidation_instance = Oxidation()

# Loop to get the slope (K1) and the value of Y(x0) (K2) for the entire window
# Definition of variables

Imodelpos = np.zeros((div_win, len(reduced_speeds)))
Imodel_1pos = np.zeros((div_win, len(reduced_speeds)))
Imodel_2pos = np.zeros((div_win, len(reduced_speeds)))
FracCapacipos = np.zeros((div_win, len(reduced_speeds)))
FracDiffuspos = np.zeros((div_win, len(reduced_speeds)))
KIdentifpos = np.zeros((div_win, 1))

p = []

for i in range(div_win):
    polpos = oxidation_instance.IKpos[i, :]
    p.append(np.polyfit(oxidation_instance.UKpos, polpos, 1))
    
    Imodelpos[i, :] = p[i][0] * reduced_speeds + p[i][1] * np.sqrt(reduced_speeds)
    Imodel_1pos[i, :] = p[i][0] * reduced_speeds
    Imodel_2pos[i, :] = p[i][1] * np.sqrt(reduced_speeds)

    FracCapacipos[i, :] = Imodel_1pos[i, :] / Imodelpos[i, :]
    FracDiffuspos[i, :] = Imodel_2pos[i, :] / Imodelpos[i, :]
    KIdentifpos[i, :] = p[i][0]

class Reduction():
    def __init__(self):
        self.IKneg= Ineg / np.sqrt(reduced_speeds)
        self.UKneg= np.sqrt(reduced_speeds)

reduction_instance = Reduction()

# Definition of variables
Imodelneg = np.zeros((div_win, len(reduced_speeds)))
Imodel_1neg = np.zeros((div_win, len(reduced_speeds)))
Imodel_2neg = np.zeros((div_win, len(reduced_speeds)))
FracCapacineg = np.zeros((div_win, len(reduced_speeds)))
FracDiffusneg = np.zeros((div_win, len(reduced_speeds)))
KIdentifneg = np.zeros((div_win, 1))

q= []

for i in range(div_win):
    polpos = reduction_instance.IKneg[i, :] # Similar to Mathlab
    q.append(np.polyfit(reduction_instance.UKneg, polpos, 1))

    Imodelneg[i, :] = q[i][0] * reduced_speeds + q[i][1] * np.sqrt(reduced_speeds)
    Imodel_1neg[i, :] = q[i][0] * reduced_speeds
    Imodel_2neg[i, :] = q[i][1] * np.sqrt(reduced_speeds)

    FracCapacineg[i, :] = Imodel_1neg[i, :] / Imodelneg[i, :]
    FracDiffusneg[i, :] = Imodel_2neg[i, :] / Imodelneg[i, :]
    KIdentifneg[i, :] = q[i][0]

################## PARAMETER B ##################

class ParameterB():
    def __init__(self):
        # Logarithm of the speed
        self.Vlog = np.emath.logn(10, reduced_speeds)
        self.bpos = []
        self.bneg = []
        self.U = normalizacion_instance.U
        # Loop to obtain the slope of the graphs of log(Vscan) VS log(Intensity) for the entire window
        for i in range(div_win):
            # Oxidation b
            logpos = np.emath.logn(10, Ipos[i,:])
            self.bpos.append(np.polyfit(self.Vlog, logpos, 1)) # The number 1 means fitting a first-degree polynomial, i.e., a straight line.
            # Reduction b
            logneg = np.emath.logn(10, Ineg[i, :])
            self.bneg.append(np.polyfit(self.Vlog, logneg, 1)) # Reviewed, the rows below do not change
        # Get the real part of the coefficients
        self.rbpos = np.real([item[0] for item in self.bpos])
        self.rbneg = np.real([item[0] for item in self.bneg])
        self.rbpos_old = self.rbpos
        self.rbneg_old = self.rbneg
        self.rbpos = correct_values(self.U,self.rbpos)
        self.rbneg = correct_values(self.U,self.rbneg)

UExp_results = []
IExp_results = []
for i in range(len(speeds)):
    # Separate measurement file
    df_FichExp = pd.read_csv(file_paths[i], delimiter='\t', header=None, names=['Voltage', 'Current'])
    UExp = df_FichExp['Voltage']
    IExp = df_FichExp['Current'] / active_mass
    UExp_results.append(UExp)
    IExp_results.append(IExp)

class Diffusive_Capacitive():
    def __init__(self):
        # Variables para plotear
        self.UExp_results = UExp_results
        self.IExp_results = IExp_results
        self.U = normalizacion_instance.U
        # Variables que cambian
        self.Imodelpos = Imodelpos
        self.Imodelneg = Imodelneg

class Capacitive_Current():
    def __init__(self):
        # Variables para plotear
        self.UExp_results = UExp_results
        self.IExp_results = IExp_results
        self.U = normalizacion_instance.U
        # Variables que cambian
        self.Imodel_1pos = Imodel_1pos
        self.Imodel_1neg = Imodel_1neg

class Diffusive_Current():
    def __init__(self):
        # Variables para plotear
        self.UExp_results = UExp_results
        self.IExp_results = IExp_results
        self.U = normalizacion_instance.U
        # Variables que cambian
        self.Imodel_2pos = Imodel_2pos
        self.Imodel_2neg = Imodel_2neg

# ~~~~~~~ PROMEDIO: CARGA NEGATIVA + CARGA POSITIVA ~~~~~~~

class Diffusive_Capacitive_Charges():
    def __init__(self):
        self.bars = []
        self.percentage_bars = []
        self.Win = normalizacion_instance.Win
        self.time_diff = self.Win / div_win

        self.Qc = np.empty(100)
        #self.Qd = np.empty(100)
        self.Qct = np.empty(5)
        self.Qdt = np.empty(5)
        self.Qtot = np.empty(5)
        self.Qt = np.empty(5)
        self.U = normalizacion_instance.U

        self.DLC = DLC

        self.x_positions = np.arange(len(self.U))
        self.barrasV_results = []
        self.Qd_results = []

        for j in range(len(speeds)):

            self.barrasV = np.empty((100, 3))
            self.Qd = np.empty(100)

            for i in range(len(self.U)):
                self.Qc[i] = (((abs(Imodel_1pos[i][j]) * self.time_diff) / reduced_speeds[j] + (abs(Imodel_1neg[i][j]) * self.time_diff) / reduced_speeds[j]) / 2) # Carga Capacitiva Q=sum(i) dt promedio de pos/neg
                self.Qd[i] = (((abs(Imodel_2pos[i][j]) * self.time_diff) / reduced_speeds[j] + (abs(Imodel_2neg[i][j]) * self.time_diff) / reduced_speeds[j]) / 2)  # Carga Difusiva Q=sum(i) dt promedio de pos/neg
                self.barrasV[i] = ([self.Qc[i] - (DLC / div_win), self.Qd[i], DLC / div_win])
            
            self.Qd_results.append(self.Qd)
            self.barrasV_results.append(self.barrasV)

            self.Qct[j] = ((np.sum(np.abs(Imodel_1pos[:, j])) * self.time_diff) / reduced_speeds[j] +
                    (np.sum(np.abs(Imodel_1neg[:, j])) * self.time_diff) / reduced_speeds[j]) / 2

            self.Qdt[j] = ((np.sum(np.abs(Imodel_2pos[:, j])) * self.time_diff) / reduced_speeds[j] +
                    (np.sum(np.abs(Imodel_2neg[:, j])) * self.time_diff) / reduced_speeds[j]) / 2

            self.Qtot[j] = ((np.sum(np.abs(Ipos[:, j])) * self.time_diff) / reduced_speeds[j] +
                    (np.sum(np.abs(Ineg[:, j])) * self.time_diff) / reduced_speeds[j]) / 2 * 1000 / 3600

            self.Qt[j] = self.Qct[j] + self.Qdt[j]

            print(f"Q capacitive at {reduced_speeds[j] * 1000} mV/s = {self.Qct[j] / 3.6} mA.h/g ó {self.Qct[j]} C/g")
            print(f"Q diffusive at {reduced_speeds[j] * 1000} mV/s = {self.Qdt[j] / 3.6} mA.h/g ó {self.Qdt[j]} C/g")
            print(f"Qtot {reduced_speeds[j] * 1000} mV/s = {self.Qtot[j]} mA.h/g ó {self.Qtot[j] * 3.6} C/g")
            print(f"Qt {reduced_speeds[j] * 1000} mV/s = {self.Qt[j] / 3.6} mA.h/g ó {self.Qt[j]} C/g")

            self.bars.append([self.Qct[j] - DLC, self.Qdt[j], DLC])

        #Corregir valores
        for num in range(len(speeds)):
            self.barrasV_results[num][:, 0] = correct_values_bars(self.barrasV_results[num][:, 0])
            self.barrasV_results[num][:, 1] = correct_values_bars(self.barrasV_results[num][:, 1])
            self.barrasV_results[num][:, 2] = correct_values_bars(self.barrasV_results[num][:, 2])
        
        for j in range(len(speeds)):
            # PERCENTAGE
            self.percentage_bars.append([(self.bars[j][0]) * 100 / self.Qt[j], (self.bars[j][1]) * 100 / self.Qt[j], (self.bars[j][2]) * 100 / self.Qt[j]])

diffusive_capacitive_charges_instance = Diffusive_Capacitive_Charges()

# STACKED BAR CHART Vs Scan Rate RAW DATA
class SpecificChargeVSSweepSpeed():
    def __init__(self):
        self.barras_transpuestas = np.array(diffusive_capacitive_charges_instance.bars).T

# STACKED BAR CHART Vs Scan Rate PERCENTAGE DATA
class PercentageofSpecificCharge():
    def __init__(self):
        self.percentage_bars_transposed = np.array(diffusive_capacitive_charges_instance.percentage_bars).T

class Masogram():
    def __init__(self):
        self.Qdpos = 0
        self.Qdneg = 0
        self.elec = electrons # Revisar
        self.masspos = np.empty(100) # Revised
        self.massneg = np.empty(100) # Revised, small variations
        self.Mmol = Mmol
        self.mass_elec = active_mass
        self.time_diff = diffusive_capacitive_charges_instance.time_diff
        self.U = normalizacion_instance.U

        self.masspos_results = []
        self.massneg_results = []

        for index, speed in enumerate(reduced_speeds):
            self.Qdpos = 0
            self.Qdneg = 0
            self.masspos = np.empty(100)
            self.massneg = np.empty(100)
            for i in range(div_win):
                self.Qdpos += abs((Imodel_2pos[i][index]*self.time_diff)/speed) # A/g*s (C)
                self.Qdneg -= (Imodel_2neg[i][index]*self.time_diff)/speed #A/g*s (C)
                self.masspos[i] = self.Mmol * self.Qdpos * self.mass_elec / (self.elec * 96500)
                self.massneg[i] = self.Mmol * self.Qdneg * self.mass_elec / (self.elec * 96500)
            self.masspos_results.append(self.masspos)
            self.massneg_results.append(self.massneg)
        
        self.UExp = UExp
        self.IExp = IExp

class InsertogramMassVersion():
    def __init__(self):
        #self.Qdpos = 0
        #self.Qdneg = 0
        self.mol_weight = mol_weight
        self.electrons = electrons
        self.density = density
        self.cteact = self.mol_weight / (electrons * 96500 * density)
        self.U = normalizacion_instance.U
        self.surface_area = surface_area
        self.div_win = div_win

        self.inser_results = []

        # Initialize the inser array with the correct shape
        self.inser = np.empty(100)

        for j in range(len(speeds)):
            value = diffusive_capacitive_charges_instance.Qd_results[j][:]
            for i in range(div_win):
                self.inser[i] = (self.cteact * ((value[i]/self.surface_area)/10000)) * 1e7
            new = correct_values(self.U, self.inser)
            self.inser_results.append(new)

class InsertogramAreaVersion():
    def __init__(self):
        #self.Qdpos = 0
        #self.Qdneg = 0
        self.mol_weight = mol_weight
        self.electrons = electrons
        self.density = density
        self.cteact = self.mol_weight / (electrons * 96500 * density)
        self.U = normalizacion_instance.U
        self.surface_area = surface_area
        self.div_win = div_win

        self.inser_results = []

        # Initialize the inser array with the correct shape
        self.inser = np.empty(100)

        for j in range(len(speeds)):
            value = diffusive_capacitive_charges_instance.Qd_results[j][:]
            for i in range(div_win):
                self.inser[i] = self.cteact * ((value[i]/self.surface_area)/10000) * 1e7
            new = correct_values(self.U, self.inser)
            self.inser_results.append(new)

# ~~~~~~~ CARGA POSITIVA ~~~~~~~

class Diffusive_Capacitive_Positive_Charge():
    def __init__(self):
        self.bars = []
        self.percentage_bars = []
        self.Win = normalizacion_instance.Win
        self.time_diff = self.Win / div_win

        self.Qc = np.empty(100)
        #self.Qd = np.empty(100)
        self.Qct = np.empty(5)
        self.Qdt = np.empty(5)
        self.Qtot = np.empty(5)
        self.Qt = np.empty(5)
        self.U = normalizacion_instance.U

        self.DLC = DLC

        self.x_positions = np.arange(len(self.U))
        self.barrasV_results = []
        self.Qd_results = []

        for j in range(len(speeds)):

            self.Qd = np.empty(100)
            self.barrasV = np.empty((100, 3))

            for i in range(len(self.U)):
                self.Qc[i] = (abs(Imodel_1pos[i][j]) * self.time_diff) / reduced_speeds[j]
                self.Qd[i] = (abs(Imodel_2pos[i][j]) * self.time_diff) / reduced_speeds[j]

                self.barrasV[i] = ([self.Qc[i] - (DLC / div_win), self.Qd[i], DLC / div_win])
            
            self.Qd_results.append(self.Qd)
            self.barrasV_results.append(self.barrasV)

            self.Qct[j] = (np.sum(np.abs(Imodel_1pos[:, j]) * self.time_diff) / reduced_speeds[j])

            self.Qdt[j] = ((np.sum(np.abs(Imodel_2pos[:, j])) * self.time_diff) / reduced_speeds[j])

            self.Qtot[j] = ((np.sum(np.abs(Ipos[:, j])) * self.time_diff) / reduced_speeds[j])* 1000 / 3600

            self.Qt[j] = self.Qct[j] + self.Qdt[j]

            print(f"Q capacitive at {reduced_speeds[j] * 1000} mV/s = {self.Qct[j] / 3.6} mA.h/g ó {self.Qct[j]} C/g")
            print(f"Q diffusive at {reduced_speeds[j] * 1000} mV/s = {self.Qdt[j] / 3.6} mA.h/g ó {self.Qdt[j]} C/g")
            print(f"Qtot {reduced_speeds[j] * 1000} mV/s = {self.Qtot[j]} mA.h/g ó {self.Qtot[j] * 3.6} C/g")
            print(f"Qt {reduced_speeds[j] * 1000} mV/s = {self.Qt[j] / 3.6} mA.h/g ó {self.Qt[j]} C/g")

            self.bars.append([self.Qct[j] - DLC, self.Qdt[j], DLC])

        #Corregir valores
        for num in range(len(speeds)):
            self.barrasV_results[num][:, 0] = correct_values_bars(self.barrasV_results[num][:, 0])
            self.barrasV_results[num][:, 1] = correct_values_bars(self.barrasV_results[num][:, 1])
            self.barrasV_results[num][:, 2] = correct_values_bars(self.barrasV_results[num][:, 2])
            sums = np.sum(self.barrasV_results[num], axis=0)  # Suma de cada columna
            self.bars[num] = (sums[0], sums[1], sums[2])
        
        for j in range(len(speeds)):
            # PERCENTAGE
            self.percentage_bars.append([(self.bars[j][0]) * 100 / self.Qt[j], (self.bars[j][1]) * 100 / self.Qt[j], (self.bars[j][2]) * 100 / self.Qt[j]])

diffusive_capacitive_positive_charge_instance = Diffusive_Capacitive_Positive_Charge()

# STACKED BAR CHART Vs Scan Rate RAW DATA
class SpecificChargeVSSweepSpeedPos():
    def __init__(self):
        self.barras_transpuestas = np.array(diffusive_capacitive_positive_charge_instance.bars).T

# STACKED BAR CHART Vs Scan Rate PERCENTAGE DATA
class PercentageofSpecificChargePos():
    def __init__(self):
        self.percentage_bars_transposed = np.array(diffusive_capacitive_positive_charge_instance.percentage_bars).T

class InsertogramMassVersionChargePos():
    def __init__(self):
        #self.Qdpos = 0
        #self.Qdneg = 0
        self.mol_weight = mol_weight
        self.electrons = electrons
        self.density = density
        self.cteact = self.mol_weight / (electrons * 96500 * density)
        self.U = normalizacion_instance.U
        self.surface_area = surface_area
        self.div_win = div_win

        self.inser_results = []

        # Initialize the inser array with the correct shape
        self.inser = np.empty(100)

        for j in range(len(speeds)):
            value = diffusive_capacitive_positive_charge_instance.Qd_results[j][:]
            for i in range(div_win):
                self.inser[i] = (self.cteact * ((value[i]/self.surface_area)/10000)) * 1e7
            new = correct_values(self.U, self.inser)
            self.inser_results.append(new)

# ~~~~~~~ CARGA NEGATIVA ~~~~~~~

class Diffusive_Capacitive_Negative_Charge():
    def __init__(self):
        self.bars = []
        self.percentage_bars = []
        self.Win = normalizacion_instance.Win
        self.time_diff = self.Win / div_win

        self.Qc = np.empty(100)
        #self.Qd = np.empty(100)
        self.Qct = np.empty(5)
        self.Qdt = np.empty(5)
        self.Qtot = np.empty(5)
        self.Qt = np.empty(5)
        self.U = normalizacion_instance.U

        self.DLC = DLC

        self.x_positions = np.arange(len(self.U))
        self.barrasV_results = []
        self.Qd_results = []

        for j in range(len(speeds)):

            self.Qd = np.empty(100)
            self.barrasV = np.empty((100, 3))

            for i in range(len(self.U)):
                self.Qc[i] = (abs(Imodel_1neg[i][j]) * self.time_diff) / reduced_speeds[j]
                self.Qd[i] = (abs(Imodel_2neg[i][j]) * self.time_diff) / reduced_speeds[j]

                self.barrasV[i] = ([self.Qc[i] - (DLC / div_win), self.Qd[i], DLC / div_win])
            
            self.barrasV_results.append(self.barrasV)
            self.Qd_results.append(self.Qd)

            self.Qct[j] = (np.sum(np.abs(Imodel_1neg[:, j]) * self.time_diff) / reduced_speeds[j])

            self.Qdt[j] = ((np.sum(np.abs(Imodel_2neg[:, j])) * self.time_diff) / reduced_speeds[j])

            self.Qtot[j] = ((np.sum(np.abs(Ineg[:, j])) * self.time_diff) / reduced_speeds[j])* 1000 / 3600

            self.Qt[j] = self.Qct[j] + self.Qdt[j]

            print(f"Q capacitive at {reduced_speeds[j] * 1000} mV/s = {self.Qct[j] / 3.6} mA.h/g ó {self.Qct[j]} C/g")
            print(f"Q diffusive at {reduced_speeds[j] * 1000} mV/s = {self.Qdt[j] / 3.6} mA.h/g ó {self.Qdt[j]} C/g")
            print(f"Qtot {reduced_speeds[j] * 1000} mV/s = {self.Qtot[j]} mA.h/g ó {self.Qtot[j] * 3.6} C/g")
            print(f"Qt {reduced_speeds[j] * 1000} mV/s = {self.Qt[j] / 3.6} mA.h/g ó {self.Qt[j]} C/g")

            self.bars.append([self.Qct[j] - DLC, self.Qdt[j], DLC])
        
        #Corregir valores
        for num in range(len(speeds)):
            self.barrasV_results[num][:, 0] = correct_values_bars(self.barrasV_results[num][:, 0])
            self.barrasV_results[num][:, 1] = correct_values_bars(self.barrasV_results[num][:, 1])
            self.barrasV_results[num][:, 2] = correct_values_bars(self.barrasV_results[num][:, 2])
        
        for j in range(len(speeds)):
            # PERCENTAGE
            self.percentage_bars.append([(self.bars[j][0]) * 100 / self.Qt[j], (self.bars[j][1]) * 100 / self.Qt[j], (self.bars[j][2]) * 100 / self.Qt[j]])

diffusive_capacitive_negative_charge_instance = Diffusive_Capacitive_Negative_Charge()

# STACKED BAR CHART Vs Scan Rate RAW DATA
class SpecificChargeVSSweepSpeedNeg():
    def __init__(self):
        self.barras_transpuestas = np.array(diffusive_capacitive_negative_charge_instance.bars).T

# STACKED BAR CHART Vs Scan Rate PERCENTAGE DATA
class PercentageofSpecificChargeNeg():
    def __init__(self):
        self.percentage_bars_transposed = np.array(diffusive_capacitive_negative_charge_instance.percentage_bars).T

class InsertogramMassVersionChargeNeg():
    def __init__(self):
        #self.Qdpos = 0
        #self.Qdneg = 0
        self.mol_weight = mol_weight
        self.electrons = electrons
        self.density = density
        self.cteact = self.mol_weight / (electrons * 96500 * density)
        self.U = normalizacion_instance.U
        self.surface_area = surface_area
        self.div_win = div_win

        self.inser_results = []

        # Initialize the inser array with the correct shape
        self.inser = np.empty(100)

        for j in range(len(speeds)):
            value = diffusive_capacitive_negative_charge_instance.Qd_results[j][:]
            for i in range(div_win):
                self.inser[i] = self.cteact * ((value[i]/self.surface_area)/10000) * 1e7
            new = correct_values(self.U, self.inser)
            self.inser_results.append(new)