import requests

def get_geolocation(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url).json()

    if response['status'] == 'success':
        print(f"IP Address: {ip_address}")
        print(f"Country: {response['country']}")
        print(f"Region: {response['regionName']}")
        print(f"City: {response['city']}")
        print(f"Latitude: {response['lat']}, Longitude: {response['lon']}")
        print(f"ISP: {response['isp']}")
    else:
        print(f"Failed to get geolocation for IP: {ip_address}")

if __name__ == "__main__":
    ip = input("Enter an IP address: ")
    get_geolocation(ip)
