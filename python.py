# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

# Subclass
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model}.")

    def specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Storage: {self.storage}GB")

phone = Smartphone("Samsung", "Galaxy S23", "Android", 128)
phone.power_on()
phone.install_app("WhatsApp")
phone.specs()
