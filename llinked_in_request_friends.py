import modules

# Using the iphone user agent for firefox
profile = modules.webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Iphone")

# Path to the webdriver, argument is the user-gent profile
driver = modules.webdriver.Firefox(profile, executable_path=r'C:\geckodriver.exe')

# Login to Linked in :
def login():
    login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    driver.get(login_url)
    # Finding the Html element by id / can be modified to adopt your needs
    username = driver.find_element_by_id("username")

    # Inserting the user-name in the username field
    username.send_keys("radu.enachi@gmail.com") # Type between quotation marks your username

    # Finding the Html element by id / can be modified to adopt your needs
    password = driver.find_element_by_id("password")

    # Inserting the password in the password field
    password.send_keys("root37379905700radyK@~") # Type between quotation marks your password

    # Finding the class name and the act on the tag
    driver.find_element_by_class_name("btn__primary--large").click()

    # Report a successful ending of the function
    print("successfully logged in")


# Friend list
def goto_network():
    # Navigate to the friends network page and the acting on it
    driver.find_element_by_id("mynetwork-tab-icon").click()


# Adding friends
def add_friends():
    # For each price range
    # Get find the element
    # Wait the random time
    for i in range(0, 100):
        try:
            driver.find_element_by_class_name("artdeco-button--secondary").click()
            modules.time.sleep(modules.randrange(5))
        except modules.ElementClickInterceptedException:
            driver.quit()
            return
        # Scroll the page
        if i == 5:
            scroll_page()


# Scroll pages till the end
def scroll_page():
    SCROLL_PAUSE_TIME = 0.5

    while True:

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        modules.time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:

            # Wait to load page
            modules.time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # check if the page height has remained the same
            if new_height == last_height:

                # if so, you are done
                break

            # if not, move on to the next loop
            else:

                last_height = new_height
                continue


def quit_task():
    driver.quit()


# Run the script
if __name__ == "__main__":
    login()
    goto_network()
    modules.time.sleep(1)
    add_friends()
    quit_task()
