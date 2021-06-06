// $(document).ready(function() {
//     $("#myCarousel").on("slide.bs.carousel", function(e) {
//         var $e = $(e.relatedTarget);
//         var idx = $e.index();
//         var itemsPerSlide = 3;
//         var totalItems = $(".carousel-item").length;

//         if (idx >= totalItems - (itemsPerSlide - 1)) {
//             var it = itemsPerSlide - (totalItems - idx);
//             for (var i = 0; i < it; i++) {
//                 // append slides to end
//                 if (e.direction == "left") {
//                     $(".carousel-item")
//                         .eq(i)
//                         .appendTo(".carousel-inner");
//                 } else {
//                     $(".carousel-item")
//                         .eq(0)
//                         .appendTo($(this).find(".carousel-inner"));
//                 }
//             }
//         }
//     });
// });

function randomChange() {
        const url = 'http://127.0.0.1:8000/api/';
        fetch(url)
            .then((resp) => resp.json())
            .then(data => {
                    let random_data = Math.floor(Math.random() * data.length)
                    console.log(data[random_data])

            })
    };


const right = document.querySelector('.right');



// right.addEventListener('click', () => {
//     x = Math.floor((Math.random() * 10) + 1);
//     console.log(x);
// });
right.addEventListener('click', randomChange());