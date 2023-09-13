#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""

def validUTF8(data):
  for i in data:
    if i >= 0 and i <= 127:
      return True
    else:
      return False