import requests
import re

def check_domain_realm():
    # Prompt the user to enter a domain
    domain = input("Enter the domain to check (e.g., example.com): ")

    # Construct the URL with the domain dynamically injected
    url = f"https://login.microsoftonline.com/getuserrealm.srf?login={domain}&xml=1"

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Use regex to extract the value within <NameSpaceType> tags
            match = re.search(r'<NameSpaceType>(.*?)</NameSpaceType>', response.text)
            if match:
                # Print only the extracted <NameSpaceType> value
                namespace_type = match.group(1)
                print("NameSpaceType:", namespace_type)
            else:
                print("No <NameSpaceType> tag found in the response.")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Run the function
check_domain_realm()
