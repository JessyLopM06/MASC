"""
Este módulo proporciona una interfaz de los menu del modelo 1-3 utilizando tkinter.
"""

import tkinter as tk
import os
from tkinter import*
from tkinter import Frame
from tkinter import filedialog 

#Para poder abrir los xcript
import subprocess

#Para las graficas   
from customtkinter import CTk, CTkTabview
import tkinter.ttk as ttk

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from cerebro_modelo import Normalizacion, Oxidation, Reduction, Diffusive_Capacitive, Capacitive_Current, Diffusive_Current, ParameterB,Diffusive_Capacitive_Charges, SpecificChargeVSSweepSpeed, PercentageofSpecificCharge, Diffusive_Capacitive_Positive_Charge, SpecificChargeVSSweepSpeedPos, PercentageofSpecificChargePos, Diffusive_Capacitive_Negative_Charge, SpecificChargeVSSweepSpeedNeg, PercentageofSpecificChargeNeg, Masogram, InsertogramMassVersion, InsertogramAreaVersion, InsertogramMassVersionChargePos, InsertogramMassVersionChargeNeg
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
insertogram_mass_values = InsertogramMassVersion()
diffusive_capacitive_positive_charge_values = Diffusive_Capacitive_Positive_Charge()
scharge_vs_sspeed_pos_values = SpecificChargeVSSweepSpeedPos()
percentage_specific_charge_pos_values = PercentageofSpecificChargePos()
diffusive_capacitive_negative_charge_values = Diffusive_Capacitive_Negative_Charge()
scharge_vs_sspeed_neg_values = SpecificChargeVSSweepSpeedNeg()
percentage_specific_charge_neg_values = PercentageofSpecificChargeNeg()
insertogram_mass_version_charge_pos_values = InsertogramMassVersionChargePos()
insertogram_mass_version_charge_neg_values = InsertogramMassVersionChargeNeg()

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
massogram_names_list = []
massogram_names_dict = {}
insertogram_mass_names_list = []
insertogram_mass_names_dict = {}
diffusive_capacitive_positive_charge_names_list = []
diffusive_capacitive_positive_charge_names_dict = {}
insertogram_mass_pos_names_list = []
insertogram_mass_pos_names_dict = {}
diffusive_capacitive_negative_charge_names_list = []
diffusive_capacitive_negative_charge_names_dict = {}
insertogram_mass_neg_names_list = []
insertogram_mass_neg_names_dict = {}

