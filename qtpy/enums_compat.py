#
# Copyright © 2009- The Spyder Development Team
# Licensed under the terms of the MIT License
"""
Compatibility functions for scoped and unscoped enums access
"""
from . import PYQT6

if PYQT6:
    import enum

    from . import sip


    def promote_specific_enums(base_class, enum_classes_list, inclusion_criteria):
        """
        Allow access for the given enumeration classes values at base class level.

        Based on:
        https://github.com/pyqtgraph/pyqtgraph/blob/pyqtgraph-0.12.1/pyqtgraph/Qt.py#L331-L377 
        """
        for enum_class_name in enum_classes_list:
            klass = getattr(base_class, enum_class_name)
            attrib_names = [x for x in dir(klass) if inclusion_criteria(x)]
            for attrib_name in attrib_names:
                attrib = getattr(klass, attrib_name)
                if not isinstance(attrib, (enum.Enum)):
                    continue
                setattr(base_class, attrib.name, attrib)


    def promote_enums(module):
        """
        Search enums in the given module and allow unscoped access.

        Taken from:
        https://github.com/pyqtgraph/pyqtgraph/blob/pyqtgraph-0.12.1/pyqtgraph/Qt.py#L331-L377 
        """
        class_names = [x for x in dir(module) if x.startswith('Q')]
        for class_name in class_names:
            klass = getattr(module, class_name)
            if not isinstance(klass, sip.wrappertype):
                continue
            attrib_names = [x for x in dir(klass) if x[0].isupper()]
            for attrib_name in attrib_names:
                attrib = getattr(klass, attrib_name)
                if not isinstance(attrib, enum.EnumMeta):
                    continue
                for e in attrib:
                    setattr(klass, e.name, e)