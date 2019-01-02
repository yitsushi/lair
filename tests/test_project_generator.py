from unittest import TestCase
from lair.project_generator import ProjectGenerator


class TestProjectGenerator(TestCase):
    def setUp(self):
        self.pg = ProjectGenerator()

    def test_properies(self):
        self.assertIsNone(self.pg.get('project-name'))

        self.pg.set('project-name', 'test-project')
        self.assertIsNotNone(self.pg.get('project-name'))
        self.assertEqual(self.pg.get('project-name'), 'test-project')

    def test_initializer(self):
        self.assertIsNone(self.pg.root())
        self.assertIsNone(self.pg.get('project-name'))
        self.assertIsNone(self.pg.get('module-name'))

        self.pg.set('project-name', 'test-project')
        self.pg.initialize()
        self.assertIsNotNone(self.pg.root())
        self.assertIsNotNone(self.pg.get('project-name'))
        self.assertIsNotNone(self.pg.get('module-name'))
        self.assertEqual(self.pg.get('project-name'), 'test-project')
        self.assertEqual(self.pg.get('module-name'), 'test_project')
