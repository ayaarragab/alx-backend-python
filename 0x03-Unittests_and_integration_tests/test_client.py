#!/usr/bin/env python3
""" Unit tests for the github org client
"""

from unittest import (
    main, TestCase, mock
)
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()


if __name__ == '__main__':
    main()
