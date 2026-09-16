"""TODO: describe this module."""
"""Module for text processing utilities such as cleaning user names."""

def clean_name(raw):
    """TODO: describe this function."""
    """Clean a messy name string by collapsing whitespace and converting to title case."""
    # TODO: collapse whitespace, then title-case
    return " ".join(raw.split()).title()

