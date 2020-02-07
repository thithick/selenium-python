from pages.common import Common
import re
import random
import string


class Help_Page(Common):
    '''Functions for help page test'''
    
    def __init__(self, selenium, url):
        '''__init__'''
        self.selenium = selenium
        self.url = url

    def visibility_of_message_type(self, error_msg_type):
        '''check if the visibility of error message panel'''
        msg_panel = self.get_object(error_msg_type)
        
        if self.is_element_visible(msg_panel):
        
            attr_value = self.get_element_attribute(msg_panel, 'class')
        
            if re.search('visuallyhidden', attr_value, re.IGNORECASE):
                return False
            else:
                return True
        else:
            return False

    def clear_value_in_textbox(self, element):
        '''clear the value in the text box'''
        elem = self.get_object(element)
        
        self.clear_textbox(elem)
    
    def random_pick_from_drop_down(self, locator):
        '''random pick option from drop down list'''
        # Expand drop down
        while not (self.is_dropdown_expanded(locator)):
            self.click_on(locator)
        
        # Initialise drop down option
        loc_option = re.sub('drop down', 'option', locator, re.IGNORECASE)
        
        # Get number of options from expanded drop down
        num = self.get_number_of_nodes(self.get_object(loc_option))
        num = random.randint(1, num)

        # Click on option list randomly
        self.click_on(loc_option, num)
    
    def random_genarate_valid_phone_number(self):
        '''genarate phone number start with 0 and with size 10, 11'''
        size_of_number = random.randint(8, 9)
        first_number = str(random.randint(1, 9))
        other_number = ''.join(random.choice(string.digits) for _ in range(size_of_number))
        
        return '0' + first_number + other_number

    def is_dropdown_expanded(self, elem):
        '''get drop down expanded status'''
        elem = elem.strip()

        loc = self.get_element_attribute(self.get_object(elem), 'class')
        
        if re.search('dropdown-active', loc, re.IGNORECASE):
            return True
        
        return False
