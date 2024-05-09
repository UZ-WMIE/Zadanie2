# Wygenerowanie próby losowej z rozkładem normalnym (dowolnie wybrane mi odraz sigma kwadrat).
import numpy as np

# parametry rozkładu
mi = 2
sigma_kwadrat = 4
# liczba wykonanych prób
n = 1000

X = np.random.normal(mi, np.sqrt(sigma_kwadrat), n)
# print(X)

# Zbudowanie przedziału ufności

# Dane
mean_X = np.mean(X)  # Średnia próbki
std_X = np.std(X, ddof=1)  # Odchylenie standardowe próbki
size_X = len(X)  # Rozmiar próbki

# Poziom ufności (załkładam 95%)
poziom_ufnosci = 0.95

# błąd standardowy
blad_standardowy = std_X / np.sqrt(n)

# Obliczanie przedziału ufności
L = mean_X - (blad_standardowy * n*poziom_ufnosci)  # górna granica
U = mean_X + (blad_standardowy * n*poziom_ufnosci)  # dolna granica

# Sprawdzenie czy mi należy do przedziału ufności
N = 1000
Y = np.zeros(N, dtype=bool)  # N to liczba przedziałów ufności

# Sprawdzamy dla każdego przedziału ufności, czy wartość średniej należy do przedziału ( wykonanie N razy).
for i in range(N):
    if U[i] <= mi <= L[i]:
        Y[i] = "TAK"
    else:
        Y[i] = "NIE"

print(Y)

# Z danych z wektora Y oszacować prawdzopodobieństwo występowania Tak (jeśli prawdziwe prawdoppodobieństwo = 1-alfa)
# przedtswić to oszacowanie i rozkład wektora na histogramie
