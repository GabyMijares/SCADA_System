$(function() {
    $('#switcher').on("click", function(){
        data = {"action": ($(this).attr('data-state')=="True")? 'N':'O'}
        let headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let loadInfo = {
            method: 'POST',
            headers: headers,
            mode: 'cors',
            body: JSON.stringify(data) 
        }
        
        let request = new Request("/api/v0/switch",loadInfo)
        
        fetch(request).then(function(result){
            $('#switcher').parent().addClass('disabled');
            return result.json() 
        }).then(function(result){
            $.notify({icon:"add_alert",message:"Su solicitud se ha enviado correctamente. Por favor espere unos segundos."},{type:"success",timer:3e3,placement:{from:'top',align:'left'}});
        }).catch(function(err){
            console.log(err);
        });
    });
});