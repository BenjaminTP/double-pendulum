import numpy as np
from scipy.integrate import solve_ivp
from derivative import derivative, l_1, l_2
import matplotlib.pyplot as plt


def main():
    t_min = 0
    t_max = 100
    t_steps = 500
    num_variations = 50
    variation = 1e-9

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.set_box_aspect((2,2,1))
    ax.set_zlim(-75, 75)

    Z = np.zeros((num_variations, t_steps))

    for i in range(num_variations):
        y0 = [np.radians(100+i*variation), 1, np.radians(1), 0.5]
        t_eval = np.linspace(t_min,t_max,t_steps)

        sol = solve_ivp(derivative, (t_min,t_max), y0, t_eval=t_eval, rtol=1e-10, atol=1e-10)
        
        theta_1 = sol.y[0]
        theta_2 = sol.y[2]

        x_2 = l_1*np.sin(theta_1) + l_2*np.sin(theta_2)

        t = sol.t

        Z[i, :] = x_2

    X, Y = np.meshgrid(np.arange(num_variations), t_eval, indexing="ij")
    ax.plot_surface(X, Y, Z, cmap="viridis")
    ax.set_xlabel("Variation in Theta1 (Multiples of 1e-6)")
    ax.set_ylabel("Time")
    ax.set_zlabel("X_2 Coordinate")
    plt.show()


if __name__=="__main__":
    main()