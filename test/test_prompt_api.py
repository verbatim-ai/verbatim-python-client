# coding: utf-8

"""
    Verbatim AI API

    **Welcome on Verbatim AI Platform!**  You'll find here advanced specs of our APIs. You can play with these APIs on our **[Swagger Playground](https://www.verbatim.cloud/api-docs/swagger)**. Feel free to check our **[Cookbook](https://www.verbatim.cloud/cookbook)** to get samples and how start easily.  _____

    The version of the OpenAPI document: v1
    Contact: api@verbatim.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from verbatim_client.api.prompt_api import PromptApi


class TestPromptApi(unittest.TestCase):
    """PromptApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PromptApi()

    def tearDown(self) -> None:
        pass

    def test_prompt(self) -> None:
        """Test case for prompt

        Run a prompt
        """
        pass


if __name__ == '__main__':
    unittest.main()
