#!/usr/bin/python3
"""If the HTTP status code is greater than or equal to 400,
   print: Error code: followed by the value of the HTTP status code
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    request_response = get(argv[1])
    if request_response.status_code >= 400:
        print(f"Error code: {request_response.status_code}")
    else:
        print(request_response.text)
