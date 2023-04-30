
var input2;
var input1;
var input3;
var input4;
var input5;
var input6;
var input7; 
var input8;


function submit() {
	// Get input values
	 input1 = document.getElementById("input1").value;
	 input2 = document.getElementById("input2").value;
	 input3 = document.getElementById("input3").value;
	 input4 = document.getElementById("input4").value;
	 input5 = document.getElementById("input5").value;
	 input6 = document.getElementById("input6").value;
	 input7 = document.getElementById("input7").value;
     input8 = document.getElementById("input8").value;

}

$(document).ready(function() {
    // Load the model using Pickle.js
    $.ajax({
      url: "RandomForestModel.pkl",
      async: true,
      success: function (modelData) {
        const model = pkl.load(modelData);
        console.log(model);
        // Use the model for prediction
        // ...
        // Define the input data for prediction
        const input = [input1, input2, input3, input4,input5,input6,input7,input8];

        // Make a prediction using the loaded model
        const prediction = model.predict([input]);
        
            
            console.log(prediction);

            document.getElementById('output').innerHTML = prediction?"Diabetes":"No Diabetes";

      }
    });
  });

  