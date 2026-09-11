class planet:
    def __init__(self,name, distanceFromSun, radius):
        self.name=name
        self.distanceFromSun=distanceFromSun
        self.radius=radius
        print("this is the constructor call, the initialized params are", self.name, self.distanceFromSun, self.radius)

    def rotate(self):
        print(f"the {self.name} is rotating at a speed of ", self.radius*self.distanceFromSun)
    def revolve(self):
        print(f"the {self.name} is revolving" )

class dummyPlanet():
    def __init__(self):
        print("this is from the dummy planet consturctor")
    def revolveDum(self):
        print("test")

earth=planet("earth",7000,6400)
mars=planet("mars",7900,5000)
venus=planet("venus",9000,7800)

pluto=dummyPlanet()
pluto.revolveDum()


earth.rotate()
mars.rotate()
venus.revolve()

""" print(earth)
print(mars)
print(venus)"""