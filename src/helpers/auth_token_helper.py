import requests

def get_auth_token(username: str, password: str, base_url:str):
    requests.urllib3.disable_warnings()

    auth_token_request = \
        requests.post(base_url + "/adm-login",verify=False,
                      headers={
                        "Content-type":"application/json; charset-utf-8"
                    },
                    json={
                        "email":username,
                        "password":password
                    })

    json_response = auth_token_request.json()
    return json_response['auth_token']