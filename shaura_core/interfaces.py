# -*- coding: utf-8 -*-
"""Base interfaces and schemas"""

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory as ZopeMessageFactory
_ = ZopeMessageFactory("shaura_core")


class IObjectManager(Interface):
    """Database access utility"""

    def __call__(**kwargs):
        """Query for objects on datastore"""
        pass

    def add(obj):
        """Add object to datastore"""
        # IObjectCreatedEvent should be triggered before before committing new
        # object to datastore.
        pass

    def update(obj):
        """Update object on datastore"""
        # IObjectModifiedEvent should be triggered before committing updated
        # object to datastore.
        pass

    def delete(obj):
        """Delete object from datastore"""
        # IObjectObsoletedEvent should be triggered before deleting object from
        # datastore.
        pass


class IObject(Interface):
    """Object"""

    def __init__(**kwargs):
        """Objects should init their properties from **kwargs during init"""
        pass


class IObjectEvent(Interface):
    """Abstract object lifecycle event"""

    target = schema.Object(
        title=_("event_target",
                default=u"Event target object"),
        schema=IObject,
        required=True
        )


class IObjectCreatedEvent(Interface):
    """Object created lifecycle event"""
    # IObjectCreatedEvent should be triggered before before committing new
    # object to datastore.

class IObjectModifiedEvent(Interface):
    """Object modified lifecycle event"""
    # IObjectModifiedEvent should be triggered before committing updated object
    # to datastore.


class IObjectObsoletedEvent(Interface):
    """Object obsoleted lifecycle event"""
    # IObjectObsoletedEvent should be triggered before deleting object from
    # datastore.
