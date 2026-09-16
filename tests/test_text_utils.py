"""Tests for src/text_utils.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import text_utils


def test_clean_name_whitespace():
    """Test that inner and outer whitespace are collapsed correctly."""
    assert text_utils.clean_name("   sara   ali   ") == "Sara Ali"


def test_clean_name_capitalisation():
    """Test that all-caps and all-lowercase names are fixed to title case."""
    assert text_utils.clean_name("SARA ALI") == "Sara Ali"
    assert text_utils.clean_name("sara ali") == "Sara Ali"
