
# Create Class
class MyCar:
    def __init__(self, wheels, engine, color, feul_type, wheels_drive):
        self.wheels = wheels
        self.engine = engine
        self.color = color
        self.feul_type = feul_type
        self.wheels_drive = wheels_drive

# Adding Values
MyCar_wheels = input("How Much Wheels Do You Want On Your Car?: ")
MyCar_engine = input("What Engine Do You Want In Your Car?: ")
MyCar_color = input("What Color Do You Want Your Car To Be? : ")
MyCar_feul_type = input("What Feul Type Do You Want Your Car To Have?: ")
MyCar_wheels_drive = input("What Wheel Drive Do You Want?: ")

# Asemble Values To Car
MyCar = (MyCar_wheels, MyCar_engine, MyCar_color, MyCar_feul_type, MyCar_wheels_drive)

# Printing Status Of Car
print("")
print("Wheels: " + str(MyCar_wheels))
print("")
print("Engine: " + str(MyCar_engine))
print("")
print("Color: " + str(MyCar_color))
print("")
print("Feul_Type: " + str(MyCar_feul_type))
print("")
print("How Many Wheels Drive: " + str(MyCar_wheels_drive))
print("")