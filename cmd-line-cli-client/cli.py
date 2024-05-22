import requests


def provision_server(hostname, os, specs):
    url = "http://localhost:8000/provision/server"
    data = {"hostname": hostname, "os": os, "specs": specs}
    response = requests.post(url, json=data)
    return response.json()


def provision_network_device(device_type, ip_address, configuration):
    url = "http://localhost:8000/provision/network_device"
    data = {"device_type": device_type,
            "ip_address": ip_address, "configuration": configuration}
    response = requests.post(url, json=data)
    return response.json()


if __name__ == "__main__":
    import sys
    command = sys.argv[1]

    if command == "provision_server":
        hostname = sys.argv[2]
        os = sys.argv[3]
        specs = eval(sys.argv[4])
        result = provision_server(hostname, os, specs)
        print(result)

    elif command == "provision_network_device":
        device_type = sys.argv[2]
        ip_address = sys.argv[3]
        configuration = eval(sys.argv[4])
        result = provision_network_device(
            device_type, ip_address, configuration)
        print(result)
