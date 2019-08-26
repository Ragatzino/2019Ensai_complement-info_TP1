class ShieldAgent:
    """
    Objet représentant un agent du shield.
    id (int) : l'id de l'agent en base
    nom (str) : le nom de l'agent
    security_level (int) : le niveau de sécurité de l'agent
    """

    def __init__(self, id, name, security_level, avengers=[]):
        """
        Constructeur avec tous les arguments
        :param id:
        :param name:
        :param security_level:
        :param avengers : liste de couple avenger/affinité de l'agent
        """
        self.id = id
        self.nom = name
        self.security_level = security_level
        self.avengers = avengers
