from database import Database

db = Database()


def continents():
    sql = f'''SELECT DISTINCT continent
              FROM country'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def countries_by_continent(continent):
    sql = f'''SELECT iso_country, name
              FROM country
              WHERE continent = %s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (continent,))
    result = cursor.fetchall()
    return result


def airports_by_country(country):
    sql = f'''SELECT ident, name, latitude_deg, longitude_deg
              FROM airport
              WHERE iso_country = %s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (country,))
    result = cursor.fetchall()
    return result


def airport(icao):
    sql = f'''SELECT name, latitude_deg, longitude_deg
              FROM airport
              WHERE ident = %s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


# get continents
print('Continents: ', continents())

# get countries by continent
continent = input('type continent code: ')
print(f'''Countries in : {continent}''', countries_by_continent(continent))

# get all by country
country = input('type country code: ')
aps = airports_by_country(country)
print(f'''Airports in {country}: ''', aps)

# get one by icao
icao = input('type icao: ')
ap = airport(icao)
print(ap)
print(f'''Name: {ap['name']}, latitude: {ap['latitude_deg']}, longitude: {ap['longitude_deg']}''')
