function calculateSavings(slider,cost){
    var saved = document.getElementById('saved');
    var slideval = document.getElementById('slideval');
    var cost = document.getElementById(cost).value;
    var calc = ((cost / 100)*slider) - 645;
    var savedvalue = (calc);
    if (savedvalue < 0)
    {
      saved.innerHTML = 0;
    }
    else {
      saved.innerHTML = (calc).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
    slideval.innerHTML = slider;
}

function update(costval, slider, cost){
  var display = document.getElementById("costval");
  display.innerHTML =  costval.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  calculateSavings(slider,cost);
}