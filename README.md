# IP Locator

## Description

The **IP Locator** is a tool designed to fetch and display geographic and network-related information about an IP address. It provides details such as location, ISP, organization, and more using APIs or data sources.

## Features

- Retrieve the geographic location of an IP address.
- Display information such as country, city, latitude, longitude, and ISP.
- Support for both IPv4 and IPv6 addresses.
- Easy-to-use interface or command-line tool.

## Installation

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed on your system.
- API key for a geolocation service like [IPStack](https://ipstack.com/) or [ipinfo.io](https://ipinfo.io/).

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/kylelknight/ip-locator.git
   cd ip-locator
2. Install dependencies:
pip install -r requirements.txt
3. Configure your API key:
Open the config.py file (or equivalent file in your project).
Add your API key to the configuration.

### Usage
Command Line
Run the script with an IP address:

python ip_locator.py <IP_ADDRESS>
