import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m1 = m2 = 1.0
l1 = l2 = 1.0


def deriv(Y):
    t1, w1, t2, w2 = Y
    d = t1 - t2
    s, c = np.sin(d), np.cos(d)
    den = m1 + m2 * s**2
    a1 = (-m2*l2*w2**2*s - m2*l1*c*w1**2*s
          - (m1+m2)*g*np.sin(t1) + m2*g*c*np.sin(t2)) / (l1*den)
    a2 = ((m1+m2)*l1*w1**2*s + m2*l2*c*w2**2*s
          + (m1+m2)*g*c*np.sin(t1) - (m1+m2)*g*np.sin(t2)) / (l2*den)
    return np.array([w1, a1, w2, a2])


def rk4_step(Y, dt):
    k1 = deriv(Y)
    k2 = deriv(Y + 0.5*dt*k1)
    k3 = deriv(Y + 0.5*dt*k2)
    k4 = deriv(Y + dt*k3)
    return Y + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)


def main():
    deg_min, deg_max = -180, 180
    N = 2500            
    t_max = 80.0       
    dt = 0.01

    ang = np.radians(np.linspace(deg_min, deg_max, N))
    TH1, TH2 = np.meshgrid(ang, ang, indexing="xy")
    Y = np.array([TH1.ravel(), np.zeros(N*N), TH2.ravel(), np.zeros(N*N)])

    flip_time = np.full(N*N, np.nan)
    active = np.ones(N*N, dtype=bool)      

    for step in range(int(t_max/dt)):
        Y[:, active] = rk4_step(Y[:, active], dt)
        newly = active & (np.abs(Y[2]) > np.pi)     
        flip_time[newly] = (step + 1)*dt
        active[newly] = False
        if not active.any():
            break

    img = flip_time.reshape(N, N)
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(img, origin="lower", extent=[deg_min, deg_max, deg_min, deg_max],
                   cmap="turbo", interpolation="nearest")
    im.cmap.set_bad("black")              
    ax.set_xlabel(r"initial $\theta_1$ (deg)")
    ax.set_ylabel(r"initial $\theta_2$ (deg)")
    ax.set_title("Time until the second arm first flips")
    fig.colorbar(im, label="flip time (s)", shrink=0.8)
    fig.tight_layout()
    fig.savefig("flip_fractal_fast.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()