class PaysLips :
    def __init__(self, name, amount, payment) -> None:
        self.name=name
        self.amount = amount
        self.payment=payment

        def pay(self):
            self.payment = "yes"

        def status(self):
            if self.payment == "yes":
                return self.name + " has been paid " + str(self.amount)
            else:
                return self.name + " has not been paid yet"



nathan = PaysLips("Nathan", 5000, "no")
roger = PaysLips("Roger", 7000, "yes")
nathan.status()
print(nathan.name, nathan.amount, nathan.payment, nathan.status())
print(roger.name, roger.amount, roger.payment)