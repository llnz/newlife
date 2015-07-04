function logData(data) {
  console.log(data);
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
    }
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
    }
  });
}

  /*
function plotPropertiesSuburbs(rawData) {
  var welLabels = [];
  var welCounts = ["Counts"];
  for (var i=0; i<wellingtonSubs.length; i++) {
    //console.log(wellingtonSubs[i]);
    welLabels.push(wellingtonSubs[i]["Name"]);

    if (wellingtonSubs[i]["Count"] != undefined) {
      welCounts.push(wellingtonSubs[i]["Count"]);
    }
    else {
      welCounts.push(0);
    }
  }
  console.log(welLabels);
  console.log(welCounts);
  var chartWellington = c3.generate({
    bindto: '#propertiesWellingtonchart',
    data: welCounts,
    axis: {
      x: {
        type: 'category',
        categories: welLabels
      }
    }
  });
}*/

//jQuery.ready = function() {
function readJSON(handleData, dataFile) {
    var div_id = "jobsdata";

    //var dataFile = "jobs.json";

    $.ajax({
        url: dataFile,
        dataType: "text",
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

//readJSON(logData, "jobs.json");
readJSON(plotJobs, "jobs.json");
//readJSON(logData, "properties.json");
readJSON(plotProperties, "properties.json");