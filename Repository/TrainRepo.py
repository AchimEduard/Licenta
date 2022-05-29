from Model.Train import *

class TrainRepo:
    def __init__(self):
        print("RepoInitialized")

    @staticmethod
    def get_train_details(train: TrainRoutesAdults):
        try:
            return session.query(TrainDetails).filter(TrainDetails.train_id == train.train_id,
                                                     TrainDetails.depart_station == train.depart_station,
                                                     TrainDetails.arrival_station == train.arrival_station,
                                                     TrainDetails.date == train.date).first()
        except Exception as e:
            print("error" + str(e))

    @staticmethod
    def get_train_details_by_stations(depart_station, arrival_station):
        try:
            return session.query(TrainDetails).filter(TrainDetails.depart_station == depart_station,
                                                     TrainDetails.arrival_station == arrival_station)
        except Exception as e:
            print("error" + str(e))

    @staticmethod
    def get_train_routes_adults():
        try:
            return session.query(TrainRoutesAdults)
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_train_routes_elev():
        try:
            return session.query(TrainRoutesElev)
        except:
            return False

    @staticmethod
    def get_train_routes_retirees():
        try:
            return session.query(TrainRoutesRetiree)
        except:
            return False

    @staticmethod
    def get_train_routes_student():
        try:
            return session.query(TrainRoutesStudent)
        except:
            return False

    @staticmethod
    def get_train_locuri_ocupate():
        try:
            return session.query(LocuriOcupate)
        except:
            return False

    @staticmethod
    def add_train_details(train_details):
        try:
            session.add(train_details)
            session.commit()
            return True
        except:
            return False

    @staticmethod
    def add_train_routes_adults(train_routes_adults):
        try:
            session.add(train_routes_adults)
            session.commit()
        except:
            return False

    @staticmethod
    def add_train_routes_elev(train_routes_elev):
        try:
            session.add(train_routes_elev)
            session.commit()
        except:
            return False

    @staticmethod
    def add_train_routes_retirees(train_routes_retirees):
        try:
            session.add(train_routes_retirees)
            session.commit()
        except:
            return False

    @staticmethod
    def add_train_routes_student(train_routes_student):
        try:
            session.add(train_routes_student)
            session.commit()
        except:
            return False

    @staticmethod
    def add_train_locuri_ocupate(train_locuri_ocupate):
        try:
            session.add(train_locuri_ocupate)
            session.commit()
            return True
        except:
            return False


    @staticmethod
    def delete_train_details(train_details):
        try:
            delete_train_details = session.query(TrainDetails).filter_by(train_id = train_details.train_id,
                                                  depart_station = train_details.depart_station,
                                                  arrival_station = train_details.arrival_station).first()
            session.delete(delete_train_details)
            session.commit()
            return True

        except:

            return False

    @staticmethod
    def delete_train_routes_adults(train_routes):
        try:
            delete_train_details = session.query(TrainRoutesAdults).filter_by(train_id = train_routes.train_id,
                                                  depart_station = train_routes.depart_station,
                                                  arrival_station = train_routes.arrival_station).first()
            session.delete(delete_train_details)
            session.commit()
            return True

        except:

            return False

    @staticmethod
    def delete_train_routes_elev(train_routes):
        try:
            delete_train_details = session.query(TrainRoutesElev).filter_by(train_id=train_routes.train_id,
                                                                         depart_station=train_routes.depart_station,
                                                                         arrival_station=train_routes.arrival_station).first()
            session.delete(delete_train_details)
            session.commit()
            return True

        except:

            return False

    @staticmethod
    def delete_train_routes_students(train_routes):
        try:
            delete_train_details = session.query(TrainRoutesStudent).filter_by(train_id=train_routes.train_id,
                                                                         depart_station=train_routes.depart_station,
                                                                         arrival_station=train_routes.arrival_station).first()
            session.delete(delete_train_details)
            session.commit()
            return True

        except:

            return False

    @staticmethod
    def delete_train_routes_retirees(train_routes):
        try:
            delete_train_details = session.query(TrainRoutesRetiree).filter_by(train_id=train_routes.train_id,
                                                                         depart_station=train_routes.depart_station,
                                                                         arrival_station=train_routes.arrival_station).first()
            session.delete(delete_train_details)
            session.commit()
            return True

        except:
            return False

    @staticmethod
    def delete_ocupied_seats(train_routes):
        try:
            delete_train_details = session.query(LocuriOcupate).filter_by(train_id=train_routes.train_id,
                                                                         depart_station=train_routes.depart_station,
                                                                         arrival_station=train_routes.arrival_station).first()
            session.delete(delete_train_details)
            session.commit()
            return True

        except:

            return False

    @staticmethod
    def update_train_details(train_details: TrainDetails):
        try:
            update_train_details = session.query(TrainDetails).filter_by(train_id = train_details.train_id,
                                                                     depart_station = train_details.depart_station,
                                                                    arrival_station = train_details.arrival_station).first()

            update_train_details.Locuri = update_train_details.Locuri - 1
            session.commit()

            return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def update_locuri_ocupate(comanda_id):
        try:
            update_locuri_ocupate = session.query(LocuriOcupate).filter_by(comanda_id = comanda_id).first()
            print(update_locuri_ocupate)
            update_locuri_ocupate.confirimata = "Da"
            session.commit()

            return True

        except Exception as e:
            print(e)
            return False
