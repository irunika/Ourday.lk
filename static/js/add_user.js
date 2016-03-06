/**
 * Created by irunika on 3/5/16.
 */

$(document).ready(function(){

    $('.selectpicker').selectpicker({
        dropupAuto: false
    });

    /**
     * THis method is called when cities need to be loaded according to the need of district
     */
    $('#select-district').change(function(){

        $('#Select-city').attr('disabled', true);
        $('#cities-loading-gif').fadeIn();

        $.ajax({
            type:'GET',
            dataType:'json',
            data:{'district':$('#select-district option:selected').text()},
            url:'/get_cities'
        }).done(function(response){
            console.log(response['cities'])
            $('#Select-city').attr('disabled', false);
            $('#Select-city').empty();
            for(var i=0; i<response['cities'].length ;i++ ){
                $('#Select-city').append(
                    '<option>'+ response['cities'][i] +'</option>'
                );
            }
            $('#Select-city').selectpicker('refresh');
            $('#cities-loading-gif').slideUp();



        }).fail(function(response){

        })
    });




});
