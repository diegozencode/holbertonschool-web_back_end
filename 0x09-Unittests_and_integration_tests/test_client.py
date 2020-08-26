#!/usr/bin/env python3
"""
Test client
"""


import unittest
from unittest.mock import Mock, patch, PropertyMock

from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test github client
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('requests.get')
    def test_org(self, org, mock_get):
        """Test org url
        """
        pass

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    def test_public_repos_url(self, org, payload):
        """test public repos url
        """
        with patch(
             'client.GithubOrgClient._public_repos_url',
             new_callable=PropertyMock
             ) as mock_repo:
            mock_repo.return_value = payload
            this_repo = GithubOrgClient(org)
            self.assertEqual(this_repo._public_repos_url, payload)

    @patch('requests.get')
    def test_public_repos(self, mock_rep):
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
