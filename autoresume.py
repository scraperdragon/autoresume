class AutoResume(object):
    def __init__(self, name='page'):
        self.name = name
        self.backend = ScraperwikiBackend()

    def save_state(self, value):
        self.backend.save(self.name, value)

    def reset(self):
        self.backend.save(self.name, None)

    @property
    def state(self):
        return self.backend.state(self.name)


class ScraperwikiBackend(object):
    def save(self, name, value):
        import scraperwiki
        if value is None:
            # TODO fix in dumptruck
            scraperwiki.sql.execute("delete from swvariables where name=?", name)
            scraperwiki.sql.commit()
        else:
            scraperwiki.sql.save_var(name, value)

    def state(self, name):
        import scraperwiki
        return scraperwiki.sql.get_var(name)
