import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_catalogue_should_see_add_to_basket_button_pass(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button, "basket not found"
    time.sleep(30)
