from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from uwosh.timeslot import timeslotMessageFactory as _

class IPFGSearchForm(Interface):
    pass


class PFGSearchForm(BrowserView):
    implements(IPFGSearchForm)

    pageTemplate = ZopeTwoPageTemplateFile('search_form.pt')

    def __init__(self): pass
