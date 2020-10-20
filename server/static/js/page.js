function init(){
    // register the event handler
    document.getElementById("submit_button").addEventListener("click", getResult);

    var result_document;
}

function getResult(){
    // show loading icon
    show_loading();

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
            result_document += result[i]+"<br><br>";
        }
        document.getElementById("result").innerHTML = result_document;

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
    var loading_object = document.getElementById("loading");
    loading_object.style.display = "block";
    var content_object = document.getElementById("content")
    content_object.style.display = "none"
}

function hide_loading(){
    var loading_object = document.getElementById("loading");
    loading_object.style.display = "none";
    var content_object = document.getElementById("content")
    content_object.style.display = "block"
}
