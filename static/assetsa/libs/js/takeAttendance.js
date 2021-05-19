var current = "";
var curlen = 0;
var marked = new Array();
var lecDate, lecSubject, lecClass, lecTopic;
lecDetails = function(){

    lecDate = $('#lecForm input[name=date]').val();
    lecSubject = $('#subjectOpt').val();
    lecClass = $('#classOpt').val();
    lecTopic = $('#lecForm input[name=topic]').val();
    
    // alert("Hello!");
    console.log(lecDate);
    console.log(lecSubject);
    console.log(lecClass);
    console.log(lecTopic);
    
    $('#disDate').text(lecDate);
    $('#disSubject').text(lecSubject);
    $('#disClass').text(lecClass);
    $('#disTopic').text(lecTopic);

    $('#lecDetails').hide();
    $('#attendanceThings').show();

}

hideOther = function(){
  $('#attendanceThings').hide();

}

$("#b1").click( function() { 
    current = current.concat("1");
    $("#calscreen").val(current);    
  });
  $("#b2").click( function() { 
    current = current.concat("2");
    $("#calscreen").val(current);    
  });
  $("#b3").click( function() { 
    current = current.concat("3");
    $("#calscreen").val(current);    
  });
  $("#b4").click( function() { 
    current = current.concat("4");
    $("#calscreen").val(current);    
  });
  $("#b5").click( function() { 
    current = current.concat("5");
    $("#calscreen").val(current);    
  });
  $("#b6").click( function() { 
    current = current.concat("6");
    $("#calscreen").val(current);    
  });
  $("#b7").click( function() { 
    current = current.concat("7");
    $("#calscreen").val(current);    
  });$("#b8").click( function() { 
    current = current.concat("8");
    $("#calscreen").val(current);    
  });$("#b9").click( function() { 
    current = current.concat("9");
    $("#calscreen").val(current);    
  });$("#b0").click( function() { 
    current = current.concat("0");
    $("#calscreen").val(current);    
  });

  $("#bac").click( function() { 
    current = "";
    $("#calscreen").val("0");    
  });
  
  $("#bdel").click( function() { 
    if((curlen = current.length) <= 1)
        $("#calscreen").val("0");    
    else  
    {
      current = current.substring(0,curlen - 1);
      $("#calscreen").val(current);
    }    
  });

  // onclick=delthis(current)

  $("#bpres").click( function() { 
    $("#calscreen").val("0");
    if(current != "" && !marked.includes(current)){
          marked.push(current);
          var strstr =  '<button id='+current+' onclick=delThis('+current+")>"+current+"</button>";
          $("#markedAttend").append(strstr);                
    }
    current = "";
  });

 $(document).on('keypress',function(e) {
  var code = e.which;
  if(code == 13) {
    $("#bpres").click();
  }
  else if(code ==8 || code ==46) {
    $("#bdel").click();
  }
  else{
    code -= 48;
    var strstr = "#b"+code.toString();
    $(strstr).click();
  }
  });

  function delThis(num){
    var index = marked.indexOf(num.toString());
    if (index > -1) {
       marked.splice(index, 1);
       $("#"+num).remove();
    }
  }          

  submitThis = function(){
      $.ajax({
        type : "POST",
        url : "markme",
        data:{
          marked : JSON.stringify(marked),
          date : lecDate,
          subject : lecSubject,
          Class : lecClass,
          topic : lecTopic,
          count : marked.length,
          csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success : function(data){
          alert("Success!");
        }
      });
  }

  $(window).on('beforeunload', function(){
      return false;
  }); 