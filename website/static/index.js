function deleteChore(choreId) {
    fetch("/delete-chore", {
      method: "DELETE",
      body: JSON.stringify({ choreId: choreId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}