# Linux Log Parser & Automation Script

A lightweight Python automation tool designed for IT Support Engineers and Systems Administrators to parse large server log files, filter out critical errors, and accelerate troubleshooting.

Features
Automated Scan: Instantly processes logs to find key system errors.
Smart Filtering: Targets specific keywords like `CRITICAL` and `ERROR 500`.
Fast Reporting: Provides a quick summary of total issues found for rapid root-cause analysis.

Tech Stack
Language: Python 3.x
Core Concepts: File I/O, String Manipulation, Automation, Linux Log Analysis

How It Works
The script opens a specified log file (e.g., `server.log`), reads it line-by-line to minimize memory usage, and prints real-time alerts whenever a critical system issue is detected.
