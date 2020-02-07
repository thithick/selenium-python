from pages.common import Common
import re


class Home_Page(Common):
    '''Functions for Home page test'''
    
    def __init__(self, selenium, url):
        '''__init__'''
        self.selenium = selenium
        self.url = url
        
    def expected_page_title(self):
        '''return expected page title for comparison'''
        # return False if error page detected
        if self.is_error_page():
            return 'Error page is found!'
        
        if re.search('carlist.my', self.url, re.IGNORECASE):
            if re.search('dealer', self.get_current_page_url(), re.IGNORECASE):
                if re.search('privateseller', self.get_current_page_url(), re.IGNORECASE):
                    exp_title = 'Carlist.my'
                else:
                    exp_title = 'Response Management System'
            else:
                exp_title = 'Carlist.my'
        elif re.search('mobil123.com', self.url, re.IGNORECASE):
            if re.search('dealer', self.get_current_page_url(), re.IGNORECASE):
                if re.search('privateseller', self.get_current_page_url(), re.IGNORECASE):
                    exp_title = 'Mobil123'
                else:
                    exp_title = 'Si Jari'
            else:
                exp_title = 'Mobil123'
        elif re.search('one2car.com', self.url, re.IGNORECASE):
            if re.search('dealer', self.get_current_page_url(), re.IGNORECASE):
                if re.search('privateseller', self.get_current_page_url(), re.IGNORECASE):
                    exp_title = 'One2car.com'
                else:
                    exp_title = 'ขายง่าย'
            else:
                exp_title = 'One2car.com'
        
        # expected string should found
        return exp_title
    
    def count_for_section_element(self, locator):
        '''return count for element'''
        locator = locator.strip().lower()
        
        elem = self.get_object(locator)
        
        return self.get_number_of_nodes(elem)

    def is_error_page(self):
        'return if current page is error page'
        err_page = self.is_element_present(self.get_object('error page'))

        return err_page
