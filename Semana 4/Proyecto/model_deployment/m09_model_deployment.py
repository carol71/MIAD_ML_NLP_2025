#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os

def predict(duration_ms, energy):

    reg = joblib.load(os.path.dirname(__file__) + '/popularity_reg.pkl') 

    x_ = pd.DataFrame([[duration_ms, energy]], columns=[['duration_ms', 'energy']])
  
    # Make prediction
    p1 = reg.predict(x_)[0]

    return p1


if __name__ == "__main__":
    #Número de argumentos que va a recibir el modelo
    if len(sys.argv) < 3:
        print('Por favor agregue la duración de la canción en milisegundos y la energía que le transmite (0 a 1)')
        
    else:

        duration_ms = int(sys.argv[1])
        energy= float(sys.argv[2])

        p1 = predict(duration_ms, energy)
        
        print(f'Duración de la canción (ms): {duration_ms}')
        print(f'Energía: {energy}')
        print('Probability of Phishing: ', p1)
        