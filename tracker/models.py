from PIL import Image
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

offices = [
    ("Harare", "Harare"),
    ("Bulawayo", "Bulawayo"),
    ("Mutare", "Mutare"),
]

condition_levels = [
    ("Good", "Good"),
    ("Functional (with issues)", "Functional (with issues)"),
    ("Non-Functional", "Non-Functional")
]


def default_condition():
    return condition_levels[0][0]


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    office = models.CharField(choices=offices, max_length=100, null=True)
    isManager = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    user = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
    is_qrent = models.BooleanField(default=False)
    brand_model = models.CharField(max_length=100, null=True)
    serial_number = models.CharField(max_length=100, unique=True, null=True)
    processor = models.CharField(max_length=100, null=True)
    ram = models.IntegerField(null=True)
    ram_type = models.CharField(max_length=100, null=True)
    max_ram = models.IntegerField()
    storage = models.IntegerField()
    operating_system = models.CharField(max_length=100, null=True)
    antivirus = models.CharField(max_length=100, null=True)
    condition = models.CharField(blank=True, max_length=100, choices=condition_levels,
                                 default=default_condition())

    def __str__(self):
        return f"{self.brand_model}: {self.serial_number}"


class Supplier(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    contact_person = models.CharField(max_length=100, null=True)


class Issues(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    resolution_date = models.DateField(null=True)
    description = models.TextField(null=True)
    sent_to = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=True, max_length=500, upload_to=f'Issues/Images', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jfif', 'exif', 'gif', 'tiff', 'bmp'])])
