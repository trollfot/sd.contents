# -*- coding: utf-8 -*-

from zope.schema import Int
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
_ = MessageFactory("sd")


class IPossibleBatchProvider(Interface):
    """Marker interface for items that can possibily provide
    their contents in a batch way (eg. Folder, BTree, Topic...).
    """

class IBatchProvider(IPossibleBatchProvider):
    """Can provide a batch with a given number of item.
    """
    batch_size = Int(
        title=_(u"batch_size", default="Size of the batch"),
        default=0,
        description=_(u"batch_size_desc",
                      default=(u"Number of items rendered."
                               u"Zero disables the  batch."))
        )
