from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Chrome browser is launched')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when(u'ecFeed homepage is opened')
def home_page(context):
    context.driver.get("https://prerelease-spa.ecfeed.com/")
    context.driver.maximize_window()\



@when(u'button is Accepted')
def accept_cookies(context):
    acceptance = context.driver.find_element(By.ID, 'btn-cookies')
    acceptance.click()


@when(u'Login button is clicked')
def login(context):
    log_in = context.driver.find_element(By.ID, "btn-main-login")
    log_in.click()

    context.driver.implicitly_wait(10)


@when(u'username "{mail}" and password "{pwd}" are entered')
def enter_credentials(context, mail, pwd):

    context.driver.find_element(By.NAME, "email").send_keys(mail)

    context.driver.find_element(By.NAME, "password").send_keys(pwd)

# context.driver.find_element_by_class_name('auth0-lock-input-email').send_keys(mail)
# context.driver.find_element_by_class_name('auth0-lock-input-show-password').send_keys(pwd)
# context.driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(mail)
# context.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(pwd)


@when(u'Submit button is clicked')
def submit(context):
    enter = context.driver.find_element_by_class_name('auth0-label-submit')
    enter.click()


@when(u'Accept cookies button')
def accept_popup(context):
    context.driver.find_element(By.ID, 'popup_button_close').click()


@then(u'Click on My Teams button')
def my_teams(context):
    context.driver.find_element(By.ID, 'btn-main-teams').click()


@then(u'Click on My Projects button')
def my_projects(context):
    context.driver.find_element(By.ID, 'btn-main-projects').click()


@then(u'Click on User Menu button')
def user_menu(context):
    context.driver.find_element(By.ID, 'btn-user-menu').click()


@then(u'Click on Settings button')
def settings(context):
    context.driver.find_element(By.ID, 'btn-user-settings').click()

@then(u'Click create new project')
def new_project(context):
    context.driver.find_element(By.ID, 'btn_new_project').click()

@then(u'Enter project name "{Test}"')
def project_name(context, Test):
    context.driver.find_element(By.ID, 'btn_new_project_name').send_keys(Test)

@then(u'Click create')
def create(context):
    context.driver.find_element(By.ID, 'btn_new_project_create').click()


@then(u'Click again on User Menu button')
def user_menu(context):
    context.driver.find_element(By.ID, 'btn-user-menu').click()


@then(u'Log out')
def log_out(context):
    context.driver.find_element(By.ID, 'btn-user-logout').click()

@then(u'Find my projects')
def fail_search(context):
    context.driver.find_element(By.ID, 'btn-main-projects').click()
