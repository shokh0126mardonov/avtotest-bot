import requests
from pprint import pprint

request = requests.get(
    url="http://testapi.sammkk.uz/api/TestCase/GetAll",
    params={
        "language":"uz",
        "isRandom":"true",
        "pageSize":2,
    }
)

result = request.json().get("result",False)


pprint(result)