from requests import request
import pytest
import requests
from lib.utils import build_request_headers

def test_get_all_comments1(login_as_admin):
    request_header = build_request_headers(login_as_admin)
    response = requests.get("http://localhost:8080/comments", headers = request_header)
    assert response.ok
    
    
def test_get_all_comments2(login_as_admin):
    request_header = build_request_headers(login_as_admin)
    response = requests.get("http://localhost:8080/comments", headers = request_header)
    assert response.ok