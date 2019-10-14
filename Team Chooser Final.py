#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Este programa es un Team Chooser')
print('')

input_nombres=input('Ingresa los nombres de cada participante separándolos con coma: ')
jugadores=input_nombres.split(',')

print('')
print('Los jugadores son:')
print('')
print(*jugadores,sep=', ')
print('')

print('¿Cómo se van a llamar los equipos?')
equipo1=input('Introduce el nombre del equipo 1: ')
print('')
equipo2=input('Introduce el nombre del equipo 2: ')
print('')

import random

equipo_alfa=[]
equipo_beta=[]

while len(jugadores)>0:
    jugador_alfa = random.choice(jugadores)
    equipo_alfa.append(jugador_alfa)
    jugadores.remove(jugador_alfa)
    
    if jugadores==[]:
        break
        
    jugador_beta = random.choice(jugadores)
    equipo_beta.append(jugador_beta)
    jugadores.remove(jugador_beta)

import time

print("\u001b[1;30m Los siguientes miembros pertenecen al equipo \n",equipo1)
print('')
for participante in range (len(equipo_alfa)):
    print("\033[36m\n",equipo_alfa [participante])
    time.sleep(1.5)
    
print('')    
print('')
print("\033[1;30m Los siguientes miembros pertenecen al equipo \n",equipo2)
print('')
for participante in range (len(equipo_beta)):
    print("\033[36m\n",equipo_beta [participante])
    time.sleep(1.5)


# Referencias
# 
# https://trinket.io/python/a699c44ce6
# 
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
# 
# https://www.geeksforgeeks.org/python-numbers-choice-function/
# 
# https://www.youtube.com/watch?v=cij9SM3YWFc&t=736s
# 
# https://bytes.com/topic/python/answers/662658-moving-items-list-list
# 
# https://www.tutorialspoint.com/python3/number_choice.htm
#     
# 

# In[ ]:




