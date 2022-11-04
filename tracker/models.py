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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    office = models.CharField(choices=offices, max_length=100, null=True)
    isManager = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


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
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    contact_person = models.CharField(max_length=100, blank=True)

    @classmethod
    def get_supplier_choice_list(cls):
        flat_list = cls.objects.all().values_list('name', flat=True)
        choice_list = []

        for value in flat_list:
            choice_list.append((value, value))

        return choice_list

    def __str__(self):
        return self.name


class Issue(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    resolution_date = models.DateField(blank=True, null=True)
    description = models.TextField(null=True)
    sent_to = models.CharField(max_length=100, choices=Supplier.get_supplier_choice_list(), blank=True)
    image = models.ImageField(blank=True, max_length=500, upload_to=f'Issues/Images', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jfif', 'exif', 'gif', 'tiff', 'bmp'])])

    def __str__(self):
        return f"{self.title} [SN: {self.laptop.serial_number} Created: {self.create_date}]"
