from django import forms
from .models import OrderItem, ColourVariation, Product, SizeVariation, Address
from django.contrib.auth import get_user_model

User = get_user_model()


class AddToCartForm(forms.ModelForm):
    colour = forms.ModelChoiceField(queryset = ColourVariation.objects.none())
    size = forms.ModelChoiceField(queryset = SizeVariation.objects.none())
    class Meta:
        model = OrderItem
        fields = ['quantity', 'colour', 'size']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id = product_id)
        super().__init__(*args, **kwargs)

        self.fields['colour'].queryset = product.available_colour.all()
        self.fields['size'].queryset = product.available_sizes.all()


class AddressForm(forms.Form):
    Direccion_linea_1 = forms.CharField()
    Direccion_linea_2 = forms.CharField()
    Codigo_Postal = forms.CharField()
    Estado = forms.CharField()
    Ciudad = forms.CharField()

    Facturacion_Direccion_linea_1 = forms.CharField()
    Facturacion_Direccion_linea_2 = forms.CharField()
    Facturacion_Codigo_Postal = forms.CharField()
    Facturacion_Estado = forms.CharField()
    Facturacion_Ciudad = forms.CharField()

    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required = False
    )
    selected_billing_address = forms.ModelChoiceField(
        Address.objects.none(), required = False
    )


    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user = User.objects.get(id = user_id)

        shipping_address_qs = Address.objects.filter(
            user = user,
            address_type = 'S'
        )

        billing_address_qs = Address.objects.filter(
            user = user,
            address_type = 'S'
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_qs
        self.fields['selected_billing_address'].queryset = billing_address_qs

        def clean(self):
            data = self.cleaned_data

            selected_shipping_address = data.get('selected_shipping_address', None)
            if selected_shipping_address is None:
                if not data.get('Direccion_linea_1', None):
                    self.add_error("Direccion_linea_1", "Por favor, rellena este campo")
                if not data.get('Direccion_linea_2', None):
                    self.add_error("Direccion_linea_2", "Por favor, rellena este campo")
                if not data.get('Codigo_Postal', None):
                    self.add_error("Codigo_Postal", "Por favor, rellena este campo")
                if not data.get('Estado', None):
                    self.add_error("Estado", "Por favor, rellena este campo")
                if not data.get('Ciudad', None):
                    self.add_error("Ciudad", "Por favor, rellena este campo")

            selected_billing_address = data.get('selected_billing_address', None)
            if selected_billing_address is None:
                if not data.get('Facturacion_Direccion_linea_1', None):
                    self.add_error("Facturacion_Direccion_linea_1", "Por favor, rellena este campo")
                if not data.get('Facturacion_Direccion_linea_2', None):
                    self.add_error("Facturacion_Direccion_linea_2", "Por favor, rellena este campo")
                if not data.get('Facturacion_Codigo_Postal', None):
                    self.add_error("Facturacion_Codigo_Postal", "Por favor, rellena este campo")
                if not data.get('Facturacion_Estado', None):
                    self.add_error("Facturacion_Estado", "Por favor, rellena este campo")
                if not data.get('Facturacion_Ciudad', None):
                    self.add_error("Facturacion_Ciudad", "Por favor, rellena este campo")
