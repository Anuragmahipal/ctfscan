"""Tests for ctfscan"""

import os
import tempfile
import unittest
from ctfscan.core import CTFScanner
from ctfscan.cli import main


class TestCTFScanner(unittest.TestCase):
    """Test cases for CTFScanner"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.scanner = CTFScanner()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test files"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_find_flags(self):
        """Test flag finding functionality"""
        # Create a test file
        test_file = os.path.join(self.temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('Here is a flag{secret_flag} in the file')
        
        # Test flag detection
        flags = self.scanner.find_flags(test_file)
        self.assertGreater(len(flags), 0)
        self.assertIn('flag{secret_flag}', flags)
    
    def test_find_flags_uppercase(self):
        """Test finding uppercase FLAG patterns"""
        test_file = os.path.join(self.temp_dir, 'test_upper.txt')
        with open(test_file, 'w') as f:
            f.write('The FLAG{UPPERCASE} format')
        
        flags = self.scanner.find_flags(test_file)
        self.assertGreater(len(flags), 0)
    
    def test_find_flags_ctf_format(self):
        """Test finding CTF{} format"""
        test_file = os.path.join(self.temp_dir, 'test_ctf.txt')
        with open(test_file, 'w') as f:
            f.write('CTF{challenge_flag}')
        
        flags = self.scanner.find_flags(test_file)
        self.assertGreater(len(flags), 0)
    
    def test_decode_base64(self):
        """Test base64 decoding"""
        test_file = os.path.join(self.temp_dir, 'b64.txt')
        with open(test_file, 'w') as f:
            f.write('aGVsbG8gd29ybGQ=')  # "hello world" in base64
        
        decoded = self.scanner.decode_base64(test_file)
        self.assertIsNotNone(decoded)
        self.assertIn('hello', decoded.lower())
    
    def test_decode_hex(self):
        """Test hex decoding"""
        test_file = os.path.join(self.temp_dir, 'hex.txt')
        with open(test_file, 'w') as f:
            f.write('68656c6c6f')  # "hello" in hex
        
        decoded = self.scanner.decode_hex(test_file)
        self.assertIsNotNone(decoded)
        self.assertIn('hello', decoded.lower())
    
    def test_cli_help(self):
        """Test CLI help functionality"""
        result = main(['-h'])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
