# Copyright 2025 Mobili Inc. All rights reserved.

import sys
from PyQt5.QtWidgets import QLabel, QDialog, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QMetaObject, QTimer, Qt


# --------------------------
# Reusable Loading Dialog
# --------------------------
class LoadingDialog(QDialog):
    def __init__(self, parent=None, title="Scanning", message="Processing..."):
        super().__init__(parent)
        self.title = title
        self.setWindowTitle(title)
        self.setModal(True)  # Block interaction with parent window (optional but clean)
        self.setFixedSize(250, 100)  # Fixed size for consistency

        # UI Elements: Message + (optional) animation
        self.message_label = QLabel(message, self)
        self.message_label.setAlignment(Qt.AlignCenter)

        # Layout (center message)
        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        elements = self.create_extented_elements()
        for ele in elements:
            layout.addWidget(ele)
        self.setLayout(layout)

        # Optional: Add a "scanning..." animation (blinking ellipsis)
        self.ellipsis_count = 0
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_ellipsis)
        self.animation_timer.start(500)  # Update every 500ms

    def create_extented_elements(self):
        return []

    def update_ellipsis(self):
        """Animate ellipsis (e.g., Scanning → Scanning. → Scanning.. → Scanning...)"""
        self.ellipsis_count = (self.ellipsis_count + 1) % 4
        self.message_label.setText(f"{self.title} {'.' * self.ellipsis_count}")

    def closeEvent(self, event):
        """Stop animation when dialog closes"""
        # self.animation_timer.stop()
        # Critical fix: Stop timer in the main thread using invokeMethod
        QMetaObject.invokeMethod(
            self.animation_timer,  # Target timer
            "stop",  # Method to call (stop the timer)
            Qt.QueuedConnection,  # Ensure execution in main thread
        )
        event.accept()


class DownloadingDialog(LoadingDialog):
    current_prograss = 0
    file_transfer = None

    def update_ellipsis(self):
        if self.file_transfer and self.file_transfer.file_size > 0:
            transfer_rate = (
                100 * self.file_transfer.current_pos / self.file_transfer.file_size
            )
            self.progress_bar.setValue(int(transfer_rate))
        self.ellipsis_count = (self.ellipsis_count + 1) % 4
        self.message_label.setText(f"{self.title} {'.' * self.ellipsis_count}")

    def create_extented_elements(self):
        elements = []
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        elements.append(self.progress_bar)
        return elements
