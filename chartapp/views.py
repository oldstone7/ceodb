from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Metrics,Finance,SalesFigure, LeadConversionRate, SupplyChain,Inventory,ProductionOutput, Efficiency, OTP
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm, ProductForm, UserForm, CustomUserCreationForm, CustomPasswordChangeForm, FinanceForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.forms import ModelForm
import json
from django.core.mail import send_mail
from django.shortcuts import render
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
from rest_framework import viewsets
from .models import OTP
from .serializers import OTPSerializer
# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FinanceSerializer, MetricsSerializer, LeadConversionRateSerializer, ProductSerializer, SupplyChainSerializer, InventorySerializer, ProductionOutputSerializer, EfficiencySerializer, SalesFigureSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Finance, Metrics, LeadConversionRate, Product
from rest_framework import viewsets
from rest_framework.decorators import api_view

class OTPViewSet(viewsets.ModelViewSet):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer


class LeadConversionRateViewSet(viewsets.ModelViewSet):
    queryset = LeadConversionRate.objects.all()
    serializer_class = LeadConversionRateSerializer


class SupplyChainViewSet(viewsets.ModelViewSet):
    queryset = SupplyChain.objects.all()
    serializer_class = SupplyChainSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ProductionOutputViewSet(viewsets.ModelViewSet):
    queryset = ProductionOutput.objects.all()
    serializer_class = ProductionOutputSerializer


class EfficiencyViewSet(viewsets.ModelViewSet):
    queryset = Efficiency.objects.all()
    serializer_class = EfficiencySerializer


class SalesFigureViewSet(viewsets.ModelViewSet):
    queryset = SalesFigure.objects.all()
    serializer_class = SalesFigureSerializer



def not_authorized(request):
    return render(request, 'not_authorized.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("login")
        else:
            messages.error(request, 'Error occurred during registration')
            return render(request, 'partials/register.html', {'registerform':form})

    context = {'registerform':form}
    return render(request, 'partials/register.html', context=context)



def my_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                return render(request, 'partials/login.html', {'error': 'Invalid password or email'})

            otp, created = OTP.objects.get_or_create(user=user)
            otp.generate_otp()

            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp.otp}',
                'your-email@gmail.com',
                [user.email],
                fail_silently=False,
            )

            request.session['email'] = email
            return redirect('verify_otp')
        except User.DoesNotExist:
            return render(request, 'partials/login.html', {'error': 'Email not found'})

    return render(request, 'partials/login.html')


def verify_otp(request):
    if request.method == 'POST':
        email = request.session.get('email')
        otp_code = request.POST.get('otp')

        try:
            user = User.objects.get(email=email)
            otp = OTP.objects.get(user=user)

            if otp.otp == otp_code and otp.is_valid():
                login(request, user)

                # Redirect based on username logic
                x = user.username[0] if user.username else ''
                if x == 'f':
                    return redirect('finance')
                elif x == 's':
                    return redirect('sales')
                elif x == 'o':
                    return redirect('op')
                elif user.id == 3:
                    return redirect('finance')

                return redirect('login')  # Default redirect if no specific condition is met

            return render(request, 'partials/verify_otp.html', {'error': 'Invalid OTP'})
        except (User.DoesNotExist, OTP.DoesNotExist):
            return redirect('login')

    return render(request, 'partials/verify_otp.html')


def user_logout(request):

    logout(request)

    return redirect("index")


def login_invalid_redirect(request):
    return render(request,"partials/login.html",{'login_invalid':'Username or password is incorrect'}) 

@login_required(login_url="login")
def home(request):

    metric1 = Metrics.objects.get(id = 1)
    metric2 = Metrics.objects.get(id = 2)
    metric3 = Metrics.objects.get(id = 3)
    metric4 = Metrics.objects.get(id = 4)
    

    fin = Finance.objects.all()

    
    
    user = request.user
    show_finance = False
    show_sales = False
    show_operations = False

    if user.username == 'ceoToby':
        show_finance = show_sales = show_operations = True
    elif user.username.startswith('f'):
        show_finance = True
    elif user.username.startswith('s'):
        show_sales = True
    elif user.username.startswith('o'):
        show_operations = True

    context = {
        'show_finance': show_finance,'show_sales': show_sales,'show_operations': show_operations,
        'metric1': metric1, 'metric2': metric2, 'metric3': metric3, 'metric4': metric4
    }

    return render(request, 'partials/home.html',context)


@login_required(login_url="login")
def finance(request):
    user = request.user
    show_finance = False
    show_sales = False
    show_operations = False

    if user.id == 3:
        show_finance = show_sales = show_operations = True
    elif user.username.startswith('f'):
        show_finance = True
    elif user.username.startswith('s'):
        show_sales = True
    elif user.username.startswith('o'):
        show_operations = True
    context = {
        'show_finance': show_finance,'show_sales': show_sales,'show_operations': show_operations
    }    
    return render(request, 'partials/finance.html',context)



