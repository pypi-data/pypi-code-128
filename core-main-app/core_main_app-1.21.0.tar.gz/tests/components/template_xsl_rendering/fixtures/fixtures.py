""" Fixtures files for TemplateXslRendering
"""

from core_main_app.components.template.models import Template
from core_main_app.components.template_xsl_rendering.models import TemplateXslRendering
from core_main_app.components.xsl_transformation.models import XslTransformation
from core_main_app.utils.integration_tests.fixture_interface import FixtureInterface


class TemplateXslRenderingFixtures(FixtureInterface):
    """TemplateXslRendering fixtures"""

    template_1 = None
    template_2 = None
    template_xsl_rendering_1 = None
    template_xsl_rendering_2 = None
    xsl_transformation_1 = None
    xsl_transformation_2 = None
    xsl_transformation_3 = None
    template_xsl_rendering_collection = None
    xsl_transformation_collection = None

    def insert_data(self):
        """Insert a set of TemplateXslRendering and XslTransformation.

        Returns:

        """
        # Make a connexion with a mock database
        self.generate_template_xsl_rendering_collection()
        self.generate_xsl_transformation_collection()

    def generate_template_xsl_rendering_collection(self):
        """Generate a TemplateXslRendering collection.

        Returns:

        """
        # NOTE: no real file to avoid using unsupported GridFS mock

        self.template_1 = Template(
            filename="template_1.xsd", content="content1", hash="hash1"
        ).save()
        self.template_2 = Template(
            filename="template_2.xsd", content="content2", hash="hash2"
        ).save()
        self.template_xsl_rendering_1 = TemplateXslRendering(
            template=str(self.template_1.id)
        ).save()
        self.xsl_transformation_3 = XslTransformation(
            name="xsl_transformation_3",
            filename="xsl_transformation_3",
            content="content_3",
        ).save()

        self.template_xsl_rendering_2 = TemplateXslRendering(
            template=str(self.template_2.id),
            default_detail_xslt=str(self.xsl_transformation_3.id),
            list_detail_xslt=[str(self.xsl_transformation_3.id)],
        ).save()

        self.template_xsl_rendering_collection = [
            self.template_xsl_rendering_1,
            self.template_xsl_rendering_2,
        ]

    def generate_xsl_transformation_collection(self):
        """Generate a XslTransformation collection.

        Returns:

        """
        # NOTE: no real file to avoid using unsupported GridFS mock

        self.xsl_transformation_1 = XslTransformation(
            name="xsl_transformation_1",
            filename="xsl_transformation_1",
            content="content1",
        ).save()
        self.xsl_transformation_2 = XslTransformation(
            name="xsl_transformation_2",
            filename="xsl_transformation_2",
            content="content_2",
        ).save()

        self.xsl_transformation_collection = [
            self.xsl_transformation_1,
            self.xsl_transformation_2,
        ]
