import allure
from selene import browser, by, be


@allure.step('Открываем главную страницу GitHub')
def browser_open_github():
    browser.open('/')

@allure.step('Ищем репозиторий {repo}')
def search_repo(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo).press_enter()

@allure.step('Переход по ссылке {repo}')
def go_to_link(repo):
    browser.element(by.link_text(repo)).click()

@allure.step('Переходим во вкладку issues')
def go_to_issues():
    browser.element('#issues-tab').click()

@allure.step('Проверяем наличие задачи')
def checking_the_task():
    browser.element(by.partial_text('#76')).should(be.visible)

def test_decorator_steps():
    browser_open_github()
    search_repo('eroshenkoam/allure-example')
    go_to_link('eroshenkoam/allure-example')
    go_to_issues()
    checking_the_task()