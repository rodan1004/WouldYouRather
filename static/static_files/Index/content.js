const content_query_child = document.querySelectorAll('.content-query-child');

const list_menu_a = document.querySelectorAll('.list-menu-a');

const menu = document.querySelector('#main-dropdown');

const category_menu = document.querySelector('.category-menu');

const start = document.querySelector('.start');

start.addEventListener('click', () => {
    window.location = 'http://127.0.0.1:8000/Time or Money'
});

const background_still = {
        first_content(index) {
            content_query_child[index].style.background = 'rgb(15, 128, 24)';
            content_query_child[index + 1].style.background = 'rgb(1, 25, 39)';
        },

        second_content(index) {
            content_query_child[index].style.background = 'rgb(15, 128, 24)';
            content_query_child[index - 1].style.background = 'rgb(1, 25, 39)';
        },

        // color() {
        //         list_menu_a.style.background = 'rgb(15, 128, 24)'
        // },

    }
    // console.log(content_query_child)

for (let i = 0; i < content_query_child.length; i++) {
    if ((i % 2) === 0) {
        content_query_child[i].addEventListener('click', () => { background_still.first_content(i) });
    } else {
        content_query_child[i].addEventListener('click', () => { background_still.second_content(i) });
    }
}

for (let list of list_menu_a) {
    list.addEventListener('click', (e) => {
        list.style.background = 'rgb(15, 128, 24)';
    })
}


category_menu.addEventListener('click', () => {
    menu.innerHTML = `
                
        
                <div class="JSdropdown"><ul><li>group.category</li></ul></div>
                <div class="JSdropdown"><ul><li>group.category2</li></ul></div>
                
                
        `
})