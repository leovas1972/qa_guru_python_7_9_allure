import allure
from selene import browser, by, be


def test_dunamic_steps():
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переход по ссылке'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переходим во вкладку issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие задачи'):
        browser.element(by.partial_text('#76')).should(be.visible)
