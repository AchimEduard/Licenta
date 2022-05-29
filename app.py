from sqlalchemy.orm import declarative_base, sessionmaker, query
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import MetaData, Table, insert, delete
import flask as flk
import flask_cors as cors
import flask_mail

import utils.utils
from Model.Train import Base, engine, TrainDetails, TrainRoutesElev, TrainRoutesStudent, TrainRoutesAdults, TrainRoutesRetiree, LocuriOcupate
from Repository import TrainRepo
from Service import TrainService
from Controller import Controller

Base.metadata.create_all(engine)

repo = TrainRepo.TrainRepo()
service = TrainService.TrainService(repo)
controler = Controller.Controller(service)
app = flk.Flask(__name__)
cors.CORS(app)
app.config['JSON_SORT_KEYS'] = False
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0c707c822e4fe0'
app.config['MAIL_PASSWORD'] = 'afbabd25c97efa'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = flask_mail.Mail(app)


@app.route('/trains', methods=['GET'])
def trains():
    if flk.request.method == "GET":
        print(flk.request.args.get('depart'))
        print(flk.request.args.get('arrival'))
        print(flk.request.args.get('tip'))
        print(flk.request.args.get('date'))
        useable_date = flk.request.args.get('date').split("-")[2] + '-' + flk.request.args.get('date').split("-")[1] + '-' + flk.request.args.get('date').split("-")[0]
        print(useable_date)
        data=controler.get_train_routes(flk.request.args.get('tip'), flk.request.args.get('depart'),
                                   flk.request.args.get('arrival'), useable_date)
        return flk.jsonify(data)

@app.route('/trains_details', methods=['GET','POST', 'OPTIONS'])
def traindetailspage():
    if flk.request.method == "GET":

        train = controler.get_train_details_for_display(flk.request.args.get("tip_calator"), flk.request.args.get("cod"),
                                                flk.request.args.get("depart"), flk.request.args.get("arrival"), flk.request.args.get("date"))

        return flk.jsonify(train)

    else:
        content_type = flk.request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            print(flk.request.data)
            json_values = flk.request.get_json()
            print(json_values)
            comanda_id = utils.utils.create_string()
            if controler.add_loc_ocupat(json_values.get('train_id'), json_values.get('depart'), json_values.get('arrival'),
                                        json_values.get('email'), json_values.get('tip_calator'), comanda_id, json_values.get('date')):

                controler.update_train_details(json_values.get('train_id'), json_values.get('depart'), json_values.get('arrival'))
                msg = flask_mail.Message('Please confirm ', sender='peter@mailtrap.io', recipients=[json_values["email"]])
                msg.body = "Please confirm at the address: https://licensefortheises.azurewebsites.net/confirmation?id=" + comanda_id
                mail.send(msg)
                print("Message sent!")
                return("okay")

        else:

            return 'Content-Type not supported!'

@app.route('/confirmation')
def confirm():
    controler.update_locuri_ocupate(flk.request.args["id"])
    return flk.render_template('test.html')

@app.route('/ping')
def ping():
    return flk.Response("200", status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

