try:
    from pprint import pprint
    import requests
    from lxml import html
    from territory.models import Region, District, PollingStation
except Exception as e:
    print(e)
    exit(1)
"""
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'VoterSurveySyste',
            'USER': 'systemadmin',
            'PASSWORD': '12345678',
            'HOST': 'localhost',
            'PORT': '',
        }
    },
    INSTALLED_APPS=[
        'territory',
    ]
)
import django

django.setup()
"""



BASE_URL = 'https://www.drv.gov.ua/portal/{}'
URL = 'https://www.drv.gov.ua/portal/!cm_core.cm_index?option=ext_dvk&prejim=2'


def get_regions(URL):
    page = requests.get(URL)
    tree = html.fromstring(page.content)
    table = tree.xpath('//*[@id="tab1"]')[0].getchildren()

    regions = []
    for row in table:
        children = row.getchildren()
        if not all(child.tag == 'td' for child in children):
            continue

        url = children[0].getchildren()[0].attrib.get('href', None)
        if url is None: continue

        name = children[0].getchildren()[0].text

        regions.append({'url': BASE_URL.format(url), 'name': name})

    return regions


def get_districts(region_url):
    page = requests.get(region_url)
    tree = html.fromstring(page.content)
    table = tree.xpath('//*[@id="tab3"]')[0].getchildren()

    districts = []
    city = None
    for row in table:
        children = row.getchildren()

        # Skipping header
        if not all(child.tag == 'td' for child in children): continue

        elem = children[0].getchildren()[0]

        # If city appears
        if elem.tag == "b":
            city = elem.text
            continue

        url = elem.attrib.get('href', None)
        if url is None: continue

        name = elem.text
        d = {
            'url': BASE_URL.format(url),
            'name': name,
            'city': city
        }
        districts.append(d)
        pprint(d)
    return districts


def get_stations(district_url):
    page = requests.get(district_url)
    tree = html.fromstring(page.content)

    stations = []
    for table in tree.xpath('//*[@id="tab3"]'):
        for row in table.getchildren():
            children = row.getchildren()
            # Skipping header
            if not all(child.tag == 'td' for child in children): continue

            d = {
                'name': children[0].text,
                'description': children[1].text,
                'address': children[2].text,
            }
            stations.append(d)
            pprint(d)
        return stations


def run():

    regions = get_regions(URL)
    Region.objects.all().delete()

    districts = []
    for region in regions:

        r = Region(name=region['name'])
        r.save()

        district = get_districts(region["url"])

        for d in district:
            d.update({'region': r})

        districts += district

    stations = []
    for district in districts:

        d = District(name=district['name'], city=district['city'], region=district['region'])
        d.save()

        station = get_stations(district['url'])
        for s in station:
            s.update({'district': d})

        stations += station

    for station in stations:
        s = PollingStation(
            number=station['name'],
            description=station['description'],
            address=station['address'],
            district=station['district'],
        )
        s.save()

        # todo: write stations to database
