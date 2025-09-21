const themeSwitch = document.getElementById("input");
const body = document.body;

// Load saved theme on page load
if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark");
    themeSwitch.checked = true;
} else {
    body.classList.remove("dark");
    themeSwitch.checked = false;
}

// Listen for toggle
themeSwitch.addEventListener("change", () => {
    if (themeSwitch.checked) {
        body.classList.add("dark");
        localStorage.setItem("theme", "dark");
    } else {
        body.classList.remove("dark");
        localStorage.setItem("theme", "light");
    }
});