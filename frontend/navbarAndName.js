

// // const isAdmin = sessionStorage.getItem("admin") === "true";

// // // יוצרים את אלמנט ה-nav
// // const nav = document.createElement("nav");

// // // פונקציה עוזרת ליצור קישור
// // function createNavLink(text, href) {
// //   const link = document.createElement("a");
// //   link.href = href;
// //   link.textContent = text;
// //   link.classList.add("nav-link"); // שימוש ב-CSS
// //   return link;
// // }

// // // מוסיפים קישורים לסרגל
// // nav.appendChild(createNavLink("Courses", "courses.html"));
// // nav.appendChild(createNavLink("Enrollments", "enrollments.html"));
// // if (isAdmin) {
// //   nav.appendChild(createNavLink("Users Management", "manageUsers.html"));
// // }

// // // קישור לוגאאוט שמנקה session
// // const logoutLink = createNavLink("Logout", "login.html");
// // logoutLink.addEventListener("click", () => {
// //   sessionStorage.clear();
// // });
// // nav.appendChild(logoutLink);

// // // מוסיפים את הסרגל ל-container
// // document.getElementById("navbar-container").appendChild(nav);

// // // פונקציה לעדכון שם המשתמש
// // function setUserName() {
// //   const nameFromSession = sessionStorage.getItem("name");
// //   const nameElement = document.getElementById("nameElement");
// //   if (nameElement) {
// //     nameElement.textContent = nameFromSession || "";
// //   }
// // }

// // // לקרוא לפונקציה כשהעמוד נטען
// // document.addEventListener("DOMContentLoaded", setUserName);



// const isAdmin = sessionStorage.getItem("admin") === "true";

// // יוצרים את האלמנט הראשי
// const header = document.createElement("header");
// header.classList.add("top-nav");

// // לוגו בצד שמאל
// const logo = document.createElement("div");
// logo.classList.add("logo");
// logo.textContent = "MyCourses";
// header.appendChild(logo);

// // יצירת הסרגל המרכזי
// const mainNav = document.createElement("div");
// mainNav.classList.add("main-nav");

// function createNavLink(text, href) {
//   const link = document.createElement("a");
//   link.href = href;
//   link.textContent = text;
//   return link;
// }

// mainNav.appendChild(createNavLink("Courses", "courses.html"));
// mainNav.appendChild(createNavLink("Enrollments", "enrollments.html"));
// if (isAdmin) {
//   mainNav.appendChild(createNavLink("Users Management", "manageUsers.html"));
// }

// header.appendChild(mainNav);

// // צד ימין – שם משתמש + logout
// const userInfo = document.createElement("div");
// userInfo.classList.add("user-info");

// const userName = document.createElement("span");
// userName.classList.add("user-name");
// userName.id = "nameElement"; // חשוב בשביל JS
// userInfo.appendChild(userName);

// const userIcon = document.createElement("div");
// userIcon.classList.add("user-icon");
// userInfo.appendChild(userIcon);

// // logout
// const logoutLink = createNavLink("Logout", "login.html");
// logoutLink.classList.add("logout-link");
// logoutLink.addEventListener("click", () => {
//   sessionStorage.clear();
// });
// userInfo.appendChild(logoutLink);

// header.appendChild(userInfo);

// // מוסיפים ל-DOM
// document.getElementById("navbar-container").appendChild(header);

// // לקרוא לעדכון שם המשתמש
// document.addEventListener("DOMContentLoaded", function() {
//   const nameFromSession = sessionStorage.getItem("name");
//   const nameEl = document.getElementById("nameElement");
//   if (nameEl) nameEl.textContent = nameFromSession || "";
// });






















// const isAdmin = sessionStorage.getItem("admin") === "true";

// // יוצרים את האלמנט הראשי
// const header = document.createElement("header");
// header.classList.add("top-nav");

// // לוגו בצד שמאל
// const logo = document.createElement("div");
// logo.classList.add("logo");
// // logo.textContent = "MyCourses";
// header.appendChild(logo);

// // יצירת הסרגל המרכזי
// const mainNav = document.createElement("div");
// mainNav.classList.add("main-nav");

// // פונקציה ליצירת קישורים
// function createNavLink(text, href) {
//   const link = document.createElement("a");
//   link.href = href;
//   link.textContent = text;
//   return link;
// }

// // הוספת קישורים
// mainNav.appendChild(createNavLink("Courses", "courses.html"));
// mainNav.appendChild(createNavLink("Enrollments", "enrollments.html"));
// if (isAdmin) {
//   mainNav.appendChild(createNavLink("Users Management", "manageUsers.html"));
// }

// header.appendChild(mainNav);

// // צד ימין – שם משתמש + אייקון + Logout
// const userInfo = document.createElement("div");
// userInfo.classList.add("user-info");

