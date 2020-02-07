from pages.base import Base
from locators.locators_common import locators
from time import sleep
from selenium.common.exceptions import TimeoutException
import re
import os


class Common(Base):
    '''Common functions class'''
    TIME_OUT = 15
    
    def go_to_page(self, url):
        '''Go to desired url'''
        try:
            self.go_to(url)
        except TimeoutException:
            self.execute_js('window.stop();')
    
    def save_auth_info_to_cookies(self):
        '''A hack to authenticate all site first before start running test'''
        testing_env_auth = 'icarasia:gears6'
        url = self.url
        buyerp_url = ''
        dealerp_url = ''
        
        if re.search('preprod', url, re.IGNORECASE):
            env = 'preprod'
        elif re.search('staging', url, re.IGNORECASE):
            env = 'staging'
        elif re.search('www1', url, re.IGNORECASE):
            env = 'canary'
        else:
            env = None
        
        # get server env: carlist, mobil123, one2car
        server_path = re.split('https://', url)
        server_path = re.split(r'\.', server_path[-1])
        server_path_split = (server_path[-2], server_path[-1])

        server_url = '.'
        server_url = server_url.join(server_path_split)

        # Form the complete URL for BP and SP
        if env == 'preprod' or env == 'staging':
            buyerp_url = 'https://%s@%s.%s' % (testing_env_auth, env, server_url)
            dealerp_url = 'https://%s@%s-dealer.%s' % (testing_env_auth, env, server_url)
        elif env == 'canary':
            buyerp_url = 'https://%s@www1.%s' % (testing_env_auth, server_url)
            dealerp_url = 'https://dealer.%s' % (server_url)
        else:
            buyerp_url = 'https://www.%s' % (server_url)
            dealerp_url = 'https://dealer.%s' % (server_url)
        
        for portal_url in [dealerp_url, buyerp_url]:
            if portal_url == '':
                continue
            
            if env != None:
                self.go_to_page(portal_url)
                self.wait_for_seconds(1)
            else:
                break
      
    def go_to_home_page(self, save_auth=True):
        '''Navigate to home page'''
        self.maximise_window()
        if save_auth:
            self.save_auth_info_to_cookies()
        
        self.go_to_page(self.url)

    def refresh_current_page(self):
        '''Refresh current page'''
        try:
            self.page_refresh()
        except TimeoutException:
            self.execute_js('window.stop();')
        
    def scroll_to_top_of_the_page(self):
        '''Scroll to top of the page'''
        self.execute_js('window.scrollTo(0, 0);')
        self.wait_for_seconds(1)
        
    def scroll_to_bottom_of_the_page(self):
        '''Scroll to bottom of the page'''
        self.execute_js('window.scrollTo(0, document.body.scrollHeight);')
        self.wait_for_seconds(1)
    
    def wait_for_seconds(self, time):
        '''Explicit wait for execution'''
        default_timeout_1s = 1
        default_timeout_2s = 2

        if time == 1:
            sleep(default_timeout_1s)
        if time == 2:
            sleep(default_timeout_2s)
        else:
            # max sleep 3 seconds
            sleep(default_timeout_2s)
            sleep(default_timeout_1s)

    def login_with_user(self, username, password='123456'):
        '''Login into buyer portal'''
        username = username.strip()
        password = password.strip()
        
        self.fill_textbox(self.get_object('username textbox'), username)
        self.fill_textbox(self.get_object('password textbox'), password)
        self.click_on('sign in button')

    def hide_bottom_ads(self):
        '''Hide the ads appear on bottom of the page'''
        # execute jquery
        path = r'pages\jquery\jquery-3.3.1.min.js'
        jq_path = os.path.join(os.getcwd(), path)
        
        jquery = open(jq_path, 'r')
        jquery = jquery.read()
        
        self.execute_js(jquery)
        
        # hide the bottom ads
        self.execute_js('$("div[id^=\'ebAd36763077_banner_div\']").hide()')

    def hide_header(self):
        '''Hack for FF to hide sticky header when page scroll to lower position'''
        js_script = 'document.getElementsByClassName("js-header--sticky-top")[0].style.visibility = "hidden";'
        self.execute_js(js_script)
        
    def unhide_header(self):
        '''Display the page header if it is hidden'''
        js_script = 'document.getElementsByClassName("js-header--sticky-top")[0].style.visibility = "visible";'
        self.execute_js(js_script)

    def get_object(self, element, num=None, text=None):
        '''Calling locator class to get locator element'''
        loc_xpath = locators(self.url)
        
        return loc_xpath.get_locator(element, num, text)

    def click_on(self, element, num=None, text=None, loc=None):
        '''Click on element'''
        if loc == None:
            loc = self.get_object(element, num, text)
        
        self.click_on_element(loc)
        
        return loc
    
    def fill_in(self, element, string):
        '''Fill the text box by giving string'''
        loc = self.get_object(element)
        
        self.fill_textbox(loc, string)
    
    def get_text_on(self, element, loc=None, num=None, skip_lower=False):
        '''Get text from element'''
        if loc == None:
            loc = self.get_object(element, num)
        
        text = self.get_text_element(loc)

        if skip_lower is True:
            return text
        
        return text.lower()

    def element_visibility(self, element):
        '''Return element visibility'''
        loc = self.get_object(element)
        
        return self.is_element_visible(loc)

    def is_checkbox_checked(self, element, loc=None):
        '''Return checkbox check status'''
        if loc == None:
            loc = self.get_object(element)

        checked_status = self.get_checkbox_checked(loc)

        return checked_status
