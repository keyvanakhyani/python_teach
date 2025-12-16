import requests
from urllib.parse import urljoin

class AutoRefreshSession(requests.Session):
    def __init__(self, login_instance):
        super().__init__()
        self.login_instance = login_instance
    
    def request(self, method, url, **kwargs):
        print(method,url,kwargs)
        response = super().request(method, url, **kwargs)

        # If we get 401, try a refresh token

        if response.status_code == 401:
            print(f"🔄 Auto-refreshing token...")
            self.login_instance.refresh_access_token()
            
            # Update header
            self.headers.update({
                'Authorization': f"Bearer {self.login_instance.accessToken}"
            })
            
            # try agane
            response = super().request(method, url, **kwargs)
            
            # If we get 401 a second time, we need to complete the login.
            if response.status_code == 401:
                print(f"⚠️ Refresh token failed! Re-logging in...")
                self.login_instance.login()  
                
                # Update header with new token
                self.headers.update({
                    'Authorization': f"Bearer {self.login_instance.accessToken}"
                })
                
                # Third and final attempt
                response = super().request(method, url, **kwargs)
                
                # If we still get 401, the user must log in manually
                if response.status_code == 401:
                    raise Exception("❌ Authentication failed completely! Please check your credentials.")
        
        return response
class loginTest2:
    accessToken_endpoint = "/auth/refresh" 
    login_endpoint = "/auth/login"
    load_Data_endpoint = "/auth/me"

    def __init__(self, url, headers):
        self.BASE_URL = url
        self.session = AutoRefreshSession(self) 
        self.session.headers.update(headers)
        self.accessToken = None
        self.refreshToken = None
    
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
            # print(f"🔑 accessToken: {self.accessToken}")
            # print(f"🔑 refreshToken: {self.refreshToken}")
            
        else:
            print(f"❌ Login error: {response.status_code}")
    
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
        elif response.status_code == 401:
            print(f"❌ accessToken error: {response.status_code}")
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
        else:
            print(f"❌ retrive_accessToken: {response.status_code}")
    

if __name__ == "__main__":
    headers = { 'Content-Type': 'application/json' }
    url = 'https://dummyjson.com'
    login_data = {
        'username': 'emilys',
        'password': 'emilyspass'}
    log = loginTest2(url=url,headers= headers)
    log.login_session(username= login_data['username'],password= login_data['password'])
    log.load_Data()
    log.load_Data(accessToken="aaaa")
    log.load_Data()