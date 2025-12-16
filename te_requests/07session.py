import requests
from urllib.parse import urljoin
from functools import wraps

class loginTest:
    accessToken_endpoint = "/auth/refresh" 
    login_endpoint = "/auth/login"
    load_Data_endpoint = "/auth/me"

    def __init__(self,url,headers):
        self.BASE_URL = url
        self.endpoint = "a"
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.accessToken = None
        self.refreshToken = None
    
    def auto_refresh_token(func):
        """Decorator that automatically refreshes the token and re-executes the request"""        
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # first attempt 
            result = func(self, *args, **kwargs)
            
            # If the result was False (i.e. 401), refresh the token.
            if result is False:
                print("🔄 Auto refreshing token...")
                if self.refresh_access_token():
                    print("♻️ Retrying request with new token...")
                    # Try again with a new token.
                    return func(self)
                else:
                    print("❌ Token refresh failed, please login again")
                    return False
            return result
        return wrapper

    def login_session(self,username,password,endpoint = None):

        login_data = {
            'username': username,
            'password': password,
        }
        if endpoint is None:
            endpoint = self.login_endpoint

        login_url = urljoin(self.BASE_URL, endpoint)
        response = self.session.post(login_url, json= login_data)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Login successful!")
            self.accessToken = data['accessToken']
            self.refreshToken = data['refreshToken']
            print(f"🔑 accessToken: {self.accessToken}")
            print(f"🔑 refreshToken: {self.refreshToken}")
            
        else:
            print(f"❌ Login error: {response.status_code}")
    
    @auto_refresh_token
    def load_Data(self,accessToken = None,endpoint = None ):
        if endpoint is None:
            endpoint = self.load_Data_endpoint
        
        token = accessToken if accessToken else self.accessToken

        load_url = urljoin(self.BASE_URL, endpoint)
        self.session.headers.update({
            'Authorization': f"Bearer {token}"
        })
        response = self.session.get(load_url)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ load_Data successful!")
            print(f"username: {data['username']}")
            print(f"email: {data['email']}")
            return True
        elif response.status_code == 401:
            print(f"❌ accessToken error: {response.status_code}")
            return False
        else:
            print(f"❌ load_Data: {response.status_code}")
            return False

    def refresh_access_token(self,endpoint = None):
        if endpoint is None:
            endpoint = self.accessToken_endpoint
        load_url = urljoin(self.BASE_URL, endpoint)
        refreshToken = {'refreshToken': self.refreshToken }
        refresh_headers = {
            'Content-Type': 'application/json'
        }
        response = self.session.post(load_url,json= refreshToken,headers= refresh_headers)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ retrive_accessToken successful!")
            self.accessToken = data['accessToken']
            self.refreshToken = data['refreshToken']
            print(f"🔑 Token: {self.accessToken}")
            print(f"🔑 Token: {self.refreshToken}")
            return True
        else:
            print(f"❌ retrive_accessToken: {response.status_code}")
            return False

try:
    from functools import wraps
    print("functools is installed and works.")
except ImportError:
    print("functools is not installed.")

url = 'https://dummyjson.com'
login_data = {
        'username': 'emilys',
        'password': 'emilyspass'}

headers = { 'Content-Type': 'application/json' }
log = loginTest(url=url,headers= headers)
log.login_session(username= login_data['username'],password= login_data['password'])
log.load_Data()
log.load_Data(accessToken="aaaa")
log.load_Data()
