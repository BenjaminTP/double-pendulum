# Double Pendulum Chaos Representations
I was interested in seeing the chaotic behaviour of a double pendulum system, so I derived the equations of motion from the Euler-Lagrange equations, and numerically solved the ODEs. There were two things I wanted to see: the time-to-flip fractal, and how much of a difference a tiny variance will make for a trajectory over time.

### Time-to-Flip Fractal
The time for the second pendulum to flip represented as a colour on a 2D grid with axes of the starting angles of each pendulum. This is produces a very well known fractal

### Tiny Variances

# Double Pendulum Equations of Motion Derivation

Let $`m_1,\ m_2,\ l_1,\ l_2,\ \theta_1,\ \theta_2`$ be the masses of 2 point masses, lengths of 2 pendulums in series, and the angles between each pendulum from the vertical. 

## Deriving Position and Velocity

We can derive the positions of each mass in a cartesian coordinate system:

```math
x_1 = l_1 \sin(\theta_1),\ y_1=-l_1 \cos(\theta_1)\\
x_2=l_1 \sin(\theta_1)+l_2 \sin(\theta_2),\ y_2 =-l_1 \cos(\theta_1) - l_2 \cos(\theta_2)
```

Differentiating each position with respect to time allows us to find the velocity in each direction as such:

```math
\dot{x}_1=l_1\omega_1 \cos(\theta_1),\ \dot{y}_1 = l_1\omega_1 \sin(\theta_1)\\
\dot{x}_2=l_1\omega_1 \cos(\theta_1)+ l_2\omega_2 \cos(\theta_2),\ \dot{y}_2 = l_1\omega_1 \sin(\theta_1)+ l_2\omega_2 \sin(\theta_2)
```

## Lagrangian Setup

We can now begin setting up the Lagrangian:

```math
\mathcal{L} = K - U\\
\mathcal{L} = \frac{1}{2}mv^2 - mgh\\
```

Using $`v_i^2=\dot{x}_i^2+\dot{y}_i^2`$ we can find the kinetic energy:

```math
K =\frac{1}{2}m_1v_1^2+\frac{1}{2}m_2v_2^2\\ \ \\

K =\frac{1}{2}(m_1(l_1^2\omega_1^2\cos^2(\theta_1)+l_1^2\omega_1^2\sin^2(\theta_1)) \\ 

+m_2(l_1^2\omega_1^2\cos^2(\theta_1)+2l_1l_2\omega_1\omega_2\cos(\theta_1)\cos(\theta_2)+l_2^2\omega_2^2\cos^2(\theta_2))\\ 

+l_1^2\omega_1^2\sin^2(\theta_1)+2l_1l_2\omega_1\omega_2\sin(\theta_1)\sin(\theta_2)+l_2^2\omega_2^2\sin^2(\theta_2))\\ \ \\

K =\frac{1}{2}(m_1l_1^2\omega_1^2+m_2(l_1^2\omega_1^2+l_2\omega_2^2+2l_1l_2\omega_1\omega_2(\cos(\theta_1)\cos(\theta_2)+\sin(\theta_1)\sin(\theta_2))))\\ \ \\

K = \frac{1}{2}(m_1l_1^2\omega_1^2+m_2(l_1^2\omega_1^2+l_2^2\omega_2^2+2l_1l_2\omega_1\omega_2\cos(\theta_1-\theta_2)))\\ \ \\

K = \frac{1}{2}(m_1+m_2)l_1^2\omega_1^2+\frac{1}{2}m_2l_2^2\omega_2^2+m_2l_1l_2\omega_1\omega_2\cos(\theta_1-\theta_2)
```

We can then derive the potential energy, which is simply the gravitational potential energy of the system:

```math
U = mgh\\ 
U = m_1gy_1+m_2gy_2\\
U = -m_1 g l_1 \cos(\theta_1) + m_2 g (-l_1 \cos(\theta_1) - l_2 \cos(\theta_2))\\
U = -m_1gl_1\cos(\theta_1) - m_2gl_1\cos(\theta_1) - m_2gl_2\cos(\theta_2)\\
U = -(m_1+m_2)gl_1\cos(\theta_1) - m_2 g l_2 \cos(\theta_2)
```

From this we can find the full Lagrangian:

```math
\mathcal{L}=K-U\\
\mathcal{L}=\frac{1}{2}(m_1+m_2)l_1^2\omega_1^2+\frac{1}{2}m_2l_2^2\omega_2^2+m_2l_1l_2\omega_1\omega_2\cos(\theta_1-\theta_2)+(m_1+m_2)gl_1\cos(\theta_1) + m_2 g l_2 \cos(\theta_2)
```

Or using $`\omega_i=\dot{\theta}_i`$:

