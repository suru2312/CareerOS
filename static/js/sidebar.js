document.addEventListener("DOMContentLoaded", () => {

    const menuBtn = document.querySelector(".menu-toggle");
    const sidebar = document.querySelector(".sidebar");

    if(menuBtn){

        menuBtn.addEventListener("click", () => {

            sidebar.classList.toggle("show");

        });

    }

});