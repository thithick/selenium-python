from pages.listing_page import Listing_Page
import re


class Details_Page(Listing_Page):
    '''Functions for Detail page test'''
    
    def __init__(self, selenium, url):
        '''__init__'''
        self.selenium = selenium
        self.url = url

    def get_listing_title_on_home_page_recommended_section(self):
        '''Get listing title for listing in home page - recommended section'''
        title = self.get_text_on('home page recommended listing title')

        return title

    def get_listing_price_on_home_page_recommended_section(self):
        '''Get listing price for listing in home page - recommended section'''
        first_listing_in_recommended_listing = 'home page first recommended listing'

        class_attr = self.get_element_attribute(self.get_object(first_listing_in_recommended_listing), 'class')

        # Check if the listing is hot deal listing
        if re.search('hotdeal', class_attr, re.IGNORECASE):

            # checking if it is a cout down timer
            class_attr = self.get_element_attribute(self.get_object('home page recommended hotdeal price checker'), 'class')

            if re.search('timer', class_attr, re.IGNORECASE):
                price = self.get_text_on('home page recommended hotdeal price checker')
            else:
                price = self.get_text_on('home page recommended hotdeal listing price')

        else:
            price = self.get_text_on('home page recommended normal listing price')

        return price
    
    def get_listing_price_on_details_page(self):
        '''Get listing price for listing in details page'''
        class_attrs = self.get_element_attribute(self.get_object('listing price hotdeal checker'), 'class')
        
        # Check if the listing is hot deal
        if re.search('hot-deal', class_attrs, re.IGNORECASE):
            class_attrs = self.get_element_attribute(self.get_object('listing price hotdeal count down checker'), 'class')

            # check for HD count down
            if re.search('hot-deal', class_attrs, re.IGNORECASE):
                price = self.get_text_on('hotdeal listing price')

            else:
                price = self.get_text_on('hotdeal countdown listing price')
        
        else:
            price = self.get_text_on('normal listing price')

        return price
    
    def round_up_engine_cc(self, engine_cc):
        '''Round up exact engince CC'''
        if re.search('-', engine_cc):
            return engine_cc

        if re.search('cc', engine_cc):
            engine_cc_str = re.sub(' cc', '', engine_cc)  # for MY and ID
        else:
            engine_cc_str = re.sub(' ซีซี', '', engine_cc)  # for TH

        engine_cc = int(engine_cc_str.strip()) / 1000
        engine_cc = round(engine_cc, 1)

        return str(engine_cc)
        
    def extract_listings_details_from_home_page_recommended_listing(self, listing_title):
        '''Extract listing details from listing title in home page'''
        title = listing_title.lower().strip()
        
        year_pattern = r'^\d+'
        listing_year = re.findall(year_pattern, title)[-1]  # to get year
        car_make_model_title = re.sub(year_pattern, '', title).strip()  # remove year from the full title
        try:
            engine_cc_pattern = r'(\d\.\d)'
            engine_cc = re.findall(engine_cc_pattern, title)[-1].strip()  # to get engine cc
        except:
            # this is for electric car, like TESLA
            engine_cc = '-'

        make_model = self.split_make_model_from_keyword_suggestion(car_make_model_title)
        
        return {'year': listing_year,
                'engine': engine_cc,
                'make': make_model[0],
                'model': make_model[1]}

    def extract_state_location_from_details_page(self, location_text):
        '''Extract state location from details page location text'''
        state_location = re.split('»', location_text)

        if len(state_location) == 2:
            loc = state_location[0]
        elif len(state_location) == 3:
            loc = state_location[1]

        return loc.strip()