@login_required
@api_view(['GET'])
def user_info(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
    }
    return Response(user_data)

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

    def get(self, request, pk=None):
        if pk:
            finance = Finance.objects.get(pk=pk)
            serializer = FinanceSerializer(finance)
        else:
            finance = Finance.objects.all()
            serializer = FinanceSerializer(finance, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Serialize the request data
        serializer = FinanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk:
            finance = Finance.objects.get(pk=pk)
            serializer = FinanceSerializer(finance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "PK not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk:
            finance = Finance.objects.get(pk=pk)
            finance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "PK not provided"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def sales_api(request):
    demand_data = [202, 188, 172, 168, 150, 176, 149, 158, 113, 107]
    forecast_steps = 5  
    months_full = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    num_demand = len(demand_data)

    # Generate month labels (dynamic to fit the actual data + forecast)
    all_months = [months_full[i % 12] for i in range(num_demand + forecast_steps)]

    # Fit the Exponential Smoothing model
    model = ExponentialSmoothing(demand_data, trend="add", seasonal=None)
    fit = model.fit()

    # Forecast the next 5 months
    forecast = fit.forecast(steps=forecast_steps)
    
    combined_data = demand_data + [None] * forecast_steps  
    forecast_only = [None] * len(demand_data) + forecast.tolist()  
    
    # Other data
    sales_data = SalesFigure.objects.all()
    conversion_data = LeadConversionRate.objects.all()
    converted_leads = sum([data.leads_converted for data in conversion_data])
    total_leads = sum([data.leads_generated for data in conversion_data])
    unconverted_leads = total_leads - converted_leads
    products = Product.objects.all()
    product_labels = [prod.category for prod in products]
    product_data = [prod.num_of_products for prod in products]
    months = [f"{sale.month} {sale.year}" for sale in sales_data]
    revenues = [float(sale.total_revenue) for sale in sales_data]
    
    chart_data = {
        'labels': months,
        'datasets': [{
            'label': 'Revenue',
            'backgroundColor': '#42A5F5',
            'borderColor': '#1E88E5',
            'data': revenues,
            'fill': False,
        }]
    }
    
    # Preparing response data
    data = {
        'combined_data': combined_data,
        'forecast_only': forecast_only,
        'months': all_months,
        'chart_data': chart_data,
        'converted_leads': converted_leads,
        'unconverted_leads': unconverted_leads,
        'total_leads': total_leads,
        'product_labels' : product_labels,
        'product_data':product_data
    }
    
    return Response(data, status=status.HTTP_200_OK)



@login_required(login_url="login")
def sales(request):

    user = request.user
    show_finance = show_sales = show_operations = False

    if user.id == 3:
        show_finance = show_sales = show_operations = True
    elif user.username.startswith('f'):
        show_finance = True
    elif user.username.startswith('s'):
        show_sales = True
    elif user.username.startswith('o'):
        show_operations = True
    
    context = {

        'show_finance': show_finance,
        'show_sales': show_sales,
        'show_operations': show_operations

        
    }

    return render(request, 'partials/sales.html', context)


@login_required(login_url="login")

def op(request):
    metric1 = Metrics.objects.get(id=1)
    metric2 = Metrics.objects.get(id=2)
    metric3 = Metrics.objects.get(id=3)
    metric4 = Metrics.objects.get(id=4)

    # Supply Chain Data
    supply_chain_data = SupplyChain.objects.all()
    supply_chain_labels = list(supply_chain_data.values_list('supplier_name', flat=True))
    avg_on_time_delivery_rate = [float(x) for x in supply_chain_data.values_list('on_time_delivery_rate', flat=True)]
    avg_cost_per_unit = [float(x) for x in supply_chain_data.values_list('cost_per_unit', flat=True)]
    avg_delivery_lead_time = [float(x) for x in supply_chain_data.values_list('delivery_lead_time', flat=True)]

    # Inventory Data
    inventory_data = Inventory.objects.all()
    inventory_labels = list(inventory_data.values_list('item_name', flat=True))
    total_stock = [float(x) for x in inventory_data.values_list('current_stock', flat=True)]
    avg_reorder_level = [float(x) for x in inventory_data.values_list('reorder_level', flat=True)]
    avg_stock_turnover_rate = [float(x) for x in inventory_data.values_list('stock_turnover_rate', flat=True)]

    # Production Output Data
    production_output_data = ProductionOutput.objects.all()
    production_output_labels = list(production_output_data.values_list('product_name', flat=True))
    total_units_produced = [float(x) for x in production_output_data.values_list('units_produced', flat=True)]
    avg_production_time = [float(x) for x in production_output_data.values_list('production_time', flat=True)]
    avg_defect_rate = [float(x) for x in production_output_data.values_list('defect_rate', flat=True)]

    # Efficiency Data
    efficiency_data = Efficiency.objects.all()
    efficiency_labels = list(efficiency_data.values_list('department_name', flat=True))
    avg_machine_utilization_rate = [float(x) for x in efficiency_data.values_list('machine_utilization_rate', flat=True)]
    avg_labor_efficiency_rate = [float(x) for x in efficiency_data.values_list('labor_efficiency_rate', flat=True)]
    total_energy_consumption = [float(x) for x in efficiency_data.values_list('energy_consumption', flat=True)]


    user = request.user
    show_finance = show_sales = show_operations = False

    if user.username == 'ceoToby':
        show_finance = show_sales = show_operations = True
    elif user.username.startswith('f'):
        show_finance = True
    elif user.username.startswith('s'):
        show_sales = True
    elif user.username.startswith('o'):
        show_operations = True

    context = {
        'show_finance': show_finance,
        'show_sales': show_sales,
        'show_operations': show_operations,
        'metric1': metric1,
        'metric2': metric2,
        'metric3': metric3,
        'metric4': metric4,
        'supply_chain_labels': json.dumps(supply_chain_labels),
        'avg_on_time_delivery_rate': json.dumps(avg_on_time_delivery_rate),
        'avg_cost_per_unit': json.dumps(avg_cost_per_unit),
        'avg_delivery_lead_time': json.dumps(avg_delivery_lead_time),
        'inventory_labels': json.dumps(inventory_labels),
        'total_stock': json.dumps(total_stock),
        'avg_reorder_level': json.dumps(avg_reorder_level),
        'avg_stock_turnover_rate': json.dumps(avg_stock_turnover_rate),
        'production_output_labels': json.dumps(production_output_labels),
        'total_units_produced': json.dumps(total_units_produced),
        'avg_production_time': json.dumps(avg_production_time),
        'avg_defect_rate': json.dumps(avg_defect_rate),
        'efficiency_labels': json.dumps(efficiency_labels),
        'avg_machine_utilization_rate': json.dumps(avg_machine_utilization_rate),
        'avg_labor_efficiency_rate': json.dumps(avg_labor_efficiency_rate),
        'total_energy_consumption': json.dumps(total_energy_consumption),
    }

    return render(request, 'partials/op.html', context)




def index(request):

    return render(request, 'chartapp/index.html')



@login_required(login_url="login")
def admindash(request):


    fin = Finance.objects.all()

    metric1 = Metrics.objects.get(id = 1)
    metric2 = Metrics.objects.get(id = 2)
    metric3 = Metrics.objects.get(id = 3)
    metric4 = Metrics.objects.get(id = 4)

    prod = Product.objects.all()
    
    

    return render(request, 'partials/admindash.html',{'fin':fin, 'prod':prod, 'metric1': metric1, 'metric2': metric2, 'metric3': metric3, 'metric4': metric4})

@login_required(login_url="login")
def admin_user_list(request):
    users = User.objects.all()
    return render(request, 'admin_panel/user_list.html', {'users': users})



@login_required(login_url="login")
def admin_user_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),
            )
            user.save()
            
            return redirect('admin_user_list')
        else:
            return render(request, 'admin_panel/user_form.html', {'error': 'Passwords do not match', 'title': 'Add New User'})
    return render(request, 'admin_panel/user_form.html', {'title': 'Add New User'})




