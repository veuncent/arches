define(['knockout', 'underscore', 'viewmodels/widget', 'bindings/input-mask'], function (ko, _, WidgetViewModel) {
    /**
    * registers a text-widget component for use in forms
    * @function external:"ko.components".text-widget
    * @param {object} params
    * @param {string} params.value - the value being managed
    * @param {function} params.config - observable containing config object
    * @param {string} params.config().label - label to use alongside the text input
    * @param {string} params.config().placeholder - default text to show in the text input
    */
    return ko.components.register('text-widget', {
        viewModel: function(params) {
            params.configKeys = ['placeholder', 'width', 'maxLength', 'inputMask'];
            WidgetViewModel.apply(this, [params]);
        },
        template: { require: 'text!widget-templates/text' }
    });
});
