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

from verbatim_client.models.prompt_document_attachment import PromptDocumentAttachment

class TestPromptDocumentAttachment(unittest.TestCase):
    """PromptDocumentAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PromptDocumentAttachment:
        """Test PromptDocumentAttachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PromptDocumentAttachment`
        """
        model = PromptDocumentAttachment()
        if include_optional:
            return PromptDocumentAttachment(
                id = '',
                text = '',
                pages = [
                    56
                    ],
                document = verbatim_client.models.document.Document(
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    corpus_id = '', 
                    state = 'unknown', 
                    filename = 'myfile.pdf', 
                    content_type = 'application/pdf', 
                    size = 1024, 
                    nb_pages = 5, 
                    pages = [
                        verbatim_client.models.document_page.DocumentPage(
                            index = 56, 
                            title = '', )
                        ], )
            )
        else:
            return PromptDocumentAttachment(
        )
        """

    def testPromptDocumentAttachment(self):
        """Test PromptDocumentAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
