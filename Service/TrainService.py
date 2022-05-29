import Model
from Repository import TrainRepo
from utils import utils

class TrainService():
    def __init__(self, repo: TrainRepo.TrainRepo):
        self.repo = repo

    def get_train_details_for_display(self, tip_calator, train_route_adults: Model.Train.TrainRoutesAdults):

        try:
            row = self.repo.get_train_details(train_route_adults)
            train_details = utils.row_to_dict(row)
            if tip_calator == "Student":
                train_detail = {"Locuri": train_details.get('Locuri'),
                                     "Durata": train_details.get('Durata'),
                                     "Pret": train_details.get("PretStud"),
                                     "Ora": train_details.get("ora"),
                                     "Date": train_details.get("date")}
                print("Student: " + str(train_detail))
                return train_detail

            if tip_calator == "Adult" or tip_calator == "":
                train_detail = {"Locuri": train_details.get('Locuri'),
                                     "Durata": train_details.get('Durata'),
                                     "Pret": train_details.get("Pret"),
                                     "Ora": train_details.get("ora"),
                                     "Date": train_details.get("date")}
                print("Adult: " + str(train_detail))
                return train_detail

            if tip_calator == "Pensionar":
                train_detail = {"Locuri": train_details.get('Locuri'),
                                     "Durata": train_details.get('Durata'),
                                     "Pret": train_details.get("PretPens"),
                                     "Ora": train_details.get("ora"),
                                     "Date": train_details.get("date")}
                print("Pensionar: " + str(train_detail))
                return train_detail

            if tip_calator == "Elev":
                train_detail = {"Locuri": train_details.get('Locuri'),
                                     "Durata": train_details.get('Durata'),
                                     "Pret": train_details.get("PretEl"),
                                     "Ora": train_details.get("ora"),
                                     "Date": train_details.get("date")}
                print("Elev: " + str(train_detail))
                return train_detail
        except:
            return {}

    def get_train_routes_adults(self, depart_station, arrival_station, date):
        try:
            rows = self.repo.get_train_routes_adults().filter(Model.Train.TrainRoutesAdults.arrival_station == arrival_station, Model.Train.TrainRoutesAdults.depart_station == depart_station)
            trains_detail_rows = self.repo.get_train_details_by_stations(depart_station, arrival_station)

            trains = []
            trains_details = []
            final_train_array = []

            for row in rows:
                trains.append(utils.row_to_dict(row))

            for row in trains_detail_rows:
                trains_details.append(utils.row_to_dict(row))


            print("trains: "  + str(trains)  + "\n")
            print("trains_details: " + str(trains_details) + "\n")

            for train in trains:
                for train_details in trains_details:
                    if train.get('train_id') == train_details.get('train_id') and int(train_details.get('Locuri'))>0 \
                            and train.get('date')==date and train.get('date')==train_details.get('date'):
                        train_dict = {"Train Code": train.get('train_id'), "Ora": train.get('ora'), "Cumpara": train.get('cumpara')}
                        final_train_array.append(train_dict)

            return final_train_array

        except Exception as e:
            print(e)
            return []

    def get_train_routes_students(self, depart_station, arrival_station, date):
        try:
            rows = self.repo.get_train_routes_student().filter(
                Model.Train.TrainRoutesStudent.arrival_station == arrival_station,
                Model.Train.TrainRoutesStudent.depart_station == depart_station)
            trains_detail_rows = self.repo.get_train_details_by_stations(depart_station, arrival_station)

            trains = []
            trains_details = []
            final_train_array = []

            for row in rows:
                trains.append(utils.row_to_dict(row))

            for row in trains_detail_rows:
                trains_details.append(utils.row_to_dict(row))

            for train in trains:
                for train_details in trains_details:
                    if train.get('train_id') == train_details.get('train_id') and int(train_details.get('Locuri')) > 0 \
                            and train.get('date')==date and train.get('date')==train_details.get('date'):
                        train_dict = {"Train Code": train.get('train_id'), "Ora": train.get('ora'), "Cumpara": train.get('cumpara')}
                        final_train_array.append(train_dict)

            return final_train_array

        except Exception as e:
            print(e)
            return []

    def get_train_routes_retirees(self, depart_station, arrival_station, date):
        try:
            rows = self.repo.get_train_routes_retirees().filter(
                Model.Train.TrainRoutesRetiree.arrival_station == arrival_station,
                Model.Train.TrainRoutesRetiree.depart_station == depart_station)
            trains_detail_rows = self.repo.get_train_details_by_stations(depart_station, arrival_station)

            trains = []
            trains_details = []
            final_train_array = []

            for row in rows:
                trains.append(utils.row_to_dict(row))

            for row in trains_detail_rows:
                trains_details.append(utils.row_to_dict(row))

            for train in trains:
                for train_details in trains_details:
                    if train.get('train_id') == train_details.get('train_id') and int(train_details.get('Locuri')) > 0 \
                            and train.get('date')==date and train.get('date')==train_details.get('date'):
                        train_dict = {"Train Code": train.get('train_id'), "Ora": train.get('ora'), "Cumpara": train.get('cumpara')}
                        final_train_array.append(train_dict)

            return final_train_array

        except Exception as e:
            print(e)
            return []

    def get_train_routes_elev(self, depart_station, arrival_station, date):
        try:
            rows = self.repo.get_train_routes_elev().filter(
                Model.Train.TrainRoutesElev.arrival_station == arrival_station,
                Model.Train.TrainRoutesElev.depart_station == depart_station)
            trains_detail_rows = self.repo.get_train_details_by_stations(depart_station, arrival_station)

            trains = []
            trains_details = []
            final_train_array = []

            for row in rows:
                trains.append(utils.row_to_dict(row))

            for row in trains_detail_rows:
                trains_details.append(utils.row_to_dict(row))
            print(trains, trains_details, sep=" : ")

            for train in trains:
                for train_details in trains_details:
                    if train.get('train_id') == train_details.get('train_id') and int(train_details.get('Locuri')) > 0 \
                            and train.get('date')==date and train.get('date')==train_details.get('date'):
                        train_dict = {"Train Code": train.get('train_id'), "Ora": train.get('ora'), "Cumpara": train.get('cumpara')}
                        final_train_array.append(train_dict)

            return final_train_array

        except Exception as e:
            print(e)
            return []

    def update_train_details(self, train_details:Model.Train.TrainDetails):
        try:
            self.repo.update_train_details(train_details)
            return True
        except:
            return False

    def update_locuri_ocupate(self, comanda_id):
        try:
            self.repo.update_locuri_ocupate(comanda_id)
            return True
        except:
            return False

    def add_locuri_ocupate(self, locuri_ocupate):
         if(self.repo.add_train_locuri_ocupate(locuri_ocupate)):
            return True
         else:
            return False

