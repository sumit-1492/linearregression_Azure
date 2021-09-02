from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

application = Flask(__name__) # initializing a flask app
app = application


@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            pt = float(request.form['pt'])
            rs = float(request.form['rs'])
            trq = float(request.form['trq'])
            tw = float(request.form['tw'])
            is_twf = request.form['twf']
            is_hdf = request.form['hdf']
            is_pwf = request.form['pwf']
            is_osf = request.form['osf']
            is_rnf = request.form['rnf']
            if is_twf == 'yes':
                twf = 1
            else:
                twf = 0
            if is_hdf == 'yes':
                hdf = 1
            else:
                hdf = 0
            if is_pwf == 'yes':
                pwf = 1
            else:
                pwf = 0
            if is_osf == 'yes':
                osf = 1
            else:
                osf = 0
            if is_rnf == 'yes':
                rnf = 1
            else:
                rnf = 0
            filename = 'ai4i2020_final_model.pickle'
            model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            temp = model.predict([[pt, rs, trq, tw, twf, hdf, pwf, osf, rnf]])
            print('Air temperature is', temp)
            # showing the prediction results in a UI
            return render_template('results.html',temp=temp[0])

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


@app.route('/report',methods=['GET','post'])  # route to display the profile report page
@cross_origin()
def pr():
    if request.method == 'POST':
        try:
            is_pf = request.form['pr']
            if is_pf == 'yes':
                return render_template("ai4i2020_profile_report.html")
            else:
                return render_template('index.html')
        except Exception as e:
            print(e)
            return 'no'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)  # running the app


