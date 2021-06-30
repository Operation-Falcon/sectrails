import requests


def subdomain(domain, api, output):
    param={"children_only":"false",
           "include_inactive":"true"}
    header={"Accept": "application/json",
            "APIKEY": f"{api}"}
    r=requests.get(f"https://api.securitytrails.com/v1/domain/{domain}/subdomains?children_only=false&include_inactive=true", params=param, headers=header)
    data=r.json()["subdomains"]
    with open(output, 'w') as file:
        for i in range(0, len(data)):
            try:
                file.writelines("%s%s%s\n"% (data[i], ".", domain))
                print("%s%s%s\n" %(data[i], ".", domain))
            except Exception as e:
                pass

def tags(domain, api, output):
    headers={"Accept":"application/json",
             "APIKEY": f"{api}"}
    r=requests.get(f"https://api.securitytrails.com/v1/domain/{domain}/tags", headers=headers)
    data=r.json()["tags"]
    with open(output, "w") as file:
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data[i])
                print("%s\n" % data[i])
            except Exception as e:
                pass

def details(domain, api, output):
    headers = {"Accept": "application/json",
               "APIKEY": f"{api}"}
    r=requests.get(f"https://api.securitytrails.com/v1/domain/{domain}", headers=headers)
    data=r.json()["current_dns"]
    with open(output, "a") as file:
        file.writelines("TXT:\n")
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data["txt"]["values"][i]["value"])
                print("%s\n" % data["txt"]["values"][i]["value"])
            except Exception as e:\
                    pass
        file.writelines("SOA:\n")
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data["txt"]["values"][i]["value"])
                print("%s\n" % data["txt"]["values"][i]["value"])
            except Exception as e: \
                    pass
        file.writelines("NS:\n")
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data["txt"]["values"][i]["value"])
                print("%s\n" % data["txt"]["values"][i]["value"])
            except Exception as e:\
                    pass
        file.writelines("MX:\n")
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data["txt"]["values"][i]["value"])
                print("%s\n" % data["txt"]["values"][i]["value"])
            except Exception as e:\
                    pass
        file.writelines("AAAA:\n")
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data["txt"]["values"][i]["value"])
                print("%s\n" % data["txt"]["values"][i]["value"])
            except Exception as e:\
                    pass
        file.writelines("A:\n")
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % data["txt"]["values"][i]["value"])
                print("%s\n" % data["txt"]["values"][i]["value"])
            except Exception as e:\
                    pass

def dns(domain, api, output):
    headers={"Accept":"application/json",
             "APIKEY": f"{api}"}
    r=requests.get(f"https://api.securitytrails.com/v1/history/{domain}/dns/a", headers=headers)
    data=r.json()["records"]
    with open(output, "w") as file:
        for i in range(0, len(data)):
            for j in range(0, len(data[i]["values"])):
                try:
                    file.writelines("%s\n" % data[i]["values"][j]["ip"])
                    print("%s\n" % data[i]["values"][j]["ip"])
                except Exception as e:
                    pass



def whois(domain, api, output):
    headers={"Accept":"application/json",
             "APIKEY": f"{api}"}
    r=requests.get(f"https://api.securitytrails.com/v1/history/{domain}/whois", headers=headers)
    data=r.json()["result"]["items"]
    with open(output, "w") as file:
        for i in range(0, len(data)):
            for j in range(0, len(data[i]["contact"])):
                try:
                    file.writelines("%s\n" % data[i]["contact"][j]["type"])
                    file.writelines("%s\n" % data[i]["contact"][j]["telephone"])
                    file.writelines("%s\n" % data[i]["contact"][j]["street1"])
                    file.writelines("%s\n" % data[i]["contact"][j]["state"])
                    file.writelines("%s\n" % data[i]["contact"][j]["postalCode"])
                    file.writelines("%s\n" % data[i]["contact"][j]["organization"])
                    file.writelines("%s\n" % data[i]["contact"][j]["name"])
                    file.writelines("%s\n" % data[i]["contact"][j]["email"])
                    file.writelines("%s\n" % data[i]["contact"][j]["country"])
                    file.writelines("%s\n" % data[i]["contact"][j]["city"])
                    file.writelines("\n\n")
                    print("%s\n" % data[i]["contact"][j]["type"])
                    print("%s\n" % data[i]["contact"][j]["telephone"])
                    print("%s\n" % data[i]["contact"][j]["street1"])
                    print("%s\n" % data[i]["contact"][j]["state"])
                    print("%s\n" % data[i]["contact"][j]["postalCode"])
                    print("%s\n" % data[i]["contact"][j]["organization"])
                    print("%s\n" % data[i]["contact"][j]["name"])
                    print("%s\n" % data[i]["contact"][j]["email"])
                    print("%s\n" % data[i]["contact"][j]["country"])
                    print("%s\n" % data[i]["contact"][j]["city"])
                    print("\n\n")
                except Exception as e:
                    pass


def neighbours(ip, api, output):
    headers={"Accept":"application/json",
             "APIKEY": f"{api}"}
    r=requests.get(f"https://api.securitytrails.com/v1/ips/nearby/{ip}", headers=headers)
    data=r.json()["blocks"]
    with open(output, "w") as file:
        for i in range(0, len(data)):
            try:
                file.writelines("%s\n" % (data[i]["ip"]))
                print("%s\n" % (data[i]["ip"]))
            except Exception as e:
                pass













