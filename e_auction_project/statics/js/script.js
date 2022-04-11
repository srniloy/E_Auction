const setActiveNav = (e) => {
    const navItems = document.querySelectorAll('.home-nav-item');
    navItems.forEach(element => {
        element.classList.remove("active");
    });
    e.classList.add("active");
}