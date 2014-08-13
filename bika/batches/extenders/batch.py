from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.batches import bikaMessageFactory as _
from bika.lims.fields import *
from bika.lims.interfaces import IBatch
from Products.Archetypes.public import *
from Products.Archetypes.references import HoldingReference
from zope.component import adapts
from zope.interface import implements
from plone.indexer import indexer
from bika.lims.browser.fields import HistoryAwareReferenceField
from bika.lims.browser.widgets import ReferenceWidget
from Products.CMFCore import permissions

import sys

class BatchSchemaExtender(object):
    adapts(IBatch)
    implements(IOrderableSchemaExtender)

    fields = [
        ExtStringField(
            'ClientRef',
            required=True,
            widget=StringWidget(
                label=_('Client Reference'),
            ),
        ),
        ExtReferenceField('BContact',
            allowed_types = ('Contact',),
            relationship = 'BatchContact',
           # default_method = 'getContacts',
            referenceClass = HoldingReference,
            vocabulary_display_path_bound = sys.maxint,
            widget=ReferenceWidget(
                label=_("Contact"),
                size=30,
                helper_js=("bika_widgets/referencewidget.js", "++resource++bika.lims.js/contact.js"),
                visible={'edit': 'visible', 'view': 'visible', 'add': 'visible'},
                base_query={'inactive_state': 'active'},
                showOn=True,
                popup_width='300px',
                colModel=[{'columnName': 'UID', 'hidden': True},
                          {'columnName': 'Fullname', 'width': '50', 'label': _('Name')},
                          {'columnName': 'EmailAddress', 'width': '50', 'label': _('Email Address')},
                         ],
            ),
        ),
        ExtReferenceField('InvoiceBContact',
            allowed_types = ('Contact',),
            relationship = 'BatchInvoiceContact',
           # default_method = 'getContacts',
            referenceClass = HoldingReference,
            vocabulary_display_path_bound = sys.maxint,
            widget=ReferenceWidget(
                label=_("Invoice to"),
                size=30,
                helper_js=("bika_widgets/referencewidget.js", "++resource++bika.lims.js/contact.js"),
                visible={'edit': 'visible', 'view': 'visible', 'add': 'visible'},
                base_query={'inactive_state': 'active'},
                showOn=True,
                popup_width='300px',
                colModel=[{'columnName': 'UID', 'hidden': True},
                          {'columnName': 'Fullname', 'width': '50', 'label': _('Name')},
                          {'columnName': 'EmailAddress', 'width': '50', 'label': _('Email Address')},
                         ],
            ),
        ),
        ExtTextField(
            'Information',
            searchable=True,
            default_content_type='text/x-web-intelligent',
            allowable_content_types=('text/plain', ),
            default_output_type="text/plain",
            widget=TextAreaWidget(
                label=_('Additional Information'),
                append_only=False,
                width=70,
            )
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        default = schematas['default']
        to_insert = [{'name': 'BContact', 'before': 'ClientBatchID'},
            {'name': 'InvoiceBContact', 'before': 'ClientBatchID'},
            {'name': 'ClientRef', 'before': 'ClientBatchID'},
            {'name': 'Information', 'before': 'BatchLabels'},
            {'name': 'BatchDate', 'before': 'BatchLabels'}]
        for field in to_insert:
            name = field['name']
            if name in default:
                default.remove(name)
            default.insert(default.index(field['before']), name)
        return schematas

    def getFields(self):
        return self.fields

class BatchSchemaModifier(object):
    adapts(IBatch)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        schema['title'].required = False
        schema['title'].widget.visible = False
        schema['Client'].required = True
        schema['BContact'].required = True
        schema['BContact'].widget.visible = True
        schema['ClientRef'].required = False
        schema['ClientRef'].widget.visible = True
        schema['InheritedObjects'].widget.visible = False
        schema['InheritedObjectsUI'].widget.visible = False
        schema['description'].required = False
        schema['description'].widget.visible = False
        schema['BatchDate'].required = True
        schema['BatchLabels'].widget.visible = False
        schema['InvoiceBContact'].required = True
        schema['ContainerCondition'].required = True
        schema['ContainerCondition'].vocabulary=['Sample(s) due','Acceptable','Compromised']
        schema['ContainerCondition'].widget=SelectionWidget(
            format='radio',
            label=_('Physical Condition'),
            description = _("If compromised then provide more details below."),
        )

        schema['ContainerTemperature'] = ExtStringField(
        'ContainerTemperature',
        default_content_type='text/x-web-intelligent',
        default_output_type="text/plain",
        widget=SelectionWidget(
            format='radio',
            label=_('Temperature on arrival'),
            description = _("The temperature of the sample container on arrival"),
        ),
        vocabulary=['Sample(s) due', 'Frozen', 'Chilled','Ambient'],
        required = True
        )
        return schema

@indexer(IBatch)
def BatchDate(instance):
    return instance.Schema().getField('BatchDate').get(instance)

