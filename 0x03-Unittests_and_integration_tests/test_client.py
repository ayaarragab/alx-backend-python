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

    # Mock get_json function in the client module
    @mock.patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """Test that the _public_repos_url property uses get_json correctly."""
        mocked_get_json.return_value = [{"name": "insta"}]
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=mock.PropertyMock) as m:
            m.return_value = "hello"
            obj = GithubOrgClient('test')
            val = obj.public_repos()
            check = [i["name"] for i in mocked_get_json.return_value]
            self.assertEqual(val, check)
            m.assert_called_once()
            mocked_get_json.assert_called_once()


if __name__ == '__main__':
    main()
