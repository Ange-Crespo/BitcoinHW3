
        $.ajax({
            type:"GET", 
            url:window.location.origin+"/orderTrade/json/", 
            data: { get_param: 'value' }, 
            success: function(data) {
               
                feed(data);
            }, 
            error: function(jqXHR, textStatus, errorThrown) {
                    
            },
            dataType:"json"
        });
        function feed(data){
            obj = data;
           
            for(i=0,x=obj.length;i<x;i++){
                var dt = new Date();
                var time = dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds();
                var price = 0;
                if(obj[i].bidprice == obj[i].askaprice){
                    price = obj[i].bidprice;
                    
                }
                else {
                    price = obj[i].bidprice;  
                    
                }
                
                var line = '<tr><td>' + time + '</td><td>' + price + '</td><td>' + obj[i].amount + '</td></tr>';
                $('#result_Trade').append(line);
            }
        };
    
    