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
    var strstsr = '<button id=' + x + " style='color:green;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    getsuggestions();

}

function addUserSymps() {
    var x = document.getElementById("myInput").value;
    symps.push(x);
    symps.push('1');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " style='color:green;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    getsuggestions();
}


document.getElementById("adduserSympButton").addEventListener("click", addUserSymps);
function addyes(){
    var x=document.getElementById("yes").value;
    symps.push(x);
    symps.push('1');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " style='color:green;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    qa();
}
function addno(){
    var x=document.getElementById("no").value;
    symps.push(x);
    symps.push('0');
    document.getElementById("myInput").value = '';
    var strstsr = '<button id=' + x + " style='color:red;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    $("#AddSympsHere").append(strstsr);
    qa();
}


function suggestSymptoms(a) {
    //hyat to array access krun yash chya decision tree la dyayachay
    var node = document.getElementById("suggestedSymps");
    node.querySelectorAll('*').forEach(n => n.remove());
    var st= '<button class="btn text-center m-1" style="border:none; background-color:#f8f9fa;">Suggested:</p>';
    $("#suggestedSymps").append(st);
    alert(a);
    if(a[0]=="nosymp"){
      var st= '<button class="btn text-center m-1" style="border:none; background-color:#f8f9fa;">None</p>';
      $("#suggestedSymps").append(st);
    }
    else{
      for(var i=0;i<a.length;i++){
          var strstsr = '<button id=' + a[i] + " class='btn btn-outline-secondary text-center m-1' onclick=addThis('" + a[i] + "')>" + a[i] + "</button>";
          //he vrcha system kdun ghyaychay for now let it be
          $("#suggestedSymps").append(strstsr);

      }
    }

    

}

function qa(){
  alert("asach");
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
          data=JSON.parse(data);
          if(symps.toString()!=data["before"].toString()){
            alert("skip");
          }
          else{
            var sugesstions=data["after"];
            alert(sugesstions);
            if(sugesstions[0]=='nosymp'){
                // alert("Result : "+sugesstions[1]);
                //this is diagnosis result by decision tree
                document.getElementById("question").innerHTML="Done with suggestions!!";
            }
            else{
              document.getElementById("question").innerHTML="Are you experincing "+sugesstions[0]+"?";
              $('#yes').attr('value', sugesstions[0]);
              $('#no').attr('value', sugesstions[0]);
            }
          }
        }
      });
}
function normal(){
  alert('in');
    document.getElementById("normal").style.display="block";
    document.getElementById("qa").style.display="none";
    getsuggestions();

}
// document.getElementById("profile-tab").addEventListener("click", qa)
// document.getElementById("home-tab").addEventListener("click", normal)

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
          data=JSON.parse(data);
          if(symps.toString()!=data["before"].toString()){
            alert("skip");
          }
          else{
            sugesstions=data["after"];
            suggestSymptoms(sugesstions);
          }
        }
      });

}

function diagnoseit(){
  if(symps.length==0){
    alert("Enter atleast one symptom");
  }
  else{
    var final='';
    for(var i=0;i<symps.length;i++){
      final+=symps[i]+',';
    }
    
    final=final.slice(0,-1);
    alert(final);
    $("#symptoms").val(final);
    alert($("#symptoms").val());
    $("#digform").submit();

  }
}