from bika.lims.browser.batchfolder import BatchFolderContentsView as _BFCV
from bika.lims import bikaMessageFactory as _


class BatchFolderContentsView(_BFCV):

    def __init__(self, context, request):
        super(BatchFolderContentsView, self).__init__(context, request)
        self.columns.update({
            'Client': {'title': _('Client')},
            'BatchDate': {'title': _('Submitted')},
            'Description': {'title': _('Additional Info')},
        })
        self.columns['Title']['toggle'] = False
        new_states = []
        for state in self.review_states:
            pos = state['columns'].index('BatchID') + 1
            state['columns'].insert(pos, 'Client')
            new_states.append(state)
        self.review_states = new_states

    def folderitems(self):
        items = super(BatchFolderContentsView, self).folderitems()
        for x, item in enumerate(items):
            if not 'obj' in item:
                continue
            obj = items[x]['obj']

            client = obj.Schema().getField('Client').get(obj)
            if client:
                val = client.Schema().getField('Name').get(client)    
                items[x]['Client'] = val
                items[x]['replace']['Client'] = "<a href='%s'>%s</a>" % \
                    (client.absolute_url(), val)
            
            info = obj.Schema().getField('Information').get(obj)
            if info:
                items[x]['Description'] = info

        return items