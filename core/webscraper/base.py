"""base class for RPA"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
)
import time
from typing import Literal


class RPA_BASE:
    def __init__(self) -> None:
        pass

    @staticmethod
    def return_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("--disable-skia-runtime-opts")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        return driver

    @staticmethod
    def return_element(
        driver,
        element_id: str,
        element_type: Literal["xpath", "link_text"] = "xpath",
        wait_time=10,
        implicit_wait=10,
        verbose: bool = True,
    ) -> WebElement | None:
        map = {"xpath": By.XPATH, "link_text": By.LINK_TEXT}
        try:
            driver.implicitly_wait(implicit_wait)
            element = WebDriverWait(
                driver,
                wait_time,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(EC.presence_of_element_located((map[element_type], element_id)))

        except TimeoutException:
            print("timeout occured when returning element")
            return False
        if verbose:
            return element
        else:
            return None

    @staticmethod
    def wait_and_click(
        driver,
        element_id: str,
        element_type: Literal["xpath", "link_text"] = "xpath",
        wait_time=10,
        verbose: bool = False,
    ) -> WebElement | None:
        """
        Wait for an element to be clickable and then click it.
        """
        map = {"xpath": By.XPATH, "link_text": By.LINK_TEXT}
        not_success = True
        attempts = 0
        while not_success:
            try:
                element = WebDriverWait(
                    driver,
                    wait_time,
                    ignored_exceptions=(
                        NoSuchElementException,
                        StaleElementReferenceException,
                    ),
                ).until(EC.element_to_be_clickable((map[element_type], element_id)))
                element.click()
                not_success = False
                if verbose:
                    return element
                else:
                    return None

            except StaleElementReferenceException:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(
                    "StaleElementReferenceException occured when waiting and clicking"
                )
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time")
                    return False
            except ElementNotInteractableException:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(
                    "ElementNotInteractableException occured when waiting and clicking"
                )
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time")
                    return False
            except Exception as e:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(f"{e} occured when waiting and clicking")
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time for waiting and clicking")
                    return False
            return False

    @staticmethod
    def scroll_and_click(
        driver,
        element_id: str,
        element_type: Literal["xpath", "link_text"] = "xpath",
        wait_time=10,
        verbose: bool = False,
    ) -> WebElement | None:
        """scroll to an element and click it"""
        map = {"xpath": By.XPATH, "link_text": By.LINK_TEXT}
        not_success = True
        attempts = 0
        while not_success:
            try:
                element = WebDriverWait(driver, wait_time).until(
                    EC.element_to_be_clickable((map[element_type], element_id))
                )
                driver.execute_script("arguments[0].scrollIntoView();", element)
                element.click()
                not_success = False
                if verbose:
                    return element
                else:
                    return None

            except StaleElementReferenceException:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(
                    "StaleElementReferenceException occured when waiting and clicking"
                )
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time")
                    return False
            except ElementNotInteractableException:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(
                    "ElementNotInteractableException occured when waiting and clicking"
                )
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time")
                    return False
            except Exception as e:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(f"{e} occured when waiting and clicking")
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time for waiting and clicking")
                    return False
            return False

    @staticmethod
    def change_frame(
        driver,
        element_id: str,
        element_type: Literal["xpath", "link_text"] = "xpath",
        wait_time=10,
        verbose: bool = False,
    ) -> WebElement | None:
        """scroll to an element and click it"""
        map = {"xpath": By.XPATH, "link_text": By.LINK_TEXT}
        try:
            frame = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((map[element_type], element_id))
            )
            driver.switch_to.frame(frame)
        except TimeoutException:
            pass
        except ElementClickInterceptedException:
            pass
        if verbose:
            return frame
        else:
            return None

    def send_keys_pick_first_option(
        self, driver, keys_to_send: str, element_id, element_type="xpath"
    ) -> None:
        """sends keys to a drop-down combobox, then picks the first option"""
        not_success = True
        attempts = 0
        while not_success:
            try:
                input_box = self.return_element(
                    driver=driver,
                    element_id=element_id,
                    element_type=element_type,
                )
                input_box.send_keys(keys_to_send)
                time.sleep(0.5)
                actions = ActionChains(driver=driver)
                actions.send_keys(Keys.DOWN * 1)
                actions.send_keys(Keys.ENTER * 1)
                actions.perform()
                not_success = False
            except StaleElementReferenceException:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(
                    "StaleElementReferenceException occured when waiting and clicking"
                )
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time")
                    return False
            except ElementNotInteractableException:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(
                    "ElementNotInteractableException occured when waiting and clicking"
                )
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time")
                    return False
            except Exception as e:
                if attempts == 0:
                    error_began = time.time()
                    attempts += 1
                print(f"{e} occured when waiting and clicking")
                if time.time() - error_began > 10:
                    # exit loop
                    print("exceeding waiting time for waiting and clicking")
                    return False
            return False
