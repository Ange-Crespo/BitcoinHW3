    function updateBuy(){
        $.ajax({
            type:"GET", 
            url:window.location.origin+"/orderAndTrade/json/bid_ask", 
            data: { get_param: 'value' }, 
            success: function(data) {
                deleteBuy();
                feed(data);
            }, 
            error: function(jqXHR, textStatus, errorThrown) {
                    console.log(jqXHR.status+ ' ' + result.statusText);
                    console.log(window.location.origin+"/orderAndTrade/json/bid_ask");
            },
            dataType:"json"
        });
        function deleteBuy(){
            $('#result_Buy').empty();
        };
        function feed(data){
            obj = data.bids;
           
            for(i=0,x=obj.length;i<x;i++){
                
                var line = '<tr><td>' + obj[i].count + '</td><td>' + obj[i].amount + '</td><td>' + obj[i].total + '</td><td>' + obj[i].price + '</td></tr>';
                $('#result_Buy').append(line);
            }
        };
    };


    function updateSell(){
        $.ajax({
            type:"GET", 
            url:window.location.origin+"/orderAndTrade/json/bid_ask", 
            data: { get_param: 'value' }, 
            success: function(data) {
                deleteSell();
                feed(data);
            }, 
            error: function(jqXHR, textStatus, errorThrown) {
                    console.log(jqXHR.status+ ' ' + result.statusText);
                    console.log(window.location.origin+"/orderAndTrade/json/bid_ask");
            },
            dataType:"json"
        });
        function deleteSell(){
            $('#result_Sell').empty();
        };
        function feed(data){
            obj = data.asks;
           
            for(i=0,x=obj.length;i<x;i++){
                
                var line = '<tr><td>' + obj[i].count + '</td><td>' + obj[i].amount + '</td><td>' + obj[i].total + '</td><td>' + obj[i].price + '</td></tr>';
                $('#result_Sell').append(line);
            }
        };
    };

    function updateTrade(){
        $.ajax({
            type:"GET", 
            url:window.location.origin+"/orderAndTrade/json/history", 
            data: { get_param: 'value' }, 
            success: function(data) {
                deleteTrade();
                feed(data);
            }, 
            error: function(jqXHR, textStatus, errorThrown) {
                    
            },
            dataType:"json"
        });
        function deleteTrade(){
            $('#result_Trade').empty();
        };
        function feed(data){
            obj = data;
           
            for(i=0,x=obj.length;i<x;i++){
                var timestamp = obj[i].timestamp*1000;
                var dt = new Date(timestamp); 
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
    };

    updateTrade(); 
    
    updateSell();
    
    updateBuy();

    
  