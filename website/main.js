function focusNavigationOn(index) {
    const navBar =  document.getElementsByTagName("nav")[0];
    const navItems = navBar.children[0].children;
    for (var i=0; i < navItems.length; i++) {
        if (i !== index) {
            navItems[i].classList.add("nav-item-masked");
        }
    }
}

function unfocusNavigation() {
    const navBar =  document.getElementsByTagName("nav")[0];
    const navItems = navBar.children[0].children;
    for (var i=0; i < navItems.length; i++) {
        navItems[i].classList.remove("nav-item-masked");
    }
}