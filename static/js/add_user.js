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
        //alert($('#select-district option:selected').text());
        $.ajax({
            type:'GET',
            dataType:'json',
            data:{'district':$('#select-district option:selected').text()},
            url:'/get_cities'
        }).done(function(response){
            console.log(response['cities'])
            $('#Select-city').empty();
            for(var i=0; i<response['cities'].length ;i++ ){
                $('#Select-city').append(
                    '<option>'+ response['cities'][i] +'</option>'
                );
            }
            $('#Select-city').selectpicker('refresh');
        }).fail(function(response){

        })
    });




});
