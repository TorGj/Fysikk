from pylab import *

# Informasjon om konstanter, konstante krefter og gjenstanden
m = 0.046     # massen av gjenstanden, kg
g = 9.81        # tyngdeakselerasjon, m/s^2
k = 0.000044    # luftmotstandstall, kg/m
G = m*g         # gravitasjonskraft, N

v_t = round((m*g/k)**0.5,3)


def a(v): # akselerasjonen er en funksjon av farten
  L = k*v**2     # luftmotstand, N
  sum_F = G - L  # kraftsum, N
  aks = sum_F/m  # akselerasjon, m/s^2
  return aks

# Startverdier for bevegelsen
s = 0  # startposisjon, m
v = 0  # startfart, m/s
t = 0  # starttid, s

# Simuleringsteknisk
#s_slutt = 500    # sluttposisjon for simulering, m
dt = 0.1       # lengde på tidssteg, s

s_verdier = [s]  # liste for lagring av posisjon
v_verdier = [v]  # liste for lagring av fart
t_verdier = [t]  # liste for lagring av tid

# Løkke som beregner ny fart, posisjon og tid
while v<v_t:  # 
  v = v + a(v)*dt   # regner ut ny v og overskriver gammel
  s = s + v*dt      # regner ut ny s og overskriver gammel
  t = t + dt        # regner ut ny t og overskriver gammel
  
  t_verdier.append(t)  # legger til ny t-verdi i listen for t
  v_verdier.append(v)  # legger til ny v-verdi i listen for v
  s_verdier.append(s)  # legger til ny s-verdi i listen for s

# Tegning av graf
print("Totalstrekning:", s, "m")
print("Sluttid:", t, "s")

plot(t_verdier, s_verdier)              # lager grafen
#plot(v_verdier, s_verdier) 
title("Strekning som funksjon av tid")  # tittel på grafen
xlabel("$t$ / s")                       # x-akse-tittel
ylabel("$s$ / m")                       # y-akse-tittel
grid()
show()                                  # viser grafen


