from django.db import models
from django.contrib.auth.models import User

offices = [
    ("Harare", "Harare"),
    ("Bulawayo", "Bulawayo"),
    ("Mutare", "Mutare"),
]


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    office = models.CharField(choices=offices, max_length=100, null=True)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    user = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
    is_qrent = models.BinaryField(null=True)
    brand_model = models.CharField(max_length=100, null=True)
    serial_number = models.CharField(max_length=100, unique=True, null=True)
    processor = models.CharField(max_length=100, null=True)
    ram = models.IntegerField(null=True)
    ram_type = models.CharField(max_length=100, null=True)
    max_ram = models.IntegerField()
    storage = models.IntegerField()
    operating_system = models.CharField(max_length=100, null=True)
    antivirus = models.CharField(max_length=100, null=True)
    condition = models.TextField(null=True)

    def __str__(self):
        return f"{self.brand_model}: {self.serial_number}"

