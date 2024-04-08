from django import forms
from app1.models import contactEnquiry
from .models import CountryGDP,Image
from .models import Person, City

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = contactEnquiry
        fields = ["name","email"]

class PersonForm(forms.ModelForm):
    
    class Meta:
        model =CountryGDP
        fields = '__all__'



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("name", "img")

#cascade dropdown
class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

