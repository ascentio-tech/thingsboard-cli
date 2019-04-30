import requests
import thingsboard_client as tb

def authenticate(url, username, password):
  path = "{}/api/auth/login".format(url)
  response = requests.post(url=path, json={'username':username, 'password':password})
  if response.status_code == requests.codes.ok:
    return True, response.json()['token']
  else:
    return False, ''


def create_api_client(url, username, password, token):
  configuration = tb.Configuration()
  configuration.username = username
  configuration.password = password
  configuration.host = url
  configuration.verify_ssl = False
  configuration.api_key['X-Authorization'] = token
  configuration.api_key_prefix['X-Authorization'] = 'Bearer'
  return tb.ApiClient(configuration=configuration)


def raw_get(api_client):
    conf = api_client.configuration
    auth = conf.auth_settings
    path = '{}/api/{}'.format(conf.host, path)
    api_key = conf.get_api_key_with_prefix('X-Authorization')
    return requests.get(url=path,headers={'X-Authorization': api_key})
