import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def test_search0(setup):
    print("test search")
    driver = setup

    driver.get("https://google.com")

    driver.find_element_by_name("q").send_keys("selenium")

    driver.find_element_by_name("btnK").submit()

    assert("Selenium" in driver.page_source)


def test_search1(setup):
    print("test 1")
    driver = setup

    driver.get("https://google.com")

    driver.find_element_by_name("q").send_keys("Software automation")

    driver.find_element_by_name("btnK").submit()

    assert("Test automation" in driver.page_source)


def test_search2(setup):
    print("test search2")
    driver = setup

    driver.get("http://the-internet.herokuapp.com/")

    assert("Welcome to the-internet" in driver.page_source)


def test_search3(setup):
    print("test search3")


def test_search4(setup):
    print("test search4")


def test_search5(setup):
    print("test search5")


@pytest.fixture(scope="function")
def setup():
    caps = DesiredCapabilities.CHROME
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=caps)
    yield driver
    driver.quit()