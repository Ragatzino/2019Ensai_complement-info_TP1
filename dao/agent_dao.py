import psycopg2

from business_object.avenger import Avenger
from business_object.shield_agent import ShieldAgent
from dao.abstract_dao import AbstractDao


class AgentDao(AbstractDao):

    def create(self, agent):
        """
        Insère un agent en base, et retourne ce même agent mis à jour de l'id généré par la base
        :param agent:
        :return: l'agent mis à jour de son id en base
        """
        cur = self.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO shield_agents (name, ) VALUES (%s, %s) RETURNING id;",
                (agent.name, agent.security_level))

            agent.id = cur.fetchone()[0]

            for avenger in agent.avengers:
                cur.execute(
                    "INSERT INTO lien_avanger_agent (agentId, avengerId, affinity) VALUES (%s, %s, %s)",
                    (agent.id, avenger[0].id, avenger[1]))

            # la transaction est enregistrée en base
            self.connection.commit()
        except:
            # la transaction est annulée
            self.connection.rollback()
        finally:
            cur.close()

        return agent

    def find_all(self):
        """
        :return: l'intégralité des agent en base
        """
        with self.connection.cursor() as cur:
            cur.execute(
                "select id, name, security_level from shield_agents")
            # on récupère des tuples et les transforme en objects ShieldAgent
            result = [ShieldAgent(id=item[0], name=item[1], security_level=item[2])
                      for item in cur.fetchall()]
            return result

    def fin_all_agent_with_avengers(self):
        with self.connection.cursor() as cur:
            cur.execute(
                "SELECT agent.id, agent.name, agent.security_level, avenger.id, avenger.name, avenger.alias "
                ", avenger.power, lien.affinity "
                "FROM shield_agents agent INNER JOIN lien_avanger_agent lien ON lien.agentId = gent.id "
                "INNER JOIN avengers avenger ON avenger.id = lien.avengerId")

            result = []
            # On défini un agent None utile pour la première itération
            agent = None
            for item in cur.fetchall():

                # on vérifie si l'id de l'agent de la ligne est different de celui de l'agent prédédement créé
                if item[0] != agent.id:
                    # On crée l'agent
                    agent = ShieldAgent(id=item[0], name=item[1], security_level=item[2], avengers=[])
                    result.append(agent)

                # On regarde s'il y a un avenger associé à l'agent
                if item[3]:
                    # On ajoute un avenger à sa liste
                    agent.avengers.append(Avenger(id=item[3], name=item[4], alias=item[5], power=item[6]))

            return result

    def update(self, agent):
        """
        Met à jour un agent spécifique grâce à son id
        :return: None, mais raise error si probleme
        """
        with self.connection.cursor() as cur:
            try:
                cur.execute(
                    "update shield_agents set name=%s, security_level=%s where id=%s",
                    (agent.name, agent.security_level, agent.id))
                self.connection.commit()
            except psycopg2.Error as error:
                self.connection.rollback()
                raise error

    def delete(self, agent):
        """
        Supprime un agent en base
        :return: None, mais raise error si probleme
        """
        with self.connection.cursor() as cur:
            try:
                cur.execute(
                    "delete from shield_agents  where id=%s",
                    (agent.id,))
                self.connection.commit()
            except psycopg2.Error as error:
                self.connection.rollback()
                raise error
