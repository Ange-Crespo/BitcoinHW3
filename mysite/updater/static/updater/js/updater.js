
socket = new WebSocket("ws://" + window.location.host + "/update/");

socket.onmessage = function(e) {
        message=e.data;
        console.log(message);
        
        updateBuy(); //define in orderBuy
        updateSell(); //define in orderSell
        updateTrade(); //define in orderTrade
    }