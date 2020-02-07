from selenium import webdriver

driver = webdriver.Chrome()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://www.anyrace.net/")

print session_id
print executor_url


driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver2.session_id = session_id
print driver2.current_url

def get_element(self,xpath):
        "Return the DOM element of the xpath or 'None' if the element is not found "
        dom_element = None
        try:
            dom_element = self.driver.find_element(xpath)
        except Exception,e:
            self.write(str(e),'debug')
            self.write("Check your locator-'%s"%xpath)
            #Print the session_id and _url in case the element is not found
            self.write("In case you want to reuse session, the session_id and _url for current browser session are: %s,%s"%(driver.session_id ,driver.command_executor._url))
 
        return dom_element


from selenium import webdriver
 
#Pass the session_url you extracted
driver = webdriver.Remote(command_executor=executor_url,desired_capabilities={})
# driver = webdriver.Remote(command_executor=session_url,desired_capabilities={})
 
#Attach to the session id you extracted
driver.session_id = session_id
 
#Resume from that browser state
elm = driver.find_element_by_xpath("xpath")
 
elm.click() #Perform required action