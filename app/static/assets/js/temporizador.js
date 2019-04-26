$(function() {
    setInterval(function(){
        let request = new Request("/api/v0/get_data");

        fetch(request).then(function(result){
            return result.json() 
        }).then(function(data){
            $('#tqc').text(data['var_tqc']);
        }).catch(function(err){
            console.log(err);
        });
    },5000);
});