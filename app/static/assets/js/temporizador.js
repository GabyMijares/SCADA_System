$(function() {
    setInterval(function(){
        let request = new Request("/api/v0/get_data");

        fetch(request).then(function(result){
            return result.json() 
        }).then(function(data){
            $('#tqc').text(data['var_tqc']);
            $('#on_off').text(data['encendido']);
            $('#luz').text(data['volt_ky']);
            $('#tsb').text(data['var_tsb']);
            if( $("#switcher").data('state') !=  data['encendido']){
                $("#switcher").parent().removeClass("disabled");
                $("#switcher").data('state',data['encendido']);
                if(data["encendido"] =="ON"){
                    $("#text_switcher").text('Apagar planta eléctrica');
                }else{
                    $("#text_switcher").text('Encender planta eléctrica');
                }
            }          
        }).catch(function(err){
            console.log(err);
        });
    },5000);
});