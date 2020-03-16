/*
    * LOVELY THINGS
    */

var options = {
  valueNames: [ 'name', 'description', 'category' ],
	page: 4,
	pagination: true
};

var featureList = new List('lovely-things-list', options);

$('#filter-games').click(function() {
  featureList.filter(function(item) {
    if (item.values().category == "Game") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-beverages').click(function() {
  featureList.filter(function(item) {
    if (item.values().category == "Beverage") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});
$('#filter-none').click(function() {
  featureList.filter();
  return false;
});
