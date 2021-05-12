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
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    suggestSymptoms();
}


document.getElementById("adduserSympButton").addEventListener("click", addUserSymps);


function suggestSymptoms() {
    //hyat to array access krun yash chya decision tree la dyayachay


    var x = 'Suggested';
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=addThis('" + x + "')>" + x + "</button>";
    //he vrcha system kdun ghyaychay for now let it be
    $("#suggestedSymps").append(strstsr);

}