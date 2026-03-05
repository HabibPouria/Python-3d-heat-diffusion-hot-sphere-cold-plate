#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import pyvista as pv
import time

# ============================================================
# 1) Plate + physics parameters
# ============================================================
Lx, Ly, Lz = 0.06, 0.06, 0.01
nx, ny, nz = 80, 80, 20

dx = Lx / (nx - 1)
dy = Ly / (ny - 1)
dz = Lz / (nz - 1)

alpha  = 1.2e-5
T_cold = 293.15
T_hot  = 1500.0
clim = [T_cold, T_hot]

dt_stable = 1.0 / (2.0 * alpha * (1/dx**2 + 1/dy**2 + 1/dz**2))
dt = 0.25 * dt_stable
nsteps = 240  # more frames = smoother animation

print("dt:", dt, " total time:", nsteps * dt)

# ============================================================
# 2) Grid + initial temperature
# ============================================================
grid = pv.ImageData(
    dimensions=(nx, ny, nz),
    spacing=(dx, dy, dz),
    origin=(-Lx/2, -Ly/2, 0.0)
)

T = np.full((nx, ny, nz), T_cold, dtype=float)
grid["Temperature"] = T.ravel(order="F")

# ============================================================
# 3) Hot sphere + contact patch (top surface)
# ============================================================
sphere_radius = 0.012
sphere_center = (0.0, 0.0, Lz + sphere_radius)
sphere = pv.Sphere(radius=sphere_radius, center=sphere_center,
                   theta_resolution=80, phi_resolution=80)

a_contact = 0.006
x = np.linspace(-Lx/2, Lx/2, nx)
y = np.linspace(-Ly/2, Ly/2, ny)
X, Y = np.meshgrid(x, y, indexing="ij")
contact_mask = (X**2 + Y**2) <= a_contact**2

# ============================================================
# 4) Explicit heat diffusion step
# ============================================================
def step_heat(T):
    Tn = T.copy()

    Tn[1:-1, 1:-1, 1:-1] = T[1:-1, 1:-1, 1:-1] + alpha * dt * (
        (T[2:,   1:-1, 1:-1] - 2*T[1:-1, 1:-1, 1:-1] + T[:-2,  1:-1, 1:-1]) / dx**2 +
        (T[1:-1, 2:,   1:-1] - 2*T[1:-1, 1:-1, 1:-1] + T[1:-1, :-2,  1:-1]) / dy**2 +
        (T[1:-1, 1:-1, 2:  ] - 2*T[1:-1, 1:-1, 1:-1] + T[1:-1, 1:-1, :-2 ]) / dz**2
    )

    # bottom Dirichlet cold
    Tn[:, :, 0] = T_cold

    # insulated sides (Neumann ~ 0)
    Tn[0, :, :]   = Tn[1, :, :]
    Tn[-1, :, :]  = Tn[-2, :, :]
    Tn[:, 0, :]   = Tn[:, 1, :]
    Tn[:, -1, :]  = Tn[:, -2, :]

    # top insulated except hot patch
    k_top = nz - 1
    Tn[:, :, k_top] = Tn[:, :, k_top - 1]
    Tn[:, :, k_top][contact_mask] = T_hot

    return Tn

# ============================================================
# 5) PyVista: rotating + temperature animation GIF
# ============================================================
p = pv.Plotter(off_screen=True)
p.window_size = (1200, 650)
p.camera_position = "iso"

# plate (3D box)
p.add_mesh(grid, scalars="Temperature", cmap="inferno", clim=clim, opacity=0.95)

# sphere overlay
p.add_mesh(sphere, opacity=0.35, color="white")

# optional: outline for depth cues
p.add_mesh(grid.outline(), color="white", opacity=0.25)

p.add_text("Hot sphere heating a cold plate (rotating)", font_size=12)
p.add_axes()

p.reset_camera()
p.camera.zoom(1.2)  # set to <1 for more zoom out, >1 for zoom in

# IMPORTANT: unique filename to avoid Windows lock
gif_name = f"rotating_temp_{int(time.time())}.gif"
p.open_gif(gif_name)

for n in range(nsteps):
    T = step_heat(T)
    grid["Temperature"] = T.ravel(order="F")

    # rotate camera each frame
    p.camera.azimuth += 2.0

    # write frame
    p.write_frame()

    if n % 40 == 0:
        print(f"step {n:4d}/{nsteps}  Tmin={T.min():.2f}  Tmax={T.max():.2f}")

p.close()
print("Saved:", gif_name)


# In[ ]:




