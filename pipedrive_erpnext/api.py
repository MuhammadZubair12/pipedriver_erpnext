import requests

@frappe.whitelist(allow_guest=True)
def test_pipedrive_token():
    api_token = frappe.get_doc("Pipedrive Integration")
    url = 'https://api.pipedrive.com/v1/users/me'
    headers = {'Authorization': f'Bearer {api_token}'}
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print('Token is valid and working correctly.')
    else:
        print('Token is invalid or there was an error.')

    # Optionally, print the response content for further inspection
    print(response.json())
