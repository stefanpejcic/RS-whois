import whois
import time

MAX_RETRIES = 3
DELAY_BETWEEN_RETRIES = 2  # Increase delay to 2 seconds

def get_expiry_date_with_retry(domain):
    for _ in range(MAX_RETRIES):
        try:
            data = whois.whois(domain)
            expiry_date = data.expiration_date
            if isinstance(expiry_date, list):
                return expiry_date[0]  # Use the first expiry date if it's a list
            return expiry_date
        except whois.parser.PywhoisError as e:
            print(f"Error: {e}")
            print(f"Retrying for {domain}...")
            time.sleep(DELAY_BETWEEN_RETRIES)

    return None  # Return None if unable to fetch the expiry date after retries

def main():
    input_file = "domains/2.txt"
    output_file = "expiry/2.txt"

    with open(input_file, "r") as input_file:
        domains = input_file.read().splitlines()

    with open(output_file, "w") as output_file:
        output_file.write("Domain,Expiry Date\n")  # Header line

        for domain in domains:
            expiry_date = get_expiry_date_with_retry(domain)
            if expiry_date:
                output_line = f"{domain},{expiry_date}\n"
                output_file.write(output_line)
                print(f"Processed {domain} - Expiry Date: {expiry_date}")
            else:
                print(f"Unable to fetch data for {domain}")

            time.sleep(0.1)  # Introduce a 100ms delay between WHOIS queries

if __name__ == "__main__":
    main()
