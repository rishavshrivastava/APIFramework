import json
import unittest
import requests


class Test(unittest.TestCase):

    def test_Register(self):
        url = "https://reqres.in/api/register"
        try:
            file = open('../Input/Register.json', 'r')
            json_input = file.read()
            request_json = json.loads(json_input)
            response = requests.post(url, request_json)
        except:
            print("Something went wrong while fetching raw data for register")
        finally:
            file.close()

        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/RegisterReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 200
        except:
            print("Something went wrong while typing register response")
            print(response.status_code)
        finally:
            f.close()


    def test_Login(self):
        url = "https://reqres.in/api/login"
        try:
            file = open('../Input/Login.json', 'r')
            json_input = file.read()
            request_json = json.loads(json_input)
            response = requests.post(url, request_json)
        except:
            print("Something went wrong while fetching raw data for login")
        finally:
            file.close()


        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/LoginReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 200
        except:
            print("Something went wrong while typing login response")
            print(response.status_code)
        finally:
            f.close()


    def test_ListUser(self):
        url = "https://reqres.in/api/users?page=1"
        response = requests.get(url)
        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/ListUserReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 200
        except:
            print("Something went wrong while typing list user response")
            print(response.status_code)
        finally:
            f.close()


    def test_DelayedResponse(self):
        url = "https://reqres.in/api/users?delay=3"
        response = requests.get(url)
        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/DelayedResponseReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 200
        except:
            print("Something went wrong while typing delayed response")
            print(response.status_code)
        finally:
            f.close()


    def test_SearchUser(self):
        url = "https://reqres.in/api/users/1"
        response = requests.get(url)
        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/SearchUserReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 200
        except:
            print("Something went wrong while typing search user response")
            print(response.status_code)
        finally:
            f.close()


    def test_UpdateUser(self):
        url = "https://reqres.in/api/users/1"
        try:
            file = open('../Input/UpdateUser.json', 'r')
            json_input = file.read()
            request_json = json.loads(json_input)
            response = requests.put(url, request_json)
        except:
            print("Something went wrong while fetching raw data for update user")
            print(response.status_code)
        finally:
            file.close()

        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/UpdateUserReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 200
        except:
            print("Something went wrong while typing update user response")
            print(response.status_code)
        finally:
            f.close()


    def test_DeleteUser(self):
        url = "https://reqres.in/api/users?page=2"
        response = requests.delete(url)
        try:
            stringResponse = response.content.decode('utf8').replace("'", '"')
            f = open("../Output/DeleteUserReport.json", "w+")
            f.write(stringResponse)
            assert response.status_code == 204
        except:
            print("Something went wrong while typing delete user response")
            print(response.status_code)
        finally:
            f.close()



if __name__ == "__main__":
    unittest.main()
