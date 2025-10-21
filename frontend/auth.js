

function setupTokenWatcher(token) {
  if (!token) return;

  const decoded = JSON.parse(atob(token.split('.')[1]));
  const expiryTime = decoded.exp * 1000;
  console.log(expiryTime);
  const now = Date.now();
  console.log(now);

  const timeLeft = expiryTime - now;

  if (timeLeft > 60000) {
    setTimeout(() => {
      alert('The token will expire in a minute. Please save your work.');
    }, timeLeft - 60000);
  }

  setTimeout(() => {
    alert('Expired. You will be redirected to the login page.');
    sessionStorage.clear();
    window.location.href = 'login.html';
  }, timeLeft);
}

// אחרי שהעמוד נטען
document.addEventListener('DOMContentLoaded', () => {
  const token = sessionStorage.getItem('token');
  setupTokenWatcher(token);
});
