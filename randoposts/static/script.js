function trig_db() {
    data = document.getElementById("db_data")
    if (data.style.display == "none") {
        data.style.display = "";
    } else {
        data.style.display = "none";
    }
    console.log(data.hidden)
}