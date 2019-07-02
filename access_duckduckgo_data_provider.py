# pip3 install unittest-data-provider
import unittest
from selenium import webdriver
from unittest_data_provider import data_provider


class TestDuckDuckGo(unittest.TestCase):


    searchData = lambda: [
        ['Selenium and Python', 'python'],
        ['Selenium and Python', 'selenium'],
        ['Udemy wikipedia', 'wiki'],
    ]

    @data_provider(searchData)
    def test_access_duckduckgo(self, search_string, expected_string):
        # Access DuckDuckGo
        driver = webdriver.Chrome()
        driver.get("https://duckduckgo.com/")

        # Insert the search text

        search_input = driver.find_element_by_id("search_form_input_homepage")
        search_input.send_keys(search_string)

        # Perform the search

        search_button = driver.find_element_by_id("search_button_homepage")
        search_button.click()

        # Find the text of the third link

        results_area = driver.find_element_by_id("links")
        results = results_area.find_elements_by_class_name("result")
        third_result = results[2]
        extras = third_result.find_element_by_class_name("result__extras")
        url_extra = extras.find_element_by_class_name("result__extras__url")
        url_link = url_extra.find_element_by_class_name("result__url")

        url_text = url_link.get_attribute("href")

        driver.close()

        assert expected_string in url_text


if __name__ == '__main__':
    unittest.main()