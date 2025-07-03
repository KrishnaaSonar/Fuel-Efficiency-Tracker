from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    distance = float(request.form['distance'])
    fuel = float(request.form['fuel'])
    price = float(request.form['price'])

    if fuel > 0 and distance > 0:
        efficiency = round(distance/fuel,2)           #km/L
        consumption = round((fuel/distance)*100,2)    #L fuel for 100km
        cost_per_km = round((fuel * price) / distance, 2)

    else:
        efficiency = consumption = cost_per_km = "Invalid input"
    
    return render_template(
        'result.html',
        efficiency = efficiency,
        consumption = consumption,
        cost_per_km = cost_per_km
    )

if __name__ == '__main__':
    app.run(debug = True)