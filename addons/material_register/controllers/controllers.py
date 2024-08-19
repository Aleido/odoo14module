import json
from odoo import http
from odoo.http import request
from werkzeug.wrappers import Response


class MaterialController(http.Controller):
    def _json_resp(self, code, message, data=None):
        response = Response(
            '{"code": %d, "message": %s, "data": %s}' % (code, message, data),
            status=code,
            content_type='application/json'
        )
        return response

    def _check_required(self, params, required_params):
        return [p for p in required_params if p not in params]

    @http.route('/api/materials', type='http', auth='public', methods=['GET'])
    def get_all_materials(self, **kwargs):
        materials = request.env['material.register'].search_read([], fields=['code', 'name', 'type', 'buy_price', 'produsen_id'])
        # return json.dumps({"code":200, "data":materials})
        return self._json_resp(200, "Success", json.dumps(materials))

    
    @http.route('/api/produsen', type='http', auth='public', methods=['GET'])
    def get_all_produsen(self, **kwargs):
        produsen = request.env['produsen.register'].search_read([], fields=['name', 'contact'])
        return self._json_resp(200, "Success", json.dumps(produsen))
    

    @http.route('/api/materials', type='json', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        try:
            params = request.jsonrequest.get('params', {})
            required_params = ["code", "name", "type", "buy_price", "produsen_id"]
            
            missing_params = self._check_required(params, required_params)
            if missing_params:
                return self._json_resp(400, f"Missing required parameters: {', '.join(missing_params)}")
            
            produsen_id = params.get("produsen_id")
            produsen_exists = request.env['produsen.register'].search_count([('id', '=', produsen_id)])

            if not produsen_exists:
                return self._json_resp(400, "produsen_id terkait tidak ditemukan.")

            material = request.env['material.register'].create(params)
            return self._json_resp(200, f"Material berhasil dibuat dengan ID: {material.id}!")

        except Exception as e:
            return self._json_resp(500, str(e))
    
    @http.route('/api/materials/<int:material_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_material(self, material_id, **kwargs):
        try:
            material = request.env['material.register'].browse(material_id)

            if not material.exists():
                return self._json_resp(404, "Material dengan ID terkait tidak ditemukan.")
            
            material.write(kwargs)
            return self._json_resp(200, "Update material berhasil!")
        
        except Exception as e:
            return self._json_resp(500, str(e))

    @http.route('/api/materials/<int:material_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_material(self, material_id):
        try:
            material = request.env['material.register'].browse(material_id)

            if not material.exists():
                return self._json_resp(404, "Material dengan ID terkait tidak ditemukan")

            material.unlink()

            return self._json_resp(200, "Hapus Material berhasil!")

        except Exception as e:
            return self._json_resp(500, str(e))

