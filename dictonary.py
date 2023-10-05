car = {
"brand": "Ford",
"model": "Mustang",
"year": 2023
}
print("my car details==",car)
car.update({
  "colour":["white","black","red","yellow"],
  "top speed":140,
})
print("the updated car details are==",car)
x = car.keys()
print(x)
y = car.values()
print(y)

z=car.items()
print("the items in car are==",z)
