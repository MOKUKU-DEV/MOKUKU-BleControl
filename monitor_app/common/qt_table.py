# Copyright 2025 Mobili Inc. All rights reserved.

import asyncio
import threading

from PyQt5.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PyQt5.QtCore import Qt


def create_qt_table(col_labels, rows_data, transpose=False):
    # 1. Create a QTableWidget
    # Parameters: row_count, column_count
    if transpose:
        table = QTableWidget(0, len(rows_data))  # Start with 0 rows, 3 columns
        table.setRowCount(len(col_labels))  # Set total row count
    else:
        table = QTableWidget(0, len(col_labels))  # Start with 0 rows, 3 columns
        table.setHorizontalHeaderLabels(col_labels)
        table.setRowCount(len(rows_data))  # Set total row count

    # 3. Customize table appearance
    table.horizontalHeader().setStretchLastSection(True)  # Stretch last column
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setAlternatingRowColors(True)  # Better readability
    table.setEditTriggers(QTableWidget.NoEditTriggers)  # Make cells non-editable
    table.horizontalHeader().setVisible(False)
    table.verticalHeader().setVisible(False)
    table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.verticalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    for row_idx, data in enumerate(rows_data):
        for col_idx, value in enumerate(data):
            item = QTableWidgetItem(value)
            if transpose:
                table.setItem(col_idx, row_idx, item)
            else:
                table.setItem(row_idx, col_idx, item)

    return table
