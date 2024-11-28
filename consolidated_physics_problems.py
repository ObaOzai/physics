# consolidated_physics_problems.py
# Author: Oba Ozai 2024
# Description: A collection of Python solutions for common college-level physics problems.

import math

# ----------------------------------------------
# 1. Kinematics: Distance, Velocity, Acceleration
# ----------------------------------------------

def calculate_distance(v0, a, t):
    """
    Calculate the distance traveled under constant acceleration.
    Formula: d = v0 * t + 0.5 * a * t^2
    Parameters:
    - v0: Initial velocity (m/s)
    - a: Acceleration (m/s^2)
    - t: Time (s)
    """
    return v0 * t + 0.5 * a * t**2

def calculate_final_velocity(v0, a, t):
    """
    Calculate the final velocity under constant acceleration.
    Formula: v = v0 + a * t
    """
    return v0 + a * t

# Example usage:
# print(calculate_distance(0, 9.8, 5))  # Output: 122.5 (Free-fall distance in 5 seconds)
# print(calculate_final_velocity(0, 9.8, 5))  # Output: 49.0 (Velocity after 5 seconds)

# ----------------------------------------------
# 2. Force: Newton's Second Law
# ----------------------------------------------

def calculate_force(mass, acceleration):
    """
    Calculate force using Newton's second law.
    Formula: F = m * a
    Parameters:
    - mass: Mass (kg)
    - acceleration: Acceleration (m/s^2)
    """
    return mass * acceleration

# Example usage:
# print(calculate_force(10, 9.8))  # Output: 98.0 (Force on a 10 kg object due to gravity)

# ----------------------------------------------
# 3. Work and Energy
# ----------------------------------------------

def calculate_work(force, distance):
    """
    Calculate work done by a force.
    Formula: W = F * d
    Parameters:
    - force: Force (N)
    - distance: Distance moved in the direction of the force (m)
    """
    return force * distance

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy.
    Formula: KE = 0.5 * m * v^2
    """
    return 0.5 * mass * velocity**2

def calculate_potential_energy(mass, height, g=9.8):
    """
    Calculate potential energy.
    Formula: PE = m * g * h
    Parameters:
    - g: Gravitational acceleration (default: 9.8 m/s^2)
    """
    return mass * g * height

# Example usage:
# print(calculate_work(50, 10))  # Output: 500 (Work done by a 50 N force over 10 m)
# print(calculate_kinetic_energy(2, 3))  # Output: 9.0 (Kinetic energy of a 2 kg object moving at 3 m/s)
# print(calculate_potential_energy(10, 5))  # Output: 490.0 (Potential energy of a 10 kg object at 5 m)

# ----------------------------------------------
# 4. Projectile Motion
# ----------------------------------------------

def calculate_projectile_range(v0, angle, g=9.8):
    """
    Calculate the horizontal range of a projectile.
    Formula: R = (v0^2 * sin(2θ)) / g
    Parameters:
    - v0: Initial velocity (m/s)
    - angle: Launch angle (degrees)
    - g: Gravitational acceleration (default: 9.8 m/s^2)
    """
    angle_radians = math.radians(angle)
    return (v0**2 * math.sin(2 * angle_radians)) / g

def calculate_max_height(v0, angle, g=9.8):
    """
    Calculate the maximum height of a projectile.
    Formula: h_max = (v0^2 * sin^2(θ)) / (2 * g)
    """
    angle_radians = math.radians(angle)
    return (v0**2 * math.sin(angle_radians)**2) / (2 * g)

# Example usage:
# print(calculate_projectile_range(20, 45))  # Output: ~40.82 m
# print(calculate_max_height(20, 45))  # Output: ~10.20 m

# ----------------------------------------------
# 5. FizzBuzz (Classic Algorithm)
# ----------------------------------------------

def fizz_buzz(n):
    """
    Classic FizzBuzz problem:
    - Print "Fizz" for multiples of 3.
    - Print "Buzz" for multiples of 5.
    - Print "FizzBuzz" for multiples of both 3 and 5.
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
# fizz_buzz(15)

# ----------------------------------------------
# 6. Ohm's Law: Electrical Power, Resistance, Voltage
# ----------------------------------------------

def calculate_voltage(current, resistance):
    """
    Calculate voltage using Ohm's Law.
    Formula: V = I * R
    """
    return current * resistance

def calculate_power(voltage, current):
    """
    Calculate electrical power.
    Formula: P = V * I
    """
    return voltage * current

# Example usage:
# print(calculate_voltage(2, 5))  # Output: 10.0 (Voltage for 2 A current and 5 Ω resistance)
# print(calculate_power(10, 2))  # Output: 20.0 (Power for 10 V and 2 A)

# ----------------------------------------------
# End of File
# ----------------------------------------------

#EOF