```math
\mathcal{L}=\frac{1}{2}(m_1+m_2)l_1^2\dot{\theta}_1^2+\frac{1}{2}m_2l_2^2\dot{\theta}_2^2+m_2l_1l_2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2)+(m_1+m_2)gl_1\cos(\theta_1) + m_2 g l_2 \cos(\theta_2)
```

## Using the Euler-Lagrange Equation

The equations of motion will come from the Euler-Lagrange equations:

```math
\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta_i}}=\frac{\partial\mathcal{L}}{\partial \theta_i}, \ i \in [1, 2]
```

To find the motion for $`\theta_1`$, we can use the equation above:

```math
\frac{\partial \mathcal{L}}{\partial \dot{\theta_1}}=(m_1+m_2)l_1^2\dot{\theta}_1+m_2l_1l_2\dot{\theta}_2\cos(\theta_1-\theta_2)\\

\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}_1}=(m_1+m_2)l_1^2\ddot{\theta}_1-m_2l_1l_2\dot{\theta}_2(\dot{\theta_1}-\dot{\theta_2})
\sin(\theta_1-\theta_2)+m_2l_1l_2\ddot{\theta}_2\cos(\theta_1-\theta_2)\\ \ \\

\frac{\partial \mathcal{L}}{\partial \theta_1}=-m_2l_1l_2\dot{\theta_1}\dot{\theta_2}\sin(\theta_1-\theta_2)-(m_1+m_2)gl_1\sin(\theta_1)\\ \ \\
```
We now have enough to solve the Euler-Lagrange equation:
```math
\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}_1}=\frac{\partial \mathcal{L}}{\partial \theta_1}\\ \ \\

\Rightarrow (m_1+m_2)l_1^2\ddot{\theta}_1-m_2l_1l_2\dot{\theta}_2(\cancel{\dot{\theta_1}}-\dot{\theta_2})

\sin(\theta_1-\theta_2)+m_2l_1l_2\ddot{\theta}_2\cos(\theta_1-\theta_2)\\=\cancel{-m_2l_1l_2\dot{\theta_1}\dot{\theta_2}\sin(\theta_1-\theta_2)}-(m_1+m_2)gl_1\sin(\theta_1)\\ \ \\

(m_1+m_2)l_1^{\cancel{2}}\ddot{\theta}_1+m_2\cancel{l_1}l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)+m_2\cancel{l_1}l_2\ddot{\theta}_2\cos(\theta_1-\theta_2)=-(m_1+m_2)g\cancel{l_1}\sin(\theta_1)\\ \ \\

\therefore (m_1+m_2)l_1\ddot{\theta}_1+m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)+m_2l_2\ddot{\theta}_2\cos(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1)=0
```

We can do the same for $`\theta_2`$:

```math
\frac{\partial \mathcal{L}}{\partial \dot{\theta}_2}=m_2l_2^2\dot{\theta}_2+m_2l_1l_2\dot{\theta}_1\cos(\theta_1-\theta_2)\\ \ \\

\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}_2}=m_2l_2^2\ddot{\theta}_2 + m_2l_1l_2\ddot{\theta}_1\cos(\theta_1-\theta_2) - m_2l_1l_2\dot{\theta}_1(\dot{\theta_1}-\dot{\theta}_2)\sin(\theta_1-\theta_2)\\ \ \\

\frac{\partial \mathcal{L}}{\partial \theta_2} = m_2l_1l_2\dot{\theta}_1\dot{\theta}_2\sin(\theta_1-\theta_2)-m_2gl_2\sin(\theta_2)\\ \ \\
```
---
```math
\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}_2}=\frac{\partial \mathcal{L}}{\partial \theta_2}\\ \ \\

m_2l_2^2\ddot{\theta}_2 + m_2l_1l_2\ddot{\theta}_1\cos(\theta_1-\theta_2) - m_2l_1l_2\dot{\theta}_1(\dot{\theta}_1-\cancel{\dot{\theta}_2)}\sin(\theta_1-\theta_2)=\cancel{m_2l_1l_2\dot{\theta}_1\dot{\theta}_2\sin(\theta_1-\theta_2)}-m_2gl_2\sin(\theta_2) \\ \ \\

m_2l_2^{\cancel{2}}\ddot{\theta}_2+m_2l_1\cancel{l_2}\ddot{\theta}_1\cos(\theta_1-\theta_2)-m_2l_1\cancel{l_2}\dot{\theta}_1^2\sin(\theta_1-\theta_2)=-m_2g\cancel{l_2}\sin(\theta_2)\\ \ \\

\cancel{m_2}l_2\ddot{\theta}_2+\cancel{m_2}l_1\ddot{\theta}_1\cos(\theta_1-\theta_2) - \cancel{m_2}l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)=-\cancel{m_2}g\sin(\theta_2)\\ \ \\

\therefore l_2\ddot{\theta}_2+l_1\ddot{\theta}_1\cos(\theta_1-\theta_2) - l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)+g\sin(\theta_2)=0
```

