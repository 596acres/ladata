import re

from pyquery import PyQuery as pq

from django.conf import settings


def parse_cell_text(cell):
    text = cell.text
    if text:
        # Remove surrounding space
        text = text.strip()

        # Remove extraneous internal space
        text = re.subn('\s+', ' ', text)[0]

    return text


def get_property_information(ain):
    """
    Get the property information from the LA County Assessor's Parcel Viewer:

        http://maps.assessor.lacounty.gov/mapping/viewer.asp
    """

    # Load page with property information
    d = pq(
        url=settings.LADATA_PARCEL_VIEWER_URL + ain,
        headers={ 'user-agent': settings.LADATA_UA }
    )

    # Parse property information, turn it into a dict
    property_information = {}
    for row in d('tr'):
        cells = row.findall('td')
        if len(cells) <= 1:
            continue
        key = parse_cell_text(cells[0])
        value = parse_cell_text(cells[1])
        property_information[key] = value

    return property_information
