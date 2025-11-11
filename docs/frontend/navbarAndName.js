



















const isAdmin = sessionStorage.getItem("admin") === "true";


const header = document.createElement("header");
header.classList.add("top-nav");


const logo = document.createElement("div");
logo.classList.add("logo");
header.appendChild(logo);

const mainNav = document.createElement("div");
mainNav.classList.add("main-nav");

function createNavLink(text, href, section) {
  const link = document.createElement("a");
  link.href = href;
  link.textContent = text;
  if (section) link.dataset.section = section; // ← חדש
  return link;
}

mainNav.appendChild(createNavLink("Courses", "courses.html", "courses"));
mainNav.appendChild(createNavLink("Enrollments", "enrollments.html", "enrollments"));
if (isAdmin) {
  mainNav.appendChild(createNavLink("Users Management", "manageUsers.html", "users"));
}

header.appendChild(mainNav);

const userInfo = document.createElement("div");
userInfo.classList.add("user-info");

const userIcon = document.createElement("div");
userIcon.classList.add("user-icon");

const img = document.createElement("img");
img.src = "https://cdn.pixabay.com/photo/2023/02/18/11/00/icon-7797704_1280.png"; // או נתיב דינמי אם יש
img.alt = "User";
userIcon.appendChild(img);

userInfo.appendChild(userIcon);


const userName = document.createElement("span");
userName.classList.add("user-name");
userName.id = "nameElement";
userInfo.appendChild(userName);

const logoutLink = createNavLink("Logout", "login.html");
logoutLink.classList.add("logout-link");
logoutLink.addEventListener("click", () => {
  sessionStorage.clear();
});
userInfo.appendChild(logoutLink);

header.appendChild(userInfo);

document.getElementById("navbar-container").appendChild(header);

function setUserName() {
  const nameFromSession = sessionStorage.getItem("name");
  const nameEl = document.getElementById("nameElement");
  if (nameEl) nameEl.textContent = nameFromSession || "";
}

document.addEventListener("DOMContentLoaded", setUserName);

const page = window.location.pathname.split("/").pop().toLowerCase();

let currentSection = null;
if (page.includes("course")) currentSection = "courses";
else if (page.includes("enroll")) currentSection = "enrollments";
else if (page.includes("user") || page.includes("manageusers")) currentSection = "users";

if (currentSection) {
  mainNav.querySelectorAll(`a[data-section="${currentSection}"]`)
    .forEach(a => a.classList.add("active"));
}




const links = document.querySelectorAll("#nav a");
links.forEach(link => {
    if (link.href === window.location.href) {
        link.classList.add("active");
    } else {
        link.classList.remove("active");
    }
});