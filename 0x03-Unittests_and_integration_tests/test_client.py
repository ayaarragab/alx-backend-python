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


if __name__ == '__main__':
    main()
