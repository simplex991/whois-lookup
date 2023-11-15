import whois
import json

domain = input("Enter the domain name: ")
whois_info = whois.whois(domain)
registrar = whois_info.registrar
creation_date = whois_info.creation_date
expiration_date = whois_info.expiration_date
name_servers = whois_info.name_servers
whois_info_dict = {
    "Registrar Name" : registrar,
    "Creation Date" : creation_date,
    "Expiration Date" : expiration_date,
    "Name Servers": name_servers
}
print(json.dumps(whois_info_dict, indent=4, sort_keys=False, default=str))