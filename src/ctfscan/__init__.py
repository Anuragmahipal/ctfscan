"""ctfscan - Instant flag finder & decoder for CTFs"""

__version__ = "1.0.0"
__author__ = "Anuragmahipal"
__email__ = "your-email@example.com"
__description__ = "Blazing-fast terminal utility for CTF players to find and decode flags"

from .core import CTFScanner

__all__ = ["CTFScanner", "__version__"]
