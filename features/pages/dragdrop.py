from numpy.testing import assert_equal
from selenium.webdriver import ActionChains
from browser import Browser
object_to_drag = "draggable"
object_to_drop = "droppable"


class drag_drop(Browser):

    def drag(self):
        source1 = self.driver.find_element_by_id(object_to_drag)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source1, 135, 22).perform()
    def affi(self):
        target1 = context.browser.find_element_by_id('droppable')
        assert_equal('Dropped!', target1.text)
        return target1
    def setUp(self, link):
        self.driver.get(link)

