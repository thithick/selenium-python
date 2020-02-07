from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

#remove automation message from browser
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")


#create a new Chrome session
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to the application home page
driver.get("https://accounts.google.com/SignUp")

#get the first name textbox
first_name = driver.find_element_by_id("FirstName")
first_name.clear()

#pull random first name from list
female_name_array = ['MARY',
'PATRICIA',
'LINDA',
'BARBARA',
'ELIZABETH',
'JENNIFER',
'MARIA',
'SUSAN',
'MARGARET',
'DOROTHY',
'LISA',
'NANCY',
'KAREN',
'BETTY',
'HELEN',
'PAZ',
'NEEDHAM',
'MOJICA',
'KUYKENDALL',
'HAMEL',
'ESCAMILLA',
'DOUGHTY',
'BURCHETT',
'AINSWORTH',
'WILBUR',
'VIDAL',
'UPCHURCH',
'THIGPEN',
'STRAUSS',
'SPRUILL',
'SOWERS',
'RIGGINS',
'RICKER',
'MCCOMBS',
'HARLOW',
'GARNETT',
'BUFFINGTON',
'YI',
'SOTELO',
'OLIVAS',
'NEGRETE',
'MOREY',
'MACON',
'LOGSDON',
'LAPOINTE',
'FLORENCE',
'CATHEY',
'BIGELOW',
]

last_name = (random.choice(last_name_array))

#enter surname
surname.send_keys(last_name)


#get username textbox
username = driver.find_element_by_id("GmailAddress")
username.clear()

#generate username
rand_4_digit_num = random.randint(1000,9999)
user_concat = combined_first_names + last_name


#enter username
username.send_keys(user_concat, rand_4_digit_num)

#get password textbox
password = driver.find_element_by_id("Passwd")
password.clear()

#generate password
alphabet = "abcdefghijklmnopqrstuvwxyz"
pw_length = 8
mypw = ""

for i in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypw = mypw + alphabet[next_index]

# replace 1 or 2 characters with a number
for i in range(random.randrange(1,3)):
    replace_index = random.randrange(len(mypw)//2)
    mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index+1:]

# replace 1 or 2 letters with an uppercase letter
for i in range(random.randrange(1,3)):
    replace_index = random.randrange(len(mypw)//2,len(mypw))
    mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]


#enter password
password.send_keys(mypw)

#get confirm password textbox
confirm_password = driver.find_element_by_id("PasswdAgain")
confirm_password.clear()

#re enter password
confirm_password.send_keys(mypw)

#select month from birthday dropdown
month = driver.find_element_by_id(":0").click()
january = driver.find_element_by_id(":1").click()

#get birth day textbox
birth_day = driver.find_element_by_id("BirthDay")
birth_day.clear()

#enter birth day
birth_day.send_keys("01")

#get birth year textbox
birth_year = driver.find_element_by_id("BirthYear")
birth_year.clear()

#enter birth year
birth_year.send_keys("1990")

#select gender from gender dropdonw
gender = driver.find_element_by_id("Gender").click()
female = driver.find_element_by_id(":e").click()

#submit form
submit = driver.find_element_by_id("submitbutton").submit()
time.sleep(2)
submit_again = driver.find_element_by_id("submitbutton").submit()

#contract agreement
scroll_button = driver.find_element_by_id("tos-scroll-button").click()
time.sleep(2)
contract_agreement = driver.find_element_by_id("iagreebutton").click()
time.sleep(2)

#verify account
phone_number = driver.find_element_by_id("signupidvinput")
phone_number.clear()
#Enter a Valid phone number for verification sms
phone_number.send_keys("0400123123")

verify_submit = driver.find_element_by_id("next-button").click()


#store username and password to file
f = open('user_details.txt', 'a')
f.write(user_concat + "    " + mypw + "\n")
f.close()









