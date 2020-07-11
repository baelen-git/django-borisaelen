// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the stickyElement
var stickyElement = document.getElementById("stickyElement");

// Get the offset position of the stickyElement
var sticky = stickyElement.offsetTop;

// Add the sticky class to the stickyElement when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    stickyElement.classList.add("fixed-top")
    stickyElement.classList.add("container")
  } else {
    stickyElement.classList.remove("fixed-top");
    stickyElement.classList.remove("container");
  }
}