odoo.define('digizilla.hide_create_button', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.mode === 'readonly') {
                this.$buttons.find('.o_form_button_create').hide();
            }
        },
    });

});
