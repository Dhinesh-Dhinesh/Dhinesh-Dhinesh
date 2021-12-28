from flask import Flask , redirect ,request, url_for, jsonify , json

app = Flask(__name__)


@app.route('/')

def first():
    return 'Hello'

#------------------------------------------------------
@app.route('/predict')
def access_param():
    elig = request.args.get('elig')

    return redirect(url_for('mlmres', iseligible = elig))

#redirect from predict to mlmres with iseligible as parameter
@app.route('/mlmres/<iseligible>')
def mlmres(iseligible):
    return "Your eligibility is {}".format(iseligible)
#------------------------------------------------------


#json data

@app.route('/returnstuff')
def returnstuff():
    num_list = [1,2,3,4,5]
    num_dict = {'numbers' : num_list, 'name' : 'Numbers'}
    return jsonify({'output' : num_dict})

#------------------------------

@app.route('/rece',methods=['POST'])
def index():
    val = request.json['ai']
    def fact(sss):
        if sss == 1:
            return 1
        else:
            return sss * fact(sss-1)
    x = fact(val)
    return jsonify({"value":x})
   

if __name__ == '__main__':
    app.run(debug=True,port=5000)