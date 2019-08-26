from dao.abstract_dao import AbstractDao
from business_object.avenger import Avenger


class DaoAvenger(AbstractDao):

    def create(self, avenger):
        """
        Insère un avenger en base, et retourne ce même avenger mis à jour de l'id généré par la base
        :param avenger:
        :return: l'avenger mis à jour de son id en base
        """
        cur = self.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO avengers (name, alias, power) VALUES (%s, %s, %s) RETURNING id;",
                (avenger.name, avenger.alias, avenger.power))

            avenger.id = cur.fetchone()[0]
            # la transaction est enregistrée en base
            self.connection.commit()
        except:
            # la transaction est annulée
            self.connection.rollback()
            raise
        finally:
            cur.close()

        return avenger

    def find_all(self):
        """
        :return: l'intégralité des avengers en base
        """
        with self.connection.cursor() as cur:
            cur.execute(
                "select id, name, alias, power from avengers") # A votre avis pourquoi on fait pas select * from avengers ?

            # on récupère des tuples et les transforme en objects Avengers
            result = [Avenger(id=item[0], name=item[2], alias=item[1], power=item[2])
                      for item in cur.fetchall()]
            return result
