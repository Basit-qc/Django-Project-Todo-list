$(document).ready(function(){
    $('#save').on('click', function() {
            var form_data = $('#add_todo_form').serialize();
            console.log(form_data);
            if ($.trim($('#id_task_name').val()) == '') {
                    alert('Please enter name');
                    return false;
            }
            if ($.trim($('#id_description').val()) == '') {
                    alert('Please enter description');
                    return false;
            }
            $.ajax(
                { url: 'add_todo',
                  type: 'POST',
                  data: form_data,
                        success: function(res){
                            alert($.parseJSON(res).response);
                            $("#myModal").modal("hide");
                        },
                        error: function(){
                            alert("error occurred while saving TODO");
                        }
                }
            );
	});
    $('.is_checked').on('change', function() {
        var task_id = $(this).val();
            $.ajax(
                { url: 'delete',
                  type: 'POST',
                  data: {
                      'task_id': task_id,
                      'csrfmiddlewaretoken': document.getElementsByName("csrfmiddlewaretoken")[0].value},
                        success: function(res){
                            alert($.parseJSON(res).response);
                        },
                        error: function(){
                            alert("error occurred while resolving TODO");
                        }
                }
            );
	});
});
