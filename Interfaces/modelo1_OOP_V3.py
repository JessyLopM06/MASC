import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from cerebro_modelo import Normalizacion, Oxidation, Reduction, ParameterB, Diffusive_Capacitive, Capacitive_Current, Diffusive_Current, Diffusive_Capacitive_Charges, SpecificChargeVSSweepSpeed, PercentageofSpecificCharge, Diffusive_Capacitive_Positive_Charge, SpecificChargeVSSweepSpeedPos, PercentageofSpecificChargePos, Diffusive_Capacitive_Negative_Charge, SpecificChargeVSSweepSpeedNeg, PercentageofSpecificChargeNeg, Masogram, Insertogram
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.ticker as mticker
from matplotlib.ticker import AutoMinorLocator
import numpy as np
from shared import speeds, DENSIDAD_DE_CORRIENTE, REFERENCE_ELECTRODE, MASS_UG

normalizacion_values = Normalizacion()
oxidation_values = Oxidation()
reduction_values = Reduction()
parameterB_values = ParameterB()
diffusive_capacitive_currents_values = Diffusive_Capacitive()
capacitive_current_values = Capacitive_Current()
diffusive_current_values = Diffusive_Current()
diffusive_capacitive_charges_values = Diffusive_Capacitive_Charges()
scharge_vs_sspeed_values = SpecificChargeVSSweepSpeed()
percentage_specific_charge_values = PercentageofSpecificCharge()
masogram_values = Masogram()
insertogram_values = Insertogram()
diffusive_capacitive_positive_charge_values = Diffusive_Capacitive_Positive_Charge()
scharge_vs_sspeed_pos_values = SpecificChargeVSSweepSpeedPos()
percentage_specific_charge_pos_values = PercentageofSpecificChargePos()
diffusive_capacitive_negative_charge_values = Diffusive_Capacitive_Negative_Charge()
scharge_vs_sspeed_neg_values = SpecificChargeVSSweepSpeedNeg()
percentage_specific_charge_neg_values = PercentageofSpecificChargeNeg()

normalization_names_list = []  # Arreglo para almacenar los nombres generados
normalization_names_dict = {}  # Diccionario para almacenar los datos
diffusive_capacitive_currents_names_list = []
diffusive_capacitive_currents_names_dict = {}
capacitive_current_names_list = []
capacitive_current_names_dict = {}
diffusive_current_names_list = []
diffusive_current_names_dict = {}
diffusive_capacitive_charges_names_list = []
diffusive_capacitive_charges_names_dict = {}
diffusive_capacitive_positive_charge_names_list = []
diffusive_capacitive_positive_charge_names_dict = {}
diffusive_capacitive_negative_charge_names_list = []
diffusive_capacitive_negative_charge_names_dict = {}
pestañas_superiores = ['Normalization', 'Ks positive current ', 'Ks negative current', 'b parameter', 'Cyclic voltammograms\n(Experimental & Model)', 'Capacitive Current', 'Diffusive Current', 'Deconvolution of\nSpecific Charge vs Scan rate', 'Specific charge vs Scan rate', '% Specific Charge vs Scan Rate', 'Massograms', 'Active Thickness', 'Deconvolution of\nSpecific Charge vs Scan rate (+)', 'Specific charge vs Scan rate (+)', '% Specific Charge vs Scan Rate (+)', 'Deconvolution of\nSpecific Charge vs Scan rate (-)', 'Specific charge vs Scan rate (-)', '% Specific Charge vs Scan Rate (-)',]

