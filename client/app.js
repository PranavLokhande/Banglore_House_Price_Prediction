function getBathValue() {
    const uiBathrooms = document.getElementsByName("uiBathrooms");
    for (let i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    const uiBHK = document.getElementsByName("uiBHK");
    for (let i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    const sqft = document.getElementById("uiSqft").value;
    const bhk = getBHKValue();
    const bathrooms = getBathValue();
    const location = document.getElementById("uiLocations").value;
    const estPrice = document.getElementById("uiEstimatedPrice");

    if (sqft === "" || bhk === -1 || bathrooms === -1 || location === "") {
        estPrice.innerHTML = "<h2>Please fill in all fields.</h2>";
        return;
    }

    const url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft),
        bhk: bhk,
        bath: bathrooms,
        location: location
    }).done(function (data) {
        console.log(data.estimated_price);
        estPrice.innerHTML = `<h2>${data.estimated_price.toString()} Lakh</h2>`;
    }).fail(function () {
        estPrice.innerHTML = "<h2>Error fetching the estimated price. Please try again later.</h2>";
    });
}

function onPageLoad() {
    console.log("document loaded");
    const url = "http://127.0.0.1:5000/get_location_names";

    $.get(url, function (data) {
        console.log("got response for get_location_names request");
        if (data) {
            const locations = data.locations;
            const uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            $('#uiLocations').append('<option value="" disabled selected>Choose a Location</option>');
            locations.forEach(function (location) {
                $('#uiLocations').append(new Option(location));
            });
        }
    }).fail(function () {
        console.log("Error fetching location names.");
    });
}

window.onload = onPageLoad;
