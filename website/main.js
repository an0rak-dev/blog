function updateNavigationMask(maskEnabled, index) {
    const navBarElements =  document.getElementsByTagName("nav")[0].children[0];
    const updateClass = (elt) => {
        if (maskEnabled) {
            elt.classList.add("masked");
        } else {
            elt.classList.remove("masked");
        }
    }
    var elements = [...navBarElements.children];
    if (maskEnabled) {
        elements = elements.filter((elt, idx) => idx !== index);
    }
    elements.forEach((elt) => {
        const svg = elt.getElementsByTagName("img");
        if (svg.length > 0) {
            updateClass(svg[0]);
        } else {
            updateClass(elt);
        }
    });
    const main = document.getElementsByTagName("main")[0];
    updateClass(main);
}

function focusNavigationOn(index) {
    updateNavigationMask(true, index);
}

function unfocusNavigation() {
    updateNavigationMask(false);
}