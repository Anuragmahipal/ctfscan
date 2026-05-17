"""Core functionality for ctfscan"""

import os
import re
import sys
import base64
import subprocess
from pathlib import Path
from typing import List, Optional


class CTFScanner:
    """Main CTFScanner class for flag detection and decoding"""

    def __init__(self):
        self.flag_patterns = [
            r'flag\{[^}]*\}',
            r'FLAG\{[^}]*\}',
            r'CTF\{[^}]*\}',
            r'flag\[[^\]]*\]',
            r'FLAG\[[^\]]*\]',
            r'CTF\[[^\]]*\]'
        ]

    def find_flags(self, file_path: str) -> List[str]:
        """
        Find FLAG{}, flag{}, and CTF{} patterns in file
        
        Args:
            file_path: Path to file to search
            
        Returns:
            List of found flags
        """
        flags = []
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                try:
                    text = content.decode('utf-8', errors='ignore')
                except:
                    text = str(content)
                
                for pattern in self.flag_patterns:
                    matches = re.finditer(pattern, text, re.IGNORECASE)
                    for match in matches:
                        flags.append(match.group(0))
        except Exception as e:
            print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        
        return flags

    def find_flags_recursive(self, directory: str) -> List[tuple]:
        """
        Recursively find flags in directory
        
        Args:
            directory: Directory path to search
            
        Returns:
            List of tuples (file_path, flags)
        """
        results = []
        try:
            path = Path(directory)
            if path.is_file():
                flags = self.find_flags(str(path))
                if flags:
                    results.append((str(path), flags))
            else:
                for file_path in path.rglob('*'):
                    if file_path.is_file():
                        flags = self.find_flags(str(file_path))
                        if flags:
                            results.append((str(file_path), flags))
        except Exception as e:
            print(f"Error scanning directory: {e}", file=sys.stderr)
        
        return results

    def decode_base64(self, file_path: str) -> Optional[str]:
        """
        Decode base64 from file
        
        Args:
            file_path: Path to file containing base64 data
            
        Returns:
            Decoded string or None
        """
        try:
            with open(file_path, 'rb') as f:
                content = f.read().decode('utf-8').strip()
            decoded = base64.b64decode(content)
            return decoded.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error decoding base64: {e}", file=sys.stderr)
            return None

    def decode_hex(self, file_path: str) -> Optional[str]:
        """
        Decode hex strings from file
        
        Args:
            file_path: Path to file containing hex data
            
        Returns:
            Decoded string or None
        """
        try:
            with open(file_path, 'rb') as f:
                content = f.read().decode('utf-8').strip()
            
            # Remove spaces and common hex formatting
            content = content.replace(' ', '').replace('\\x', '').replace('0x', '')
            
            decoded = bytes.fromhex(content)
            return decoded.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error decoding hex: {e}", file=sys.stderr)
            return None

    def advanced_scan(self, file_path: str) -> dict:
        """
        Advanced scan using exiftool, binwalk, and strings
        
        Args:
            file_path: Path to file to scan
            
        Returns:
            Dictionary with scan results
        """
        results = {
            'exiftool': None,
            'binwalk': None,
            'strings': []
        }
        
        # Try exiftool
        try:
            result = subprocess.run(['exiftool', file_path], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                results['exiftool'] = result.stdout
        except Exception as e:
            print(f"Warning: exiftool not available: {e}", file=sys.stderr)
        
        # Try binwalk
        try:
            result = subprocess.run(['binwalk', file_path], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                results['binwalk'] = result.stdout
        except Exception as e:
            print(f"Warning: binwalk not available: {e}", file=sys.stderr)
        
        # Try strings + grep for flags
        try:
            result = subprocess.run(['strings', file_path], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                pattern = r'([A-Za-z0-9+/=]{12,}|flag|f1ag|fl4g|ctf\{)'
                for line in lines:
                    if re.search(pattern, line, re.IGNORECASE):
                        results['strings'].append(line.strip())
        except Exception as e:
            print(f"Warning: strings command not available: {e}", file=sys.stderr)
        
        return results
