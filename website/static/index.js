function deleteChore(choreId) {
    fetch("/delete-chore", {
      method: "POST",
      body: JSON.stringify({ choreId: choreId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}