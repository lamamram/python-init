# %%
# CamelCase
# type custom
class Voiture:
    brand = None
    nb_roues = 4
    vitesse_max = 200

    def __init__(self, brand) -> None:
        self.brand = brand

    def __str__(self):
        return f"bagnole de brand: {self.brand} etc..."
        
    def max_energy(self):
        return 0.5 * self.vitesse_max ** 2

        
    
    def get_nb_roues(self):
        return self.nb_roues


testarossa = Voiture("ferrari")

# testarossa.set_brand("ferrari")

print(testarossa.brand)
print(testarossa.get_nb_roues())
print(testarossa.max_energy())

type(testarossa)

print(testarossa)
# %%
