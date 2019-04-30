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
        }).catch(function(err){
            console.log(err);
        });
    },5000);
});