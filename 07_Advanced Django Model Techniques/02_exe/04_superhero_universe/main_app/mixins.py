class RechargeEnergyMixin:
    def recharge_energy(self, amount):
        self.energy += amount

        if self.energy > 100:
            self.energy = 100

        self.save()
