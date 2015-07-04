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

function countJobs(rawData) {
  var subCategories = rawData['Subcategories'];
  //console.log("subCat", subCategories);
  //xlabels = [];
  counts = 0;

  for (var i=0; i<subCategories.length; i++) {
    //console.log(subCategories[i]);
    //xlabels.push(subCategories[i]["Name"]);
    if (subCategories[i]["Count"] != undefined) {
      counts += subCategories[i]["Count"];
    }
  }
  document.getElementById("jobsnb").innerHTML = counts;
}

function countProperties(rawData) {
  var districts = rawData[0]['Districts'];
  counts = 0;
  for (var i=0; i<districts.length; i++) {
    if (districts[i]["Count"] != undefined) {
      counts += districts[i]["Count"];
    }
  }
  document.getElementById("propertiesnb").innerHTML = counts;
}

function countCrimes(rawData) {
  counts = 0;
  for (var i=0; i<rawData.length; i++) {
    counts += rawData[i]["Value"];
  }
  document.getElementById("idsafety").innerHTML = counts;
}

function getLocalityData() {
  var locality = "Wellington";
  var locID = 15;
  //document.getElementById("tabtitle").innerHTML = locality;
  queryJsonAPI(countJobs, "http://api.trademe.co.nz/v1/Categories/5000.json?region=15&with_counts=true");
  queryJsonAPI(countProperties, "http://api.trademe.co.nz/v1/Localities/Region/15.json?with_counts=true");
  queryJsonAPI(countCrimes, "CrimeStatsWgn.json");
}

getLocalityData()