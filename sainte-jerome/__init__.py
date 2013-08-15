from pupa.scrape import Jurisdiction

from .people import Sainte_JeromePersonScraper
from utils import lxmlize

import re

class Sainte_Jerome(Jurisdiction):
  jurisdiction_id = 'ca-on-burlington'
  geographic_code = 2475017
  def get_metadata(self):
    return {
      'name': 'Sainte-Jerome',
      'legislature_name': 'Sainte-Jerome City Council',
      'legislature_url': 'http://www.ville.saint-jerome.qc.ca/pages/aSavoir/conseilMunicipal.aspx',
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
        return Sainte_JeromePersonScraper

  def scrape_session_list(self):
    return ['2010-2014']
    