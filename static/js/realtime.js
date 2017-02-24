
function append_to_dom(data) {
    var data = JSON.parse(data)
    if (data.length == 0) {
        return
    }
    var blocks = data.map(function (stock) {

        var block = "<div class='col s12 m4'><div class='card blue-grey darken-2'><div class='card-content white-text'><span class='card-title'>" + stock.Symbol;
        block += "</span><table><tr><td>LTP : </td><td>" + stock["Last Traded Price"] + "</td></tr>";
        block += "<tr><td>% Change :</td><td>" + stock["% Change"] + "</td></tr>";
        block += "<tr><td>Traded Qty :</td><td>" + stock["Traded Volume"] + "</td></tr>";
        block += "<tr><td>Value(Lakhs) :</td><td>" + stock["Traded Value"] + "</td></tr>";
        block += "<tr><td>Open :</td><td>" + stock["Open"] + "</td></tr>";
        block += "<tr><td>High :</td><td>" + stock["High"] + "</td></tr>";
        block += "<tr><td>Low :</td><td>" + stock["Low"] + "</td></tr>";
        block += "<tr><td>Prev. Close :</td><td>" + stock["Previous Close"] + "</td></tr>";
        block += "<tr><td>Latest Ex Date :</td><td>" + stock["Latest Ex Date"] + "</td></tr></table>";
        block += "</div></div></div>";
        return block;

    });
    $("#realtime").html(blocks).hide().fadeIn();
}

function ajaxPolling() {
    $.ajax({
        url: "update",
        data: {
            "timestamp": 0
        }
    }).done(function (data) {
        append_to_dom(data);
    }).always(function () {
        setTimeout(ajaxPolling, 60000);
    })
}

$(document).ready(function () {
    ajaxPolling();
})

