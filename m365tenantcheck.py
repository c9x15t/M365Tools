import requests
import re

def check_domain_realm_and_openid():
    # Prompt the user to enter a domain
    domain = input("Enter the domain to check (e.g., example.com): ")

    # Check the realm information
    realm_url = f"https://login.microsoftonline.com/getuserrealm.srf?login={domain}&xml=1"
    try:
        # Send a GET request to check the realm
        realm_response = requests.get(realm_url)
        if realm_response.status_code == 200:
            # Use regex to extract the value within <NameSpaceType> tags
            match = re.search(r'<NameSpaceType>(.*?)</NameSpaceType>', realm_response.text)
            if match:
                namespace_type = match.group(1)
                print("NameSpaceType:", namespace_type)
            else:
                print("No <NameSpaceType> tag found in the realm response.")
        else:
            print(f"Failed to retrieve realm data. Status code: {realm_response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking realm: {e}")
        return

    # Check the OpenID configuration to retrieve tenant ID
    openid_url = f"https://login.microsoftonline.com/{domain}/.well-known/openid-configuration"
    try:
        openid_response = requests.get(openid_url)
        openid_response.raise_for_status()  # Raise exception for HTTP errors
        data = openid_response.json()
        
        # Extract the tenant ID
        issuer_url = data.get("issuer", "")
        tenant_id = issuer_url.rstrip("/").split("/")[-1] if issuer_url else "Unknown"
        
        # Print tenant ID and construct the Device Code URL
        print("\n--- OpenID Configuration ---")
        print(f"Tenant ID: {tenant_id}")
        device_code_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/devicecode"
        print(f"Device Code URL: {device_code_url}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while retrieving OpenID configuration: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
check_domain_realm_and_openid()
