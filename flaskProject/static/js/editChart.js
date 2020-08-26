function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    chart.update();
}

function replaceData(chart, value, dataset) {
    chart.data.datasets[dataset].data[0] = value
    chart.update()
}
function random_rgba() {
    let o = Math.round, r = Math.random, s = 255;
    return 'rgba(' + o(r()*s) + ',' + o(r()*s) + ',' + o(r()*s) + ', 0.2)';
}
function insertDataset(chart, newLabel, values) {
    let backcolor = random_rgba();
    let bordcolor = backcolor.substring(0,backcolor.length-4)+'1)'

    let newDataSet = {

        label: newLabel,
        backgroundColor: backcolor,
        borderColor: bordcolor,
        data: values,
    }

    chart.data.datasets.push(newDataSet);
    chart.update();
}

function removeDataset(chart, targetLabel) {
    chart.data.datasets = chart.data.datasets.filter(function(obj) {
        return (obj.label != targetLabel);
    });

    chart.update();

}