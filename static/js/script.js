$('.pluscart').click(function(){
    var id=$(this).attr("productid").toString();
    console.log(id)
    var x=this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"../pluscart",
        data:{
            product_id:id
        },
        success:function(data){
            console.log(data)
            x.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    });
});

$('.minuscart').click(function(){
    var id=$(this).attr("productid").toString();
    console.log(id)
    var x=this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"../minuscart",
        data:{
            product_id:id
        },
        success:function(data){
            console.log(data)
            x.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
          
        }
    });
});