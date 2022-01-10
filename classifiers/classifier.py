from flask import Blueprint, render_template, redirect, request, session, url_for
from forms.forms_templates import BRHouseRentDataForm
import joblib

classifier_bp = Blueprint('classifier_bp', __name__, template_folder='templates', static_folder='static', static_url_path='assets')

@classifier_bp.route('/predicting_house_rent_price', methods=['GET', 'POST'])
def predicting_house_rent_price():

    form = BRHouseRentDataForm(request.form)

    if request.method == 'POST' and form.validate():

        results = [result.data for result in form][:-1]
        print(results)

        with open('classifiers/models/city_encoder.pkl', 'rb') as f:
            city_encoder = joblib.load(f)

        with open('classifiers/models/pet_encoder.pkl', 'rb') as f:
            pet_encoder =  joblib.load(f)

        with open('classifiers/models/furniture_encoder.pkl', 'rb') as f:
            furniture_encoder = joblib.load(f)

        with open('classifiers/models/br_house_rent_classifier.pkl', 'rb') as f:
            classifier = joblib.load(f)

        results[0] = city_encoder.transform([results[0]])[0]
        results[6] = pet_encoder.transform([results[6]])[0]
        results[7] = furniture_encoder.transform([results[7]])[0]

        print(results)

        y_pred = classifier.predict([results])
        print(y_pred)

        return render_template('classifiers/house_rent_price_prediction.html', result=f"{y_pred[0]:.2f}")

    return redirect(url_for('general_bp.index'))