/* Modify URL in depends on selected value for section */
function selectInit() {
	$('form').change(function () {
        var select = document.getElementById('id_section');
	    var select_value = select.options[select.selectedIndex].value;
        $(this).submit();
		var HOST = window.location.href;
		var re = /[\?\&]section=([\w+\%]+)/;

		if (HOST.indexOf('?section') || HOST.indexOf('&section')) {
			HOST = HOST.replace(re, "");
		}
        var newURL = HOST;
		if ((HOST.indexOf("q") > -1) || (HOST.indexOf("page")) > -1){
			newURL = HOST + "&section=" + select_value;
		} else {
			newURL = HOST + "?section=" + select_value;
		}
		window.location.assign(newURL);
	});
}

$(document).ready(function () {
	selectInit();
});
