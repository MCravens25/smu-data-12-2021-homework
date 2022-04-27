$(document).ready(function() {
    console.log("Page Loaded");
    doWork();

    $("#selDataset").on("change", function() {
        makeDashboard()
    });
});

// Create a variable to help run our code efficiently
var global_data;

function doWork() {
    // Problem 1: Can I read in the data and then print?
    var url = "static/data/samples.json";
    requestD3(url);
}

function makeDashboard() {
    let id = $("#selDataset").val();

    createMetadata(id);
    createBarChart(id);
    createBubbleChart(id);
    createGaugeChart(id);
}

function requestD3(url) {
    d3.json(url).then(function(data) {
        console.log(data);
        // This variable will hold the data that we can always call to because it will be unchanged
        global_data = data;
        createDropdown();
        makeDashboard();
    });
}

function createDropdown() {
    var names = global_data.names;
    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        let html = `<option>${name}</option>`;
        $("#selDataset").append(html);
    }
}

function createMetadata(id) {
    $("#sample-metadata").empty();
    let info = global_data.metadata.filter(x => x.id == id)[0];
    console.log(info);
    Object.entries(info).map(function(x) {
        let html = `<h6>${x[0]}: ${x[1]}</h6>`;
        $("#sample-metadata").append(html);
    });
}

function createBarChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        type: 'bar',
        // .reverse() to help sort the barchart in descending order
        x: sample.sample_values.slice(0, 10).reverse(),
        y: sample.otu_ids.map(x => `OTU ${x}`).slice(0, 10).reverse(),
        text: sample.otu_labels.slice(0, 10).reverse(),
        orientation: 'h'
    }

    var data1 = [trace1];
    var layout = {
        "title": "Most found bacteria Within Each Individual",
        "xaxis": {
            "title": 'Count of Bacteria Found',
            "titlefont": {
                "family": 'Arial, sans-serif',
                "size": 18,
                "color": 'black'
            }
        },
        "yaxis": {
            "title": 'OTU_ID',
            "titlefont": {
                "family": 'Arial, sans-serif',
                "size": 18,
                "color": 'black'
            }
        }
    }

    Plotly.newPlot('bar', data1, layout);
}

function createBubbleChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        x: sample.otu_ids,
        y: sample.sample_values,
        text: sample.otu_labels.slice(0, 10).reverse(),
        mode: 'markers',
        marker: {
            size: sample.sample_values,
            color: sample.otu_ids,
            colorscale: "RdBu"
        }
    }

    var data1 = [trace1];
    var layout = {
        "title": "Bacteria By the Bubble",
        "xaxis": {
            "title": 'OTU_ID',
            "titlefont": {
                "family": 'Arial, sans-serif',
                "size": 18,
                "color": 'black'
            }
        },
        "yaxis": {
            "title": 'Bacteria Found',
            "titlefont": {
                "family": 'Arial, sans-serif',
                "size": 18,
                "color": 'black'
            }
        }
    }

    Plotly.newPlot('bubble', data1, layout);
}

function createGaugeChart(id) {
    let info = global_data.metadata.filter(x => x.id == id)[0];
    let avg = global_data["metadata"].map(x => x.wfreq).reduce((a, b) => a + b, 0) / global_data.metadata.length;

    var trace = {
        domain: { x: [0, 1], y: [0, 1] },
        value: info["wfreq"],
        type: "indicator",
        mode: "gauge+number+delta",
        delta: { reference: avg.toFixed(2) },
        gauge: {
            axis: { range: [null, 10] },
            steps: [
                { range: [0, 5], color: "lightgray" },
                { range: [5, 7], color: "gray" }
            ],
            threshold: {
                line: { color: "red", width: 4 },
                thickness: 0.75,
                value: 9.5
            }
        }
    };

    var data1 = [trace];

    var layout = {
        title: "OTU ID's Washing Frequency per Week"
    };
    Plotly.newPlot('gauge', data1, layout);
}


