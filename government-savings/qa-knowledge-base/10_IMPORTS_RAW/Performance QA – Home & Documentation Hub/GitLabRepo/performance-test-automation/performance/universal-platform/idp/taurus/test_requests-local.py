# coding=utf-8

import logging
import random
import string
import sys
import unittest
from time import time, sleep

import apiritif

import os
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.options import ArgOptions
from bzt.resources.selenium_extras import get_locator, wait_for, waiter, find_element_by_shadow, add_flow_markers
reader_1 = apiritif.CSVReaderPerThread('C:\\work\\git\\qa-automation\\automation\\performance-test-automation\\performance\\universal-platform\\idp\\taurus\\data.csv', loop=True, quoted=False, delimiter=',')
waittime = 0.5
timeout = 15.0

class TestBlazemeterIdpLoginLocal(unittest.TestCase):

    def setUp(self):
        self.vars = {}
        reader_1.read_vars()
        self.vars.update(reader_1.get_vars())
        
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.set_capability('unhandledPromptBehavior', 'ignore')
        options.headless = True
        service = Service(log_file='C:\\work\\git\\qa-automation\\automation\\performance-test-automation\\performance\\universal-platform\\idp\\taurus\\2025-09-03_12-32-16.596807\\webdriver.log')
        options.set_capability('browserName', 'chrome')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(timeout)
        add_flow_markers()
        apiritif.put_into_thread_store(timeout=timeout, func_mode=False, driver=self.driver, windows={}, scenario_name='Blazemeter-IDP-Login-Local', data_sources=True)
    
    def _1_0_Navigate_to_Login(self):
        with apiritif.smart_transaction('0. Navigate to Login'):
            self.driver.set_window_size('1535', '743')
            self.driver.get(self.vars['login'])
            
            waiter()
            sleep(waittime)

    def _2_1a_Fill_in_Credentials(self):
        with apiritif.smart_transaction('1a. Fill in Credentials'):
            find_element_by_shadow("auth-form-input[name='username'], input").clear()
            find_element_by_shadow("auth-form-input[name='username'], input").send_keys(self.vars['username'])
            waiter()
            
            find_element_by_shadow("auth-form-input[name='fakePassword'], input").clear()
            find_element_by_shadow("auth-form-input[name='fakePassword'], input").send_keys(self.vars['password'])
            waiter()
            sleep(waittime)

    def _3_1b_Submit_Login(self):
        with apiritif.smart_transaction('1b. Submit Login'):
            wait_for('clickable', [{'shadow': "auth-button[type='submit'], button"}], 10.0)
            
            find_element_by_shadow("auth-button[type='submit'], button").click()
            waiter()

    def _4_2a_Wait_For_Overview(self):
        with apiritif.smart_transaction('2a. Wait for Overview'):
            wait_for('present', [{'CSS': '#content-begin'}], timeout)
            waiter()
            
    def _5_2b_Verify_Overview(self):
        with apiritif.smart_transaction('2b. Verify Overview'):
            var_loc_as = get_locator([{'CSS': '#content-begin > header > h1'}])
            self.assertIn('Welcome back'.strip(), self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip())
            sleep(waittime)

    def _6_3_Screenshot(self):
        with apiritif.smart_transaction('3. Screenshot'):
            id = "images\\" + str(random.randint(1000, 9999)) + "-" + str(self.vars['username'])
            self.driver.save_screenshot(id)
            sleep(waittime)

    def test_Blazemeter_IDP_Login_Local(self):
        self._1_0_Navigate_to_Login()
        self._2_1a_Fill_in_Credentials()
        self._3_1b_Submit_Login()
        self._4_2a_Wait_For_Overview()
        self._5_2b_Verify_Overview()

    def tearDown(self):
        #self._6_3_Screenshot()
        if self.driver:
            self.driver.quit()
