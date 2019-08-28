from dao.avenger_dao import DaoAvenger
from business_object.avenger import Avenger

daoAvenger = DaoAvenger()

if __name__ == "__main__":
    try:
        # création d'Avenger
        avenger = Avenger(name="Tony Stark", alias="Iron Man",
                          power="génie, philanthrope, milliardaire avec une armure high-tec")
        created = daoAvenger.create(avenger)
        print('------------------------------------------------\n')
        print("Avenger créé : ")
        print(created)
        found = daoAvenger.find_all()

        print('\n------------------------------------------------\n')
        print("Avengers enregistrés : ")
        print(found)

    finally:
        # fermeture de la connexion avec la base
        daoAvenger.connection.close()
