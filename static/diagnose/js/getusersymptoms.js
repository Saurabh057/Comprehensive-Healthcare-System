var symps = new Array();
function delThis(num) {

    var index = symps.indexOf(num);
    if (index > -1) {
        symps.splice(index, 1);
        $("#" + num).remove();
    }
}

function addThis(x) {


    var node = document.getElementById("suggestedSymps");
    node.querySelectorAll('*').forEach(n => n.remove());



    symps.push(x);
    document.getElementById("myInput").value = '';
    alert(symps);
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    suggestSymptoms();

}

function addUserSymps() {
    var x = document.getElementById("myInput").value;
    symps.push(x);
    document.getElementById("myInput").value = '';
    alert(symps);

    let strstsr = `<button type="button" id=` + x + ` class="btn alert alert-success" data-dismiss="alert" onclick=delThis('` + x + `') aria-label="Close">
                        <span>`+ x + `</span>
    </button>`

    // var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    suggestSymptoms();
}


document.getElementById("adduserSympButton").addEventListener("click", addUserSymps);

function addSuggestedSymp(x) {
    document.getElementById("myInput").value = x;
    $('#adduserSympButton').click();
}

function suggestSymptoms() {
    //hyat to array access krun yash chya decision tree la dyayachay

    $("#suggesionss").empty();
    
    var x = 'Suggested';

    //ithe fkt max 5 suggestions thev not more than that

    let strstsr = `<div class="sugestionsclass"> 
    Here are some <br> suggestions for you!<br>
                    <button type="button" class="btn alert alert-success" data-dismiss="alert" onclick=addSuggestedSymp('`+ x + `') aria-label="Close">
                        <span>`+ x + `</span> 
                    </button> <br><div>
                    `


    //he vrcha system kdun ghyaychay for now let it be
    $("#suggesionss").append(strstsr);

}



function changeContent(num) {
    if (num == 1) {
        //ithe ulti chya thikani symptom taak
        $("#inputsearchbar").hide();
        $("#quesanswers").show();


        $('#changeContentButt').html('Enter Sypmtoms');
        $("#changeContentButt").attr("onclick", "changeContent(2)");
    }
    else {

        $("#quesanswers").hide();
        $("#inputsearchbar").show();

        $('#changeContentButt').html('Prefer Questions?');
        $("#changeContentButt").attr("onclick", "changeContent(1)");
    }
}