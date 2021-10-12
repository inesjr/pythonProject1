import time
from behave import given,when,then
from numpy.testing import assert_equal
from selenium.webdriver import ActionChains

import features


@given(u'the user is on the home page')
def step_impl(context):

    context.dd.setUp('https://qavbox.github.io/demo/dragndrop/')


@when(u'he drag and drop the grey box in the blue box')
def step_impl(context):

    context.dd.drag()
    time.sleep(5)


@then(u'he sees a message "Dropped!"')
def step_impl(context):
    target1 = context.browser.find_element_by_id('droppable')
    assert_equal('Dropped!', target1.text)


