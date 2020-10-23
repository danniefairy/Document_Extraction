function init(){
    // register the event handler
    document.getElementById("submit_button").addEventListener("click", getResult);
    document.getElementById("language-selection").addEventListener("change", switch_lang);

    // initialize the result
    var english_result;
    var chinese_result;
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
        english_result = response.data.english_result;
        chinese_result = response.data.chinese_result;

        // set english result as default result
        document.getElementById("language-selection").value = "en";
        set_result(english_result);

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

function switch_lang(){
    var e = document.getElementById("language-selection");
    if(e.value=="en"){
        set_result(english_result);
    } else if (e.value=="zh-tw"){
        set_result(chinese_result);
    }
}

function set_result(result){
    var result_document = "";
    for (var i=0; i<result.length;i++){
        result_document += result[i]+"\n";
    }
    document.getElementById("result").value = result_document;
}

function show_loading(){
    document.getElementById('body').style.backgroundImage = "url('/static/images/loadingimage.gif')";
    document.getElementById('body').style.backgroundRepeat = "no-repeat";
    document.getElementById('body').style.backgroundPosition = "center";
    document.getElementById('body').style.backgroundSize = "300px";
    var content_object = document.getElementById("content")
    content_object.style.display = "none"
}

function hide_loading(){
    document.getElementById('body').style.backgroundImage = "";
    var content_object = document.getElementById("content")
    content_object.style.display = "block"
}
