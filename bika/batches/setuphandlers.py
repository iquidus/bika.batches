""" Bika setup handlers. """

from bika.batches.permissions import *


class Empty:
    pass


def setupAnalyticaVarious(context):
    """ Setup Bika site structure """

    if context.readDataFile('bika.batches.txt') is None:
        return
    # portal = context.getSite()
