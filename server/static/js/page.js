function init(){
    // register the event handler
    document.getElementById("submit_button").addEventListener("click", getResult);

    var result_document;
}

function getResult(){
    // show loading icon
    show_loading();

    // get initial time
    var start_time = new Date()

    // get input data 
    var doc = document.getElementById("doc");
    var params = {};
    params.document = doc.value;

    axios.post(
        'http://localhost:5000/inference', 
        {params}            
    )
    .then((response) => {
        // get response
        var result = response.data.result;
        result_document = "";
        for (var i=0; i<result.length;i++){
            result_document += result[i]+"\n";
        }
        document.getElementById("result").value = result_document;

        // calculate the duration
        var end_time = new Date();
        document.getElementById("duration").textContent = "Duration: "+ (end_time-start_time)+"ms";

        // hide loading icon
        hide_loading();
    })
    .catch(function (error) {
        console.log(error);
    });

}

function concate_result(sentence){
    result_document += item+"/n";
    document.getElementById("result").innerHTML = result_document;
}

function show_loading(){
    //var loading_object = document.getElementById("loading");    
    //loading_object.style.display = "block";
    document.getElementById('body').style.backgroundImage = "url('/static/images/loadingimage.gif')";
    document.getElementById('body').style.backgroundRepeat = "no-repeat";
    document.getElementById('body').style.backgroundPosition = "center";
    document.getElementById('body').style.backgroundSize = "300px";
    var content_object = document.getElementById("content")
    content_object.style.display = "none"
}

function hide_loading(){
    //var loading_object = document.getElementById("loading");
    //loading_object.style.display = "none";
    document.getElementById('body').style.backgroundImage = "";
    var content_object = document.getElementById("content")
    content_object.style.display = "block"
}
