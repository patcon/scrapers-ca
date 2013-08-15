from pupa.scrape import Jurisdiction

from .people import Wood_BuffaloPersonScraper
from utils import lxmlize

import re

class Wood_Buffalo(Jurisdiction):
  jurisdiction_id = 'ca-on-burlington'
  geographic_code = 4816037
  def get_metadata(self):
    return {
      'name': 'Wood Buffalo',
      'legislature_name': 'Wood Buffalo City Council',
      'legislature_url': 'http://www.woodbuffalo.ab.ca/Municipal-Government/Mayor-and-Council/Councillor-Profiles.htm',
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
        return Wood_BuffaloPersonScraper

  def scrape_session_list(self):
    return ['2010-2014']
    