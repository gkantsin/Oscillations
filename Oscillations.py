# imports
import math as m
import matplotlib.pyplot as plt
import numpy as np


# Variables

class SHMOscillation:
    def __init__(self, num, name, amplitude, initialPhase, omega):
        self.name = name
        self.num = num
        self.amplitude = amplitude
        self.initialPhase = initialPhase
        self.omega = omega

    def calculate(self, t):
        x = self.amplitude * m.sin(self.omega * t + self.initialPhase)
        v = self.omega * self.amplitude * m.cos(self.omega * t + self.initialPhase)
        print(x, "m")
        print(v, "m/s")

    def getValues(self):
        oscValues = [self.amplitude, self.initialPhase, self.omega]
        return oscValues

    def printInfo(self):
        print(f"-----------------------~ Initial Conditions for {self.name} ~-----------------------")
        values = ["Amplitude", "Initial Phase", "Angular Velocity"]
        d = ["m", "rad", "rad/s"]
        for i in range(3):
            print(values[i], "=", self.getValues()[i], d[i])
        print('\n')

    def plotting(self):
        t = np.arange(0, 4 * m.pi, 0.01)
        x = self.amplitude * np.sin(self.omega * t + self.initialPhase)
        v = self.omega * self.amplitude * np.cos(self.omega * t + self.initialPhase)
        a = self.omega ** 2 * self.amplitude * np.sin(self.omega * t + self.initialPhase)

        f = plt.figure(self.num)

        plt.plot(t, x, label="Distance (m)")
        plt.plot(t, v, label="Velocity (m/s)")
        plt.plot(t, a, label="Acceleration (m/s^2)")
        plt.title(self.name)
        plt.grid()
        plt.xlabel("Time (s)")


def showPlots():
    plt.legend()
    plt.show()
