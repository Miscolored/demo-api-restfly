from __future__ import annotations

from reqres.api import API as ReqresAPI

reqres_api = ReqresAPI()

for user in reqres_api.users.list():
    print(user)
