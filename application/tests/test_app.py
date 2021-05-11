
from flask import url_for
from flask_testing import TestCase

import os
from application import app, db
from application.models import Army

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URI'),
            SECRET_KEY=os.getenv('TEST_SECRET'),
            DEBUG=True,
            WTF_CRSF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()

        sample1 = Army(name='Necrons',faction='Xenos',codex=9)

        sample2 = Army(name='Sisters of battle', faction='Imperium', codex=8)

        db.session.add(sample1)
        db.session.commit()
        db.session.add(sample2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Necrons', response.data)

    def test_add_get(self):
        response = self.client.get(url_for('add_army'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Name of army', response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('add_army'),
            data = dict(
                name='Sisters of battle', 
                faction='Imperium',
                codex=8),
            follow_redirects=True
        )
        self.assertIn(b'Sisters of battle',response.data)