3D Thermal Simulation: Hot Sphere Heating a Cold Plate (Python)

This project demonstrates a 3D transient heat diffusion simulation implemented in Python. The model simulates the thermal interaction between a hot spherical object and a cold metallic plate, showing how heat propagates inside the solid over time.

The simulation uses an explicit numerical solver for the heat equation and produces a rotating 3D animation of the temperature field using PyVista.

OVERVIEW

The model represents a thermal contact problem where a hot spherical body is placed on top of a cold plate. Heat is transferred through a circular contact region on the top surface, and the temperature distribution evolves inside the plate according to the heat diffusion equation.

The goal of this project is to demonstrate how scientific simulations can be implemented entirely in Python using numerical methods and modern visualization tools.

PHYSICS MODEL

The temperature evolution follows the three-dimensional transient heat equation:

dT/dt = alpha * Laplacian(T)

where:

T = temperature
t = time
alpha = thermal diffusivity

The equation is solved using an explicit finite difference method on a structured grid.

GEOMETRY

Plate dimensions:

60 mm × 60 mm × 10 mm

A spherical heat source is positioned above the plate and transfers heat through a circular contact patch on the top surface.

Conceptual geometry:

    Hot Sphere
        O
        |
        | heat transfer
| |
| Plate |
| |
       Cold boundary

BOUNDARY CONDITIONS

Bottom Surface
Constant temperature boundary condition (cold plate)

T = 293 K

Side Surfaces
Thermally insulated boundaries

dT/dn = 0

Top Surface
Insulated except for the circular contact region where the temperature is fixed:

T = 1500 K

NUMERICAL METHOD

The simulation uses:

Explicit finite difference method (FDM)

Structured three-dimensional grid

Central difference Laplacian

Stability-controlled timestep

The explicit scheme must satisfy the stability condition:

dt <= 1 / [2 * alpha * (1/dx^2 + 1/dy^2 + 1/dz^2)]

VISUALIZATION

The simulation results are visualized using PyVista.

The visualization includes:

3D temperature distribution inside the plate

rotating camera animation

animated GIF output

The animation shows heat spreading through the plate while the scene rotates in 3D.

TECHNOLOGIES USED

Python
NumPy – numerical computation
PyVista – 3D scientific visualization
Finite Difference Method – PDE solver

RUNNING THE SIMULATION

Install required libraries:

pip install numpy pyvista

Run the simulation:

python hot_sphere_plate_heating.py

The simulation will generate an animation file:

rotating_plate_heating.gif

APPLICATIONS

This simulation illustrates concepts commonly used in:

Heat transfer modeling
Thermal contact problems
Electronics cooling
Materials processing
Scientific computing workflows
Engineering visualization

AUTHOR

Habib Pouriayevali
Computational Mechanics | Finite Element Modeling | Scientific Computing
