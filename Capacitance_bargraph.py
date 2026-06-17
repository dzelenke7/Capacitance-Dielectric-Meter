import numpy as np
import matplotlib.pyplot as plt

nominal_values = [47, 100, 220, 330, 470, 680, 1000]

measured_values = [61.14, 118.6, 248.4, 322.2, 530.7, 676, 1486.3]

percent_errors = []
for nominal, measured in zip(nominal_values, measured_values):
    error = (measured - nominal) / nominal * 100
    percent_errors.append(error)

x = np.arange(len(nominal_values))
width = 0.35

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

ax1.bar(x - width/2, nominal_values, width, label='Nominal')
ax1.bar(x + width/2, measured_values, width, label='Measured')
ax1.set_xlabel('Capacitor')
ax1.set_ylabel('Capacitance (pF)')
ax1.set_title('Measured vs Nominal Capacitance')
ax1.set_xticks(x)
ax1.set_xticklabels(nominal_values)
ax1.legend()

ax2.bar(x, percent_errors, color='red')
ax2.set_xlabel('Capacitor')
ax2.set_ylabel('Percent Error (%)')
ax2.set_title('Measurement Error by Capacitor')
ax2.set_xticks(x)
ax2.set_xticklabels(nominal_values)

plt.tight_layout()
plt.show()
plt.show()