## Isolating for $`\ddot{\theta}_1`$ and $`\ddot{\theta}_2`$

Since there no solution to the differential equations, we must solve them numerically. To do so we need to isolate for $`\ddot{\theta}_1`$ and $`\ddot{\theta}_2`$. 

We have a system of equations with 2 variables and 2 equations:

```math
(m_1+m_2)l_1\ddot{\theta}_1+m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)+m_2l_2\ddot{\theta}_2\cos(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1)=0 \\ \ \\

\Rightarrow (m_1+m_2)l_1\ddot{\theta}_1+m_2l_2\cos(\theta_1-\theta_2)\ddot{\theta}_2=-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)
```

---

```math
l_2\ddot{\theta}_2+l_1\ddot{\theta}_1\cos(\theta_1-\theta_2) - l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)+g\sin(\theta_2)=0\\ \ \\

\Rightarrow l_1\cos(\theta_1-\theta_2)\ddot{\theta}_1 + l_2\ddot{\theta}_2= l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2)
```

We can easily set up a matrix from this and solve for $`\ddot{\theta}_1`$ and $`\ddot{\theta}_2`$:

```math
\begin {bmatrix}
(m_1+m_2)l_1\ddot{\theta}_1+m_2l_2\cos(\theta_1-\theta_2)\ddot{\theta}_2\\

l_1\cos(\theta_1-\theta_2)\ddot{\theta}_1 + l_2\ddot{\theta}_2
\end {bmatrix}
=
\begin {bmatrix}
-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)\\

l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2)
\end {bmatrix}
\\ \ \\

\begin {bmatrix}
(m_1+m_2)l_1 & m_2l_2\cos(\theta_1-\theta_2)\\

l_1\cos(\theta_1-\theta_2) & l_2
\end {bmatrix}

\begin {bmatrix}
\ddot{\theta}_1\\

\ddot{\theta}_2
\end {bmatrix}

=

\begin {bmatrix}
-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)\\

l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2)
\end {bmatrix}
```

Using Cramer's Rule, we can find the solution to the system:

```math
\begin {bmatrix}
a_1 & b_1 \\ a_2 & b_2
\end {bmatrix}

\begin {bmatrix}
x \\ y
\end {bmatrix}
=
\begin {bmatrix}
c_1\\c_2
\end {bmatrix}

\Rightarrow
x=\frac{c_1b_2-b_1c_2}{a_1b_2-b_1a_2},\ y=\frac{a_1c_2-c_1a_2}{a_1b_2-b_1a_2}
```

---

```math
\ddot{\theta}_1=\frac{(-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1))(l_2)-(m_2l_2\cos(\theta_1-\theta_2))(l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2))}{((m_1+m_2)l_1)(l_2)-(m_2l_2\cos(\theta_1-\theta_2))(l_1\cos(\theta_1-\theta_2))}\\ \ \\

\ddot{\theta}_2=\frac{((m_1+m_2)l_1)(l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2))-(-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1))(l_1\cos(\theta_1-\theta_2))}{((m_1+m_2)l_1)(l_2)-(m_2l_2\cos(\theta_1-\theta_2))(l_1\cos(\theta_1-\theta_2))}
```

By simplifying the denominator we get:

```math
((m_1+m_2)l_1)(l_2)-(m_2l_2\cos(\theta_1-\theta_2))(l_1\cos(\theta_1-\theta_2))\\
=m_1l_1l_2+m_2l_1l_2-m_2l_1l_2\cos^2(\theta_1-\theta_2)\\
=m_1l_1l_2+m_2l_1l_2(1-\cos^2(\theta_1-\theta_2))\\
=l_1l_2(m_1+m_2\sin^2(\theta_1-\theta_2))
```

By simplifying the numerator of $`\ddot{\theta}_1`$ we get:

```math
(-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1))(l_2)-(m_2l_2\cos(\theta_1-\theta_2))(l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2))\\

=-m_2l_2^2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)gl_2\sin(\theta_1)-m_2l_1l_2\dot{\theta}_1^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+m_2l_2g\cos(\theta_1-\theta_2)\sin(\theta_2)\\

=(l_2)(-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)-m_2l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+m_2g\cos(\theta_1-\theta_2)\sin(\theta_2))
```

Combining numerator and denominator for $`\ddot{\theta}_1`$ gives us:

