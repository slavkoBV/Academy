$(document).ready(function() {
            var url = window.location.toString();
            $('#ajax_block').load(url + 'project-about');
            $('#links a').click(function() {
             var url=$(this).attr('href');
             $('#ajax_block').load(url);
             return false;
          });
        });
