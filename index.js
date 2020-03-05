

const content_query_child = document.querySelectorAll('.content-query-child')
//
const background_still = {       
        first_content() {
                content_query_child[0].style.background = 'rgb(15, 128, 24)';
                content_query_child[1].style.background = 'rgb(1, 25, 39)';
        },

        second_content() {
                content_query_child[1].style.background = 'rgb(15, 128, 24)';
                content_query_child[0].style.background = 'rgb(1, 25, 39)';
        }
}
// console.log(content_query_child)

content_query_child[0].addEventListener('click', background_still.first_content);
content_query_child[1].addEventListener('click', background_still.second_content);


        
                
                






