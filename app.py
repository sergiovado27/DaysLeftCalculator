from datetime import date

# Captura la fecha real de este momento
today = date.today() 
target = date(2027, 4, 14)

days_left = (target - today).days

if days_left > 0:
    print(f"Faltan {days_left} días para el objetivo.")
elif days_left == 0:
    print("¡Es hoy!")
else:
    print(f"El objetivo pasó hace {abs(days_left)} días.")