# -*- coding: utf-8 -*-
#############################################################################
#
#    Infinity Draw.
#
#    Copyright (C) 2024-HOY Infinity Draw (<https://infinitydraw.es>)
#    Autor: Fernan Nerd (<https://infinitydraw.es>)
#
#    Puedes modificarlo bajo los términos de GNU LESSER.
#    LICENCIA PÚBLICA GENERAL (LGPL v3), Versión 3.
#
#    Este programa se distribuye con la esperanza de que sea útil,
#    pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
#    COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR.  Ver el
#    LICENCIA PÚBLICA GENERAL MENOR GNU (LGPL v3) para más detalles.
#
#    Debería haber recibido una copia de la LICENCIA PÚBLICA GENERAL MENOR DE GNU
#    (LGPL v3) junto con este programa.
#    En caso contrario, consulte <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    "name": "Website Search Button",
    "summary": "A button for search the products in website",
    "category": "Website",
    "version": "18.0.0.1.0",
    "website": "https://github.com/Fernando-Draw/website_search_button",
    "author": "Fernando-Draw",
    "maintainers": ["Fernando-Draw"],
    "license": "AGPL-3",
    "depends": ["website"],
    "data": [
        "templates/website.xml",
        "views/res_config_settings.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_search_button/static/src/scss/website.scss",
            "website_search_button/static/src/js/website_search_button.js",
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
