# serializers.py in the app folder (e.g., finance app)
from rest_framework import serializers
from rest_framework import serializers
from .models import OTP, Product, Metrics, LeadConversionRate, Finance, SupplyChain, Inventory, ProductionOutput, Efficiency, SalesFigure

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'  # or specify the fields you want


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'  # This will include all fields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'


class LeadConversionRateSerializer(serializers.ModelSerializer):
    conversion_rate = serializers.SerializerMethodField()  # Adding the custom field

    class Meta:
        model = LeadConversionRate
        fields = ['month', 'year', 'leads_generated', 'leads_converted', 'conversion_rate']  # Include conversion_rate

    # Method to calculate conversion rate
    def get_conversion_rate(self, obj):
        return obj.conversion_rate()  # Call the model's method


class SupplyChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyChain
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ProductionOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionOutput
        fields = '__all__'


class EfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Efficiency
        fields = '__all__'


class SalesFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesFigure
        fields = '__all__'
