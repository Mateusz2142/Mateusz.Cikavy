'''
Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakładamy że:
-liczba mrugnięć na minute to 20
-liczba minut w godzinie to 20
-liczba godzin w dobie 24
-licza lat (czyli nasz X) 50
Uwaga: jeżeli przyjhąc że spimu 8 godzin to liczba godzin na dobe powinnna wynosić 16
'''
#liczba mrugnięć okiem na minute

blinksPerMin = 20

#liczba minut na godzine i liczba godzin w dobie

minInHour = 60
hoursInDay = 16
daysInYear = 365
years = 50

# liczba mrugnięć w ciągu X lat
 #result
print(blinksPerMin * minInHour * hoursInDay * daysInYear * years)
