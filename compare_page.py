from pages.details_page import Details_Page
import re


class Compare_Page(Details_Page):
    '''Functions for Compare page test cases'''
    
    def __init__(self, selenium, url):
        '''__init__'''
        self.selenium = selenium
        self.url = url

    def visibility_of_compare_pop_up_element(self, element):
        '''
        Return visibility of compare pop up

        TODO: Will need to refactor with functions which will return visibility by class attr - 'visuallyhidden'
        '''
        element = element.lower().strip()

        compare_pop_up_is_showing = self.get_element_attribute(self.get_object(element), 'class')

        return not re.search('visuallyhidden', compare_pop_up_is_showing, re.IGNORECASE)

    def get_compare_pop_up_count(self):
        '''Get listing count on compare pop up header'''
        count = self.get_text_on('compare pop up count')

        return count.strip()

    def is_listing_compare_checkbox_checked(self, id_number):
        '''Return check box checked status for specific listing by giving listing id'''
        listing_compare_button_xpath = self.get_specific_listing_save_compare_button_xpath_by_listing_id(id_number, 'compare status')

        return self.is_checkbox_checked(element=None, loc=listing_compare_button_xpath)

    def remove_parentheses_from_xpath(self, xpath_text):
        '''Remove parentheses () from xpath'''
        xpath_text = re.sub(r'^\(', '', xpath_text)
        xpath_text = re.sub(r'\)$', '', xpath_text)

        return xpath_text

    def get_specific_listing_single_stat(self, id_number, stat):
        '''
        Return single listing details in search listing page:

        1. Listing title
        2. Ads type
        3. Seller type
        '''
        stat = stat.lower().strip()

        # Get specific listing xpath
        specific_listing_xpath = self.get_specific_listing_xpath_by_listing_id(id_number)

        # Extract the xpath for listing title for specific listing
        listing_single_stat_xpath = self.remove_parentheses_from_xpath(self.get_object(stat))

        # Combine both specific listing xpath and listing title xpath
        specific_listing_single_stat_xpath = specific_listing_xpath + listing_single_stat_xpath

        text = self.get_text_on(element=None, loc=specific_listing_single_stat_xpath)

        return text

    def extract_listing_title_on_search_page(self, listing_title):
        '''Get listing details from listing title in search listing page'''
        listing_title = re.split(' - ', listing_title)[0].strip()
        listing_title = self.extract_listings_details_from_home_page_recommended_listing(listing_title)

        return listing_title

    def remove_specific_listing_in_compare_pop_up(self, listing_id):
        '''Click on close button on compare pop up to remove sepecific listing based on listing ID'''
        close_button = self.get_specific_listing_xpath_by_listing_id(id_number=listing_id, element='compare pop up listings close button')

        self.click_on(element=None, loc=close_button)

    def click_on_listing_card_in_compare_pop_up(self, listing_id):
        '''Click on listing card on compare pop up based in listing ID'''
        listing_card = self.get_specific_listing_xpath_by_listing_id(id_number=listing_id, element='compare pop up listings')
        listing_card = listing_card.replace(r'/i', r'/article//a')

        self.click_on(element=None, loc=listing_card)

    def remove_spefific_listing_in_compare_page(self, listing_id):
        '''Click on remove button for listing card in compare page'''
        listing_card_xpath = self.get_specific_listing_xpath_by_listing_id(id_number=listing_id, element='listing section in compare page')
        remove_button = listing_card_xpath + self.get_object('remove button in compare page')

        self.click_on(element=None, loc=remove_button)
