from __future__ import absolute_import

import pytest
from qtpy import QtSql

def test_qtsvg():
    """Test the qtpy.QtSql namespace"""
    assert QtSql.QSqlDatabase is not None
    # assert QtSql.QSqlDriverCreator is not None
    assert QtSql.QSqlDriverCreatorBase is not None
    assert QtSql.QSqlDriver is not None
    assert QtSql.QSqlDriverPlugin is not None
    assert QtSql.QSqlError is not None
    assert QtSql.QSqlField is not None
    assert QtSql.QSqlIndex is not None
    assert QtSql.QSqlQuery is not None
    assert QtSql.QSqlRecord is not None
    assert QtSql.QSqlResult is not None
    assert QtSql.QSqlQueryModel is not None
    assert QtSql.QSqlRelationalDelegate is not None
    assert QtSql.QSqlRelation is not None
    assert QtSql.QSqlRelationalTableModel is not None
    assert QtSql.QSqlTableModel is not None
