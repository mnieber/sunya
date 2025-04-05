"""
Chapter model for the bookie application.
"""

from dataclassy import dataclass
from typing import List


@dataclass
class Chapter:
    title: str
    paragraphs: List[str] = []
