import serial
import time
import matplotlib.pyplot as plt


ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)

data = []
for i in range(100):
    line = ser.readline()   
    if line:
        string = line.decode()  
        num = int(string) 
        print(num)
        data.append(num) 

# build the plot
plt.plot(data)
plt.xlabel('Tiempo')
plt.ylabel('Lectura del potenciometro')
plt.title('Lectura de potenciometro vs. Tiempo')
plt.show()