#!/usr/bin/env python3
import os

task_name = os.environ.get('CYLC_TASK_NAME', 'unknown')
print(f"Hello from Cylc! This is the {task_name} task.")
