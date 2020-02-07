from selenium import webdriver
from SeleniumLibrary.base import keyword
import SeleniumLibrary
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword
from SeleniumLibrary.keywords import BrowserManagementKeywords
import time
import types
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.locators import WindowManager
from SeleniumLibrary.utils import (is_truthy, is_noney, secs_to_timestr,
                                   timestr_to_secs)

# from SeleniumLibrary.webdrivertools import WebDriverCreator
# import WebDriverCreator

from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.keywords import BrowserManagementKeywords

# class browsersession():
class browsersession():


    @keyword
    def get_executor_url(self):
        return self.driver.command_executor._url

    @keyword
    def get_executor_url0(self):
        logger.info('Getting currently open browser desired capabilities')
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        return sl.driver.command_executor._url
