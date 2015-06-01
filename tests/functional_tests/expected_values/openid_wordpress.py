import fixtures
from authomatic.providers import openid

conf = fixtures.get_configuration('openid_wordpress')

CONFIG = {
    'logout_url': 'https://peterhudec.wordpress.com/wp-login.php?action=logout',
    'login_url': 'https://wordpress.com/wp-login.php',
    'login_xpath': '//*[@id="user_login"]',
    'password_xpath': '//*[@id="user_pass"]',
    'consent_xpaths': [
        '//*[@id="main"]/div/form/p[3]/input[2]',
    ],
    'after_login_wait_seconds': 1,
    'class_': openid.OpenID,
    'user': {
        'id': conf.user_id,
        'email': conf.user_email,
        'username': None,
        'name': conf.user_name,
        'first_name': None,
        'last_name': None,
        'nickname': conf.user_nickname,
        'birth_date': None,
        'city': None,
        'country': None,
        'gender': None,
        'link': None,
        'locale': None,
        'location': None,
        'phone': None,
        'picture': None,
        'postal_code': None,
        'timezone': None,
    },
}