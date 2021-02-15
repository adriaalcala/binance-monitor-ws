"""Exceptions module."""


class StopProcessing(Exception):
    """Raised to abort the processing pipeline."""
    stop_reason = 'stopped'
