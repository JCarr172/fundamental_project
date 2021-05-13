
from flask import url_for
from flask_testing import TestCase

import os
from application import app, db
from application.models import Army, Unit

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URI'),
            SECRET_KEY=os.getenv('TEST_SECRET'),
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()

        army1 = Army(name='Necrons',faction='Xenos',codex=9)
        db.session.add(army1)
        db.session.commit()

        army2 = Army(name='Sisters of battle', faction='Imperium', codex=8)
        db.session.add(army2)
        db.session.commit()

        unit1 = Unit(
            name='Necron Lord',
            category='HQ',
            price=90,
            quantity=1,
            army_id=1
        )
        db.session.add(unit1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Necrons', response.data)

    def test_add_army_get(self):
        response = self.client.get(url_for('add_army'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Name of army', response.data)

    def test_update_army_get(self):
        response = self.client.get(url_for('update_army', number = 1))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Original information', response.data)

    def test_view_army_get(self):
        response = self.client.get(url_for('view_army', number = 2))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Sisters of battle', response.data)

    def test_add_unit_get(self):
        response = self.client.get(url_for('add_unit', number = 1))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Necrons', response.data)

    def test_update_unit_get(self):
        response = self.client.get(url_for('update_unit', number = 1))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Necron Lord', response.data)

class TestAdd(TestBase):
    def test_add_unit_post(self):
        response = self.client.post(
            url_for('add_unit'),
            data = dict(
                name='Retributor',
                category='Heavy Support',
                price='25',
                quantity='5',
                army=2),
            follow_redirects=True
        )
        self.assertIn(b'Retributor',response.data)

    def test_add_army_post(self):
        response = self.client.post(
            url_for('add_army'),
            data = dict(
                name='Imperial Guard', 
                faction='Imperium',
                codex='8'),
            follow_redirects=True
        )
        self.assertIn(b'Imperial Guard',response.data)

    def test_add_army_error_post(self):
        response = self.client.post(
            url_for('add_army'),
            data = dict(
                name='This is a string that is too long for the field', 
                faction='Imperium',
                codex=8),
            follow_redirects=True
        )
        self.assertIn(b'Input was too long',response.data)

    def test_add_unit_error_post(self):
        response = self.client.post(
            url_for('add_unit'),
            data = dict(
                name='Warrior',
                category='Troops',
                price=10,
                quantity='Thirty',
                army=1),
            follow_redirects=True
        )
        self.assertIn(b'Please enter a number',response.data)


class TestUpdate(TestBase):
    def test_update_army_post(self):
        response = self.client.post(
            url_for('update_army', number = 2),
            data = dict(
                name='Adeptus Sororitas',
                faction='Imperium',
                codex=8),
            follow_redirects=True
        )
        self.assertIn(b'Adeptus Sororitas',response.data)

    def test_update_unit_post(self):
        response = self.client.post(
            url_for('update_unit', number = 1),
            data = dict(
                name='Warrior',
                category='Troops',
                price='10',
                quantity='30',
                army=1),
            follow_redirects=True
        )
        self.assertIn(b'Warrior',response.data)

    def test_update_army_error_post(self):
        response = self.client.post(
            url_for('update_army', number = 1),
            data = dict(
                name='This is a string that is too long for the field', 
                faction='Imperium',
                codex=8),
            follow_redirects=True
        )
        self.assertIn(b'Input was too long',response.data)

    def test_update_unit_error_post(self):
        response = self.client.post(
            url_for('update_unit', number = 1),
            data = dict(
                name='Warrior',
                Category='Troops',
                price=10,
                quantity='Thirty',
                army_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Please enter a number',response.data)

class TestDelete(TestBase):
    def test_delete_army_post(self):
        response = self.client.post(
            url_for('delete_army', number = 2),
            follow_redirects=True
        )
        self.assertNotIn(b'Sisters of battle',response.data)

    def test_delete_army_with_units_post(self):
        response = self.client.post(
            url_for('delete_army', number = 1),
            follow_redirects=True
        )
        self.assertNotIn(b'Necrons',response.data)

    def test_delete_unit_post(self):
        response = self.client.post(
            url_for('delete_unit', number = 1),
            follow_redirects=True
        )
        self.assertNotIn(b'Necron Lord',response.data)