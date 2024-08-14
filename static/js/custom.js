$('.addToCartBtn').click(function (e) {
  e.preventDefault()

  var tour_id = $(this).closest('.tour_data').find('.tour_id').val()
  var token = $('input[name=csrfmiddlewaretoken]').val()
  $.ajax({
    method: 'POST',
    url: '/add_to_cart',
    data: {
      tour_id,
      csrfmiddlewaretoken: token
    },
    success: function (res) {
      alert(String(res.status))
      window.location = '/all_my_cart'
    }
  })
})

$('.delete-item-cart').click(function (e) {
  e.preventDefault()
  var tour_id = $(this).closest('.tour_data').find('.tour_id').val()
  // console.log(tour_id)
  // var token = $('input[name=csrfmiddlewaretoken]').val()

  // $.ajax({
  //   method: 'POST',
  //   url: '/delete_cart_item',
  //   data: {
  //     tour_id,
  //     csrfmiddlewaretoken: token
  //   },
  //   success: function (res) {
  //     alert(String(res.status))
  //     window.location = 'all_my_cart'
  //   }
  // })
})
