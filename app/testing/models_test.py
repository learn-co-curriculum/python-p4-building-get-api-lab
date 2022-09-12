from datetime import date

from app import app
from models import db, Animal, Zookeeper, Enclosure

class TestAnimal:
    '''Animal model in models.py'''

    with app.app_context():
        a = Animal.query.filter(Animal.name == "Fluffy")
        for fluffy in a:
            db.session.delete(fluffy)
        db.session.commit()

    def test_can_instantiate(self):
        '''can be instantiated with a name and species.'''
        a = Animal(name="Fluffy", species="Lion")
        assert(a)

    def test_can_save_to_db(self):
        '''can be saved to the database.'''
        with app.app_context():
            a = Animal(name="Fluffy", species="Lion")
            db.session.add(a)
            db.session.commit()

    def test_can_be_retrieved_from_db(self):
        '''can be retrieved from the database by name.'''
        with app.app_context():
            a = Animal.query.filter(Animal.name == "Fluffy").first()
            assert(a.name == "Fluffy")
    
class TestZookeeper:
    '''Zookeeper model in models.py'''

    with app.app_context():
        zk = Zookeeper.query.filter(Zookeeper.name == "Bob Barker")
        for bb in zk:
            db.session.delete(bb)
        db.session.commit()

    def test_can_instantiate(self):
        '''can be instantiated with a name and birthday.'''
        zk = Zookeeper(name="Bob Barker", birthday=date(1923, 12, 12))
        assert(zk)

    def test_can_save_to_db(self):
        '''can be saved to the database.'''
        with app.app_context():
            zk = Zookeeper(name="Bob Barker", birthday=date(1923, 12, 12))
            db.session.add(zk)
            db.session.commit()

    def test_can_be_retrieved_from_db(self):
        '''can be retrieved from the database by name.'''
        with app.app_context():
            zk = Zookeeper.query.filter(Zookeeper.name == "Bob Barker").first()
            assert(zk.name == "Bob Barker")

class TestEnclosure:
    '''Enclosure model in models.py'''

    with app.app_context():
        e = Enclosure.query.filter(Enclosure.environment == "Tundra")
        for tundra in e:
            db.session.delete(tundra)
        db.session.commit()

    def test_can_instantiate(self):
        '''can be instantiated with an environment and whether it is open to visitors or not.'''
        e = Enclosure(environment="Tundra", open_to_visitors=True)
        assert(e)

    def test_can_save_to_db(self):
        '''can be saved to the database.'''
        with app.app_context():
            e = Enclosure(environment="Tundra", open_to_visitors=True)
            db.session.add(e)
            db.session.commit()

    def test_can_be_retrieved_from_db(self):
        '''can be retrieved from the database by name.'''
        with app.app_context():
            e = Enclosure.query.filter(Enclosure.environment == "Tundra").first()
            assert(e.environment == "Tundra")
