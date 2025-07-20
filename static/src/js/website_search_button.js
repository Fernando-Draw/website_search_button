/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.FloatingSearchButton = publicWidget.Widget.extend({
    selector: '.website_search_floating_btn',
    events: {
        'click': '_onClick',
    },

    start: function () {
        this._lastScroll = window.scrollY;
        this._onScroll = this._onScroll.bind(this);
        window.addEventListener('scroll', this._onScroll, { passive: true });
        console.log('[WSB] Widget cargado');

        return this._super.apply(this, arguments);
    },

    destroy: function () {
        window.removeEventListener('scroll', this._onScroll);
        this._super.apply(this, arguments);
    },

    _onClick: function () {
        console.log('[WSB] Botón clickeado');
        
        // Si ya existe el modal, no lo vuelvas a crear
        if (document.getElementById('wsb_floating_search_modal')) return;

        // Crear el modal a pantalla completa
        const modal = document.createElement('div');
        modal.id = 'wsb_floating_search_modal';
        modal.className = 'wsb-modal-bg';
        modal.innerHTML = `
            <div class="wsb-modal-content">
                <form class="wsb-search-form" autocomplete="off">
                    <input type="search" class="wsb-search-input" name="search" placeholder="Buscar…" autofocus />
                    <button type="submit" class="wsb-search-btn" aria-label="Buscar">
                        <i class="oi oi-search"></i>
                    </button>
                </form>
            </div>
        `;
        document.body.appendChild(modal);

        // Animación de entrada
        setTimeout(() => {
            modal.classList.add('wsb-modal-bg-show');
            const input = modal.querySelector('.wsb-search-input');
            if (input) input.focus();
        }, 10);

        // Cerrar modal al hacer click fuera de la barra
        modal.addEventListener('mousedown', (e) => {
            if (e.target === modal) {
                modal.classList.remove('wsb-modal-bg-show');
                setTimeout(() => modal.remove(), 300);
            }
        });

        // Cerrar modal con ESC
        modal.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                modal.classList.remove('wsb-modal-bg-show');
                setTimeout(() => modal.remove(), 300);
            }
        });

        // Enviar búsqueda
        const form = modal.querySelector('.wsb-search-form');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const value = form.search.value.trim();
            if (value) {
                window.location.href = '/website/search?search=' + encodeURIComponent(value);
            }
        });
    },

    _onScroll: function () {
        const currentScroll = window.scrollY;
        const goingDown = currentScroll > this._lastScroll;

        if (goingDown && currentScroll > 50) {
            this.$el.addClass('hide-by-scroll');
        } else {
            this.$el.removeClass('hide-by-scroll');
        }

        this._lastScroll = currentScroll;
    },
});