import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"Domain name: {w.domain_name}")
        print(f"Register: {w.register}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"Error: {e}")

target = input('Nhập target: ')
whois_lookup(target)

