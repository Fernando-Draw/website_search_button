# Copyright 2025 Infinity Draw - Fernando de la Torre <fernando@infinitydraw.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    search_button_enabled = fields.Boolean(
        related="website_id.search_button_enabled",
        readonly=False,
    )
    search_button_position = fields.Selection(
        related="website_id.search_button_position",
        readonly=False,
    )
    search_button_margin_bottom = fields.Integer(
        related="website_id.search_button_margin_bottom",
        readonly=False,
    )
    search_button_margin_side = fields.Integer(
        related="website_id.search_button_margin_side",
        readonly=False,
    )
    search_button_bg_color = fields.Char(
        related="website_id.search_button_bg_color",
        readonly=False,
    )
    search_button_icon_color = fields.Char(
        related="website_id.search_button_icon_color",
        readonly=False,
    )
    search_button_size = fields.Integer(
        related="website_id.search_button_size",
        readonly=False,
    )
    search_button_shape = fields.Selection(
        related="website_id.search_button_shape",
        readonly=False,
    )
    search_button_show_desktop = fields.Boolean(
        related="website_id.search_button_show_desktop",
        readonly=False,
    )
    search_button_show_mobile = fields.Boolean(
        related="website_id.search_button_show_mobile",
        readonly=False,
    )
