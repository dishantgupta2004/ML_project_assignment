from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import joblib
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Define the form class
class PredictionForm(FlaskForm):
    feature1 = StringField('Feature 1', validators=[DataRequired()])
    feature2 = StringField('Feature 2', validators=[DataRequired()])
    submit = SubmitField('Predict')

# Load the ML model
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PredictionForm()
    if form.validate_on_submit():
        feature1 = float(form.feature1.data)
        feature2 = float(form.feature2.data)
        prediction = model.predict(np.array([[feature1, feature2]]))
        flash(f'Prediction: {prediction[0]}')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
