from django.db import models
from django.contrib.auth.models import User
import random



class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def is_valid(self):
        # Optionally, you could add expiration logic here.
        return True  # Add expiration time logic if needed.



class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.num_of_products}'
    

class Metrics(models.Model):
    heading = models.CharField(max_length=15)
    data = models.IntegerField()
    percentage = models.IntegerField()  

    def __str__(self):
        return f'{self.heading} - {self.data} - {self.percentage}'


class Finance(models.Model):
    Client = models.CharField(max_length=100 ,blank=True)
    order = models.CharField(max_length=40, null=True ,blank=True)
    cash = models.IntegerField(null=True , blank=True)
    amount = models.IntegerField(null=True)
    liquid = models.IntegerField(null=True , blank=True)
    asset =  models.IntegerField(null=True , blank=True)
    liab = models.IntegerField(null=True , blank=True)
    date = models.DateField(null=True)  


class LeadConversionRate(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    leads_generated = models.IntegerField()
    leads_converted = models.IntegerField()

    def conversion_rate(self):
        return (self.leads_converted / self.leads_generated) * 100 if self.leads_generated > 0 else 0

    def __str__(self):
        return f"{self.month} {self.year} - {self.conversion_rate()}%"


class SupplyChain(models.Model):
    supplier_name = models.CharField(max_length=100)
    on_time_delivery_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_lead_time = models.IntegerField()  # In days
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.supplier_name


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    current_stock = models.IntegerField()
    reorder_level = models.IntegerField()
    stock_turnover_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Times per year
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class ProductionOutput(models.Model):
    product_name = models.CharField(max_length=100)
    units_produced = models.IntegerField()
    production_time = models.DecimalField(max_digits=5, decimal_places=2)  # Hours
    defect_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Efficiency(models.Model):
    department_name = models.CharField(max_length=100)
    machine_utilization_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage
    labor_efficiency_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage
    energy_consumption = models.DecimalField(max_digits=10, decimal_places=2)  # kWh
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name


class SalesFigure(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    total_transactions = models.IntegerField()

    def __str__(self):
        return f"{self.month} {self.year} - ${self.total_revenue}"






    

