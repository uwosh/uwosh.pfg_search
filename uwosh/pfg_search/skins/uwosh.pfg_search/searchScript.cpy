# imports
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

def build_date_query(fromDate, toDate):
    date_list = list()  
    date_list.append(DateTime(fromDate))
    date_list.append(DateTime(toDate))
    return {"query":date_list, "range":"minmax"}  

#-------------------------------------------------

print 'The Demons are coming'

import pdb; pdb.set_trace()
state.setNextAction('traverse_to:string:pfg-search_results_view')
return state
