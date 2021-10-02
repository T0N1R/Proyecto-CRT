from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math
import matplotlib.pyplot as plt
import numpy as np

# ecuacion para ejes "X" y "Y" utilizando la amplitud, frecuencia, tiempo y fase
def eje(amp, freq, fase, time ):
    cOperation = (freq * time) + fase
    return float(amp * math.cos(cOperation) )
  
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot():
  
    # the figure that will contain the plot
    fig = plt.figure(figsize = (5, 5),
                 dpi = 100)

    x_values = []
    y_values = []


    current_time = 0

    # X parameters for "eje" function
    amplitudeX = 5
    frequencyX = 2
    phaseX = math.pi / 2

    # Y parameters for "eje" function
    amplitudeY = 5
    frequencyY = 3
    phaseY = 0

    while current_time < 300:
        x_values.append(eje(amplitudeX, frequencyX, phaseX, current_time))
        y_values.append(eje(amplitudeY, frequencyY, phaseY, current_time))
        current_time += 1

    t = np.arange(0.0, 2.0, 0.01)
    s1 = np.sin(2*np.pi*t)
    s2 = np.sin(4*np.pi*t)

    plt.subplot(311)
    plt.plot(t, s1)
    plt.subplot(312)
    plt.plot(t, s1)
    plt.subplot(313)
    plt.scatter(x_values, y_values)

    # plt.show()
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=7, column=2)
  

    """
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    """
    
  
# the main Tkinter window
window = Tk()
  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")

# Amplitude X
Label(window, text = "Amplitud X").grid(row=2, column=0)
amplitudX = Entry(window, width = 5)
amplitudX.grid(row= 2, column=1)

# Amplitud Y
Label(window, text = "Amplitud Y").grid(row=2, column=3)
amplitudY = Entry(window, width = 5)
amplitudY.grid(row= 2, column=4)

# Frecuencia X
Label(window, text = "Frecuencia X").grid(row=3, column=0)
frecuenciaX = Entry(window, width = 5)
frecuenciaX.grid(row=3, column=1)

# Frecuencia Y
Label(window, text = "Frecuencia Y").grid(row=3, column=3)
frecuenciaY = Entry(window, width = 5)
frecuenciaY.grid(row=3, column=4)

# Fase X
Label(window, text = "Fase X").grid(row=4, column=0)
faseX = Entry(window, width = 5)
faseX.grid(row=4, column=1)

# Fase Y
Label(window, text = "Fase Y").grid(row=4, column=3)
faseY = Entry(window, width = 5)
faseY.grid(row=4, column=4)

# Tiempo
Label(window, text = "Tiempo").grid(row=5, column=0)
tiempo = Entry(window, width = 5)
tiempo.grid(row=5, column=1)

  
# button that displays the plot
plot_button = Button(master = window, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.grid(row=6, column=0)
  
# run the gui
window.mainloop()