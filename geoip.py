import geoip2.database

with geoip2.database.Reader('ipdat\\GeoLite2-City.mmdb') as reader:
    response = reader.city('128.101.101.101')
    print(response)