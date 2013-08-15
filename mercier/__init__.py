from pupa.scrape import Jurisdiction

from .people import MercierPersonScraper
from utils import lxmlize

import re

class Mercier(Jurisdiction):
  jurisdiction_id = 'ca-qc-mercier'
  geographic_code = 2466072
  def get_metadata(self):
    return {
      'name': 'Mercier',
      'legislature_name': 'Mercier City Council',
      'legislature_url': 'http://www.ville.mercier.qc.ca/02_viedemocratique/default.asp',
      'terms': [{
        'name': '2010-2014',
        'sessions': ['2010-2014'],
        'start_year': 2010,
        'end_year': 2014,
      }],
      'provides': ['people'],
      'parties': [],
      'session_details': {
        '2010-2014': {
          '_scraped_name': '2010-2014',
        }
      },
      'feature_flags': [],
    }

  def get_scraper(self, term, session, scraper_type):
    if scraper_type == 'people':
        return MercierPersonScraper

  def scrape_session_list(self):
    return ['2010-2014']
    