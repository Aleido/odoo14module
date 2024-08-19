from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material.register']
        self.Produsen = self.env['produsen.register']

    def test_create_material(self):
        produsen = self.Produsen.create({'produsen_name': 'Test Produsen'})
        material = self.Material.create({
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 120,
            'related_produsen_id': produsen.id
        })
        self.assertEqual(material.material_code, 'M001')
    
    def test_invalid_price(self):
        produsen = self.Produsen.create({'produsen_name': 'Test Produsen'})
        with self.assertRaises(ValidationError):
            self.Material.create({
                'material_code': 'M002',
                'material_name': 'Invalid Material',
                'material_type': 'fabric',
                'material_buy_price': 80,
                'related_produsen_id': produsen.id
            })
