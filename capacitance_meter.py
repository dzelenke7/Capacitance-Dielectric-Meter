import serial
import matplotlib.pyplot as plt
import time

ser = serial.Serial('COM5', 9600)
time.sleep(2)

frequencies = []
capacitances = []
dielectric_constants = []

print("Reading data... press Ctrl+C to stop and plot")
    
while True:
    try:
        line1 = ser.readline().decode('utf-8').strip()
        line2 = ser.readline().decode('utf-8').strip()
        line3 = ser.readline().decode('utf-8').strip()

        print(f"Raw: '{line1}' '{line2}' '{line3}'")

        frequencies.append(float(line1))
        capacitances.append(float(line2))
        dielectric_constants.append(float(line3))

        print(f"Freq: {float(line1):.1f} Hz | C: {float(line2):.2e} F | er: {float(line3):.3f}")

    except KeyboardInterrupt:
        break

    except Exception as e:
        print(f"Error: {e}")
        print(f"Bad data was: '{line1}' '{line2}' '{line3}'")

print(f"Total readings collected: {len(frequencies)}")
print(frequencies)

plt.plot(frequencies)
plt.title("Frequency over time")
plt.xlabel("Reading Number")
plt.ylabel("Frequency (Hz)")
plt.show()

plt.plot(capacitances)
plt.title("Capacitance over time")
plt.xlabel("Reading Number")
plt.ylabel("Capacitance (F)")
plt.show()

plt.plot(dielectric_constants)
plt.title("Dielectric Constants over time")
plt.xlabel("Reading Number")
plt.ylabel("Dielectric Constants (er)")
plt.show()
ser.close()
