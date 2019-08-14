class Avenger:
    """
    Un avenger est un super héros qui fait partie de l'équipe des Avengers. Rien n'empêche un héros
    de faire partie de plusieurs groupes en même temps (cf Spider Man qui est un avenger, et fut un membre des
    4 Fantastiques)
    """

    def __init__(self, name, alias, power, id=0):
        """
        :param name: str, le nom de l'avenger (ex Tony Stark)
        :param alias: str, son nom de super héros (ex Iron Man)
        :param power: str, une description de ses pouvoirs (génie, philanthrope, milliardaire avec une armure high-tech)
        :param id: int, l'id en base, par défaut, 0
        """
        self.id = id
        self.name = name
        self.alias = alias
        self.power = power

    def __str__(self):
        return '%s : %s plus connu sous le nom de %s \n' \
               '\t super pouvoir : %s' % (self.id, self.name, self.alias, self.power)

    def __repr__(self):
        return '(id=%s, name=%s, alias= %s, power=%s)' % (self.id, self.name, self.alias, self.power)
