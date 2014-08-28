(function( $ ) {
function applyComboFilter(element, filterkey, filtervalue) {
    var base_query=$.parseJSON($(element).attr("base_query"));
    base_query[filterkey] = filtervalue;
    $(element).attr("base_query", $.toJSON(base_query));
    var options = $.parseJSON($(element).attr("combogrid_options"));
    options.url = window.location.href.split("/batches")[0] + "/" + options.url;
    options.url = options.url + "?_authenticator=" + $("input[name='_authenticator']").val();
    options.url = options.url + "&catalog_name=" + $(element).attr("catalog_name");
    options.url = options.url + "&base_query=" + $.toJSON(base_query);
    options.url = options.url + "&search_query=" + $(element).attr("search_query");
    options.url = options.url + "&colModel=" + $.toJSON( $.parseJSON($(element).attr("combogrid_options")).colModel);
    options.url = options.url + "&search_fields=" + $.toJSON($.parseJSON($(element).attr("combogrid_options")).search_fields);
    options.url = options.url + "&discard_empty=" + $.toJSON($.parseJSON($(element).attr("combogrid_options")).discard_empty);
    options.force_all="false";
    $(element).combogrid(options);
    $(element).addClass("has_combogrid_widget");
    $(element).attr("search_query", "{}");
}
$(document).ready(function() {
    $("#Client").on("change", function() {
        var clientuid = $(this).attr("uid");
        var element = $("#BContact");
        applyComboFilter(element, "getParentUID", clientuid);
        element = $("#InvoiceBContact");
        applyComboFilter(element, "getParentUID", clientuid);
    });

    $("[id$='BContact']").on("focusin", function() {
        $(this).val("");
        $(this).attr("UID", "");
        $("#Client").change();
    });
});
}(jQuery));

