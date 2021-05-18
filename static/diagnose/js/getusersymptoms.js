var symps = new Array();
function delThis(num) {

    var index = symps.indexOf(num);
    if (index > -1) {
        symps.splice(index, 2);
        $("#" + num).remove();
    }
}

// function addThis(x) {


//     var node = document.getElementById("suggestedSymps");
//     node.querySelectorAll('*').forEach(n => n.remove());



//     symps.push(x);
//     symps.push('1');
//     document.getElementById("myInput").value = '';
//     var strstsr = '<button id=' + x + " style='color:green;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

//     $("#AddSympsHere").append(strstsr);
//     getsuggestions();

// }

function addUserSymps(dir=2,color="green") {
  alert(symps);
    var x = document.getElementById("myInput").value;
    symps.push(x);
    if(color=="green")
      symps.push('1');
    else
      symps.push('0');
    document.getElementById("myInput").value = '';
    let strstsr = `<button type="button" id=` + x + ` style=" color: `+ color+ `;" class="btn alert alert-success" data-dismiss="alert" onclick=delThis('` + x + `') aria-label="Close">
    <span>`+ x + `</span>
      </button>`
    $("#AddSympsHere").append(strstsr);
    getsuggestions(dir);
}


document.getElementById("adduserSympButton").addEventListener("click", addUserSymps);
function addyes(){
    var x=document.getElementById("yes").value;
    addSuggestedSymp(x,1,"green");
    // symps.push(x);
    // symps.push('1');
    // document.getElementById("myInput").value = '';
    // var strstsr = '<button id=' + x + " style='color:green;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    // $("#AddSympsHere").append(strstsr);
    // qa();
}
function addno(){
    var x=document.getElementById("no").value;
    addSuggestedSymp(x,1,"red");
    // symps.push(x);
    // symps.push('0');
    // document.getElementById("myInput").value = '';
    // var strstsr = '<button id=' + x + " style='color:red;' class='btn btn-outline-secondary text-center m-1' onclick=delThis('" + x + "')>" + x + "</button>";

    // $("#AddSympsHere").append(strstsr);
    // qa();
}


function suggestSymptoms(a) {


  $("#suggesionss").empty();
    
  //ithe fkt max 5 suggestions thev not more than that

  let strstsr = `<div class="sugestionsclass"> 
  Here are some <br> suggestions for you!<br>
                  </div>
                  `

  $("#suggesionss").append(strstsr);

    //hyat to array access krun yash chya decision tree la dyayachay
    // var node = document.getElementById("suggestedSymps");
    // node.querySelectorAll('*').forEach(n => n.remove());

    // var st= '<button class="btn text-center m-1" style="border:none; background-color:#f8f9fa;">Suggested:</p>';
    // $("#suggestedSymps").append(st);

    alert(a);
    if(a[0]=="nosymp"){
      // var st= '<button class="btn text-center m-1" style="border:none; background-color:#f8f9fa;">None</p>';
      // $("#suggestedSymps").append(st);
      var x=`<button type="button" class="btn alert alert-success" data-dismiss="alert"  aria-label="Close" disabled>
                      <span> None </span> 
                  </button> <br>`;
      $('.sugestionsclass').append(x);
    }
    else{
      for(var i=0;i<a.length;i++){
          // var strstsr = '<button id=' + a[i] + " class='btn btn-outline-secondary text-center m-1' onclick=addThis('" + a[i] + "')>" + a[i] + "</button>";
          // //he vrcha system kdun ghyaychay for now let it be
          // $("#suggestedSymps").append(strstsr);

          var x=` <button type="button" class="btn alert alert-success" data-dismiss="alert" onclick=addSuggestedSymp('`+ a[i] + `') aria-label="Close">
                    <span>`+ a[i] + `</span> 
                  </button> <br>`;
      $('.sugestionsclass').append(x);

      }
    }
}

