from flask import Flask, render_template
import pandas as pd
import random 
from faker import Faker

fake = Faker()

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/random')
def randomnumber():
    number_var = random.randint(1, 10000)
    fake_address = fake.address()
    return render_template('random.html', single_number=number_var, single_address =fake_address)

df = pd.read_csv('https://raw.githubusercontent.com/amnasyed1/datasci_1_loading/main/data/newborn-screening-disorders-californiaraceethnicity-2009-2019_final.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
