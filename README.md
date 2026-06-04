# Capacitance-Dielectric-Meter

## Overview
This project is a capacitance meter and dielectric characterization tool built 
around a 555 timer circuit and an Arduino Uno. The device works by placing an 
unknown capacitor into a 555 astable oscillator circuit, where the capacitance 
directly controls the oscillation frequency. The Arduino measures that frequency 
and back-calculates both the capacitance and the dielectric constant (ε_r) of 
the material between the plates using known resistor values and plate geometry. 
Accurate characterization of real-world dielectric materials is critical in 
semiconductor device engineering, where gate dielectric properties directly 
impact transistor performance at advanced nodes.
## Theory

### 555 astable timing equation
The capacitor charges toward Vcc from Vi 1/3Vcc. Using the general Rc charging eqn:

V(t) = Vcc - 2/3Vcc * e(-t/tau)

Solve for the time to reach 2/3Vcc
Set V(t) = 2/3Vcc

2/3Vcc = Vcc - 2/3Vcc * e(-t/tau) --->
2/3Vcc - Vcc = -2/3Vcc * e(-t/tau) --->
-1/3Vcc = -2/3Vcc * e(-t/tau) --->
1/2 = e(-t/tau) --->
-t/tau = ln(1/2) --->
-t/tau = -ln(2) --->
t = ln(2) * tau --->
t = 0.693 * tau 

This gives the charge and discharge times of:
 - t_charge = 0.693 * (R1 + R2) * C
 - t_discharge = 0.693 * R2 * C
 - t_tot = 0.693 * (R1 + 2R2) * C
 - f = 1.44/((R1+2R2) * C)
   
### Capacitance equation, using frequency
Rearranging the timing equation:
C = 1.44/((R1+2R2) * f)

### Dielectric Constant equation, using Capacitance
Using the parallel plate capacitor equation:
C = (ε_r)((ε_0) * A/d

Solving for ε_r:
ε_r = C/((ε_0) * A/d)

## Hardware 
 - Arduino Uno
 - 1k Ohm Resistor
 - 100k Ohm Resistor
 - 750k Ohm Resistor
 - 555 timing chip
 - 10nF Capacitor
 - 91.3pF timing Capacitor (4'' x 4'' Tin Foil capacitor with 1mm of seperation with cardboard, serves as the unknown capacitor under test)
 - Dielectric samples (paper, cardboard, plastic)
## Software

## Results

## How to Run