function addSuggestedSymp(x, dir=2,color="green") {
  $("#suggesionss").empty();
  document.getElementById("myInput").value = x;
  addUserSymps(dir,color);
}

// function qa(){
//   alert("asach");
//     document.getElementById("normal").style.display="none";
//     document.getElementById("qa").style.display="block";
//     $.ajax({
//         type : 'POST',
//         url : "suggest",
//         data:{
//           "symptoms": symps.toString(),
//           csrfmiddlewaretoken: '{{ csrf_token }}',
//         },
//         success : function(data){
//           data=JSON.parse(data);
//           if(symps.toString()!=data["before"].toString()){
//             alert("skip");
//           }
//           else{
//             var sugesstions=data["after"];
//             alert(sugesstions);
//             if(sugesstions[0]=='nosymp'){
//                 // alert("Result : "+sugesstions[1]);
//                 //this is diagnosis result by decision tree
//                 document.getElementById("question").innerHTML="Done with suggestions!!";
//             }
//             else{
//               document.getElementById("question").innerHTML="Are you experincing "+sugesstions[0]+"?";
//               $('#yes').attr('value', sugesstions[0]);
//               $('#no').attr('value', sugesstions[0]);
//             }
//           }
//         }
//       });
// }
// function normal(){
//   alert('in');
//     document.getElementById("normal").style.display="block";
//     document.getElementById("qa").style.display="none";
//     getsuggestions();

// }
// document.getElementById("profile-tab").addEventListener("click", qa)
// document.getElementById("home-tab").addEventListener("click", normal)

function getsuggestions(num){
  // alert(symps);
  // alert(num);
    $.ajax({
        type : 'POST',
        url : "suggest",
        data:{
          "symptoms": symps.toString(),
          csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success : function(data){
          // alert(data);
          data=JSON.parse(data);
          // alert(data);
          // alert(symps.toString());
          // alert(data["after"]);
          // alert(data["before"].toString());
          if(symps.toString()!=data["before"].toString()){
            alert("skip");
          }
          else{
            sugesstions=data["after"];
            // alert(sugesstions);
            if(num==1){
              if(sugesstions[0]=='nosymp'){
                document.getElementById("question").innerHTML="Done with suggestions!!";
                $("#yes").prop('disabled', true);
                $("#yes").prop('disabled', true);
              }
              else{
                document.getElementById("question").innerHTML="Are you experincing "+sugesstions[0]+"?";
                $('#yes').attr('value', sugesstions[0]);
                $('#no').attr('value', sugesstions[0]);
                $("#yes").prop('disabled', false);
                $("#yes").prop('disabled', false);
              }
            }
            else{
              sugesstions=data["after"];
              // alert(sugesstions);
              suggestSymptoms(sugesstions);
            }
          }
        }
      });

}

function changeContent(num) {
  // alert(num);
  if (num == 1) {
      //ithe ulti chya thikani symptom taak
      $("#inputsearchbar").hide();
      $("#quesanswers").show();

      
      $('#changeContentButt').html('Enter Sypmtoms');
      $("#changeContentButt").attr("onclick", "changeContent(2)");

      let strstr = `
      <h5 class="pt-3">&nbsp;&nbsp;&nbsp;&nbsp;Not sure what's &nbsp;&nbsp;&nbsp;&nbsp;happening?</h5>
      <img class="logoimage" src="../../static/diagnose/image/dTree.png">
      <h6 class="text-center">We'll suggest you something using our decision tree..<br>
          &nbsp;&nbsp;&nbsp;Add any one symptom to get started!</h6>
      `;
      $("#suggesionss").empty();
      $("#suggesionss").append(strstr);
  }
  else {

      $("#quesanswers").hide();
      $("#inputsearchbar").show();

      $('#changeContentButt').html('Prefer Questions?');
      $("#changeContentButt").attr("onclick", "changeContent(1)");
  }
  getsuggestions(num);
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