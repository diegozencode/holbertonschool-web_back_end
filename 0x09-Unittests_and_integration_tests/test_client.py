#!/usr/bin/env python3
"""
Test client
"""


import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test github client
    """
    @patch('requests.get')
    def test_org(self, mock_get):
        """Test org url
        """
        pass

    def test_public_repos_url(self):
        """test public repos url
        """
        pass

    def test_public_repos(self):
        """test public repos
        """
        pass

    def test_has_license(self):
        """if has license
        """
        pass


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test integration
    """
    pass