// // אייקון משתמש
// const userIcon = document.createElement("div");
// userIcon.classList.add("user-icon");

// const img = document.createElement("img");
// img.src = "https://cdn.pixabay.com/photo/2023/02/18/11/00/icon-7797704_1280.png"; // או נתיב דינמי אם יש
// img.alt = "User";
// userIcon.appendChild(img);

// userInfo.appendChild(userIcon);

// userIcon.textContent = sessionStorage.getItem("name") ? sessionStorage.getItem("name")[0].toUpperCase() : "?";
// userInfo.appendChild(userIcon);

// // שם משתמש
// const userName = document.createElement("span");
// userName.classList.add("user-name");
// userName.id = "nameElement";
// userInfo.appendChild(userName);

// // Logout
// const logoutLink = createNavLink("Logout", "login.html");
// logoutLink.classList.add("logout-link");
// logoutLink.addEventListener("click", () => {
//   sessionStorage.clear();
// });
// userInfo.appendChild(logoutLink);

// header.appendChild(userInfo);

// // מוסיפים ל-DOM
// document.getElementById("navbar-container").appendChild(header);

// // הגדרת שם המשתמש
// function setUserName() {
//   const nameFromSession = sessionStorage.getItem("name");
//   const nameEl = document.getElementById("nameElement");
//   if (nameEl) nameEl.textContent = nameFromSession || "";
// }

// // לקרוא לפונקציה כשהעמוד נטען
// document.addEventListener("DOMContentLoaded", setUserName);

// // סימון העמוד הנוכחי ב-navbar
// const currentPage = window.location.pathname.split("/").pop(); 
// mainNav.querySelectorAll("a").forEach(link => {
//   if(link.getAttribute("href") === currentPage) {
//     link.classList.add("active");
//   }
// });



// const links = document.querySelectorAll("#nav a");
// links.forEach(link => {
//     if (link.href === window.location.href) {
//         link.classList.add("active");
//     } else {
//         link.classList.remove("active");
//     }
// });




















const isAdmin = sessionStorage.getItem("admin") === "true";

// יוצרים את האלמנט הראשי
const header = document.createElement("header");
header.classList.add("top-nav");

// לוגו בצד שמאל
const logo = document.createElement("div");
logo.classList.add("logo");
// logo.textContent = "MyCourses";
header.appendChild(logo);

// יצירת הסרגל המרכזי
const mainNav = document.createElement("div");
mainNav.classList.add("main-nav");

// פונקציה ליצירת קישורים
function createNavLink(text, href, section) {
  const link = document.createElement("a");
  link.href = href;
  link.textContent = text;
  if (section) link.dataset.section = section; // ← חדש
  return link;
}

// הוספת קישורים
mainNav.appendChild(createNavLink("Courses", "courses.html", "courses"));
mainNav.appendChild(createNavLink("Enrollments", "enrollments.html", "enrollments"));
if (isAdmin) {
  mainNav.appendChild(createNavLink("Users Management", "manageUsers.html", "users"));
}

header.appendChild(mainNav);

// צד ימין – שם משתמש + אייקון + Logout
const userInfo = document.createElement("div");
userInfo.classList.add("user-info");

// אייקון משתמש
const userIcon = document.createElement("div");
userIcon.classList.add("user-icon");

const img = document.createElement("img");
img.src = "https://cdn.pixabay.com/photo/2023/02/18/11/00/icon-7797704_1280.png"; // או נתיב דינמי אם יש
img.alt = "User";
userIcon.appendChild(img);

userInfo.appendChild(userIcon);

// userIcon.textContent = sessionStorage.getItem("name") ? sessionStorage.getItem("name")[0].toUpperCase() : "?";
// userInfo.appendChild(userIcon);

// שם משתמש
const userName = document.createElement("span");
userName.classList.add("user-name");
userName.id = "nameElement";
userInfo.appendChild(userName);

// Logout
const logoutLink = createNavLink("Logout", "login.html");
logoutLink.classList.add("logout-link");
logoutLink.addEventListener("click", () => {
  sessionStorage.clear();
});
userInfo.appendChild(logoutLink);

header.appendChild(userInfo);

// מוסיפים ל-DOM
document.getElementById("navbar-container").appendChild(header);

// הגדרת שם המשתמש
function setUserName() {
  const nameFromSession = sessionStorage.getItem("name");
  const nameEl = document.getElementById("nameElement");
  if (nameEl) nameEl.textContent = nameFromSession || "";
}

// לקרוא לפונקציה כשהעמוד נטען
document.addEventListener("DOMContentLoaded", setUserName);

// סימון העמוד הנוכחי ב-navbar
// // סימון העמוד הנוכחי ב-navbar העליון (top-nav)
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