```math
\ddot{\theta}_1=\frac{(\cancel{l_2})(-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)-m_2l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+m_2g\cos(\theta_1-\theta_2)\sin(\theta_2))}{l_1\cancel{l_2}(m_1+m_2\sin^2(\theta_1-\theta_2))}\\ \ \\

\ddot{\theta}_1=\frac{-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)-m_2l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+m_2g\cos(\theta_1-\theta_2)\sin(\theta_2)}{l_1(m_1+m_2\sin^2(\theta_1-\theta_2))}
```

The numerator of $`\ddot{\theta}_2`$ is:

```math
((m_1+m_2)l_1)(l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2))-(-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1))(l_1\cos(\theta_1-\theta_2))\\ \ \\

=(l_1)((m_1+m_2)(l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-g\sin(\theta_2))+(m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1))(\cos(\theta_1-\theta_2))) \\ \ \\

=(l_1)((m_1+m_2)l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_2) + m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1)\cos(\theta_1-\theta_2))
```

---

```math
\ddot{\theta}_2=\frac{\cancel{(l_1)}((m_1+m_2)l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_2) + m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1)\cos(\theta_1-\theta_2))}{\cancel{l_1}l_2(m_1+m_2\sin^2(\theta_1-\theta_2)}\\ \ \\

\ddot{\theta}_2=\frac{((m_1+m_2)l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_2) + m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1)\cos(\theta_1-\theta_2))}{l_2(m_1+m_2\sin^2(\theta_1-\theta_2)}
```

The final two expressions are:

```math
\ddot{\theta}_1=\frac{-m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_1)-m_2l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+m_2g\cos(\theta_1-\theta_2)\sin(\theta_2)}{l_1(m_1+m_2\sin^2(\theta_1-\theta_2))}
\\ \ \\ 
\ddot{\theta}_2=\frac{((m_1+m_2)l_1\dot{\theta}_1^2\sin(\theta_1-\theta_2)-(m_1+m_2)g\sin(\theta_2) + m_2l_2\dot{\theta}_2^2\sin(\theta_1-\theta_2)\cos(\theta_1-\theta_2)+(m_1+m_2)g\sin(\theta_1)\cos(\theta_1-\theta_2))}{l_2(m_1+m_2\sin^2(\theta_1-\theta_2))}
```

## Solving the ODEs

From this, we can use ```solve_ivp()``` from ```scipy.integrate``` to numerically solve the ODEs. The function takes in another function that is in the form $`\frac{dy}{dt}=f(t,y)`$, a time span to integrate over, the initial values, an array of times to store the computed solutions, and some tolerances (```rtol/atol```) for the solver.

Using the accelerations computed above, we can create a function that takes in positions and velocity, and returns the derivates of each.

```python
g = 9.81
m_1, m_2 = 10.0, 10.0
l_1, l_2 = 10.0, 10.0

def derivative(t, y):
    #Unpack positions and velocities
    theta_1, omega_1, theta_2, omega_2 = y 

    #Simplify these repeating terms
    s = np.sin(theta_1-theta_2)
    c = np.cos(theta_1-theta_2)

    #Using the formulas above, find the accelerations
    alpha_1 =  (-m_2*l_2*omega_2**2*s - (m_1+m_2)*g*np.sin(theta_1)
                - m_2*l_1*omega_1**2*s*c + m_2*g*c*np.sin(theta_2))/(l_1*(m_1 + m_2*s**2))
    
    alpha_2 =  ((m_1+m_2)*l_1*omega_1**2*s - (m_1+m_2)*g*np.sin(theta_2)
                +m_2*l_2*omega_2**2*s*c+(m_1+m_2)*g*c*np.sin(theta_1))/(l_2*(m_1+m_2*s**2))
    
    return [omega_1, alpha_1, omega_2, alpha_2]
```

Then we can plug this all into ```solve_ivp()``` and parse the results:

```python
t_min = 0
t_max = 20
t_steps = 1000

y0 = [np.radians(100), 0, np.radians(0), 0]
t = np.linspace(t_min,t_max,t_steps)

sol = solve_ivp(derivative, (t_min,t_max), y0, t_eval=t, rtol=1e-10, atol=1e-10)
```

The result comes out as ```sol```, and the positions/velocities can be found at ```sol.y[i]``` $`i\in[0,3]`$. We can also extract the time from ```sol.t```.

From this we can use the position equations from the very beginning to find the positions of each mass.

```python
#Extract angles
theta_1 = sol.y[0]
theta_2 = sol.y[2]

#Calculate coordinates of each mass
x_1 = l_1*np.sin(theta_1)
y_1 = -l_1*np.cos(theta_1)
x_2 = x_1 + l_2*np.sin(theta_2)
y_2 = y_1 - l_2*np.cos(theta_2)
```
From here, you can do whatever is needed, as you have all the positions as a function of time.

