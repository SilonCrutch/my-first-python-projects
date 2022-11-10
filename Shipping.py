#Weight
weight = 4.8
premimum_weight = 4.8
drone_weight = 4.8

#Ground shipping
if weight <= 2:
  print((1.50*weight) + 20)
elif weight <= 6:
  print((3.00*weight) + 20)
elif weight <= 10:
  print((4.00*weight) + 20)
else:
  print((4.75*weight) + 20)

#Ground shipping premium
ground_shipping = premimum_weight + 125.00
print(ground_shipping)

#Drone shipping
if drone_weight <= 2:
  print((4.50*drone_weight))
elif drone_weight <= 6:
  print((9.00*drone_weight))
elif drone_weight <= 10:
  print((12.00*drone_weight))
else:
  print((14.25*weight))