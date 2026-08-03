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
from bzt.resources.selenium_extras import get_locator, waiter, wait_for, add_flow_markers
reader_1 = apiritif.CSVReaderPerThread('C:\\work\\git\\ags-automation\\performance\\universal-enrollment\\taurus\\data.csv', loop=False, quoted=False, delimiter=',')
waittime = 0.5
timeout = 15.0

workInState = False

class TestBlazemeterUeLocal(unittest.TestCase):

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
        service = Service(log_file='C:\\work\\git\\ags-automation\\performance\\universal-enrollment\\taurus\\2024-01-12_11-27-15.634300\\webdriver.log')
        options.set_capability('browserName', 'chrome')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(timeout)
        add_flow_markers()
        apiritif.put_into_thread_store(timeout=timeout, func_mode=True, driver=self.driver, windows={}, scenario_name='Blazemeter-UE-Local', data_sources=True)

    def _01_0_Navigate_to_Enrollment(self):
        with apiritif.smart_transaction('0. Navigate to Enrollment'):
            self.driver.set_window_size('1535', '743')
            self.driver.get('https://agsup-ui-enrollment-stage2.gs.ascensus.com/enrollments/mddirect')
            #self.driver.get('https://agsup-ui-enrollment-qc1.gs.ascensus.com/enrollments/mddirect')

            waiter()
            self.assertEqual(self.driver.title, 'Universal Enrollment')
            sleep(5)

    def _02_1a_Fill_in_Prospect(self):
        with apiritif.smart_transaction('1a. Fill in Prospect'):
            id = str(random.randint(1000000, 9999999))
            
            var_loc_keys = get_locator([{'CSS': '#firstName'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['ownerFirstName'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#lastName'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['ownerLastName'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#email input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('test' + id + '@test.com')
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#confirmEmail input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('test' + id + '@test.com')
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#username'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('username' + id)
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#password input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('Test@123')
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#confirmPassword input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('Test@123')
            waiter()

    def _03_1b_Submit_Prospect(self):
        with apiritif.smart_transaction('1b. Submit Prospect'):
            wait_for('clickable', [{'CSS': '#createLogin'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#createLogin'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#acct-details-phone-number'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'Tell us about yourself'.strip())

    def _04_2a_Fill_in_Owner_Details(self):
        with apiritif.smart_transaction('2a. Fill in Owner Details'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-phone-number input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-phone-number input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['phone'])
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-phone-type'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            ssn = random.randint(100000000, 999999999)
            var_loc_keys = get_locator([{'CSS': '#acct-details-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(ssn)
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-confirm-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-confirm-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(ssn)
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-dob input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(Keys.ARROW_LEFT)
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(Keys.ARROW_LEFT)
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-dob input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['ownerDob'])
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-citizen'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()

    def _05_2b_Submit_Owner_Details(self):
        with apiritif.smart_transaction('2b. Submit Owner Details'):
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#address1'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'What is your address?'.strip())

    def _06_3a_Fill_in_Owner_Address(self):
        with apiritif.smart_transaction('3a. Fill in Owner Address'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#address1'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['address'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#city'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['city'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#state'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:nth-of-type(26)'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:nth-of-type(26)'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#zipcode'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('02459')
            waiter()
            
            if workInState:
                var_loc_keys = get_locator([{'CSS': '#workInStateNo'}])
                self.driver.find_element(
                var_loc_keys[0], 
                var_loc_keys[1]).click()
                waiter()

    def _07_3b_Submit_Owner_Address(self):
        with apiritif.smart_transaction('3b. Submit Owner Address'):
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#relationshipMyself'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'Who are you saving for?'.strip())

    def _08_4_Submit_Saving_For(self):
        with apiritif.smart_transaction('4. Submit Saving For'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#relationshipChild'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#bene-first-name'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'Tell us about the future scholar'.strip())

    def _09_5a_Fill_in_Beneficiary_Details(self):
        with apiritif.smart_transaction('5a. Fill in Beneficiary Details'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#bene-first-name'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['beneFirstName'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bene-last-name'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['ownerLastName'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bene-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            ssn = random.randint(100000000, 999999999)
            var_loc_keys = get_locator([{'CSS': '#bene-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(ssn)
            
            var_loc_keys = get_locator([{'CSS': '#bene-confirm-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bene-confirm-ssn input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(ssn)
            
            var_loc_keys = get_locator([{'CSS': '#bene-dob input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(Keys.ARROW_LEFT)
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(Keys.ARROW_LEFT)
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bene-dob input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['beneDob'])
            
            var_loc_keys = get_locator([{'CSS': '#acct-details-citizen'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()

    def _10_5b_Submit_Beneficiary_Details(self):
        with apiritif.smart_transaction('5b. Submit Beneficiary Details'):
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#contribution-type'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), "How much would you like to contribute to {}'s account to get started?".format(self.vars['beneFirstName']).strip())

    def _11_6a_Fill_Funding_Details(self):
        with apiritif.smart_transaction('6a. Fill Funding Details'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#contribution-type'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:nth-of-type(3)'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:nth-of-type(3)'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#routing-number'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('011000138')
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bank-name'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys('Bank of America')
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#account-type'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#account-number input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['bankAcct'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#confirm-account-number input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['bankAcct'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#ah-first-name'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['ownerFirstName'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#ah-last-name'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['ownerLastName'])
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#is-domestic'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#contribution-amount'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).clear()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['amount'])
            waiter()

    def _12_6b_Submit_Funding_Details(self):
        with apiritif.smart_transaction('6b. Submit Funding Details'):
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#dollars-50-container'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), "What would you like to contribute to {}'s account on a regular basis?".format(self.vars['beneFirstName']).strip())

    def _13_7a_Fill_Recurring_Details(self):
        with apiritif.smart_transaction('7a. Fill Recurring Details'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#dollars-50-container'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#contribution-type'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bene-dob input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(Keys.ARROW_LEFT)
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(Keys.ARROW_LEFT)
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#bene-dob input'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).send_keys(self.vars['startDate'])
            
            var_loc_keys = get_locator([{'CSS': '#annual-increase'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#month-increase'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': 'kendo-popup li:first-child'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': 'kendo-popup li:first-child'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()

    def _14_7b_Submit_Recurring_Details(self):
        with apiritif.smart_transaction('7b. Submit Recurring Details'):
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#keep-it-simple'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'How would you like to invest? '.strip())

    def _15_8a_Submit_How_to_Invest(self):
        with apiritif.smart_transaction('8a. Submit How to Invest'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#keep-it-simple'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#learn-more-link'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), "Select {}'s Portfolio".format(self.vars['beneFirstName']).strip())

    def _16_8b_Submit_Keep_it_Simple(self):
        with apiritif.smart_transaction('8b. Submit Keep it Simple'):
            sleep(waittime)

            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()

    def _17_8c_Continue_Enrollment(self):
        with apiritif.smart_transaction('8c. Continue Enrollment'):
            wait_for('present', [{'CSS': '#add-bene-modal'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': 'kendo-dialog-titlebar'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'Would you like to add another Beneficiary now?'.strip())
            
            var_loc_keys = get_locator([{'CSS': '#btn-finish'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '#upromise-modal'}], 10.0)
            
            var_loc_keys = get_locator([{'CSS': '#not-right-now'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': '.review-page-container'}], 10.0)
            
            var_loc_as = get_locator([{'CSS': '.form-title'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), "You're almost there!".strip())

    def _18_9a_Fill_Review_Page(self):
        with apiritif.smart_transaction('9a. Fill Review Page'):
            sleep(waittime)
            
            var_loc_keys = get_locator([{'CSS': '#delivery-checkbox'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            
            var_loc_keys = get_locator([{'CSS': '#terms-checkbox'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()

    def _19_9b_Submit_Review_Page(self):
        with apiritif.smart_transaction('9b. Submit Review Page'):
            wait_for('clickable', [{'CSS': '#bottomNavPrimaryBtn'}], 20.0)
            
            var_loc_keys = get_locator([{'CSS': '#bottomNavPrimaryBtn'}])
            self.driver.find_element(
            var_loc_keys[0], 
            var_loc_keys[1]).click()
            waiter()
            wait_for('present', [{'CSS': 'ue-post-account-creation'}], 45.0)
            
            var_loc_as = get_locator([{'CSS': 'h1'}])
            self.assertEqual(self.driver.find_element(
            var_loc_as[0], 
            var_loc_as[1]).get_attribute('innerText').strip(), 'Your account has been successfully opened!'.strip())

    def _20_9c_Screenshot(self):
        with apiritif.smart_transaction('9c. Screenshot'):
            id = "images\\" + str(random.randint(1000, 9999)) + "-" + str(self.vars['screenshot'])
            self.driver.save_screenshot(id)
            sleep(0.5)

    def test_Blazemeter_UE_Grid(self):
        self._01_0_Navigate_to_Enrollment()
        self._02_1a_Fill_in_Prospect()
        self._03_1b_Submit_Prospect()
        self._04_2a_Fill_in_Owner_Details()
        self._05_2b_Submit_Owner_Details()
        self._06_3a_Fill_in_Owner_Address()
        self._07_3b_Submit_Owner_Address()
        self._08_4_Submit_Saving_For()
        self._09_5a_Fill_in_Beneficiary_Details()
        self._10_5b_Submit_Beneficiary_Details()
        self._11_6a_Fill_Funding_Details()
        self._12_6b_Submit_Funding_Details()
        self._13_7a_Fill_Recurring_Details()
        self._14_7b_Submit_Recurring_Details()
        self._15_8a_Submit_How_to_Invest()
        self._16_8b_Submit_Keep_it_Simple()
        self._17_8c_Continue_Enrollment()
        self._18_9a_Fill_Review_Page()
        self._19_9b_Submit_Review_Page()

    def tearDown(self):
        self._20_9c_Screenshot()
        if self.driver:
            self.driver.quit()
