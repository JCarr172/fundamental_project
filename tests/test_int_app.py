from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from selenium.webdriver.support.ui import Select

import os
from application import app, db
from application.models import Army, Unit

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URI'),
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all()
        army1 = Army(name='Necrons',faction='Xenos',codex=9)
        db.session.add(army1)
        db.session.commit()

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    def test_create(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Sisters of battle')
        self.driver.find_element_by_xpath('//*[@id="faction"]').send_keys('Imperium')
        self.driver.find_element_by_xpath('//*[@id="codex"]').send_keys('8')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.assertIn(url_for('home'), self.driver.current_url)

        text = self.driver.find_element_by_xpath('/html/body/h3[2]').text
        self.assertEqual(text, 'Sisters of battle')

        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('Battle Sister')
        self.driver.find_element_by_xpath('//*[@id="category"]').click()
        self.driver.find_element_by_xpath('//*[@id="category"]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys('10')
        self.driver.find_element_by_xpath('//*[@id="quantity"]').send_keys('10')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.assertIn(url_for('home'), self.driver.current_url)

        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()

        text = self.driver.find_element_by_xpath('/html/body/p[1]').text
        assert 'Battle Sister' in text