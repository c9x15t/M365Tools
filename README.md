# M365Tools - Tenant Checker

This script allows you to check if a Microsoft 365 domain is **unknown** or **managed** using the Microsoft Online API. It outputs the relevant information in the terminal.

## Features
- Quickly query the status of a domain against Microsoft 365.
- Determine if a domain is **unknown** (not associated with M365) or **managed** (associated with M365).
- Simple to use, with clear and concise output.

## Prerequisites
- Python 3.x installed on your system.
- The `requests` library installed. Install it using:

  ```bash
  pip install requests
  ```

## Usage
1. Clone or download the repository to your local machine.
2. Navigate to the folder containing the script.
3. Run the script using Python:

   ```bash
   python m365tenantcheck.py
   ```

4. When prompted, enter the domain you want to check (e.g., `example.com`).
5. The script will query the Microsoft Online API and display the result in your terminal.

### Example Output
- If the domain is **unknown**:
  ```
  NameSpaceType: Unknown
  ```
- If the domain is **managed**:
  ```
  NameSpaceType: Managed
  ```

## Notes
- Ensure you have a stable internet connection when running the script.
- This script is designed for informational purposes and should not be used for unauthorized testing or activities.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to suggest improvements or contribute to this project!
