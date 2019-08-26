from abc import ABC, abstractmethod

from connection import get_connection


class AbstractDao(ABC):
    """Classe abstraite dont les DAO doivent hériter. Permet de gérer simplement la connection, et d'avoir des noms
    méthodes de base des DAO identique. Permet une meilleure lisibilité du code"""

    connection = get_connection()

    @abstractmethod
    def find_by_id(self, id):
        """Va chercher une élément de la base grâce à son id et retourne l'objet python associé"""

    @abstractmethod
    def find_all(self):
        """Retourne tous les éléments d'une table sous forme de liste d'objets python"""

    @abstractmethod
    def update(self, business_object):
        """Met à jour la ligne en base de donnée associé à l'objet métier en paramètre"""

    @abstractmethod
    def create(self, business_object):
        """Insère une ligne en base avec l'objet en paramètre. Retourne l'objet mise à jour avec son id de la base"""

    @abstractmethod
    def delete(self, business_object):
        """Supprime la ligne en base représentant l'objet en paramètre"""
