# Copyright 2025 Infinity Draw - Fernando de la Torre <fernando@infinitydraw.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    # Activar/desactivar botón flotante de búsqueda
    search_button_enabled = fields.Boolean(
        string="Activar botón de búsqueda flotante",
        default=True,
    )
    # Posición: 'Inf-Izq' o 'Inf-Der'
    search_button_position = fields.Selection(
        [
            ("right", "Inferior derecha"),
            ("left", "Inferior izquierda"),
        ],
        string="Posición del botón",
        default="right",
    )
    # Márgenes
    search_button_margin_bottom = fields.Integer(
        string="Margen inferior (px)",
        default=100,
    )
    search_button_margin_side = fields.Integer(
        string="Margen lateral (px)",
        default=10,
    )
    # Colores
    search_button_bg_color = fields.Char(
        string="Color de fondo",
        default="#000000",
    )
    search_button_icon_color = fields.Char(
        string="Color del icono",
        default="#ffffff",
    )
    # Tamaño
    search_button_size = fields.Integer(
        string="Tamaño del botón (px)",
        default=60,
    )
    # Forma
    search_button_shape = fields.Selection(
        [
            ("circle", "Círculo"),
            ("square", "Cuadrado con esquinas redondeadas"),
        ],
        string="Forma del botón",
        default="circle",
    )
    # Visibilidad
    search_button_show_desktop = fields.Boolean(
        string="Mostrar en escritorio",
        default=True,
    )
    search_button_show_mobile = fields.Boolean(
        string="Mostrar en móvil",
        default=True,
    )
