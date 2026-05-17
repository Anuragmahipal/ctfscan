"""Command-line interface for ctfscan"""

import sys
import argparse
from typing import Optional
from .core import CTFScanner


def print_usage():
    """Print usage information"""
    print("""
Usage: ctfscan <option> <file>

Options:
  -ff     Find FLAG{...}, flag{...}, CTF{...} patterns
  -d64    Decode base64 from file
  -dhex   Decode hex strings
  -scan   Run exiftool, binwalk, and strings analysis
  -h      Show help
""")


def main(argv: Optional[list] = None) -> int:
    """Main entry point for CLI"""
    
    if argv is None:
        argv = sys.argv[1:]
    
    if not argv or argv[0] == '-h':
        print_usage()
        return 0
    
    scanner = CTFScanner()
    option = argv[0]
    
    if len(argv) < 2 and option not in ['-h']:
        print("Error: Missing file argument", file=sys.stderr)
        print_usage()
        return 1
    
    file_path = argv[1] if len(argv) > 1 else None
    
    try:
        if option == '-ff':
            # Find flags (recursive if directory)
            results = scanner.find_flags_recursive(file_path)
            
            if results:
                for file, flags in results:
                    for flag in flags:
                        print(flag)
            else:
                print("No flags found.", file=sys.stderr)
                return 1
        
        elif option == '-d64':
            # Decode base64
            decoded = scanner.decode_base64(file_path)
            if decoded:
                print(decoded)
            else:
                return 1
        
        elif option == '-dhex':
            # Decode hex
            decoded = scanner.decode_hex(file_path)
            if decoded:
                print(decoded)
            else:
                return 1
        
        elif option == '-scan':
            # Advanced scan
            print(f"🔎 Scanning: {file_path}\n")
            results = scanner.advanced_scan(file_path)
            
            if results['exiftool']:
                print("📷 Exiftool output:")
                print(results['exiftool'])
                print()
            
            if results['binwalk']:
                print("🧩 Binwalk output:")
                print(results['binwalk'])
                print()
            
            if results['strings']:
                print("🔎 Suspicious strings found:")
                for s in results['strings']:
                    print(f"  {s}")
        
        elif option == '-h':
            print_usage()
        
        else:
            print(f"Error: Invalid option '{option}'", file=sys.stderr)
            print_usage()
            return 1
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
