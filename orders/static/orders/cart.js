$(document).ready(function(){
    console.log("document ready");
    
    
    $("#pizza").change(function(){
        const pizza = $(this).val();

        $("#pizza").prop("disabled", true);
        $("#size-block").css("opacity", "1");
        $("#size").prop("disabled", false);

        $("#size").change(function(){

            if (pizza == "Regular_pizza"){
                console.log(pizza);
                $("#addition-block-for-regular").css("opacity", "1");
                $("#addition-for-regular").prop("disabled", false);
                $("#addition-block-for-sicilian").remove();
            }
            else{
                console.log(pizza);
                $("#addition-block-for-sicilian").css("opacity", "1");
                $("#addition-for-sicilian").prop("disabled", false);
                $("#addition-block-for-regular").remove();
            }

            const size = $(this).val();
            console.log(size);
            $("#size").prop("disabled", true);

            $(".addition").change(function(){

                const addition = $(this).val();
                toppings = [];
                console.log(addition)
                $(".addition").prop("disabled", true);
                $("#addtocart").prop("disabled", true);



                if (addition === "1 topping"){
                    var flag = 1;
                    $("#button-block").css("opacity","1");
                    $("#toppings").prop("disabled", false);    
                    $("#toppingsheading").html("Select 1 topping");
                }
                else if (addition === "2 toppings"){
                    var flag = 2;
                    $("#button-block").css("opacity","1");
                    $("#toppings").prop("disabled", false);
                    $("#toppingsheading").html("Select 2 toppings");
                }
                else if (addition === "3 toppings"){
                    var flag = 3;
                    $("#button-block").css("opacity","1");
                    $("#toppings").prop("disabled", false);
                    $("#toppingsheading").html("Select 3 toppings");
                }
                else{
                    $("#addtocart").prop("disabled", false);
                    $("#toppings").prop("disabled", true);
                    $("#button-block").css("opacity","0");
                   
                };        //close else block



                $('input[name=toppings]').on('change', function (e) {

                    if ($('input[name=toppings]:checked').length < flag){
                        $("#toppingsubmit").prop("disabled", true);
                    }


                    if ($('input[name=toppings]:checked').length == flag){
                        $("#toppingsubmit").prop("disabled", false);
                        $("#toppingsubmit").click(function(){

                            toppings = [];
                            $.each($("input[name=toppings]:checked"), function(){            
                                toppings.push($(this).val());
                            });

                            $("#addtocart").prop("disabled", false);


                            $("#toppings").remove();
                            $("#button-block").text("Selected Toppings : "+toppings);

                        })           // close toppings submit click event                  
                        
                    }   // close flag == number of checked boxes
                    
                    if ($('input[name="toppings]:checked').length > flag) {
                        $(this).prop('checked', false);
                        alert(`allowed only ${flag} choice`);
                    }


                });  //close input type checkbox code





                $.ajax(
                    {
                    type:"POST",
                    url: "/ajax",
                    data:{
                        'csrfmiddlewaretoken' :$('[name=csrfmiddlewaretoken]').val(),
                        pizza : pizza,
                        size : size,
                        addition : addition
                        
                        },
                    success: function( data ) 
                            {
                        var response = $.parseJSON(data)
                        const price = response.price
                        console.log(`data received ${response.pizza} ${response.addition}`);
                        $("#price").text('Pizza Price: $'+response.price);   


                        $("#addtocart").click(function(){
                            alert("ajax started");
                        $.ajax(
                            {
                            type:"POST",
                            url: "/addtocart",
                            data:{
                                'csrfmiddlewaretoken' :$('[name=csrfmiddlewaretoken]').val(),
                                pizza : pizza,
                                 
                                size : size,
                                
                                addition : addition,

                                price : price,

                                toppings : toppings
                                  
                            },
                            success: function( data ){
                                console.log("success");
                                alert("Pizza added to cart");
                                $("#addtocart").prop("disabled", true);

                                }
                            
                            });    //close 2nd ajax
                            
                        });  //close add-to-cart button click
                        
                            }   //close 1st ajax success block
                    });      //close 1st ajax block                
                                         
            });    //close of addition change
        });         //close of size change
    });         //close of pizza change



    $("#dinner").change(function(){
        const dinner = $(this).val();
        console.log(dinner);
        $("#dinner").prop("disabled", true);
        $("#size-dinner").prop("disabled", false);
        $("#size-block-dinner").css("opacity", "1");
        $("#size-dinner").change(function(){
            const size = $(this).val();
            console.log(size);
            $("#size-dinner").prop("disabled", true);

            $.ajax(
                {
                    type : "POST",
                    url : "/ajax2",
                    data :{
                        'csrfmiddlewaretoken' :$('[name=csrfmiddlewaretoken]').val(),
                        dinner : dinner,
                        size : size
                    },
                    success: function(data){
                        var response = $.parseJSON(data)
                        const price = response.price
                        console.log(price);
                        $("#price-dinner").text(`Dinner Price: $${price}`)
                        $("#addtocart-dinner").prop("disabled", false);
                        $("#addtocart-dinner").click(function(){
                            console.log("button click");
                            $.ajax(
                                {
                                    type : "POST",
                                    url : "/addtocart_dinner",
                                    data :{
                                        'csrfmiddlewaretoken' :$('[name=csrfmiddlewaretoken]').val(),
                                        dinner : dinner,
                                        size : size,
                                        price : price
                                    },
                                    success: function(data){
                                        console.log("success");
                                        alert("Pizza added to cart");
                                        $("#addtocart-dinner").prop("disabled", true);

                                    }

                                }
                            )
                            
                        });
                    }
                }
            )


        });
    });         //dinner section close




    $("#pasta-dinner").change(function(){
        $("#addtocart-pasta-salad").prop("disabled", false);
        const pasta = parseFloat($(this).val());
        price = pasta;
        if (isNaN(parseFloat($("#salad-dinner").val()))){
            $("#block-pasta-salad").text("Total Price: $"+price);
           
        }
        else{
            const salad = parseFloat($("#salad-dinner").val());
            const price = (pasta + salad);
            $("#block-pasta-salad").text("Total price: $"+price);
        }
        
    });

    $("#salad-dinner").change(function(){
        $("#addtocart-pasta-salad").prop("disabled", false);
        const salad = parseFloat($(this).val());
        const pasta = parseFloat($("#pasta-dinner").val());
        if (isNaN(pasta)){
            $("#block-pasta-salad").text("Total price: $"+salad);
        }
        else{
            const price = (pasta + salad);
            $("#block-pasta-salad").text("Total price: $"+price);
        }

        
        
    });

    $("#addtocart-pasta-salad").click(function(){
        const pasta_price = parseFloat($("#pasta-dinner").val());
        const salad_price = parseFloat($("#salad-dinner").val());

        var selected_salad = $("#salad-dinner").find('option:selected');
        var salad = selected_salad.data('value');

        var selected_pasta = $("#pasta-dinner").find('option:selected');
        var pasta = selected_pasta.data('value');

        item = {};

        if((typeof(pasta) != "undefined") && (!isNaN(pasta_price)) && (typeof(salad) != "undefined") && (!isNaN(salad_price))){
            console.log("hola!!");
            console.log("mola!!!");
            item.pasta = pasta;
            item.salad = salad;
            item.price = pasta_price + salad_price;

        }

        else if ((typeof(pasta) != "undefined") && (!isNaN(pasta_price))){
            console.log("hola!!");
            item.pasta = pasta;
            item.price = pasta_price;
        }
        else{
            console.log("mola!!!");
            item.salad = salad;
            item.price = salad_price;
        }

        console.log(item);
        console.log(price);
        console.log(typeof(item));
        var json = JSON.stringify( item ); 
        $.ajax(
            {
                type : "POST",
                url : "addtocart_pasta_salad",
                data : {
                    'csrfmiddlewaretoken' :$('[name=csrfmiddlewaretoken]').val(),
                    item : json
                },
                success : function(data){
                    alert("item added to cart");
                    $("#addtocart-pasta-salad").prop("disabled", true);

                }
            }
        )

    });


    $("#sub").change(function(){
        $("#sub").prop("disabled", true);
        $("#subsizeblock").css("opacity", "1");
        $("#subsize").prop("disabled", false)
    });
    $("#subsize").change(function(){
        $("#subsize").prop("disabled", true);
        $("#extrabutton").prop("disabled", false);
        $("#extrabutton").css("opacity", "1");
        $("#addtocart-sub").prop("disabled", false);
        if($(this).val() == "small"){
            el = $("#sub").find(':selected').data('small')
       }
        else{
            el = $("#sub").find(':selected').data('large')
        }
        totalprice = parseFloat(el)
        $("#block-sub-price").text(`Price: $${totalprice}`)

    });
        $("#extrasubmit").click(function(){
            extraprice = 0
            $.each($("input[name=extra]:checked"), function(){            
                extraprice+=0.50;
            });
            if($("#subsize").val() == "small"){
                el = $("#sub").find(':selected').data('small')
           }
            else{
                el = $("#sub").find(':selected').data('large')
            }
            totalprice = parseFloat(extraprice)+parseFloat(el)
            $("#block-sub-price").text(`Price: $${totalprice}`)
            $("#addtocart-sub").prop("disabled", false);

        });
        $("#addtocart-sub").click(function(){
            var extra = []
            $.each($("input[name=extra]:checked"), function(){            
                extra.push($(this).val());
            });

            sub = $("#sub").val();
            size = $("#subsize").val();
            console.log(extra)
            $.ajax(
                {
                    type : "post",
                    url : "/addtocart_sub",
                    data : {
                        'csrfmiddlewaretoken' :$('[name=csrfmiddlewaretoken]').val(),
                        sub : sub,
                        size : size,
                        extra : extra,
                        price : totalprice
                    },
                    success : function(data){
                    $("#addtocart-sub").prop("disabled", true);
                        alert(data);
                    }
                }
            )
        
        
        });


    




});      //close document ready