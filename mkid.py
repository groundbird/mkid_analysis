#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class SweepData(object):
    def __init__(self, fname):
        self.fname = fname
        self.data  = np.loadtxt(self.fname)

    @property
    def f(self):
        return self.data[:,0]
    @property
    def i(self):
        return self.data[:,1]
    @property
    def q(self):
        return self.data[:,2]
    @property
    def amp(self):
        return np.abs(self.i + 1j*self.q)
    @property
    def pha(self):
        return np.angle(self.i + 1j*self.q)
    
    def plot_iq(self, grid=True, axis='scaled', norm=True, title=''):
        fig, ax = plt.subplots()
        norm = max(self.amp) if norm else 1
        ret = ax.plot(self.i/norm, self.q/norm)
        plt.xlabel('I')
        plt.ylabel('Q')
        ax.axis(axis)
        ax.grid(grid)
        return ret
    def plot_amp(self, lo=, grid=True, title=''):
        fig, ax = plt.subplots()
        ret = ax.plot(self.f/1e6, self.amp)
        plt.xlabel('Frequency [MHz] + %s' % lo)
        plt.ylabel('Amplitude [a.u.]')
        plt.title(title)
        ax.grid(grid)
        return ret
    def plot_pha(self, grid=True, title=''):
        fig, ax = plt.subplots()
        ret = ax.plot(self.f, self.pha)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Phase [deg]')
        plt.title(title)
        ax.grid(grid)
        return ret
