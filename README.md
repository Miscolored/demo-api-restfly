[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Miscolored/demo-api-restfly/main.svg)](https://results.pre-commit.ci/latest/github/Miscolored/demo-api-restfly/main)
# demo-api-restfly
Demonstration of using RESTfly to wrap Reqres API call

# instructions
If you've got the time do you want to try and wrap up the fake list users API here: https://reqres.in/ using RestFly: https://restfly.readthedocs.io/en/latest/

The finished code should wrap up the API and be able to iterate through all pages of data.

# usage
`pip install -r requirements.txt`

`python app.py`

`pip install -r test-requirements.txt`

`pre-commit run -a`

`pytest --verbose`

# notes
known to support python 3.8.5, others untested
