/* Modify URL in depends on selected value for section */
function selectInit() {
	$('form').change(function () {
        var select = document.getElementById('id_section');
	    var select_value = select.options[select.selectedIndex].value;
        $(this).submit();
		var url = window.location.toString();
		var re = /[\?\&]section=([\w+\%]+)/;

		if (url.indexOf('section')) {
			url = url.replace(re, "");
		}
		if ((url.indexOf("q") > -1) || (url.indexOf("page") > -1)){
		    url = url + "&section=" + select_value;
        }
		else {
			url = url + "?section=" + select_value;
		}
		window.location.assign(url);
	});
}

$(document).ready(function () {
	selectInit();
});
