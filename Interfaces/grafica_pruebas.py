import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class MeanBars:
    def __init__(self, velocidad, capacitiva, difusiva, dlc):
        self.velocidad = velocidad
        self.capacitiva = capacitiva
        self.difusiva = difusiva
        self.dlc = dlc

class GraphBars:
    def __init__(self, array_barras: list[pd.DataFrame], velocidades: list[float]) -> plt.figure:
        self.headers = ['Capacitiva', 'Difusiva', 'Doble layer']
        self.lista_velocidades: list[float] = []
        self.lista_medias_capacitiva: list[float] = []
        self.lista_medias_difusiva: list[float] = []
        self.lista_medias_dlc: list[float] = []

        self.lista_vel = [str(vel) for vel in velocidades]

        for i in range(len(array_barras)):
            self.lista_medias_capacitiva.append(array_barras[i].iloc[:, 0].mean())
            self.lista_medias_difusiva.append(array_barras[i].iloc[:, 1].mean())
            self.lista_medias_dlc.append(array_barras[i].iloc[:, 2].mean())

        data = MeanBars(velocidad=self.lista_vel, capacitiva=self.lista_medias_capacitiva,
                        difusiva=self.lista_medias_difusiva, dlc=self.lista_medias_dlc)

        plt.cla()
        self.fig, self.ax = plt.subplots(1, 1)
        self.ax.bar(data.velocidad, data.capacitiva, label='Pseudocapacitive', color='#FF5733')
        self.ax.bar(data.velocidad, data.difusiva, bottom=data.capacitiva, label='Difusiva', color='#33FF57')
        self.ax.bar(data.velocidad, data.dlc, bottom=np.add(data.capacitiva, data.difusiva), label='DLC', color='#337AFF')
        self.ax.legend()

        plt.xlabel('Scan rate (m*s^-1)')
        plt.ylabel('Specific charge (C*g^-1)')
        
    def get_canvas(self):
        return self.fig

class GOxidacion:
    def __init__(self, Ukpos, IKpos) -> None:
        fig = plt.figure('OXIDACION')
        ax = fig.add_subplot()
        ax.set_title('OXIDACION')
        ax.plot(Ukpos, IKpos, color='#FF5733')  # Cambiar color de la línea
        ax.set_ylabel('Intensity')
        ax.set_xlabel('Scan rate')

        self.canvas = fig

    def get_canvas(self) -> plt.figure:
        return self.canvas

# Generar datos simulados
dataframes = [pd.DataFrame({
    'Capacitiva': np.random.rand(10),
    'Difusiva': np.random.rand(10),
    'Doble layer': np.random.rand(10)
}) for _ in range(5)]

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear instancias de las clases y mostrar los gráficos
graph_bars = GraphBars(dataframes, [1.0, 2.0, 3.0, 4.0, 5.0])
fig_bars = graph_bars.get_canvas()
plt.show(fig_bars)

graph_oxidation = GOxidacion(x, y)
fig_oxidation = graph_oxidation.get_canvas()
plt.show(fig_oxidation)
