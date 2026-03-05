3D Thermal Simulation: Hot Sphere Heating a Cold Plate (Python)

This project presents a 3D transient heat diffusion simulation implemented in Python. The model investigates the thermal interaction between a hot spherical body and a cold metallic plate, illustrating how heat propagates through the solid over time. The temperature field is computed by solving the transient heat equation on a structured three-dimensional grid, and the results are visualized through rotating animated temperature distributions using PyVista.

Overview

The simulation models a simplified thermal contact problem in which a hot spherical object is placed on top of a cold plate. Heat is transferred through a localized circular contact region on the top surface of the plate. As time progresses, heat diffuses throughout the plate according to the governing heat equation.

The objective of this project is to demonstrate how scientific computing workflows and heat-transfer simulations can be implemented entirely in Python, combining numerical methods with modern 3D visualization tools.

Physics Model

The temperature evolution inside the plate is governed by the three-dimensional transient heat equation

∂T/∂t = α ∇²T

where

T — temperature
t — time
α — thermal diffusivity
∇²T — Laplacian of the temperature field

The equation is solved using an explicit finite difference method (FDM) on a structured computational grid.

Geometry

The simulation domain consists of a rectangular plate with dimensions:

60 mm × 60 mm × 10 mm

A hot spherical body is positioned above the plate and transfers heat through a circular contact patch on the top surface.

Conceptual geometry:

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

The thermal model includes the following boundary conditions:

Bottom surface

Constant temperature boundary representing a cold plate

T = 293 K

Side surfaces

Thermally insulated boundaries

∂T/∂n = 0

Top surface

Thermally insulated except for the circular contact region where temperature is prescribed

T = 1500 K

Numerical Method

The simulation employs:

Explicit finite difference method (FDM)

Structured three-dimensional computational grid

Central difference approximation of the Laplacian operator

Stability-controlled explicit time integration

The time step must satisfy the stability condition

Δt ≤ 1 / [ 2α (1/dx² + 1/dy² + 1/dz²) ]

Visualization

Simulation results are visualized using PyVista, enabling high-quality scientific visualization and animation. The visualization displays the evolving temperature field inside the plate while the camera rotates around the model.

The resulting animation illustrates:

Heat diffusion from the contact region

Temperature gradients developing within the plate

Rotating three-dimensional visualization of the thermal field

The simulation generates an animation file such as:

rotating_plate_heating.gif
Technologies Used

Python

NumPy — numerical computation

PyVista — 3D scientific visualization

Finite Difference Method (FDM) — numerical solution of the heat equation

Running the Simulation

Install the required Python libraries:

pip install numpy pyvista

Run the simulation script:

python PyVista.py

The simulation will generate an animated visualization of the temperature distribution saved as:

rotating_plate_heating.gif
Applications

This example demonstrates numerical techniques commonly used in:

Heat transfer analysis

Thermal contact modeling

Materials processing simulations

Electronics cooling analysis

Scientific computing workflows

Engineering simulation visualization

Author

Habib Pouriayevali
Computational Mechanics | Finite Element Modeling | Scientific Computing
