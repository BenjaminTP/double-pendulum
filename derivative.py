import numpy as np

g = 9.81
m_1, m_2 = 10.0, 10.0
l_1, l_2 = 10.0, 10.0

def derivative(t, y):
    theta_1, omega_1, theta_2, omega_2 = y
    s = np.sin(theta_1-theta_2)
    c = np.cos(theta_1-theta_2)
    
    alpha_1 =  (-m_2*l_2*omega_2**2*s - (m_1+m_2)*g*np.sin(theta_1)
                - m_2*l_1*omega_1**2*s*c + m_2*g*c*np.sin(theta_2))/(l_1*(m_1 + m_2*s**2))
    
    alpha_2 =  ((m_1+m_2)*l_1*omega_1**2*s - (m_1+m_2)*g*np.sin(theta_2)
                +m_2*l_2*omega_2**2*s*c+(m_1+m_2)*g*c*np.sin(theta_1))/(l_2*(m_1+m_2*s**2))
    
    return [omega_1, alpha_1, omega_2, alpha_2]