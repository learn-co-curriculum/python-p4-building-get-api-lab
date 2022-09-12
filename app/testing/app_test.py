from os import environ
import re

from app import app

class TestApp:
    '''Flask application in flask_app.py'''

    def test_animal_route(self):
        '''has a resource available at "/animal/<id>".'''
        response = app.test_client().get('/animal/1')
        assert(response.status_code == 200)

    def test_animal_route_has_attrs(self):
        '''displays attributes in animal route in <ul> tags called Name, Species.'''
        name_ul = re.compile(r'\<ul\>[Nn]ame.+')
        species_ul = re.compile(r'\<ul\>[Ss]pecies.+')
        
        response = app.test_client().get('/animal/1')

        assert(len(name_ul.findall(response.data.decode())) == 1)
        assert(len(species_ul.findall(response.data.decode())) == 1)

    def test_animal_route_has_many_to_one_attrs(self):
        '''displays attributes in animal route in <ul> tags called Zookeeper, Enclosure.'''
        zookeeper_ul = re.compile(r'\<ul\>Zookeeper.+')
        enclosure_ul = re.compile(r'\<ul\>Enclosure.+')
        
        response = app.test_client().get('/animal/1')

        assert(len(zookeeper_ul.findall(response.data.decode())) == 1)
        assert(len(enclosure_ul.findall(response.data.decode())) == 1)

    def test_zookeeper_route(self):
        '''has a resource available at "/zookeeper/<id>".'''
        response = app.test_client().get('/zookeeper/1')
        assert(response.status_code == 200)

    def test_zookeeper_route_has_attrs(self):
        '''displays attributes in zookeeper route in <ul> tags called Name, Birthday.'''
        name_ul = re.compile(r'\<ul\>[Nn]ame.+')
        birthday_ul = re.compile(r'\<ul\>[Bb]irthday.+')
        
        response = app.test_client().get('/zookeeper/1')

        assert(len(name_ul.findall(response.data.decode())) == 1)
        assert(len(birthday_ul.findall(response.data.decode())) == 1)

    def test_zookeeper_route_has_one_to_many_attr(self):
        '''displays attributes in zookeeper route in <ul> tags called Animal.'''
        animal_ul = re.compile(r'\<ul\>Animal.+')
        
        id = 1
        animals_bool = False
        while not animals_bool:
            response = app.test_client().get(f'/zookeeper/{id}')
            if len(animal_ul.findall(response.data.decode())):
                animals_bool = True

        assert(animals_bool)

    def test_enclosure_route(self):
        '''has a resource available at "/enclosure/<id>".'''
        response = app.test_client().get('/enclosure/1')
        assert(response.status_code == 200)

    def test_enclosure_route_has_attrs(self):
        '''displays attributes in enclosure route in <ul> tags called Environment, Open to Visitors.'''
        environment_ul = re.compile(r'\<ul\>[Ee]nvironment.+')
        open_ul = re.compile(r'\<ul\>[Oo]pen\s[Tt]o\s[Vv]isitors.+')
        
        response = app.test_client().get('/enclosure/1')

        assert(len(environment_ul.findall(response.data.decode())) == 1)
        assert(len(open_ul.findall(response.data.decode())) == 1)

    def test_enclosure_route_has_one_to_many_attr(self):
        '''displays attributes in enclosure route in <ul> tags called Animal.'''
        animal_ul = re.compile(r'\<ul\>Animal.+')
        
        id = 1
        animals_bool = False
        while not animals_bool:
            response = app.test_client().get(f'/enclosure/{id}')
            if len(animal_ul.findall(response.data.decode())):
                animals_bool = True

        assert(animals_bool)
