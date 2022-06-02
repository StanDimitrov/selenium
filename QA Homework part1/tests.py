import requests

def test_api_get():
    resp = requests.get("https://petstore.swagger.io/#")
    assert (resp.status_code == 200), "Status code is not 200. : " + str(resp.status_code)
    for record in resp.json()['category']:
        if record['id'] == 1:
            assert record['name'] == "doggie",\
                "Data not matched! Expected : doggie, found : " + str(record['name'])
            assert record['status'] == "pending",\
                "Data not matched! Expected : pending, but found : " + str(record['status'])

def test_api_post():
    data = {"bread" : "chihuahua",
            "name" : "Sparky",
            "age": "1"}
    resp = requests.post(url="https://petstore.swagger.io/#/pet/uploadFile", data=data)
    data = resp.json()
    assert (resp.status_code == 201), "Status code is not 201. Rather found : "\
        + str(resp.status_code)
    assert data['name'] == "Sparky", "Pet created with wrong name. \
        Expected : Sparky, found : " + str(data['name'])
    assert data['bread'] == "chihuahua", "pet created with wrong bread. \
        Expected : chihuahua, found : " + str(data['name'])