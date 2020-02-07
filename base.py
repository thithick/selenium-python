from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Base(object):
    '''All selenium functions'''
    TIME_OUT = 15
    
    def go_to(self, url):
        '''instruct selenium to go to expected page'''
        self.selenium.get(url)

    def wait_for_element(self, element):
        '''Selenium implicit wait for 60 seconds until element is present'''
        try:
            WebDriverWait(self.selenium, self.TIME_OUT).until(lambda driver: self.selenium.find_element_by_xpath(element))
        except TimeoutException:
            raise Exception('Unable to locate element: %s' % (element))

    def get_page_title(self):
        '''Get current page title'''
        page_title = self.selenium.title
        
        return page_title.strip()

    def maximise_window(self):
        '''Maximize browser window'''
        # self.selenium.maximize_window()
        self.selenium.set_window_size(1360, 1020)  # this is to set height and width manually to cater docker env
    
    def get_current_page_url(self):
        '''Return current page url'''
        url = self.selenium.current_url
        
        return url

    def click_on_element(self, element, skip_wait=False):
        '''Click on element on the page'''
        if not skip_wait:
            self.wait_for_element(element)
        
        action = ActionChains(self.selenium)
        action.move_to_element(self.selenium.find_element_by_xpath(element))
        action.click()
        action.perform()
        
        self.wait_for_seconds(1)

    def hover_on_top_of_element(self, element):
        '''Hover on top of an element'''
        action = ActionChains(self.selenium)
        action.move_to_element(self.selenium.find_element_by_xpath(element))
        action.perform()
        
        self.wait_for_seconds(1)
    
    def get_text_element(self, element):
        '''Get text from an element'''
        self.wait_for_element(element)
        text = self.selenium.find_element_by_xpath(element).text
        
        return text.strip()
    
    def get_radio_button_selected(self, element):
        '''Get the checked status for radio button'''
        self.wait_for_element(element)
        
        checked = self.selenium.find_element_by_xpath(element).is_selected()
        
        return checked
    
    def get_checkbox_checked(self, element):
        '''Get the checked status for radio button'''
        self.wait_for_element(element)
        
        checked = self.selenium.find_element_by_xpath(element).is_selected()
        
        return checked
        
    def execute_js(self, js_script):
        '''Execute javascript by selenium'''
        self.selenium.execute_script(js_script)

    def page_refresh(self):
        '''refresh the current page'''
        self.selenium.refresh()

    def go_to_previous_page(self):
        '''Cliking on browser back button'''
        self.selenium.back()
        self.wait_for_seconds(1)

    def close_window(self):
        '''Close the current window tab'''
        self.selenium.close()

    def get_element_attribute(self, element, attribute):
        '''Get attribute of element'''
        self.wait_for_element(element)
        value = self.selenium.find_element_by_xpath(element).get_attribute(attribute)
        
        return value.strip()
    
    def get_current_window_handler(self):
        '''Return current active window handler'''
        window_handles = self.selenium.current_window_handle
        
        return window_handles
        
    def switch_to_new_window(self, window=None):
        '''Switch to new opened window'''
        if window == None:
            window_handles = self.selenium.window_handles
            
            if len(window_handles) <= 1:
                raise Exception('No new window found!')
            
            self.selenium.switch_to.window(window_handles[1])
        else:
            self.selenium.switch_to.window(window)

    def fill_textbox(self, element, string):
        '''Fill the text box by giving string'''
        self.wait_for_element(element)
        
        if string == 'ESC':
            self.selenium.find_element_by_xpath(element).send_keys(Keys.ESCAPE)
        else:
            self.selenium.find_element_by_xpath(element).send_keys(string)

    def clear_textbox(self, element):
        '''Clear the value in the text box'''
        self.wait_for_element(element)
        self.selenium.find_element_by_xpath(element).clear()

    def get_number_of_nodes(self, element, wait=True):
        '''Return count for elements'''
        if wait:
            self.wait_for_element(element)
        num = self.selenium.find_elements_by_xpath(element)
        
        return len(num)
    
    def is_loading(self):
        '''return true is loading icon is visible on the listing page'''
        return self.is_element_visible(self.get_object('loading icon'))
    
    def is_element_visible(self, locator):
        '''Return true if element is visible on page'''
        attempt = 0
        while attempt < 3:
            try:
                return self.selenium.find_element_by_xpath(locator).is_displayed()
            except NoSuchElementException:
                return False
            except ElementNotVisibleException:
                return False
            except StaleElementReferenceException:
                pass
            attempt = attempt + 1

    def is_element_present(self, locator):
        '''Return true if element exist inside page, no matter it is visible'''
        # try:
            # self.selenium.find_element_by_xpath(locator)
            # return True
        # except NoSuchElementException:
            # return False
        # finally:
            # set back to where you once belonged
            # pass
        
        try:
            WebDriverWait(self.selenium, self.TIME_OUT).until(EC.presence_of_element_located(self.selenium.find_element_by_xpath(locator)))
            return True
        except:
            return False