pestañas_superiores = ['Normalization', 'Ks positive current', 'Ks negative current', 'Cyclic voltammograms\n(Experimental & Model)', 'Capacitive Current', 'Diffusive Current', 'b parameter', 'Deconvolution of\nSpecific Charge vs Scan rate', 'Specific charge vs Scan rate', '% Specific Charge vs Scan Rate', 'Massograms', 'Active Thickness', 'Deconvolution of\nSpecific Charge vs Scan rate (+)', 'Specific charge vs Scan rate (+)', '% Specific Charge vs Scan Rate (+)', 'Active Thickness (+)', 'Deconvolution of\nSpecific Charge vs Scan rate (-)', 'Specific charge vs Scan rate (-)', '% Specific Charge vs Scan Rate (-)', 'Active Thickness (-)']

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
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/ks_positive_current.png') #graph
            self.save_data(oxidation_values.UKpos, text='OOPVersion/generated_data/ks_positive_current_UKpos.txt') # x
            self.save_data(oxidation_values.IKpos[i], text='OOPVersion/generated_data/ks_positive_current_IKpos.txt') # y
        elif self.label == pestañas_superiores[2]:
            for i in range(len(reduction_values.IKneg)):
                self.ax.plot(reduction_values.UKneg, reduction_values.IKneg[i], label=f'Line {i+1}', linewidth=0.8)
            self.ax.set_xlabel('Scan rate')
            self.ax.set_ylabel('Intensity')
            self.ax.grid(False)
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/ks_negative_current.png') #graph
            self.save_data(reduction_values.UKneg, text='OOPVersion/generated_data/ks_negative_current_UKneg.txt') # x
            self.save_data(reduction_values.IKneg[i], text='OOPVersion/generated_data/ks_negative_current_IKneg.txt') # y
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
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/cyclic_voltammograms_{speed}mVs.png') #graph
            self.save_data(data1[0], text=f'OOPVersion/generated_data/cyclic_voltammograms_UExp_results_{speed}mVs.txt') # x1
            self.save_data(data1[1], text=f'OOPVersion/generated_data/cyclic_voltammograms_IExp_results_{speed}mVs.txt') # y1
            self.save_data(data2[0], text=f'OOPVersion/generated_data/cyclic_voltammograms_U_mVs.txt') # x (1&2) para todas las velocidades.
            self.save_data(data2[1], text=f'OOPVersion/generated_data/cyclic_voltammograms_Imodelpos_{speed}mVs.txt') # y1
            self.save_data(data3[1], text=f'OOPVersion/generated_data/cyclic_voltammograms_Imodelneg_{speed}mVs.txt') # y1
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
        elif self.label == pestañas_superiores[6]:
            self.ax.plot(parameterB_values.U, parameterB_values.rbpos, 'r', label='b oxidation')
            self.ax.plot(parameterB_values.U, parameterB_values.rbneg, 'b', label='b reduction')
            self.ax.set_xlabel(REFERENCE_ELECTRODE)
            self.ax.set_ylabel('b parameter')
            self.ax.set_title('b - oxidation & reduction')
            self.ax.legend()
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/B_Parameter_Oxidation_Reduction.png') #graph
            self.save_data(parameterB_values.U, text=f'OOPVersion/generated_data/B_Parameter_U.txt') # x (1&2)
            self.save_data(parameterB_values.rbpos, text=f'OOPVersion/generated_data/B_Parameter_rbpos.txt') # y1
            self.save_data(parameterB_values.rbneg, text=f'OOPVersion/generated_data/B_Parameter_rbneg.txt') # y2
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
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/deconvolution_specific_charge_vs_scan_rate_{speed}mVs.png') #graph
            self.save_data(data1[0], text='OOPVersion/generated_data/deconvolution_specific_charge_vs_scan_rate_x_positions_mVs.txt') # x (1,2&3) para todas las velocidades
            self.save_data(data1[1], text=f'OOPVersion/generated_data/deconvolution_specific_charge_vs_scan_rate_Pseudocapacitive_{speed}mVs.txt') # y1 (Bottom)
            self.save_data(data2[1], text=f'OOPVersion/generated_data/deconvolution_specific_charge_vs_scan_rate__Diffusive_{speed}mVs.txt') # y2 (Middle)
            self.save_data(data3[1], text=f'OOPVersion/generated_data/deconvolution_specific_charge_vs_scan_rate_DoubleLayer_{speed}mVs.txt') # y3 (Top)
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
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/specific_charge_vs_scan_rate.png')
            self.save_data(self.barras_transpuestas[0], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_Pseudocapacitive.txt') # y1 (Bottom)
            self.save_data(self.barras_transpuestas[1], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_Diffusive.txt') # y2 (Middle)
            self.save_data(self.barras_transpuestas[2], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_DoubleLayer.txt') # y3 (Top)
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
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/Percentage_of_specific_charge_vs_scan_rate.png')
            self.save_data(self.percentage_bars_transposed[0], text='OOPVersion/generated_data/Percentage_of_specific_charge_vs_scan_rate_Pseudocapacitive.txt') # y1 (Bottom)
            self.save_data(self.percentage_bars_transposed[1], text='OOPVersion/generated_data/Percentage_of_specific_charge_vs_scan_rate_Diffusive.txt') # y2 (Middle)
            self.save_data(self.percentage_bars_transposed[2], text='OOPVersion/generated_data/Percentage_of_specific_charge_vs_scan_rate_DoubleLayer.txt') # y3 (Top)
        elif self.label in massogram_names_dict: #self.label == pestañas_superiores[10]:
            # Get values
            options = massogram_names_dict[self.label]
            speed = options['speed']
            self.U = options['data_x_blue']
            self.masspos = options['data_y_blue_1']
            self.ax.plot(self.U, self.masspos * 1e6, 'b', linewidth=3, label='mass (ug)')
            # Customize the plot
            self.ax.set_xlabel(REFERENCE_ELECTRODE)
            self.ax.set_ylabel(MASS_UG, color='b')
            self.ax.tick_params('y', colors='b')

            # Get values
            self.massneg = options['data_y_blue_2']
            # Add the negative data series to the first data series (blue)
            self.ax.plot(self.U, self.massneg * 1e6, 'b', linewidth=3)
            # Create the second data series (red)
            self.ax2 = self.ax.twinx()
            self.UExp = options['data_x_red']
            self.IExp = options['data_y_red']
            self.ax2.plot(self.UExp, self.IExp, 'r', linewidth=3, label=DENSIDAD_DE_CORRIENTE) # x=UExp y=IExp
            self.ax2.set_ylabel(DENSIDAD_DE_CORRIENTE, color='r')
            self.ax2.tick_params('y', colors='r')

            self.ax.set_title(options['title'])

            #Final
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/Massograms_{speed}mVs.png') #graph
            self.save_data(self.U, text=f'OOPVersion/generated_data/Massograms_U_{speed}mVs.txt') # x(1&2)
            self.save_data(self.masspos, text=f'OOPVersion/generated_data/Massograms_masspos_{speed}mVs.txt') # y1
            self.save_data(self.massneg * 1e6, text=f'OOPVersion/generated_data/Massograms_massneg_{speed}mVs.txt') # y2
            self.save_data(self.UExp, text=f'OOPVersion/generated_data/Massograms_UExp_{speed}mVs.txt') # x3
            self.save_data(self.IExp, text=f'OOPVersion/generated_data/Massograms_IExp_{speed}mVs.txt') # y3
        elif self.label in insertogram_mass_names_dict: #self.label == pestañas_superiores[11]:
            # Get values
            options = insertogram_mass_names_dict[self.label]
            speed = options['speed']
            self.U = options['data_x']
            self.inser = options['data_y']
            self.ax.plot(self.U, self.inser, 'b', linewidth=1)
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ax.set_title(options['title'])
            #Final
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/Active_Thickness_{speed}mVs.png') #graph
            self.save_data(self.U, text=f'OOPVersion/generated_data/Active_Thickness_U.txt') # x
            self.save_data(self.inser, text=f'OOPVersion/generated_data/Active_Thickness_inser_{speed}mVs.txt', fmt='%0.15f') # y
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
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/deconvolution_Positive_Charge_{speed}mVs.png') #graph
            self.save_data(data1[0], text='OOPVersion/generated_data/deconvolution_Positive_Charge_x_positions_mVs.txt') # x (1,2&3) para todas las velocidades
            self.save_data(data1[1], text=f'OOPVersion/generated_data/deconvolution_Positive_Charge_Pseudocapacitive_{speed}mVs.txt') # y1 (Bottom)
            self.save_data(data2[1], text=f'OOPVersion/generated_data/deconvolution_Positive_Charge_Diffusive_{speed}mVs.txt') # y2 (Middle)
            self.save_data(data3[1], text=f'OOPVersion/generated_data/deconvolution_Positive_Charge_DoubleLayer_{speed}mVs.txt') # y3 (Top)
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
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/specific_charge_vs_scan_rate_Pos.png')
            self.save_data(self.barras_transpuestas[0], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_Pseudocapacitive_Pos.txt') # y1 (Bottom)
            self.save_data(self.barras_transpuestas[1], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_Diffusive_Pos.txt') # y2 (Middle)
            self.save_data(self.barras_transpuestas[2], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_DoubleLayer_Pos.txt') # y3 (Top)
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
        elif self.label in insertogram_mass_pos_names_dict: #self.label == pestañas_superiores[11]:
            # Get values
            options = insertogram_mass_pos_names_dict[self.label]
            speed = options['speed']
            self.U = options['data_x']
            self.inser = options['data_y']
            self.ax.plot(self.U, self.inser, 'b', linewidth=1)
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ax.set_title(options['title'])
            #Final
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/Active_Thickness_Positive_{speed}mVs.png') #graph
            self.save_data(self.U, text=f'OOPVersion/generated_data/Active_Thickness_U_Positive.txt') # x
            self.save_data(self.inser, text=f'OOPVersion/generated_data/Active_Thickness_inser_Positive_{speed}mVs.txt', fmt='%0.15f') # y
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
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/deconvolution_Negative_Charge_{speed}mVs.png') #graph
            self.save_data(data1[0], text='OOPVersion/generated_data/deconvolution_Negative_Charge_x_positions_mVs.txt') # x (1,2&3) para todas las velocidades
            self.save_data(data1[1], text=f'OOPVersion/generated_data/deconvolution_Negative_Charge_Pseudocapacitive_{speed}mVs.txt') # y1 (Bottom)
            self.save_data(data2[1], text=f'OOPVersion/generated_data/deconvolution_Negative_Charge_Diffusive_{speed}mVs.txt') # y2 (Middle)
            self.save_data(data3[1], text=f'OOPVersion/generated_data/deconvolution_Negative_Charge_DoubleLayer_{speed}mVs.txt') # y3 (Top)
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
            self.ajustar_guardar_cerrar_graph('OOPVersion/generated_graphs/specific_charge_vs_scan_rate_Neg.png')
            self.save_data(self.barras_transpuestas[0], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_Pseudocapacitive_Neg.txt') # y1 (Bottom)
            self.save_data(self.barras_transpuestas[1], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_Diffusive_Neg.txt') # y2 (Middle)
            self.save_data(self.barras_transpuestas[2], text='OOPVersion/generated_data/specific_charge_vs_scan_rate_DoubleLayer_Neg.txt') # y3 (Top)
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
        elif self.label in insertogram_mass_neg_names_dict: #self.label == pestañas_superiores[11]:
            # Get values
            options = insertogram_mass_neg_names_dict[self.label]
            speed = options['speed']
            self.U = options['data_x']
            self.inser = options['data_y']
            self.ax.plot(self.U, self.inser, 'b', linewidth=1)
            self.ax.set_xlabel(options['x_label'])
            self.ax.set_ylabel(options['y_label'])
            self.ax.set_title(options['title'])
            #Final
            self.ajustar_guardar_cerrar_graph(f'OOPVersion/generated_graphs/Active_Thickness_Negative_{speed}mVs.png') #graph
            self.save_data(self.U, text=f'OOPVersion/generated_data/Active_Thickness_U_Negative.txt') # x
            self.save_data(self.inser, text=f'OOPVersion/generated_data/Active_Thickness_inser_Negative_{speed}mVs.txt', fmt='%0.15f') # y
        if y is not None:
            self.ax.set_title(self.label)
            self.canvas.draw()

    def ajustar_guardar_cerrar_graph(self, texto_guardado):
        #plt.tight_layout()
        #plt.savefig(texto_guardado)
        #plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.2)
        plt.close(self.figure)
    
    def save_data(self, data, text, fmt='%f'):
        #np.savetxt(text, data, fmt=fmt)
        print('Hello')

class PestañasVerticales(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        #self.master.title("Pestañas Verticales")

        # Create a style object
        style = ttk.Style(self)

        style.configure('Treeview', rowheight=40)
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
#Colors
#00ff00,#ffffff,#ff0000,#ffff00,#ff00ff

#Azules
#0000ff ,#5353ec, #1919e6,#1414b8,#2c2c7d,#00aaff,#0066cc,#003399,#000080           
Verdes= "#00A000"                   '                       '        
Grises="#C0C0C0"             
   


class TabViewWithColoredMargin:
    def __init__(self, root) -> None:
        self.root = root

        # Creamos un Frame adicional para el margen con color personalizado
        self.margin_frame = tk.Frame(root, padx=10, pady=10, bg='#116c2c',width=1000,height=1000)  # Cambia 'verde' por el color que desees
        self.margin_frame.pack(fill=tk.BOTH)

        # Creamos el TabView dentro del Frame con margen
        self.tabview = CTkTabview(self.margin_frame, fg_color='#abbbb0',width=1070,height=470)#ancho x largo 840 x 320
        self.tabview.pack(side='right',fill=tk.BOTH)

        # Agregamos las pestañas al TabView
        for tab_name  in ['Interpolation', 'Obtaining of K', 'VOLTAMPEROGRAM', 'Total Q', 'Q%', 'MASOGRAMA', 'ACTIVE THICKNESS', 'Barras 2']:
            self.tabview.add(tab_name)



#List box de inico del modelo 1
def choose_files(listbox):
    file_paths = filedialog.askopenfilenames(filetypes=[('Text Files', '*.txt')])
    for file_path in file_paths:
        listbox.insert(tk.END, file_path)

def clear_selected_files(listbox):
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        listbox.delete(index)

def abrir_registro():
    subprocess.Popen(['python', 'Interfaces/excel.py'])

#Para vincular las ventanas(scripts)
def abrir_script_python():
    ruta_script = "Interfaces/masa.py"  # Reemplaza con la ruta de tu script
    subprocess.Popen(['python', ruta_script])  

def ejecutar_descarga():
    # Ejecutar el script descarga.py
    subprocess.Popen(["python", "Interfaces/descarga.py"])


def ejecutar_settings():
#Ejecutar el script donde se van a subir las velociadades de barrido y
#conforme a eso se va apoder saber cuando el usuario ingrese la velocidad de barrido
#a que archivo pertenece"""

    subprocess.Popen(["python", "Interfaces/archivos.py"])


def funcion_del_boton_Masa():
    subprocess.run(["python", "Masa.py"])


def funcion_del_boton_Area():
    subprocess.run(["python", "Area_activa.py"]) 

def ejecutar_velocities():
    #Ejecutar el script usuario_M.py
    subprocess.Popen(['python',"Avancess/usuario_M.py"])


root = tk.Tk()
root.geometry('1000x1000')#Ancho x Largo
#root.resizable(0, 0)


# Crear un frame principal
main_frame = ttk.Frame(root)
main_frame.pack()

ruta_icono = "./imagenes/wh.ico"
root.iconbitmap(ruta_icono)
root.title('MASC: Multiple Analysis Software for Supercapacitors')

"""texto_copyright = "Copyright © rlucioporto.com\nLa ciencia, una luz en la oscuridad.\n   "
label_copyright = tk.Label(root, text=texto_copyright, bg="navy", fg="white", font=("Arial", 8,'bold'))
label_copyright.pack(side="bottom", fill="both")"""

#Se desliza el inidicador
def switch(indicator_lb, page):

    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child['bg']= 'SystemButtonFace'


  # Ajusta el grosor del borde para hacer el indicador más grande
    indicator_lb['bg'] = '#0097e8'
    #indicator_lb['borderwidth'] = 100  # Puedes ajustar el valor según tu preferencia
    indicator_lb['width'] = 100 # Puedes ajustar el valor según tu preferencia
    indicator_lb['height'] = 100# Puedes ajustar el valor según tu preferencia

#Para que aparezca informacion en diferente boton
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()
   
    page()
    
#Color de la barra de menu
options_fm= tk.Frame(root,bg='blue4')#bg=gray 

#Primer Boton

home_btn = tk.Button(options_fm, text='Comments', font=('Arial', 13,'bold'),bg='blue4',
                     bd=0, fg='snow', activeforeground='#1414b8',
                     command=abrir_registro)

'''home_btn = tk.Button(options_fm, text='' , font=('Arial, 13'),
                     bd=0, fg='#0097e8' ,activeforeground='#0097e8',
                     command=lambda:switch(indicator_lb=home_inidicator_lb,
                                        page=home_page))'''

home_btn.place(x=0 , y=0, width=125  )

#Indicadores 
#Boton 1
home_inidicator_lb = tk.Label(options_fm, bg='blue4')
home_inidicator_lb.place(x=22, y=30, width=80, height=2)

#boton 2
modelo1_inidicator_lb = tk.Label(options_fm)
modelo1_inidicator_lb.place(x=147, y=30, width=80, height=2)

#Boton 3
modelo2_inidicator_lb = tk.Label(options_fm)
modelo2_inidicator_lb.place(x=272, y=30, width=80, height=2)

#Boton 4
modelo3_inidicator_lb = tk.Label(options_fm)
modelo3_inidicator_lb.place(x=397, y=30, width=80, height=2)

#Boton 5
about_inidicator_lb = tk.Label(options_fm)
about_inidicator_lb.place(x=525, y=30, width=80, height=2)

                   
#Segundo Boton
modelo1_btn = tk.Button(options_fm, text='Model 1', font=('Arial', 11,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=modelo1_inidicator_lb,
                     page=modelo1_page))

modelo1_btn.place(x=125 , y=0, width=125  )

#Tercer Boton
modelo2_btn = tk.Button(options_fm, text='Model 2' , font=('Arial', 11,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=modelo2_inidicator_lb,
                                           page=modelo2_page))

modelo2_btn.place(x=250 , y=0, width=125  )

#Cuarto Boton
modelo3 = tk.Button(options_fm, text='Model 3' , font=('Arial', 11,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=modelo3_inidicator_lb,
                                           page=modelo3_page))

modelo3.place(x=375 , y=0, width=125  )

#Quinto Boton
modelo3_btn = tk.Button(options_fm, text='About' , font=('Arial', 11,'bold'),bg='blue4',
                     bd=0, fg='snow' ,activeforeground='#1414b8',
                     command=lambda:switch(indicator_lb=about_inidicator_lb,
                                           page=about_page))

modelo3_btn.place(x=500 , y=0, width=125  )
options_fm.pack(pady=5)

#Tamaño del menu
options_fm.pack_propagate(False)
options_fm.configure(width=1400 ,height=35)

"""# Texto debajo de las imágenes
texto = "Dr. Raúl Lucio Porto\nCentro de Innovación, Investigación y Desarrollo en Ingeniería y Tecnología\nCentro de Innovación en Ingeniería de Tecnología Inteligente Biomédica y Mecatrónica\n"
label_texto = tk.Label( root,text=texto, justify="center", wraplength=1000, width=1400, bg="blue4", fg="white", font=("Arial", 9, 'bold'))
label_texto.pack()"""


def home_page():
    home_page_fm = tk.Frame(main_fm)#Para cambiar el fondo , bg='gray'

    home_page_lb = tk.Label(home_page_fm,
                            font=('Arial',25), fg='#0097e8')

    home_page_lb.pack(pady=80)

    home_page_fm.pack(fill=tk.BOTH, expand=True)

def modelo1_page():
    
    # Elimina los frames existentes en main_fm
    for widget in main_fm.winfo_children():
        widget.destroy()

    # Crear un canvas para contener el frame interior,es el fondo
    canvas = tk.Canvas(main_fm, bg='gray84', highlightthickness=0)#main_fm, bg='#0097e8', highlightthickness=0
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar_x = ttk.Scrollbar(main_fm, orient=tk.HORIZONTAL, command=canvas.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)  # Añade un pequeño padding horizontal
    canvas.configure(xscrollcommand=scrollbar_x.set)
    

    # Crear el frame interior que contendrá todos los elementos deslizables
    inner_frame = ttk.Frame(canvas)
    inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Crear el primer frame dentro del frame interior
    frame1 = Frame(inner_frame, bg='gray84', width=3000, height=3000)
    frame1.grid(column=0, row=0, sticky='nsew')

     #Botones para el inicio del modelo 1 download,setings y continue
    # Button to download
    btn_download = Button(frame1, text='⬇ Download Files', font=('Arial', 10, 'bold'), bg='blue4', fg='white',activebackground='snow',activeforeground='blue4', command=ejecutar_descarga)
    btn_download.grid(row=4, column=0, columnspan=2, pady=2, padx=(10,10), sticky='nsew')  # Alinea a la derecha
    
    #Button to setiings
    btn_settings = Button(frame1, text='⚙ Settings', bg='blue4', fg='white', font=('Arial', 10, 'bold'),activeforeground='blue4',command=ejecutar_settings)
    btn_settings.grid(row=5,column=0,columnspan=2,pady=2,padx=(10,10),sticky='nsew')

    #Button to continue
    btn_continue = tk.Button(frame1, text='➡ Start', bg='blue4', fg='white', font=('Arial', 10, 'bold'),activebackground='snow',activeforeground='blue4')
    btn_continue.grid(row=7,column=0,columnspan=2,pady=2,padx=(5,5),sticky='nsew')

    # Crear el segundo frame dentro del frame interior
    frame2 = Frame(inner_frame, bg='gray64')#ancho x alto
    frame2.config(width=200, height=700)
    frame2.grid(column=1, row=0, sticky='nsew')

    

    # Agregar el código TabView al frame2
    app = PestañasVerticales(frame2)
    app.pack(expand=True, fill='both')

    # Crear pestañas (frames) dentro del notebook principal
    normalizacion_tab = ttk.Frame(app)
    oxidation_tab = ttk.Frame(app)
    reduction_tab = ttk.Frame(app)
    diffusive_capacitive_currents_tab = ttk.Frame(app)
    capacitive_current_tab = ttk.Frame(app)
    diffusive_current_tab = ttk.Frame(app)
    parameterB_tab = ttk.Frame(app)
    diffusive_capacitive_charges_tab = ttk.Frame(app)
    scharge_vs_sspeed_tab = ttk.Frame(app)
    percentage_scharge_tab = ttk.Frame(app)
    masogram_tab = ttk.Frame(app)
    insertogram_mass_ver_tab = ttk.Frame(app)
    diffusive_capacitive_positive_charge_tab = ttk.Frame(app)
    scharge_vs_sspeed_pos_tab = ttk.Frame(app)
    percentage_scharge_pos_tab = ttk.Frame(app)
    insertogram_mass_ver_pos_tab = ttk.Frame(app)
    diffusive_capacitive_negative_charge_tab = ttk.Frame(app)
    scharge_vs_sspeed_neg_tab = ttk.Frame(app)
    percentage_scharge_neg_tab = ttk.Frame(app)
    insertogram_mass_ver_neg_tab = ttk.Frame(app)

    app.add(normalizacion_tab, pestañas_superiores[0])
    app.add(oxidation_tab, pestañas_superiores[1])
    app.add(reduction_tab, pestañas_superiores[2])
    app.add(diffusive_capacitive_currents_tab, pestañas_superiores[3])
    app.add(capacitive_current_tab, pestañas_superiores[4])
    app.add(diffusive_current_tab, pestañas_superiores[5])
    app.add(parameterB_tab, pestañas_superiores[6])
    app.add(diffusive_capacitive_charges_tab, pestañas_superiores[7])
    app.add(scharge_vs_sspeed_tab, pestañas_superiores[8])
    app.add(percentage_scharge_tab, pestañas_superiores[9])
    app.add(masogram_tab, pestañas_superiores[10])
    app.add(insertogram_mass_ver_tab, pestañas_superiores[11])
    app.add(diffusive_capacitive_positive_charge_tab, pestañas_superiores[12])
    app.add(scharge_vs_sspeed_pos_tab, pestañas_superiores[13])
    app.add(percentage_scharge_pos_tab, pestañas_superiores[14])
    app.add(insertogram_mass_ver_pos_tab, pestañas_superiores[15])
    app.add(diffusive_capacitive_negative_charge_tab, pestañas_superiores[16])
    app.add(scharge_vs_sspeed_neg_tab, pestañas_superiores[17])
    app.add(percentage_scharge_neg_tab, pestañas_superiores[18])
    app.add(insertogram_mass_ver_neg_tab, pestañas_superiores[19])

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

    massogram_notebook = ttk.Notebook(masogram_tab)
    massogram_notebook.pack(fill=tk.BOTH, expand=True)

    insertogram_mass_ver_notebook = ttk.Notebook(insertogram_mass_ver_tab)
    insertogram_mass_ver_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_capacitive_positive_charge_notebook = ttk.Notebook(diffusive_capacitive_positive_charge_tab)
    diffusive_capacitive_positive_charge_notebook.pack(fill=tk.BOTH, expand=True)

    insertogram_mass_ver_pos_notebook = ttk.Notebook(insertogram_mass_ver_pos_tab)
    insertogram_mass_ver_pos_notebook.pack(fill=tk.BOTH, expand=True)

    diffusive_capacitive_negative_charge_notebook = ttk.Notebook(diffusive_capacitive_negative_charge_tab)
    diffusive_capacitive_negative_charge_notebook.pack(fill=tk.BOTH, expand=True)

    insertogram_mass_ver_neg_notebook = ttk.Notebook(insertogram_mass_ver_neg_tab)
    insertogram_mass_ver_neg_notebook.pack(fill=tk.BOTH, expand=True)

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
    global massogram_names_list
    global massogram_names_dict
    global insertogram_mass_names_list
    global insertogram_mass_names_dict
    global diffusive_capacitive_positive_charge_names_list
    global diffusive_capacitive_positive_charge_names_dict
    global insertogram_mass_pos_names_list
    global insertogram_mass_pos_names_dict
    global diffusive_capacitive_negative_charge_names_list
    global diffusive_capacitive_negative_charge_names_dict
    global insertogram_mass_neg_names_list
    global insertogram_mass_neg_names_dict

    for num, speed in enumerate(speeds):
        # Generar nombres y agregar al arreglo
        normalization_name = f"{speed} mV/s - {pestañas_superiores[0]}"
        normalization_names_list.append(normalization_name)
        diffusive_capacitive_currents_name = f"{speed} mV/s - {pestañas_superiores[3]}"
        diffusive_capacitive_currents_names_list.append(diffusive_capacitive_currents_name)
        capacitive_current_name = f"{speed} mV/s - {pestañas_superiores[4]}"
        capacitive_current_names_list.append(capacitive_current_name)
        diffusive_current_name = f"{speed} mV/s - {pestañas_superiores[5]}"
        diffusive_current_names_list.append(diffusive_current_name)
        diffusive_capacitive_charges_name = f"{speed} mV/s - {pestañas_superiores[7]}"
        diffusive_capacitive_charges_names_list.append(diffusive_capacitive_charges_name)
        massogram_name = f"{speed} mV/s - {pestañas_superiores[10]}"
        massogram_names_list.append(massogram_name)
        insertogram_mass_name = f"{speed} mV/s - {pestañas_superiores[11]}"
        insertogram_mass_names_list.append(insertogram_mass_name)
        diffusive_capacitive_positive_charge_name = f"{speed} mV/s - {pestañas_superiores[12]}"
        diffusive_capacitive_positive_charge_names_list.append(diffusive_capacitive_positive_charge_name)
        insertogram_mass_pos_name = f"{speed} mV/s - {pestañas_superiores[15]}"
        insertogram_mass_pos_names_list.append(insertogram_mass_pos_name)
        diffusive_capacitive_negative_charge_name = f"{speed} mV/s - {pestañas_superiores[16]}"
        diffusive_capacitive_negative_charge_names_list.append(diffusive_capacitive_negative_charge_name)
        insertogram_mass_neg_name = f"{speed} mV/s - {pestañas_superiores[19]}"
        insertogram_mass_neg_names_list.append(insertogram_mass_neg_name)
        
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
        massogram_names_dict[massogram_name] = {
            'speed': speed,
            'data_x_blue': masogram_values.U,
            'data_y_blue_1': masogram_values.masspos_results[num],
            'data_y_blue_2': masogram_values.massneg_results[num],
            'data_x_red': masogram_values.UExp,
            'data_y_red': masogram_values.IExp,
            'title': f'{speeds[num]} mV/s'
        }
        insertogram_mass_names_dict[insertogram_mass_name] = {
            'speed': speed,
            'data_x': insertogram_mass_values.U,
            'data_y': insertogram_mass_values.inser_results[num],
            'x_label': REFERENCE_ELECTRODE,
            'y_label': 'Active Thickness (nm)',
            'title': f'{speeds[num]} mV/s'
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
        insertogram_mass_pos_names_dict[insertogram_mass_pos_name] = {
            'speed': speed,
            'data_x': insertogram_mass_version_charge_pos_values.U,
            'data_y': insertogram_mass_version_charge_pos_values.inser_results[num],
            'x_label': REFERENCE_ELECTRODE,
            'y_label': 'Active Thickness (nm)',
            'title': f'{speeds[num]} mV/s'
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
        insertogram_mass_neg_names_dict[insertogram_mass_neg_name] = {
            'speed': speed,
            'data_x': insertogram_mass_version_charge_neg_values.U,
            'data_y': insertogram_mass_version_charge_neg_values.inser_results[num],
            'x_label': REFERENCE_ELECTRODE,
            'y_label': 'Active Thickness (nm)',
            'title': f'{speeds[num]} mV/s'
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
    # Massogram
    for massogram_name in massogram_names_list:
        tab = ttk.Frame(massogram_notebook)
        massogram_notebook.add(tab, text=massogram_name) 

        graph = ZoomableGraph(tab, massogram_name)
        graph.show()
    # Insertogram (Mass ver.)
    for insertogram_mass_name in insertogram_mass_names_list:
        tab = ttk.Frame(insertogram_mass_ver_notebook)
        insertogram_mass_ver_notebook.add(tab, text=insertogram_mass_name) 

        graph = ZoomableGraph(tab, insertogram_mass_name)
        graph.show()
    # Pos
    for diffusive_capacitive_positive_charge_name in diffusive_capacitive_positive_charge_names_list:
        tab = ttk.Frame(diffusive_capacitive_positive_charge_notebook)
        diffusive_capacitive_positive_charge_notebook.add(tab, text=diffusive_capacitive_positive_charge_name) 

        graph = ZoomableGraph(tab, diffusive_capacitive_positive_charge_name)
        graph.show()
    for insertogram_mass_pos_name in insertogram_mass_pos_names_list:
        tab = ttk.Frame(insertogram_mass_ver_pos_notebook)
        insertogram_mass_ver_pos_notebook.add(tab, text=insertogram_mass_pos_name) 

        graph = ZoomableGraph(tab, insertogram_mass_pos_name)
        graph.show()
    # Neg
    for diffusive_capacitive_negative_charge_name in diffusive_capacitive_negative_charge_names_list:
        tab = ttk.Frame(diffusive_capacitive_negative_charge_notebook)
        diffusive_capacitive_negative_charge_notebook.add(tab, text=diffusive_capacitive_negative_charge_name) 

        graph = ZoomableGraph(tab, diffusive_capacitive_negative_charge_name)
        graph.show()
    for insertogram_mass_neg_name in insertogram_mass_neg_names_list:
        tab = ttk.Frame(insertogram_mass_ver_neg_notebook)
        insertogram_mass_ver_neg_notebook.add(tab, text=insertogram_mass_neg_name) 

        graph = ZoomableGraph(tab, insertogram_mass_neg_name)
        graph.show()

    # Otros que no requieren pestañas inferiores
    # Oxidation
    graph = ZoomableGraph(oxidation_tab, pestañas_superiores[1])
    graph.show()
    # Reduction
    graph = ZoomableGraph(reduction_tab, pestañas_superiores[2])
    graph.show()
    # Parameter B
    graph = ZoomableGraph(parameterB_tab, pestañas_superiores[6])
    graph.show()
    # Specific Charge VS Sweed Speed
    graph = ZoomableGraph(scharge_vs_sspeed_tab, pestañas_superiores[8])
    graph.show()
    # Percentage of Specific Charge
    graph = ZoomableGraph(percentage_scharge_tab, pestañas_superiores[9])
    graph.show()
    # Masogram
    #graph = ZoomableGraph(masogram_tab, pestañas_superiores[10])
    #graph.show()
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

    # Hacer que los frames sean expansibles
    main_fm.columnconfigure(0, weight=1)
    main_fm.rowconfigure(0, weight=1)

def modelo2_page():
    modelo2_page_fm = tk.Frame(main_fm)#Para cambiar el fondo , bg='gray'

    modelo2_page_lb = tk.Label(modelo2_page_fm, text='Model 2',
                            font=('Arial',18,'bold'), fg='#1414b8')

    modelo2_page_lb.pack(pady=20)

    modelo2_page_fm.pack(fill=tk.BOTH, expand=True)

def modelo3_page():
    modelo3_page_fm = tk.Frame(main_fm)#Para cambiar el fondo , bg='gray'

    modelo3_page_lb = tk.Label(modelo3_page_fm, text='Model 3',
                            font=('Arial',18,'bold'), fg='#1414b8')

    modelo3_page_lb.pack(pady=20)

    modelo3_page_fm.pack(fill=tk.BOTH, expand=True)    

def about_page():
    global image_left, image_center, image_right  # Hacer las variables de imagen globales
    about_page_fm = tk.Frame(main_fm)  # Cambiar el fondo del marco a gris
    about_page_fm.pack(fill=tk.BOTH, expand=True)

    about_page_lb = tk.Label(about_page_fm, text='About MASC: Multiple Analysis Software for Supercpacitors',
                            font=('Arial', 15, 'bold'), fg='#1414b8')
    about_page_lb.pack(pady=10, padx=10)

    # Crear un marco para contener las imágenes
    image_frame = tk.Frame(about_page_fm)
    image_frame.pack(side=tk.TOP, fill=tk.X)

    # Configurar columnas para que se expandan y centren las imágenes
    image_frame.columnconfigure(0, weight=1)
    image_frame.columnconfigure(1, weight=1)
    image_frame.columnconfigure(2, weight=1)

    # Cargar las imágenes
    image_left = tk.PhotoImage(file="imagenes/uniM.png")
    label_left = tk.Label(image_frame, image=image_left)
    label_left.grid(row=0, column=0, padx=10)

    image_center = tk.PhotoImage(file="imagenes/logM1.png")  # m2ph
    label_center = tk.Label(image_frame, image=image_center)
    label_center.grid(row=0, column=1)

    image_right = tk.PhotoImage(file="imagenes/92.png")
    label_right = tk.Label(image_frame, image=image_right)
    label_right.grid(row=0, column=2, padx=10)

    texto_copyright = "Copyright © rlucioporto.com\nLa ciencia, una luz en la oscuridad.\n   "
    label_copyright = tk.Label(about_page_fm, text=texto_copyright, bg="navy", fg="white", font=("Arial", 8,'bold'))
    label_copyright.pack(side="bottom", fill="both")

    # Texto debajo de las imágenes
    texto = "Dr. Raúl Lucio Porto\nCentro de Innovación, Investigación y Desarrollo en Ingeniería y Tecnología\nCentro de Innovación en Ingeniería de Tecnología Inteligente Biomédica y Mecatrónica\n"
    label_texto = tk.Label( about_page_fm,text=texto, justify="center", wraplength=1000, width=1400, bg="blue4", fg="white", font=("Arial", 9, 'bold'))
    label_texto.pack()

    about_text = """
    1. Introduction
The research on energy storage devices such as supercapacitors and batteries generates a lot of data that must be processed manually in several software, slowing down its analysis and interpretation. Thus, the lack of specialized software hinders accurate data analysis in the field of  supercapacitors, especially for non-programming users.
In this work we report a new software designed to simplify the electrochemical data analysis obtained in the study of new materials and devices for electrochemical capacitors and batteries. The Multiple Analyses of Supercapacitors Software (MASC) offers an efficient solution for electrochemical data analysis in this growing field.

 2. Methodology​
MASC is purpose-built software for simplifying electrochemical data analysis in the quest for new supercapacitor materials and devices. Developed in Python with tkinter, MASC efficiently executes complex calculations using various functions.
Functionality: MASC accurately computes electrochemical properties, ensuring comprehensive coverage. Testing: Stringent testing protocols validate its accuracy and reliability across scenarios.
Structured in three modules, MASC seamlessly integrates data processing workflows, utilizing CSV files for input. Its goal is to offer an intuitive interface for researchers and scientists.
MASC aims to enhance data analysis efficiency by providing specialized and intuitive software. Initially targeted at CIIDIT's supercapacitor lab, future iterations will cater to users with diverse experience levels.
Requirements Analysis: Comprehensive understanding of project needs is key. Software Design: Focus on creating an intuitive and functional interface. Functionality Implementation: Robust algorithms for precise calculations. Testing and Validation: Extensive testing ensures reliability. Implementation and Distribution: Initial deployment planned in the research lab, with broader accessibility in future phases.​
    """

    about_text_txt = tk.Text(about_page_fm, wrap="word")
    about_text_txt.insert(tk.END, about_text)
    about_text_txt.config(state="disabled", font=("Arial", 11), bg="gray84", fg="black")
    about_text_txt.pack(expand=True, fill="both", padx=60, pady=10)

    about_page_fm.pack(fill=tk.BOTH, expand=True)

main_fm = tk.Frame(root, bg='gray84')  # Cambiar el fondo del marco principal a gris
main_fm.pack(fill=tk.BOTH, expand=True)

home_page()

root.mainloop()
