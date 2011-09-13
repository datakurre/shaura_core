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
        # WONTFIX: This should be alternative for triggering
        # IObjectCreatedEvent. Nothing else. Redundant, but convenient.
        pass

    def update(obj):
        """Update object on datastore"""
        # WONTFIX: This should be alternative for triggering
        # IObjectModifiedEvent. Nothing else. Redundant, but convenient.
        pass

    def delete(obj):
        """Delete object from datastore"""
        # WONTFIX: This should be alternative for triggering
        # IObjectObsoletedEvent. Nothing else. Redundant, but convenient.
        pass


class IObject(Interface):
    """Objects should support RESTful GET (read), PUT (update) and DELETE"""

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


class IObjectModifiedEvent(Interface):
    """Object modified lifecycle event"""


class IObjectObsoletedEvent(Interface):
    """Object obsoleted lifecycle event"""
