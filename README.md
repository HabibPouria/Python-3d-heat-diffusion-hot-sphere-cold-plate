3D Thermal Simulation: Hot Sphere Heating a Cold Plate (Python)

This project demonstrates a 3D transient heat diffusion simulation implemented in Python. The model simulates the thermal interaction between a hot spherical object and a cold metallic plate, showing how heat propagates through the plate over time. The simulation solves the transient heat equation on a structured 3D grid and produces a rotating animated visualization of the temperature field using PyVista.

Overview

The model represents a simple thermal contact problem in which a hot spherical body is placed on top of a cold plate. Heat is transferred through a circular contact region on the top surface, and the temperature distribution evolves inside the plate according to the heat diffusion equation. The goal of this project is to demonstrate how scientific simulations and numerical heat-transfer models can be implemented entirely in Python using modern numerical and visualization libraries.

Physics Model

The temperature evolution inside the plate follows the three-dimensional transient heat equation:

∂T/∂t = α ∇²T

where:

T is temperature

t is time

α is the thermal diffusivity

∇²T is the Laplacian of the temperature field

The equation is solved using an explicit finite difference method (FDM) on a structured grid.

Geometry

The simulation domain is a rectangular plate with dimensions:

60 mm × 60 mm × 10 mm

A spherical heat source is positioned above the plate and transfers heat through a circular contact region on the top surface.

Conceptual representation:

        Hot Sphere
            O
            |
            | heat transfer
   ---------------------------
   |                         |
   |          Plate          |
   |                         |
   ---------------------------
           Cold boundary
Boundary Conditions

The model includes three types of thermal boundary conditions:

Bottom surface

Constant temperature boundary condition representing a cold plate.

T = 293 K

Side surfaces

Thermally insulated boundaries.

∂T/∂n = 0

Top surface

Insulated except for the circular contact region where the temperature is fixed.

T = 1500 K

Numerical Method

The simulation uses:

Explicit finite difference method (FDM)

Structured 3D computational grid

Central difference approximation for the Laplacian

Stability-controlled time stepping

The explicit scheme must satisfy the stability condition:

Δt ≤ 1 / [2α (1/dx² + 1/dy² + 1/dz²)]

Visualization

Simulation results are visualized using PyVista, enabling interactive 3D rendering and animation. The visualization shows the temperature distribution inside the plate while the camera rotates around the model.

The output animation illustrates:

Heat spreading from the contact region

Temperature gradients inside the plate

Rotating 3D visualization of the thermal field

The simulation generates an animated file such as:

rotating_plate_heating.gif
Technologies Used

Python

NumPy – numerical computation

PyVista – 3D scientific visualization

Finite Difference Method (FDM) – numerical solution of the heat equation

Running the Simulation

Install required libraries:

pip install numpy pyvista

Run the simulation script:

XXXX.py

The simulation will generate an animated temperature visualization saved as:

rotating_plate_heating.gif
Applications

This example demonstrates numerical techniques commonly used in:

Heat transfer modeling

Thermal contact problems

Materials processing

Electronics cooling

Scientific computing workflows

Engineering simulation visualization

Author

Habib Pouriayevali
Computational Mechanics | Finite Element Modeling | Scientific Computing
