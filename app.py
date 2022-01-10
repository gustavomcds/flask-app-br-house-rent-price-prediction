from flask import Flask
from forms.forms import forms_bp
from general.general import general_bp
from classifiers.classifier import classifier_bp
from analysis.analysis import analysis_bp

app = Flask(__name__)
app.config.from_object('config.DevConfig')

print(__name__)

app.register_blueprint(general_bp, url_prefix='/')
app.register_blueprint(forms_bp, url_prefix='/forms/')
app.register_blueprint(classifier_bp, url_prefix='/classifier')
app.register_blueprint(analysis_bp, url_prefix='/analysis')

if __name__ == '__main__':

    app.run()