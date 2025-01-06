import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = pd.read_csv('/content/populations_lapins_renards.csv', skiprows=1)
lapin_reel = data.iloc[:,1].tolist() 
renard_reel = data.iloc[:,2].tolist()
time_reel = data.iloc[:,0].tolist()

prediction_lapin = []  
prediction_renard = []

start_time = 0  
time = [start_time + i * step for i in range(len(time_reel))] 

alpha, beta, delta, gama = 4/3, 4/3, 4/3, 4/3
step = 0.001

for _ in range(0, 1000):
  new_value_time = time[-1] + step 
  new_value_lapin = lapin_reel[-1] * (alpha - beta * renard_reel[-1]) * step + lapin_reel[-1]
  new_value_renard = renard_reel[-1] * (delta * lapin_reel[-1] - gama * renard_reel[-1]) * step + renard_reel[-1]
  prediction_lapin.append(new_value_lapin) 
  prediction_renard.append(new_value_renard) 
  time.append(new_value_time)



mse_lapin = mean_squared_error(lapin_reel, prediction_lapin[:len(lapin_reel)])  
mse_renard = mean_squared_error(renard_reel, prediction_renard[:len(renard_reel)]) 

print("MSE pour les lapins :", mse_lapin)
print("MSE pour les renards :", mse_renard)

plt.figure(figsize=(15, 6))
plt.plot(time_reel, lapin_reel, '-b') # Plot the real data with original time 
plt.plot(time_reel, renard_reel, '-r') # Plot the real data with original time
plt.show()
