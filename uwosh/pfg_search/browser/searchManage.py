from Products.Five import BrowserView

class SearchManageView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    #return only relevant field ids, things such as fieldsets are of no use
    #returns and accesor to the actual field, enables us to get title and other 
    #attributes
    def getFields(self):
        fields = self.context.fgFields()
        parent = self.context.aq_inner.aq_parent
        
        finalFields = []
        for i in fields:
            widgetName = i.getWidgetName()
            if widgetName is 'FieldsetStartWidget':
                parent = parent[i.getName()]
            elif widgetName is 'FieldsetEndWidget':
                parent = parent.getParentNode()
            else:
                finalFields.append(parent[i.getName()])
        return finalFields

