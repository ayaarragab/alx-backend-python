#!/usr/bin/env python3
""" Unit tests for the github org client
"""

from unittest import (
     main, TestCase, mock
)

from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """
    Class for Unit tests for the github org client
    """
    @parameterized.expand([('google'), ('abc')])
    # pathes the function according to where it used in
    @mock.patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """ tests org()
        """
        res = GithubOrgClient(input)
        res.org()
        url = f"https://api.github.com/orgs/{input}"
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """test_public_repos_url
        """
        with mock.patch('client.GithubOrgClient.org') as m:
            m.return_value = {'name': 'test_org', 'public_repos': 10}
            res = GithubOrgClient('test')
            self.assertEqual(res.org(),
                             {'name': 'test_org', 'public_repos': 10})

    @mock.patch('client.get_json')  # Mock get_json function in the client module
    def test_public_repos(self, mocked_get_json):
        """Test that the _public_repos_url property uses get_json correctly."""
        # Mocking the response of get_json
        mocked_get_json.return_value = {
            "repos_url": "https://api.github.com/orgs/test/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient('test')
        
        # Access the org method to trigger the mocked get_json call
        org_data = client.org  # This calls get_json, fetching the org's data

        # Verify the get_json was called with the correct URL
        mocked_get_json.assert_called_once_with("https://api.github.com/orgs/test")

        # Access the _public_repos_url property
        repos_url = client._public_repos_url

        # Assertions to check the behavior
        self.assertEqual(repos_url, "https://api.github.com/orgs/test/repos")
        self.assertEqual(org_data, {"repos_url": "https://api.github.com/orgs/test/repos"})


if __name__ == '__main__':
    main()
