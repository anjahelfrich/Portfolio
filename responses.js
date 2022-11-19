function burgerMenu() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function openBurgerMenu() {
  document.getElementById("myTopnav").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}

function closeBurgerMenu() {
  document.getElementById("myTopnav").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

function homeMap() {
  var map = L.map('map').setView([35.1072, -106.6166], 13)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
}
