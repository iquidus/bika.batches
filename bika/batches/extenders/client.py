from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.batches import bikaMessageFactory as _
from bika.lims.fields import *
from bika.lims.interfaces import IClient
from Products.Archetypes.public import *
from Products.Archetypes.references import HoldingReference
from zope.component import adapts
from zope.interface import implements

import sys

class ClientSchemaExtender(object):
    adapts(IClient)
    implements(IOrderableSchemaExtender)

    fields = [
        ExtStringField(
            'ClientUMFHA',
            required=False,
            widget=StringWidget(
                label=_('UMFHA #'),
            ),
        ),
    ]

    def __init__(self, context):
      self.context = context

    def getOrder(self, schematas):
        default = schematas['default']
        to_insert = [{'name': 'ClientUMFHA', 'before': 'BulkDiscount'}]
        for field in to_insert:
            name = field['name']
            if name in default:
                default.remove(name)
            default.insert(default.index(field['before']), name)
        return schematas

    def getFields(self):
        return self.fields