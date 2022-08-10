from flask import Flask, render_template, request
import getdata
import model

application = Flask(__name__)


@application.route('/', methods= ['POST','GET'])

def homePage():
    return render_template("index.html")

@application.route('/predict', methods= ['POST'])

def prediction():
    try:
        if (request.method == 'POST'):
            data = getdata.getdata()
            pred = model.prediction_(data)


            print('prediction is',pred.predic)
            if pred.predic==0:
                pred.predic="The Person will pay the credit card bill"
            else:
                pred.predic="The person will defualt"

            return render_template('results.html',prediction=pred.predic)

        else:

            return render_template('index.html')
    except Exception as e:
        return render_template('results.html',prediction=e)


if __name__ == "__main__":
    application.run(port=200, debug=True)









