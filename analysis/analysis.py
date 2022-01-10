from flask import Blueprint, render_template
import pandas as pd

analysis_bp = Blueprint('analysis_bp', __name__, template_folder='templates', static_folder='static', static_url_path='assets')

@analysis_bp.route('/dataset_analysis', methods=['GET', 'POST'])
def dataset_analysis():

    df = pd.read_csv('classifiers/assets/houses_to_rent_v2.csv')

    results = df.sample(10)

    return render_template('analysis/dataset_analysis.html', table = results.to_html(classes='data table', index=False, header='true'))

@analysis_bp.route('/rent_vs_hoa', methods=['GET', 'POST'])
def rent_vs_hoa():

    df = pd.read_csv('classifiers/assets/houses_to_rent_v2.csv')

    hoa = df['hoa (R$)'].to_list()
    rent = df['rent amount (R$)'].to_list()

    return render_template('analysis/rent_vs_hoa.html', hoa=hoa, rent=rent)

@analysis_bp.route('/rent_vs_area', methods=['GET', 'POST'])
def rent_vs_area():

    df = pd.read_csv('classifiers/assets/houses_to_rent_v2.csv')

    area = df['area'].to_list()
    rent = df['rent amount (R$)'].to_list()

    return render_template('analysis/rent_vs_area.html', area=area, rent=rent)

@analysis_bp.route('/rent_vs_property_tax', methods=['GET', 'POST'])
def rent_vs_property_tax():

    df = pd.read_csv('classifiers/assets/houses_to_rent_v2.csv')

    property_tax = df['property tax (R$)'].to_list()
    rent = df['rent amount (R$)'].to_list()

    return render_template('analysis/rent_vs_property_tax.html', property_tax=property_tax, rent=rent)

@analysis_bp.route('/rent_vs_fire_insurance', methods=['GET', 'POST'])
def rent_vs_fire_insurance():

    df = pd.read_csv('classifiers/assets/houses_to_rent_v2.csv')

    fire_insurance = df['fire insurance (R$)'].to_list()
    rent = df['rent amount (R$)'].to_list()

    return render_template('analysis/rent_vs_fire_insurance.html', fire_insurance=fire_insurance, rent=rent)