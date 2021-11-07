from odoo import models, fields,api
from odoo.exceptions import UserError


class ApiAlbum(models.Model):

    _name = "api.album"
    _description = "Album"

    name = fields.Char(string="Name")
    release_date = fields.Date(string="Date of release")

    artist_id = fields.Many2one(comodel_name="api.artist", string="Artist")
    album_group_id = fields.Many2one(comodel_name="api.group", string="Group")
    song_ids = fields.One2many(comodel_name="api.song", inverse_name="album_id", string="Song")

    @api.model
    def create(self, vals):
        """
        Creating new album if there is no album with the same name and name is correct
        """
        if self.env["api.album"].search([("name", "=", vals["name"])]):
            raise UserError("This name for album is already exist,please change it.")
        elif vals["name"] is False:
            raise UserError("Album name can't be empty")
        else:
            res = super(ApiAlbum, self).create(vals)
            return res

    def write(self, vals):
        """
        Editing new album if there is no album with the same name and name is correct
        """
        if "name" in vals and self.env["api.album"].search([("name", "=", vals["name"])]) and vals["name"] != self.name:
            raise UserError("This name for album is already exist,please change it.")
        elif "name" in vals and vals["name"] is False:
            raise UserError("Album name can't be empty")
        else:
            res = super(ApiAlbum, self).write(vals)
            return res
