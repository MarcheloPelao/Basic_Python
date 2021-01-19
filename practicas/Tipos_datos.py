# área del circulo pi*r^2
pi=3.1415
radio=4
area=pi*radio**2
print(type(radio))
print(type(area))
print(isinstance(area,float))
print('area del circulo de radio',radio , 'es :')
print(area)
print(round(area))

print('Area de ciirculo  de radio ' + str(radio) +' = '+ str(area))

radio_str='5'
area=pi*int(radio_str)**2
print('area del circulo de radio',int(radio_str ), 'es :')
print(round(area,2))

