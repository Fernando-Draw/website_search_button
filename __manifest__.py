# Copyright 2022 Studio73 - Ioan Galan <ioan@studio73.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Website Search Button",
    "summary": "A button for search the products in website",
    "category": "Website",
    "version": "18.0.0.1.0",
    "website": "https://github.com/OCA/website",
    "author": "Studio73, Odoo Community Association (OCA)",
    "maintainers": ["ioans73"],
    "license": "AGPL-3",
    "depends": ["website"],
    "data": [
        "templates/website.xml",
        "views/res_config_settings.xml",
    ],
    "assets": {
        "web.assets_frontend": ["/website_whatsapp/static/src/scss/website.scss"]
    },
    "installable": True,
}
