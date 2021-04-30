# coding=utf-8
"""Try to access the logs page. feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.options.logs import PageLogs  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import SimpleUserFactory  # pylint: disable=import-error
from pbraiders.user import DisabledUserFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/logs/logs.feature')


@scenario('Accessing the logs page.')
def test_accessing_the_logs_page():
    """Accessing the logs page.."""


@scenario('Not accessing the logs page.', example_converters=dict(type=str))
def test_not_accessing_the_logs_page():
    """Not accessing the logs page.."""


@when('I am the admin user')
def i_am_the_admin_user(the_config, the_browser, the_database) -> None:
    """I am the admin user."""
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, AdminUserFactory().initialize(the_config["data"]["users"]))
    del p_page_signin


@when('I am the <type> user')
def i_am_the_type_user(the_config, the_browser, type) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    switcher = {
        "admin": AdminUserFactory().initialize(the_config["data"]["users"]),
        "simple": SimpleUserFactory().initialize(the_config["data"]["users"]),
        "deactivated": DisabledUserFactory().initialize(the_config["data"]["users"]),
    }
    # Connect
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    assert p_page_signin.sign_out().visit() is True
    p_page_signin.set_user(switcher.get(type, None)).fill_credential().click()
    del p_page_signin


@then('I cannot access to the logs page')
def i_cannot_access_to_the_logs_page(the_config, the_browser) -> None:
    """I cannot access to the logs page."""
    p_page_logs = PageLogs(browser=the_browser, config=the_config['urls'])
    assert p_page_logs.visit() is False


@then('I can access to the logs page')
def i_can_access_to_the_logs_page(the_config, the_browser) -> None:
    """I can access to the logs page."""
    p_page_logs = PageLogs(browser=the_browser, config=the_config['urls'])
    assert p_page_logs.visit() is True
