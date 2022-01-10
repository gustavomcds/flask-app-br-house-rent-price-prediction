from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired
import json

with open('classifiers/assets/choices_dict.json', 'r') as f:
    options = json.load(f)

class BRHouseRentDataForm(FlaskForm):

    city = SelectField('Cidade', choices=options.get('city'))
    area_m2 = IntegerField('Área (m²)')
    rooms = IntegerField('Nº de cômodos')
    bathrooms = IntegerField('Nº de banheiros')
    parking_spaces = IntegerField('Vagas de garagem')
    floors = IntegerField('Andar')
    pet = SelectField('Aceita pet', choices=options.get('animal'))
    furniture = SelectField('Possui mobília', choices=options.get('furniture'))
    hoa_tax = IntegerField('Taxa de condomínio')
    property_tax = IntegerField('IPTU')
    fire_insurance = IntegerField('Seguro de incêndio')