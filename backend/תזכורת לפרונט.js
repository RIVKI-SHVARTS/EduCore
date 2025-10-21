//מצד הפרונט – ב־fetch (או axios), צריך לשלוח את הטוקן כך:


fetch("/users", {
  headers: {
    "Authorization": "Bearer " + localStorage.getItem("token")
  }
})