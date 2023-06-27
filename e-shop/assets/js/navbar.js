// MENU & SEARCH
const menuBtn = document.querySelector(".menu-icon span");
const searchBtn = document.querySelector(".search-icon");
const cancelBtn = document.querySelector(".cancel-icon");
const items = document.querySelector(".nav-items");
const form = document.querySelector("form");
menuBtn.onclick = () => {
  items.classList.add("active");
  menuBtn.classList.add("hide");
  searchBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}
cancelBtn.onclick = () => {
  items.classList.remove("active");
  menuBtn.classList.remove("hide");
  searchBtn.classList.remove("hide");
  cancelBtn.classList.remove("show");
  form.classList.remove("active");
  cancelBtn.style.color = "#ff3d00";
}
searchBtn.onclick = () => {
  form.classList.add("active");
  searchBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}


// Close the menu
const closeMenu = () => {
  items.classList.remove("active");
  menuBtn.classList.remove("hide");
  searchBtn.classList.remove("hide");
  cancelBtn.classList.remove("show");
  form.classList.remove("active");
  cancelBtn.style.color = "#ff3d00";
};

//  Event listener to close the menu when clicked outside
// document.addEventListener("click", (event) => {
//   const isClickInsideMenu = items.contains(event.target);
//   const isClickOnMenuButton = menuBtn.contains(event.target);
//   if (!isClickInsideMenu && !isClickOnMenuButton) {
//     closeMenu();
//   }
// });
// Doesn't work currently, it messes up the search form pop-up. Will be fixed later on.


// BORDER & COLOR CHANGE ON SCROLL
window.addEventListener('scroll', function () {
  var navbar = document.querySelector('nav');
  var scrollPosition = window.scrollY;

  // Set the scroll position at which we want to add the border
  var scrollThreshold = window.innerHeight * 0.62; // 75% of viewport height, around end of hero header
  if (scrollPosition >= scrollThreshold) {
    navbar.classList.add('nav-border');
    navbar.classList.add('nav-dark');

  } else {
    navbar.classList.remove('nav-border');
    navbar.classList.remove('nav-dark');
  }
});
