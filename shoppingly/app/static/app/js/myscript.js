$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }

})

function change_item(id,action) {
        // var id = $(this).attr('pid').toString();
        // var action = $(this).attr('etype').toString();
        // var add = this.parentNode.children[2];
        $.ajax({
            type: 'GET',
            url: '/edit_product',
        
            data: {
                "id": id,
                "action": action
            },

            success: function (data) {
                // console.log(data);
                // console.log(document.getElementById("quantity"));
                if (data.type != "remove") {
                    document.getElementById("quantity").innerText = data.quantity;
                }
                else {
                    document.getElementById("minus").parentNode.parentNode.parentNode.parentNode.remove();
                }
                // add.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.total_amount;

            }
        
        })
}