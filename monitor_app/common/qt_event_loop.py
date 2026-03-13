# Copyright 2025 Mobili Inc. All rights reserved.

import asyncio
import threading

# install with : pip install qasync
from qasync import QEventLoop  # Critical for integrating asyncio with PyQt


class QtEventLoop:
    def __init__(self, app):
        # 1. Create a QEventLoop (integrates asyncio with PyQt)
        self.loop = QEventLoop(app)
        # 2. Set it as the default asyncio loop
        asyncio.set_event_loop(self.loop)

        # self.thread = threading.Thread(target=self.run_loop, daemon=True)
        # self.thread.start()

    def run_loop(self):
        # 3. Run the loop (critical: starts the event loop)
        with self.loop:
            self.loop.run_forever()
