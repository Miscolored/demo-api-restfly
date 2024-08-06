# demo-api-restfly
Demonstration of using RESTfly to wrap Reqres API call

# instructions
If you've got the time do you want to try and wrap up the fake list users API here: https://reqres.in/ using RestFly: https://restfly.readthedocs.io/en/latest/

The finished code should wrap up the API and be able to iterate through all pages of data.

# implementation notes
`app.py` demonstrates calls to demo.ReqresAPI object - wrapped `reqres.in/api` using RESTfly.

# usage
`pip install -r requirements.txt`
`python app.py`

# testing notes
known to support python 3.8.5
pre-commit is used to enfore some standards, run `pre-commit run --all-files` to check your staged changes manually prior to attempting commit.
