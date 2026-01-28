import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Observed data
A = np.array([36, 34, 14, 16])  
somme = np.sum(A) 
print("La somme est:", somme)


donne_theorique = somme / 4  
print("Donne_theorique =", donne_theorique)

# Calculate Chi-square statistic

KHI2 = np.sum((A - donne_theorique)**2 / donne_theorique)
print("KHI2 =", KHI2)


degree_liberte = len(A) - 1  # Degrees of freedom
x_theorique = chi2.ppf(0.95, degree_liberte)  # Critical value for alpha = 0.05
print("On a ddl =", degree_liberte, "et la valeur théorique est:", x_theorique)

# Decision based on Chi-square test
if KHI2 > x_theorique:
    print("Hypothèse nulle rejetée, donc il existe un lien entre les facteurs et le choix.")
else:
    print("Hypothèse nulle acceptée, donc il n'existe pas de lien entre les facteurs et le choix.")

# Plotting the Chi-square distribution
x = np.linspace(0, 16, 500)  # Range for Chi-square distribution
y = chi2.pdf(x, degree_liberte)
#  probability density function for 3 degrees of freedom

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Chi-square Distribution", color="blue")
plt.axvline(x=x_theorique, color="red", linestyle="--", label="Critical Value (7.815)")
plt.xlabel("Observation")
plt.ylabel("Probability Density")
plt.title("Graphique de Khi-deux", color="black", fontweight="bold", fontsize=11)
plt.legend()
plt.grid(True)
plt.show()
