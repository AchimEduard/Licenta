import Model
import Service
class Controller:
    def __init__(self, service: Service.TrainService.TrainService):
        self.service = service

    def get_train_details_for_display(self, tip_calator, train_id, depart_station, arrival_station, date):
        train_details = Model.Train.TrainDetails(train_id = train_id, depart_station = depart_station, arrival_station = arrival_station, date = date)
        return self.service.get_train_details_for_display(tip_calator, train_details)

    def get_train_routes(self, tip_calator, depart_station, arrival_station, date):
        if tip_calator == "Student":
            return self.service.get_train_routes_students(depart_station, arrival_station, date)
        if tip_calator == "Adult":
            return self.service.get_train_routes_adults(depart_station, arrival_station, date)
        if tip_calator == "Pensionar":
            return self.service.get_train_routes_retirees(depart_station, arrival_station, date)
        if tip_calator == "Elev":
            return self.service.get_train_routes_elev(depart_station, arrival_station, date)

    def update_locuri_ocupate(self, comanda_id):
        if self.service.update_locuri_ocupate(comanda_id):
            return True
        else:
            return False

    def update_train_details(self, train_id, depart_station, arrival_station):
        train_details = Model.Train.TrainDetails(train_id=train_id, depart_station=depart_station,
                                                 arrival_station=arrival_station)
        if self.service.update_train_details(train_details):
            return True
        else:
            return False

    def add_loc_ocupat(self, train_id, depart_station, arrival_station, email, tip_calator, comanda_id, date ):
        loc_ocupat = Model.Train.LocuriOcupate(train_id=train_id, depart_station=depart_station,
                                               arrival_station=arrival_station,email=email, tip_calator=tip_calator,
                                               comanda_id=comanda_id, confirimata="Nu", date = date)
        if self.service.add_locuri_ocupate(loc_ocupat):
            return True
        else:
            return False
