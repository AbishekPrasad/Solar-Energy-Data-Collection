from solar_data import solarEnergy
from data_clean import dataClean

solar_flux = "https://mosdac.gov.in/apienergy/solar?lat=16.088&lon=79.805"
wind_speed = "https://mosdac.gov.in/apienergy/wind?lat=16.088&lon=79.805"

dataset = solarEnergy(solar_flux, wind_speed)
fullSolarData ,todaySolarData = dataClean(dataset)

fullSolarData.to_csv('full_solar_dataset.csv', index=False, header=False, mode='a')
todaySolarData.to_csv('today_solar_dataset.csv', index=False, header=False, mode='a')

print('Uploaded data sucessully!')