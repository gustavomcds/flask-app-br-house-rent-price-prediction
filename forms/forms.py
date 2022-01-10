from flask import Blueprint, render_template, request, redirect, url_for, session
from forms.forms_templates import BRHouseRentDataForm

forms_bp = Blueprint('forms_bp', __name__, template_folder='templates', static_folder='static', static_url_path='assets')

@forms_bp.route('/form_br_house_rent_classifier', methods=['GET', 'POST'])
def form_br_house_rent_classifier():

    form = BRHouseRentDataForm(request.form)

    if request.method == 'POST' and form.validate():

        # results = [result for result in form]
        # return render_template('forms/form_br_house_rent.html', results=results)
        # session['results'] = results

        return redirect(url_for('classifier_bp.predicting_house_rent_price'))#, results=results))

    return render_template('forms/form_br_house_rent.html', form=form)