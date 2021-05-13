var symps = new Array();
function delThis(num) {

    var index = symps.indexOf(num);
    if (index > -1) {
        symps.splice(index, 2);
        $("#" + num).remove();
    }
}

function addThis(x) {


    var node = document.getElementById("suggestedSymps");
    node.querySelectorAll('*').forEach(n => n.remove());



    symps.push(x);
    symps.push('1');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    getsuggestions();

}

function addUserSymps() {
    var x = document.getElementById("myInput").value;
    symps.push(x);
    symps.push('1');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    getsuggestions();
}


document.getElementById("adduserSympButton").addEventListener("click", addUserSymps);
function addyes(){
    var x=document.getElementById("yes").value;
    symps.push(x);
    symps.push('1');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    qa();
}
function addno(){
    var x=document.getElementById("no").value;
    symps.push(x);
    symps.push('0');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    qa();
}


function suggestSymptoms(a) {
    //hyat to array access krun yash chya decision tree la dyayachay
    var node = document.getElementById("suggestedSymps");
    node.querySelectorAll('*').forEach(n => n.remove());
    var st= '<button class="btn text-center m-1" style="border:none; background-color:#f8f9fa;">Suggested:</p>';
    $("#suggestedSymps").append(st);
    for(var i=0;i<a.length;i++){
        var strstsr = '<button id=' + a[i] + " class='btn btn-outline-secondary text-center m-1' onclick=addThis('" + a[i] + "')>" + a[i] + "</button>";
        //he vrcha system kdun ghyaychay for now let it be
        $("#suggestedSymps").append(strstsr);

    }

    

}

function qa(){
    document.getElementById("normal").style.display="none";
    document.getElementById("qa").style.display="block";
    $.ajax({
        type : 'POST',
        url : "suggest",
        data:{
          "symptoms": symps.toString(),
          csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success : function(data){
          var sugesstions=data.split(",");
          alert(sugesstions);
          if(sugesstions[0]=='ans'){
              alert("Result : "+sugesstions[1]);
              //this is diagnosis result by decision tree
              document.getElementById("question").innerHTML="Tula "+sugesstions[1]+" ahe bhava";
          }
          else{
            document.getElementById("question").innerHTML="Are you experincing "+sugesstions[0]+"?";
            $('#yes').attr('value', sugesstions[0]);
            $('#no').attr('value', sugesstions[0]);
          }
        }
      });
}
function normal(){
    document.getElementById("normal").style.display="block";
    document.getElementById("qa").style.display="none";

}
document.getElementById("profile-tab").addEventListener("click", qa)
document.getElementById("home-tab").addEventListener("click", normal)

function getsuggestions(){
    alert(symps.toString());
    $.ajax({
        type : 'POST',
        url : "suggest",
        data:{
          "symptoms": symps.toString(),
          csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success : function(data){
          var sugesstions=data.split(",");
          alert(sugesstions);
          if(sugesstions[0]=='ans'){
            alert("Result : "+sugesstions[1]);
            //this is diagnosis result by decision tree
            suggestSymptoms([sugesstions[1]]);
        }
        else
          suggestSymptoms(sugesstions);
        }
      });

}