class ZoomableGraph:
    def __init__(self, parent, label):
        self.label = label
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent)
        self.toolbar = NavigationToolbar2Tk(self.canvas, parent)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def show(self):
        self.ax.clear()
        x = np.linspace(0, 10, 100)
        y = np.linspace(0, 10, 100)

        if self.label in normalization_names_dict:
            options = normalization_names_dict[self.label]
            data = options['data']
            speed = options['speed']
            self.ax.plot(data[0], data[1], options['fmt'], markersize=2, label=options['label'])
            self.ax.set_title(options['title'])
            self.ax.xaxis.set_major_formatter(options['x_major_formatter'])
            self.ax.xaxis.set_major_locator(options['x_major_locator'])
            self.ax.xaxis.set_minor_locator(options['x_minor_locator'])
            self.ax.yaxis.set_major_formatter(options['y_major_formatter'])
            self.ax.yaxis.set_major_locator(options['y_major_locator'])
            self.ax.yaxis.set_minor_locator(options['y_minor_locator'])
            self.ax.legend()
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/normalization_{speed}mVs.png') #graph
            self.save_data(data=data[0], text=f'OOPVersion/generated_data/normalization_UExp_{speed}mVs.txt') # x
            self.save_data(data=data[1], text=f'OOPVersion/generated_data/normalization_IExp_{speed}mVs.txt') # y
        elif self.label == pestañas_superiores[1]:
            for i in range(len(oxidation_values.IKpos)):
                self.ax.plot(oxidation_values.UKpos, oxidation_values.IKpos[i], label=f'Line {i+1}', linewidth=0.8)
            self.ax.set_xlabel('Scan rate')
            self.ax.set_ylabel('Intensity')
            self.ax.grid(False)
            #self.ax.set_title()
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Oxidation_ScanRate_vs_Intensity.png') #graph
            self.save_data(oxidation_values.UKpos, text='OOPVersion/generated_data/Oxidation_UKpos.txt') # x
            self.save_data(oxidation_values.IKpos[i], text='OOPVersion/generated_data/Oxidation_IKpos.txt') # y
        elif self.label == pestañas_superiores[2]:
            for i in range(len(reduction_values.IKneg)):
                self.ax.plot(reduction_values.UKneg, reduction_values.IKneg[i], label=f'Line {i+1}', linewidth=0.8)
            self.ax.set_xlabel('Scan rate')
            self.ax.set_ylabel('Intensity')
            self.ax.grid(False)
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Intensity_ScanRate_vs_Intensity.png') #graph
            self.save_data(reduction_values.UKneg, text='OOPVersion/generated_data/Reduction_UKneg.txt') # x
            self.save_data(reduction_values.IKneg[i], text='OOPVersion/generated_data/Reduction_IKneg.txt') # y
        elif self.label == pestañas_superiores[3]:
            self.ax.plot(parameterB_values.U, parameterB_values.rbpos, 'r', label='b oxidation')
            self.ax.plot(parameterB_values.U, parameterB_values.rbneg, 'b', label='b reduction')
            self.ax.set_xlabel(REFERENCE_ELECTRODE)
            self.ax.set_ylabel('b parameter')
            self.ax.set_title('b - oxidation & reduction') 
            self.ax.legend()
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/ParameterB_Oxidation_Reduction.png') #graph
            self.save_data(parameterB_values.U, text=f'OOPVersion/generated_data/ParameterB_U.txt') # x (1&2)
            self.save_data(parameterB_values.rbpos, text=f'OOPVersion/generated_data/ParameterB_rbpos.txt') # y1
            self.save_data(parameterB_values.rbneg, text=f'OOPVersion/generated_data/ParameterB_rbneg.txt') # y2
        elif self.label in diffusive_capacitive_currents_names_dict:
            options = diffusive_capacitive_currents_names_dict[self.label]
            speed = options['speed']
            data1 = options['data1']
            data2 = options['data2']
            data3 = options['data3']
            self.ax.plot(data1[0], data1[1],options['fmt1'], markersize=options['markersize1'])
            self.ax.plot(data2[0], data2[1],options['fmt2'], markersize=options['markersize2'])
            self.ax.plot(data3[0], data3[1],options['fmt3'], markersize=options['markersize3'])
            self.ax.set_title(options['title'])
            self.ax.xaxis.set_major_formatter(options['x_major_formatter'])
            self.ax.xaxis.set_major_locator(options['x_major_locator'])
            self.ax.xaxis.set_minor_locator(options['x_minor_locator'])
            self.figure.legend(options['legend'])
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/C&D_Currents_{speed}mVs.png') #graph
            self.save_data(data1[0], text=f'OOPVersion/generated_data/C&D_Currents_UExp_results_{speed}mVs.txt') # x1
            self.save_data(data1[1], text=f'OOPVersion/generated_data/C&D_Currents_IExp_results_{speed}mVs.txt') # y1
            self.save_data(data2[0], text=f'OOPVersion/generated_data/C&D_Currents_U_mVs.txt') # x (1&2) para todas las velocidades.
            self.save_data(data2[1], text=f'OOPVersion/generated_data/C&D_Currents_Imodelpos_{speed}mVs.txt') # y1
            self.save_data(data3[1], text=f'OOPVersion/generated_data/C&D_Currents_Imodelneg_{speed}mVs.txt') # y1
        elif self.label in capacitive_current_names_dict:
            options = capacitive_current_names_dict[self.label]
            speed = options['speed']
            data1 = options['data1']
            data2 = options['data2']
            data3 = options['data3']
            self.ax.plot(data1[0], data1[1],options['fmt1'], markersize=options['markersize1'])
            self.ax.plot(data2[0], data2[1],options['fmt2'], markersize=options['markersize2'])
            self.ax.plot(data3[0], data3[1],options['fmt3'], markersize=options['markersize3'])
            self.ax.set_title(options['title'])
            self.ax.xaxis.set_major_formatter(options['x_major_formatter'])
            self.ax.xaxis.set_major_locator(options['x_major_locator'])
            self.ax.xaxis.set_minor_locator(options['x_minor_locator'])
            self.figure.legend(options['legend'])
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/Capacitive_Current_{speed}mVs.png') #graph
            self.save_data(data1[0], text=f'OOPVersion/generated_data/Capacitive_Current_UExp_results_{speed}mVs.txt') # x1
            self.save_data(data1[1], text=f'OOPVersion/generated_data/Capacitive_Current_IExp_results_{speed}mVs.txt') # y1
            self.save_data(data2[0], text=f'OOPVersion/generated_data/Capacitive_Current_U_mVs.txt') # x (1&2) para todas las velocidades.
            self.save_data(data2[1], text=f'OOPVersion/generated_data/Capacitive_Current_Imodel_1pos_{speed}mVs.txt') # y1
            self.save_data(data3[1], text=f'OOPVersion/generated_data/Capacitive_Current_Imodel_1neg_{speed}mVs.txt') # y1
        elif self.label in diffusive_current_names_dict:
            options = diffusive_current_names_dict[self.label]
            speed = options['speed']
            data1 = options['data1']
            data2 = options['data2']
            data3 = options['data3']
            self.ax.plot(data1[0], data1[1],options['fmt1'], markersize=options['markersize1'])
            self.ax.plot(data2[0], data2[1],options['fmt2'], markersize=options['markersize2'])
            self.ax.plot(data3[0], data3[1],options['fmt3'], markersize=options['markersize3'])
            self.ax.set_title(options['title'])
            self.ax.xaxis.set_major_formatter(options['x_major_formatter'])
            self.ax.xaxis.set_major_locator(options['x_major_locator'])
            self.ax.xaxis.set_minor_locator(options['x_minor_locator'])
            self.figure.legend(options['legend'])
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/Diffusive_Current_{speed}mVs.png') #graph
            self.save_data(data1[0], text=f'OOPVersion/generated_data/Diffusive_Current_UExp_results_{speed}mVs.txt') # x1
            self.save_data(data1[1], text=f'OOPVersion/generated_data/Diffusive_Current_IExp_results_{speed}mVs.txt') # y1
            self.save_data(data2[0], text=f'OOPVersion/generated_data/Diffusive_Current_U_mVs.txt') # x (1&2) para todas las velocidades.
            self.save_data(data2[1], text=f'OOPVersion/generated_data/Diffusive_Current_Imodel_2pos_{speed}mVs.txt') # y1
            self.save_data(data3[1], text=f'OOPVersion/generated_data/Diffusive_Current_Imodel_2neg_{speed}mVs.txt') # y1
        elif self.label in diffusive_capacitive_charges_names_dict:
            options = diffusive_capacitive_charges_names_dict[self.label]
            speed = options['speed']
            data1 = options['data1']
            data2 = options['data2']
            data3 = options['data3']
            self.ax.bar(data1[0], data1[1], bottom=options['bottom1'], label=options['label1'])
            self.ax.bar(data2[0], data2[1], bottom=options['bottom2'], label=options['label2'])
            self.ax.bar(data3[0], data3[1], bottom=options['bottom3'], label=options['label3'])
            self.ax.set_title(options['title'])
            self.ax.set_xticks(options['set_xticks'])
            self.ax.set_xticklabels(options['set_xticklabels'])
            self.ax.locator_params(axis=options['locator_params_axis'], nbins=options['nbins'])
            self.ax.legend()
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/C&D_Charges_{speed}mVs.png') #graph
            self.save_data(data1[0], text='OOPVersion/generated_data/C&D_Charges_x_positions_mVs.txt') # x (1,2&3) para todas las velocidades
            self.save_data(data1[1], text=f'OOPVersion/generated_data/C&D_Charges_Pseudocapacitive_{speed}mVs.txt') # y1 (Bottom)
            self.save_data(data2[1], text=f'OOPVersion/generated_data/C&D_Charges_Diffusive_{speed}mVs.txt') # y2 (Middle)
            self.save_data(data3[1], text=f'OOPVersion/generated_data/C&D_Charges_DoubleLayer_{speed}mVs.txt') # y3 (Top)
        elif self.label == pestañas_superiores[8]:
            self.barras_transpuestas = scharge_vs_sspeed_values.barras_transpuestas
            self.bars = self.ax.bar(range(len(self.barras_transpuestas[0])), self.barras_transpuestas[0])
            # Add stacked bars
            for i in range(1, len(self.barras_transpuestas)):
                self.bars = self.ax.bar(range(len(self.barras_transpuestas[i])), self.barras_transpuestas[i], bottom=np.sum(self.barras_transpuestas[:i], axis=0))
            # Customize the plot
            self.ax.set_xlabel('Scan Rate (mV/s)')
            self.ax.set_xticks(range(len(speeds)))
            self.ax.set_xticklabels(speeds)
            self.ax.set_ylabel('Specific Charge (C/g)')
            self.ax.legend(['Pseudocapacitive', 'Diffusive', 'Double Layer'])
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Specific_Charge_VS_Sweed_Speed.png')
            self.save_data(self.barras_transpuestas[0], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_Pseudocapacitive.txt') # y1 (Bottom)
            self.save_data(self.barras_transpuestas[1], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_Diffusive.txt') # y2 (Middle)
            self.save_data(self.barras_transpuestas[2], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_DoubleLayer.txt') # y3 (Top)
        elif self.label == pestañas_superiores[9]:
            self.percentage_bars_transposed = percentage_specific_charge_values.percentage_bars_transposed
            self.bars = self.ax.bar(range(len(self.percentage_bars_transposed[0])), self.percentage_bars_transposed[0])
            # Add stacked bars
            for i in range(1, len(self.percentage_bars_transposed)):
                self.bars = self.ax.bar(range(len(self.percentage_bars_transposed[i])), self.percentage_bars_transposed[i], bottom=np.sum(self.percentage_bars_transposed[:i], axis=0))
            # Customize the plot
            self.ax.set_xlabel('Scan Rate (mV/s)')
            self.ax.set_xticks(range(len(speeds)))
            self.ax.set_xticklabels(speeds)
            self.ax.set_ylabel('Charge (%)')
            self.ax.legend(['Pseudocapacitive', 'Diffusive', 'Double Layer'])
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Percentage_of_Specific_Charge.png')
            self.save_data(self.percentage_bars_transposed[0], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_Pseudocapacitive.txt') # y1 (Bottom)
            self.save_data(self.percentage_bars_transposed[1], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_Diffusive.txt') # y2 (Middle)
            self.save_data(self.percentage_bars_transposed[2], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_DoubleLayer.txt') # y3 (Top)
        elif self.label == pestañas_superiores[10]:
            # Get values
            self.U = masogram_values.U
            self.masspos = masogram_values.masspos
            self.ax.plot(self.U, self.masspos * 1e6, 'b', linewidth=3, label='mass (ug)')
            # Customize the plot
            self.ax.set_xlabel(REFERENCE_ELECTRODE)
            self.ax.set_ylabel(MASS_UG, color='b')
            self.ax.tick_params('y', colors='b')
            # Get values
            self.massneg = masogram_values.massneg
            # Add the negative data series to the first data series (blue)
            self.ax.plot(self.U, self.massneg * 1e6, 'b', linewidth=3)
            # Create the second data series (red)
            self.ax2 = self.ax.twinx()
            self.ax2.plot(masogram_values.UExp, masogram_values.IExp, 'r', linewidth=3, label=DENSIDAD_DE_CORRIENTE) # x=UExp y=IExp
            self.ax2.set_ylabel(DENSIDAD_DE_CORRIENTE, color='r')
            self.ax2.tick_params('y', colors='r')
            #Final
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Masogram.png') #graph
            self.save_data(self.U, text='OOPVersion/generated_data/Masogram_U.txt') # x(1&2)
            self.save_data(self.masspos, text='OOPVersion/generated_data/Masogram_masspos.txt') # y1
            self.save_data(self.massneg * 1e6, text='OOPVersion/generated_data/Masogram_massneg.txt') # y2
            self.save_data(masogram_values.UExp, text='OOPVersion/generated_data/Masogram_UExp.txt') # x3
            self.save_data(masogram_values.IExp, text='OOPVersion/generated_data/Masogram_IExp.txt') # y3
        elif self.label == pestañas_superiores[11]:
            # Get values
            self.U = insertogram_values.U
            self.inser = insertogram_values.inser
            self.ax.plot(self.U, self.inser, 'b', linewidth=1)
            self.ax.set_xlabel(REFERENCE_ELECTRODE)
            self.ax.set_ylabel('Active Thickness (cm)')
            #Final
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Insertogram.png') #graph
            self.save_data(self.U, text='OOPVersion/generated_data/Insertogram_U.txt') # x
            self.save_data(self.inser, text='OOPVersion/generated_data/Insertogram_masspos.txt') # y
        elif self.label in diffusive_capacitive_positive_charge_names_dict:
            options = diffusive_capacitive_positive_charge_names_dict[self.label]
            speed = options['speed']
            data1 = options['data1']
            data2 = options['data2']
            data3 = options['data3']
            self.ax.bar(data1[0], data1[1], bottom=options['bottom1'], label=options['label1'])
            self.ax.bar(data2[0], data2[1], bottom=options['bottom2'], label=options['label2'])
            self.ax.bar(data3[0], data3[1], bottom=options['bottom3'], label=options['label3'])
            self.ax.set_title(options['title'])
            self.ax.set_xticks(options['set_xticks'])
            self.ax.set_xticklabels(options['set_xticklabels'])
            self.ax.locator_params(axis=options['locator_params_axis'], nbins=options['nbins'])
            self.ax.legend()
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/C&D_Positive_Charge_{speed}mVs.png') #graph
            self.save_data(data1[0], text='OOPVersion/generated_data/C&D_Positive_Charge_x_positions_mVs.txt') # x (1,2&3) para todas las velocidades
            self.save_data(data1[1], text=f'OOPVersion/generated_data/C&D_Positive_Charge_Pseudocapacitive_{speed}mVs.txt') # y1 (Bottom)
            self.save_data(data2[1], text=f'OOPVersion/generated_data/C&D_Positive_Charge_Diffusive_{speed}mVs.txt') # y2 (Middle)
            self.save_data(data3[1], text=f'OOPVersion/generated_data/C&D_Positive_Charge_DoubleLayer_{speed}mVs.txt') # y3 (Top)
        elif self.label == pestañas_superiores[13]:
            self.barras_transpuestas = scharge_vs_sspeed_pos_values.barras_transpuestas
            self.bars = self.ax.bar(range(len(self.barras_transpuestas[0])), self.barras_transpuestas[0])
            # Add stacked bars
            for i in range(1, len(self.barras_transpuestas)):
                self.bars = self.ax.bar(range(len(self.barras_transpuestas[i])), self.barras_transpuestas[i], bottom=np.sum(self.barras_transpuestas[:i], axis=0))
            # Customize the plot
            self.ax.set_xlabel('Scan Rate (mV/s)')
            self.ax.set_xticks(range(len(speeds)))
            self.ax.set_xticklabels(speeds)
            self.ax.set_ylabel('Specific Charge (C/g)')
            self.ax.legend(['Pseudocapacitive', 'Diffusive', 'Double Layer'])
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Specific_Charge_VS_Sweed_Speed_Pos.png')
            self.save_data(self.barras_transpuestas[0], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_Pseudocapacitive_Pos.txt') # y1 (Bottom)
            self.save_data(self.barras_transpuestas[1], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_Diffusive_Pos.txt') # y2 (Middle)
            self.save_data(self.barras_transpuestas[2], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_DoubleLayer_Pos.txt') # y3 (Top)
        elif self.label == pestañas_superiores[14]:
            self.percentage_bars_transposed = percentage_specific_charge_pos_values.percentage_bars_transposed
            self.bars = self.ax.bar(range(len(self.percentage_bars_transposed[0])), self.percentage_bars_transposed[0])
            # Add stacked bars
            for i in range(1, len(self.percentage_bars_transposed)):
                self.bars = self.ax.bar(range(len(self.percentage_bars_transposed[i])), self.percentage_bars_transposed[i], bottom=np.sum(self.percentage_bars_transposed[:i], axis=0))
            # Customize the plot
            self.ax.set_xlabel('Scan Rate (mV/s)')
            self.ax.set_xticks(range(len(speeds)))
            self.ax.set_xticklabels(speeds)
            self.ax.set_ylabel('Charge (%)')
            self.ax.legend(['Pseudocapacitive', 'Diffusive', 'Double Layer'])
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Percentage_of_Specific_Charge_Pos.png')
            self.save_data(self.percentage_bars_transposed[0], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_Pseudocapacitive_Pos.txt') # y1 (Bottom)
            self.save_data(self.percentage_bars_transposed[1], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_Diffusive_Pos.txt') # y2 (Middle)
            self.save_data(self.percentage_bars_transposed[2], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_DoubleLayer_Pos.txt') # y3 (Top)
        elif self.label in diffusive_capacitive_negative_charge_names_dict:
            options = diffusive_capacitive_negative_charge_names_dict[self.label]
            speed = options['speed']
            data1 = options['data1']
            data2 = options['data2']
            data3 = options['data3']
            self.ax.bar(data1[0], data1[1], bottom=options['bottom1'], label=options['label1'])
            self.ax.bar(data2[0], data2[1], bottom=options['bottom2'], label=options['label2'])
            self.ax.bar(data3[0], data3[1], bottom=options['bottom3'], label=options['label3'])
            self.ax.set_title(options['title'])
            self.ax.set_xticks(options['set_xticks'])
            self.ax.set_xticklabels(options['set_xticklabels'])
            self.ax.locator_params(axis=options['locator_params_axis'], nbins=options['nbins'])
            self.ax.legend()
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/C&D_Negative_Charge_{speed}mVs.png') #graph
            self.save_data(data1[0], text='OOPVersion/generated_data/C&D_Negative_Charge_x_positions_mVs.txt') # x (1,2&3) para todas las velocidades
            self.save_data(data1[1], text=f'OOPVersion/generated_data/C&D_Negative_Charge_Pseudocapacitive_{speed}mVs.txt') # y1 (Bottom)
            self.save_data(data2[1], text=f'OOPVersion/generated_data/C&D_Negative_Charge_Diffusive_{speed}mVs.txt') # y2 (Middle)
            self.save_data(data3[1], text=f'OOPVersion/generated_data/C&D_Negative_Charge_DoubleLayer_{speed}mVs.txt') # y3 (Top)
        elif self.label == pestañas_superiores[16]:
            self.barras_transpuestas = scharge_vs_sspeed_neg_values.barras_transpuestas
            self.bars = self.ax.bar(range(len(self.barras_transpuestas[0])), self.barras_transpuestas[0])
            # Add stacked bars
            for i in range(1, len(self.barras_transpuestas)):
                self.bars = self.ax.bar(range(len(self.barras_transpuestas[i])), self.barras_transpuestas[i], bottom=np.sum(self.barras_transpuestas[:i], axis=0))
            # Customize the plot
            self.ax.set_xlabel('Scan Rate (mV/s)')
            self.ax.set_xticks(range(len(speeds)))
            self.ax.set_xticklabels(speeds)
            self.ax.set_ylabel('Specific Charge (C/g)')
            self.ax.legend(['Pseudocapacitive', 'Diffusive', 'Double Layer'])
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Specific_Charge_VS_Sweed_Speed_Neg.png')
            self.save_data(self.barras_transpuestas[0], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_Pseudocapacitive_Neg.txt') # y1 (Bottom)
            self.save_data(self.barras_transpuestas[1], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_Diffusive_Neg.txt') # y2 (Middle)
            self.save_data(self.barras_transpuestas[2], text='OOPVersion/generated_data/Specific_Charge_VS_Sweed_Speed_DoubleLayer_Neg.txt') # y3 (Top)
        elif self.label == pestañas_superiores[17]:
            self.percentage_bars_transposed = percentage_specific_charge_neg_values.percentage_bars_transposed
            self.bars = self.ax.bar(range(len(self.percentage_bars_transposed[0])), self.percentage_bars_transposed[0])
            # Add stacked bars
            for i in range(1, len(self.percentage_bars_transposed)):
                self.bars = self.ax.bar(range(len(self.percentage_bars_transposed[i])), self.percentage_bars_transposed[i], bottom=np.sum(self.percentage_bars_transposed[:i], axis=0))
            # Customize the plot
            self.ax.set_xlabel('Scan Rate (mV/s)')
            self.ax.set_xticks(range(len(speeds)))
            self.ax.set_xticklabels(speeds)
            self.ax.set_ylabel('Charge (%)')
            self.ax.legend(['Pseudocapacitive', 'Diffusive', 'Double Layer'])
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Percentage_of_Specific_Charge_Neg.png')
            self.save_data(self.percentage_bars_transposed[0], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_Pseudocapacitive_Neg.txt') # y1 (Bottom)
            self.save_data(self.percentage_bars_transposed[1], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_Diffusive_Neg.txt') # y2 (Middle)
            self.save_data(self.percentage_bars_transposed[2], text='OOPVersion/generated_data/Percentage_of_Specific_Charge_DoubleLayer_Neg.txt') # y3 (Top)

        if y is not None:
            self.ax.set_title(self.label)
            self.canvas.draw()

    def ajustar_guardar_cerrar_graph(self, texto_guardado):
        plt.tight_layout()
        plt.savefig(texto_guardado)
        plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.2)
        plt.close(self.figure)
    
    def save_data(self, data, text):
        np.savetxt(text, data, fmt='%f')

class PestañasVerticales(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.title("Pestañas Verticales")

        # Create a style object
        style = ttk.Style(self)

        style.configure('Treeview', rowheight=36)
        self.tree = ttk.Treeview(self, selectmode='browse')
        self.tree.pack(side='left', fill='y', ipadx=3)

        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scroll.pack(side='left', fill='y')
        self.tree.configure(yscrollcommand=self.scroll.set)

        self.pages = {}
        self.current_graph = None

    def add(self, page, text):
        page.pack_forget()
        id = self.tree.insert('', 'end', text=text)
        self.pages[id] = page
        self.tree.bind('<ButtonRelease-1>', lambda e: self.show_selected())

    def show_selected(self):
        item = self.tree.selection()
        if item:
            page = self.pages[item[0]]
            # Hide the previous graph if exists
            if self.current_graph:
                self.current_graph.pack_forget()
            # Show the selected page
            page.pack(fill='both', expand=True)
            # Update the current graph
            self.current_graph = page

def main():
    root = tk.Tk()
    root.geometry('900x550')  # Ajustar tamaño de la ventana
    
    app = PestañasVerticales(root)
    app.pack(expand=True, fill='both')

    # Crear pestañas (frames) dentro del notebook principal
    normalizacion_tab = ttk.Frame(app)
    oxidation_tab = ttk.Frame(app)
    reduction_tab = ttk.Frame(app)
    parameterB_tab = ttk.Frame(app)
    diffusive_capacitive_currents_tab = ttk.Frame(app)
    capacitive_current_tab = ttk.Frame(app)
    diffusive_current_tab = ttk.Frame(app)
    diffusive_capacitive_charges_tab = ttk.Frame(app)
    scharge_vs_sspeed_tab = ttk.Frame(app)
    percentage_scharge_tab = ttk.Frame(app)
    masogram_tab = ttk.Frame(app)
    insertogram_tab = ttk.Frame(app)
    diffusive_capacitive_positive_charge_tab = ttk.Frame(app)
    scharge_vs_sspeed_pos_tab = ttk.Frame(app)
    percentage_scharge_pos_tab = ttk.Frame(app)
    diffusive_capacitive_negative_charge_tab = ttk.Frame(app)
    scharge_vs_sspeed_neg_tab = ttk.Frame(app)
    percentage_scharge_neg_tab = ttk.Frame(app)

    app.add(normalizacion_tab, pestañas_superiores[0])
    app.add(oxidation_tab, pestañas_superiores[1])
    app.add(reduction_tab, pestañas_superiores[2])
    app.add(parameterB_tab, pestañas_superiores[3])
    app.add(diffusive_capacitive_currents_tab, pestañas_superiores[4])
    app.add(capacitive_current_tab, pestañas_superiores[5])
    app.add(diffusive_current_tab, pestañas_superiores[6])
    app.add(diffusive_capacitive_charges_tab, pestañas_superiores[7])
    app.add(scharge_vs_sspeed_tab, pestañas_superiores[8])
    app.add(percentage_scharge_tab, pestañas_superiores[9])
    app.add(masogram_tab, pestañas_superiores[10])
    app.add(insertogram_tab, pestañas_superiores[11])
    app.add(diffusive_capacitive_positive_charge_tab, pestañas_superiores[12])
    app.add(scharge_vs_sspeed_pos_tab, pestañas_superiores[13])
    app.add(percentage_scharge_pos_tab, pestañas_superiores[14])
    app.add(diffusive_capacitive_negative_charge_tab, pestañas_superiores[15])
    app.add(scharge_vs_sspeed_neg_tab, pestañas_superiores[16])
    app.add(percentage_scharge_neg_tab, pestañas_superiores[17])

    # Crear notebooks adicionales dentro de cada pestaña para alojar los gráficos específicos
    normalizacion_notebook = ttk.Notebook(normalizacion_tab)
    normalizacion_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_capacitive_currents_notebook = ttk.Notebook(diffusive_capacitive_currents_tab)
    diffusive_capacitive_currents_notebook.pack(fill=tk.BOTH, expand=True)

    capacitive_current_notebook = ttk.Notebook(capacitive_current_tab)
    capacitive_current_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_current_notebook = ttk.Notebook(diffusive_current_tab)
    diffusive_current_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_capacitive_charges_notebook = ttk.Notebook(diffusive_capacitive_charges_tab)
    diffusive_capacitive_charges_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_capacitive_positive_charge_notebook = ttk.Notebook(diffusive_capacitive_positive_charge_tab)
    diffusive_capacitive_positive_charge_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_capacitive_negative_charge_notebook = ttk.Notebook(diffusive_capacitive_negative_charge_tab)
    diffusive_capacitive_negative_charge_notebook.pack(fill=tk.BOTH, expand=True)

    # Crear nombres de pestañas: Velocidades.
    global normalization_names_list # Arreglo para almacenar los nombres generados
    global normalization_names_dict # Diccionario para almacenar los datos
    global diffusive_capacitive_currents_names_list
    global diffusive_capacitive_currents_names_dict
    global capacitive_current_names_list
    global capacitive_current_names_dict
    global diffusive_current_names_list
    global diffusive_current_names_dict
    global diffusive_capacitive_charges_names_list
    global diffusive_capacitive_charges_names_dict
    global diffusive_capacitive_positive_charge_names_list
    global diffusive_capacitive_positive_charge_names_dict
    global diffusive_capacitive_negative_charge_names_list
    global diffusive_capacitive_negative_charge_names_dict

    for num, speed in enumerate(speeds):
        # Generar nombres y agregar al arreglo
        normalization_name = f"{speed} mV/s - {pestañas_superiores[0]}"
        normalization_names_list.append(normalization_name)
        diffusive_capacitive_currents_name = f"{speed} mV/s - {pestañas_superiores[4]}"
        diffusive_capacitive_currents_names_list.append(diffusive_capacitive_currents_name)
        capacitive_current_name = f"{speed} mV/s - {pestañas_superiores[5]}"
        capacitive_current_names_list.append(capacitive_current_name)
        diffusive_current_name = f"{speed} mV/s - {pestañas_superiores[6]}"
        diffusive_current_names_list.append(diffusive_current_name)
        diffusive_capacitive_charges_name = f"{speed} mV/s - {pestañas_superiores[7]}"
        diffusive_capacitive_charges_names_list.append(diffusive_capacitive_charges_name)
        diffusive_capacitive_positive_charge_name = f"{speed} mV/s - {pestañas_superiores[12]}"
        diffusive_capacitive_positive_charge_names_list.append(diffusive_capacitive_positive_charge_name)
        diffusive_capacitive_negative_charge_name = f"{speed} mV/s - {pestañas_superiores[15]}"
        diffusive_capacitive_negative_charge_names_list.append(diffusive_capacitive_negative_charge_name)
        
        # Para 'normalization'
        normalization_names_dict[normalization_name] = {
            'speed': speed,
            'data': (normalizacion_values.UExp_results[num], normalizacion_values.IExp_results[num]),
            'fmt': 'o b', 'label': f'{int(speeds[num])} mV/s',
            'title': 'Normalization', 'x_major_formatter': mticker.FormatStrFormatter('%.2f'),
            'x_major_locator': mticker.MaxNLocator(5), 'x_minor_locator': AutoMinorLocator(3),
            'y_major_formatter': mticker.FormatStrFormatter('%.2f'), 'y_major_locator': mticker.MaxNLocator(7),
            'y_minor_locator': AutoMinorLocator(5),
            'x_label': REFERENCE_ELECTRODE,
            'y_label': DENSIDAD_DE_CORRIENTE
        }
        # Para 'Diffusive & Capacitive Currents'
        diffusive_capacitive_currents_names_dict[diffusive_capacitive_currents_name] = {
            'speed': speed,
            'data1': (diffusive_capacitive_currents_values.UExp_results[num], diffusive_capacitive_currents_values.IExp_results[num]),
            'fmt1': 'o b', 
            'markersize1': 2,
            'data2': (diffusive_capacitive_currents_values.U, diffusive_capacitive_currents_values.Imodelpos[:, num]),
            'fmt2': 'o r', 
            'markersize2': 2,
            'data3': (diffusive_capacitive_currents_values.U, diffusive_capacitive_currents_values.Imodelneg[:, num]),
            'fmt3': 'o r', 
            'markersize3': 2,
            'title': f'{pestañas_superiores[4]} - {speeds[num]}mV/s',
            'x_major_formatter': mticker.FormatStrFormatter('%.1f'),
            'x_major_locator': mticker.MaxNLocator(5), 'x_minor_locator': AutoMinorLocator(3),
            'x_label': REFERENCE_ELECTRODE,
            'y_label': DENSIDAD_DE_CORRIENTE,
            'legend': ['Experimental', 'Theoretical']
        }
        # Para 'Capacitive Currents'
        capacitive_current_names_dict[capacitive_current_name] = {
            'speed': speed,
            'data1': (capacitive_current_values.UExp_results[num], capacitive_current_values.IExp_results[num]),
            'fmt1': 'o b', 
            'markersize1': 2,
            'data2': (capacitive_current_values.U, capacitive_current_values.Imodel_1pos[:, num]),
            'fmt2': 'o r', 
            'markersize2': 2,
            'data3': (capacitive_current_values.U, capacitive_current_values.Imodel_1neg[:, num]),
            'fmt3': 'o r', 
            'markersize3': 2,
            'title': f'{pestañas_superiores[5]} - {speeds[num]}mV/s',
            'x_major_formatter': mticker.FormatStrFormatter('%.1f'),
            'x_major_locator': mticker.MaxNLocator(5), 'x_minor_locator': AutoMinorLocator(3),
            'x_label': REFERENCE_ELECTRODE,
            'y_label': DENSIDAD_DE_CORRIENTE,
            'legend': ['Experimental', 'Theoretical']
        }
        # Para 'Diffusive Currents'
        diffusive_current_names_dict[diffusive_current_name] = {
            'speed': speed,
            'data1': (diffusive_current_values.UExp_results[num], diffusive_current_values.IExp_results[num]),
            'fmt1': 'o b', 
            'markersize1': 2,
            'data2': (diffusive_current_values.U, diffusive_current_values.Imodel_2pos[:, num]),
            'fmt2': 'o r', 
            'markersize2': 2,
            'data3': (diffusive_current_values.U, diffusive_current_values.Imodel_2neg[:, num]),
            'fmt3': 'o r', 
            'markersize3': 2,
            'title': f'{pestañas_superiores[5]} - {speeds[num]}mV/s',
            'x_major_formatter': mticker.FormatStrFormatter('%.1f'),
            'x_major_locator': mticker.MaxNLocator(5), 'x_minor_locator': AutoMinorLocator(3),
            'x_label': REFERENCE_ELECTRODE,
            'y_label': DENSIDAD_DE_CORRIENTE,
            'legend': ['Experimental', 'Theoretical']
        }
        # Para 'Capacitive & Diffusive Charges'
        diffusive_capacitive_charges_names_dict[diffusive_capacitive_charges_name] = {
            'speed': speed,
            'data1': (diffusive_capacitive_charges_values.x_positions, diffusive_capacitive_charges_values.barrasV_results[num][:, 0]),
            'bottom1': np.zeros(len(diffusive_capacitive_charges_values.x_positions)),
            'label1': 'Pseudocapacitive',
            'data2': (diffusive_capacitive_charges_values.x_positions, diffusive_capacitive_charges_values.barrasV_results[num][:, 1]),
            'fmt2': 'o r', 
            'bottom2': diffusive_capacitive_charges_values.barrasV_results[num][:, 0],
            'label2': 'Diffusive',
            'data3': (diffusive_capacitive_charges_values.x_positions, diffusive_capacitive_charges_values.barrasV_results[num][:, 2]),
            'fmt3': 'o r', 
            'bottom3': diffusive_capacitive_charges_values.barrasV_results[num][:, 0] + diffusive_capacitive_charges_values.barrasV_results[num][:, 1],
            'label3': 'Double Layer',
            'title': f'{speeds[num]} mV/s',
            #'title': f'{pestañas_superiores[11]} - {speeds[num]} mV/s',
            'set_xticks': diffusive_capacitive_charges_values.x_positions,
            'set_xticklabels': ['{:.2f}'.format(val) for val in diffusive_capacitive_charges_values.U],
            'locator_params_axis': 'x',
            'nbins': 10,
            'x_label': REFERENCE_ELECTRODE,
            'y_label': 'Specific Charge (C/g)',
        }
        # Para 'Capacitive & Diffusive Positive Charge'
        diffusive_capacitive_positive_charge_names_dict[diffusive_capacitive_positive_charge_name] = {
            'speed': speed,
            'data1': (diffusive_capacitive_positive_charge_values.x_positions, diffusive_capacitive_positive_charge_values.barrasV_results[num][:, 0]),
            'bottom1': np.zeros(len(diffusive_capacitive_positive_charge_values.x_positions)),
            'label1': 'Pseudocapacitive',
            'data2': (diffusive_capacitive_positive_charge_values.x_positions, diffusive_capacitive_positive_charge_values.barrasV_results[num][:, 1]),
            'fmt2': 'o r', 
            'bottom2': diffusive_capacitive_positive_charge_values.barrasV_results[num][:, 0],
            'label2': 'Diffusive',
            'data3': (diffusive_capacitive_positive_charge_values.x_positions, diffusive_capacitive_positive_charge_values.barrasV_results[num][:, 2]),
            'fmt3': 'o r', 
            'bottom3': diffusive_capacitive_positive_charge_values.barrasV_results[num][:, 0] + diffusive_capacitive_positive_charge_values.barrasV_results[num][:, 1],
            'label3': 'Double Layer',
            'title': f'{speeds[num]} mV/s',
            #'title': f'{pestañas_superiores[12]} - {speeds[num]} mV/s',
            'set_xticks': diffusive_capacitive_positive_charge_values.x_positions,
            'set_xticklabels': ['{:.2f}'.format(val) for val in diffusive_capacitive_positive_charge_values.U],
            'locator_params_axis': 'x',
            'nbins': 10,
            'x_label': REFERENCE_ELECTRODE,
            'y_label': 'Specific Charge (C/g)',
        }
        # Para 'Capacitive & Diffusive Negative Charge'
        diffusive_capacitive_negative_charge_names_dict[diffusive_capacitive_negative_charge_name] = {
            'speed': speed,
            'data1': (diffusive_capacitive_negative_charge_values.x_positions, diffusive_capacitive_negative_charge_values.barrasV_results[num][:, 0]),
            'bottom1': np.zeros(len(diffusive_capacitive_negative_charge_values.x_positions)),
            'label1': 'Pseudocapacitive',
            'data2': (diffusive_capacitive_negative_charge_values.x_positions, diffusive_capacitive_negative_charge_values.barrasV_results[num][:, 1]),
            'fmt2': 'o r', 
            'bottom2': diffusive_capacitive_negative_charge_values.barrasV_results[num][:, 0],
            'label2': 'Diffusive',
            'data3': (diffusive_capacitive_negative_charge_values.x_positions, diffusive_capacitive_negative_charge_values.barrasV_results[num][:, 2]),
            'fmt3': 'o r', 
            'bottom3': diffusive_capacitive_negative_charge_values.barrasV_results[num][:, 0] + diffusive_capacitive_negative_charge_values.barrasV_results[num][:, 1],
            'label3': 'Double Layer',
            'title': f'{speeds[num]} mV/s',
            #'title': f'{pestañas_superiores[15]} - {speeds[num]} mV/s',
            'set_xticks': diffusive_capacitive_negative_charge_values.x_positions,
            'set_xticklabels': ['{:.2f}'.format(val) for val in diffusive_capacitive_negative_charge_values.U],
            'locator_params_axis': 'x',
            'nbins': 10,
            'x_label': REFERENCE_ELECTRODE,
            'y_label': 'Specific Charge (C/g)',
        }

    # Crear gráficos en las pestañas correspondientes
    # Velocidades dentro de Normalización
    for normalization_name in normalization_names_list:
        tab = ttk.Frame(normalizacion_notebook)
        normalizacion_notebook.add(tab, text=normalization_name) 

        graph = ZoomableGraph(tab, normalization_name)
        graph.show()
    # Velocidades dentro de Diffusive y Capacitive Currents
    for diffusive_capacitive_currents_name in diffusive_capacitive_currents_names_list:
        tab = ttk.Frame(diffusive_capacitive_currents_notebook)
        diffusive_capacitive_currents_notebook.add(tab, text=diffusive_capacitive_currents_name) 

        graph = ZoomableGraph(tab, diffusive_capacitive_currents_name)
        graph.show()
    # Velocidades dentro de Capacitive Current
    for capacitive_current_name in capacitive_current_names_list:
        tab = ttk.Frame(capacitive_current_notebook)
        capacitive_current_notebook.add(tab, text=capacitive_current_name) 

        graph = ZoomableGraph(tab, capacitive_current_name)
        graph.show()
    for diffusive_current_name in diffusive_current_names_list:
        tab = ttk.Frame(diffusive_current_notebook)
        diffusive_current_notebook.add(tab, text=diffusive_current_name) 

        graph = ZoomableGraph(tab, diffusive_current_name)
        graph.show()
    # Velocidades dentro de las cargas capacitivas y difusivas
    for diffusive_capacitive_charges_name in diffusive_capacitive_charges_names_list:
        tab = ttk.Frame(diffusive_capacitive_charges_notebook)
        diffusive_capacitive_charges_notebook.add(tab, text=diffusive_capacitive_charges_name) 

        graph = ZoomableGraph(tab, diffusive_capacitive_charges_name)
        graph.show()
    # Pos
    for diffusive_capacitive_positive_charge_name in diffusive_capacitive_positive_charge_names_list:
        tab = ttk.Frame(diffusive_capacitive_positive_charge_notebook)
        diffusive_capacitive_positive_charge_notebook.add(tab, text=diffusive_capacitive_positive_charge_name) 

        graph = ZoomableGraph(tab, diffusive_capacitive_positive_charge_name)
        graph.show()
    # Neg
    for diffusive_capacitive_negative_charge_name in diffusive_capacitive_negative_charge_names_list:
        tab = ttk.Frame(diffusive_capacitive_negative_charge_notebook)
        diffusive_capacitive_negative_charge_notebook.add(tab, text=diffusive_capacitive_negative_charge_name) 

        graph = ZoomableGraph(tab, diffusive_capacitive_negative_charge_name)
        graph.show()

    # Otros que no requieren pestañas inferiores
    # Oxidation
    graph = ZoomableGraph(oxidation_tab, pestañas_superiores[1])
    graph.show()
    # Reduction
    graph = ZoomableGraph(reduction_tab, pestañas_superiores[2])
    graph.show()
    # Parameter B
    graph = ZoomableGraph(parameterB_tab, pestañas_superiores[3])
    graph.show()
    # Specific Charge VS Sweed Speed
    graph = ZoomableGraph(scharge_vs_sspeed_tab, pestañas_superiores[8])
    graph.show()
    # Percentage of Specific Charge
    graph = ZoomableGraph(percentage_scharge_tab, pestañas_superiores[9])
    graph.show()
    # Masogram
    graph = ZoomableGraph(masogram_tab, pestañas_superiores[10])
    graph.show()
    # Insertogram
    graph = ZoomableGraph(insertogram_tab, pestañas_superiores[11])
    graph.show()
    # Specific Charge VS Sweed Speed (+)
    graph = ZoomableGraph(scharge_vs_sspeed_pos_tab, pestañas_superiores[13])
    graph.show()
    # Percentage of Specific Charge (+)
    graph = ZoomableGraph(percentage_scharge_pos_tab, pestañas_superiores[14])
    graph.show()
    # Specific Charge VS Sweed Speed (-)
    graph = ZoomableGraph(scharge_vs_sspeed_neg_tab, pestañas_superiores[16])
    graph.show()
    # Percentage of Specific Charge (-)
    graph = ZoomableGraph(percentage_scharge_neg_tab, pestañas_superiores[17])
    graph.show()

    root.mainloop()

if __name__ == "__main__":
    main()