@login_required(login_url="login")
def admin_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('admin_user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'admin_panel/user_detail.html', {'form': form, 'user': user})

@login_required(login_url="login")
def admin_user_update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('admin_user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'admin_panel/user_detail.html', {'form': form, 'title': 'Edit User'})

@login_required(login_url="login")
def admin_user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('admin_user_list')
    return render(request, 'admin_panel/user_confirm_delete.html', {'user': user})

@login_required(login_url="login")
def admin_user_change_password(request, user_id):
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important to update the session with the new password
            messages.success(request, 'Password changed successfully!')
            return redirect('admin_user_list')
    else:
        form = CustomPasswordChangeForm(user)

    return render(request, 'admin_panel/change_password.html', {'form': form, 'user': user})


@login_required(login_url="login")
def product_list(request):
    products = Product.objects.all()
    return render(request, 'admin_panel/product_list.html', {'products': products})

@login_required(login_url="login")
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'admin_panel/product_form.html', {'form': form, 'title': 'Add Product'})

@login_required(login_url="login")
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_panel/product_form.html', {'form': form, 'title': 'Edit Product', 'product': product})

@login_required(login_url="login")
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_list')
    return render(request, 'admin_panel/product_confirm_delete.html', {'product': product})



@login_required(login_url="login")
def finance_list(request):
    finances = Finance.objects.all()
    return render(request, 'admin_panel/finance_list.html', {'finances': finances})

@login_required(login_url="login")
def finance_create(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Finance record created successfully.')
            return redirect('finance_list')
    else:
        form = FinanceForm()
    return render(request, 'admin_panel/finance_form.html', {'form': form, 'title': 'Add Finance Record'})

@login_required(login_url="login")
def finance_update(request, finance_id):
    finance = get_object_or_404(Finance, id=finance_id)
    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=finance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Finance record updated successfully.')
            return redirect('finance_list')
    else:
        form = FinanceForm(instance=finance)
    return render(request, 'admin_panel/finance_form.html', {'form': form, 'title': 'Edit Finance Record', 'finance': finance})

@login_required(login_url="login")
def finance_delete(request, finance_id):
    finance = get_object_or_404(Finance, id=finance_id)
    if request.method == 'POST':
        finance.delete()
        messages.success(request, 'Finance record deleted successfully.')
        return redirect('finance_list')
    return render(request, 'admin_panel/finance_confirm_delete.html', {'finance': finance})
