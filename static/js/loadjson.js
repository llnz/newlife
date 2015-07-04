function logData(data) {
  console.log(data);
}

function readJSON(handleData, dataFile) {
    var div_id = "jobsdata";

    //var dataFile = "jobs.json";

    $.ajax({
        url: dataFile,
        dataType: "text",
        mimeType: "application/json",
        success: function(data){
            //var obj = JSON.parse(data);
            //console.log(obj);
            handleData(JSON.parse(data));
        },
        error: function(){
            alert("Error loading file");
        }
    });
}

function queryJsonAPI(handleData, urlAPI) {
  $.ajax({
    url: urlAPI,
    dataType: "text",
    mimeType: "application/json",
    success: function(data){
        //var obj = JSON.parse(data);
        //console.log(obj);
        handleData(JSON.parse(data));
    },
    error: function(){
        alert("Error loading file");
    }
  });
}

function plotJobs(rawData) {
  var subCategories = rawData['Subcategories'];
  //console.log("subCat", subCategories);
  xlabels = [];
  counts = ["Counts"];

  for (var i=0; i<subCategories.length; i++) {
    //console.log(subCategories[i]);
    xlabels.push(subCategories[i]["Name"]);
    if (subCategories[i]["Count"] != undefined) {
      counts.push(subCategories[i]["Count"]);
    }
    else {
      counts.push(0);
    }
  }
  //console.log("xlabels", xlabels);
  //console.log("count", counts);
  countData = {columns: [counts], type: 'bar'};
  //console.log("ylabels", countData);

  var chart = c3.generate({
    bindto: '#jobschart',
    data: countData,
    axis: {
      x: {
        type: 'category',
        categories: xlabels
      }
    },
    legend: {hide: true}
  });
}

function plotProperties(rawData) {
  var districts = rawData[0]['Districts'];
  //console.log("districts", districts);
  xlabels = [];
  counts = ["Counts"];
  var wellingtonSubs;
  for (var i=0; i<districts.length; i++) {
    //console.log(districts[i]);
    xlabels.push(districts[i]["Name"]);
    if ((districts[i]["Name"]) == "Wellington") {
      wellingtonSubs = districts[i]["Suburbs"];
    }

    if (districts[i]["Count"] != undefined) {
      counts.push(districts[i]["Count"]);
    }
    else {
      counts.push(0);
    }
  }
  //console.log("xlabels", xlabels);
  //console.log("count", counts);
  countData = {columns: [counts], type: 'bar'};
  //console.log("ylabels", countData);

  var chart = c3.generate({
    bindto: '#propertieschart',
    data: countData,
    axis: {
      x: {
        type: 'category',
        categories: xlabels
      }
    },
    legend: {hide: true}
  });
}

queryJsonAPI(plotJobs, "http://api.trademe.co.nz/v1/Categories/5000.json?region=15&with_counts=true")
queryJsonAPI(plotProperties, "http://api.trademe.co.nz/v1/Localities/Region/15.json?with_counts=true")