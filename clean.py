

import json
import pandas as pd


def clean_title(data):
  size =  len(data['_source'])
  for i in range(0,size):
    remove = False
    if 'zoom' in data['_source'][i]['title']:
      remove = True
    elif 'Office Hour' in data['_source'][i]['title']:
      remove = True
    elif 'Gradescope' in data['_source'][i]['title']:
      remove = True
    elif 'submission' in data['_source'][i]['title']:
      remove = True
    if remove == True:
      data = data.drop(i)
  return data


