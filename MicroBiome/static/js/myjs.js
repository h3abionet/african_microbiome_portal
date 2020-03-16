$(function() {

    "use strict";

    $('.modal').modal();
    $('#responsiveTabsDemo').responsiveTabs({
        startCollapsed: 'accordion',
        collapsible: false,
        animation: 'slide'

    });
    /* Materialize css checkbox incompatibility with Thymeleaf */
    $('input[name="_phenoDataRequested"]').remove();
    $('input[name="_hasSpecimens"]').remove();
    $('input[name="_hasDataSets"]').remove();


    $('#table-studies').DataTable( {
        columnDefs: [
            {
                targets: [ 0, 1, 2 ],
                className: 'mdl-data-table__cell--non-numeric'
            }
        ],
    	"bLengthChange": false
    } );
    
    $('#query-specimens').DataTable( {
        columnDefs:[
        	{"type": "num"}
        ],
        'ordering': false,
        'info': false,
    	"bLengthChange": false
    } );
    
    $("div.alert-card .close").click(function(){
        $(this).closest("div.alert-card").fadeOut("slow")
    });

    $("button[id^='process-csv']").click(function () {
        $("input[name='delete']").remove();
    });

    $("button[id^='delete-csv']").click(function () {
        $("input[name='process']").remove();
    });
    
    // Column chart
    $("div.summary-charts > a").click(function() {
    	var id = $(this).attr('id');
    	var containerId = $(this).closest("div").next().attr('id');
    	$('#' + containerId).fadeToggle("fast", function() {
    		if($('#' + containerId).is(':visible')) {
    			columnChart(id, containerId);
    		}else {
    			$('#' + containerId).empty();
    		}
    	});
    });
    
    function columnChart(id, containerId) {
    	$.get("/api/study/" + id, function (data) {
    		if (!data ) return;
    		var countries = [];
    		var series = [];
    		$.each(data, function(k, v){
    			countries.push(k);
    			series.push(v);
    		});
    		Highcharts.chart(containerId, {
    			chart: {
    		        type: 'column'
    		    },
    		    title: {
    		        text: 'Samples by countries'
    		    },
    		    xAxis: {
    		        categories: countries,
    		        title: {
    		            text: null
    		        }
    		    },
    		    yAxis: {
    		        min: 0,
    		        title: {
    		            text: 'Number of samples'
    		        }
    		    },
    		    legend: {
    		        shadow:false
    		    },
    		    tooltip: {
    		        shared: true
    		    },
    		    plotOptions: {
                    column: {
                        grouping: false,
                        shadow: false,
                        borderWidth: 0
                    }
                },
    		    series: [{
    		    	name : 'Number samples by country',
    		    	color: '#1E6FA8',
    		    	data: series,
    		    	pointPadding: 0.3,
                    pointPlacement: 0
    		    }]
    		});
    	});
    }

    // click on show more advanced search
    $('span.show-more').on('click', function() {
        $('div.advanced-search').toggleClass("hide");
        var hasClass = $('div.advanced-search').hasClass("hide");
        var showMore = '<a class="btn-floating btn waves-effect waves-light blue">' +
                       '<i class="material-icons">keyboard_arrow_down</i></a> SHOW MORE';
        var showLess = '<a class="btn-floating btn waves-effect waves-light blue">' +
                       '<i class="material-icons">keyboard_arrow_up</i></a> SHOW LESS';
        $('span.show-more').html(
            hasClass ? showMore : showLess);
    });

    // Cart shopping
    $("a[id^='addtocart']").click(function () {
        var idArray = $(this).attr('id').split('-');
        var acronym = idArray[1];
        if ($(this).hasClass("remove")){
            $('#span-' + acronym).remove();
            $(this).removeClass("remove");
            $(this).html('<i class="material-icons right">shopping_cart</i>Add');
            if ($('#selected_studies').children().length == 1) {
                $('#cart-opts').hide();
            }
        } else {
            $('#selected_studies').append(
                '<span class="selected_study_box" id="span-'+acronym +'">' +
                '<input type="text" name="'+acronym+'" value="'+acronym+'" hidden/> ' + acronym +
                '<a href="#">' +
                '<i class="material-icons tiny right cart-delete red" ' +
                   'id="i-'+acronym+'" style="color: #FFFFFF;">close</i>' +
                '</a></span>'
            );
            $(this).addClass("remove");
            $(this).html('<i class="material-icons right">remove_shopping_cart</i>Remove');
            $('#cart-opts').show();
        }
    });

    $('#selected_studies').on('click', 'i.cart-delete', function () {
        var acronym = $(this).attr('id').split('-')[1];
        $('#span-' + acronym).remove();
        var projectCard = $('#addtocart-' + acronym);
        projectCard.removeClass("remove");
        projectCard.html('<i class="material-icons right">shopping_cart</i>Add');
        if ($('#selected_studies').children().length == 1) {
            $('#cart-opts').hide();
        }
    });

    // Download user cart
    var searchQuery = {
        'description': '', 'studyName': '', 'design': '',
        'country': '', 'gender': '', 'specType': '', 'character': '',
        'ethnicity': '', 'ageOp': '', 'bmiOp': '', 'disease': '',
        'hasSpecimens': false, 'hasDatasets': false
    };

    $.fn.convertToCSV = function (args) {

        var result, ctr, keys, columnDelimiter, lineDelimiter, data;
        data = args.data || null;
        if (data == null) {
            return null;
        }

        columnDelimiter = args.columnDelimiter || ',';
        lineDelimiter = args.lineDelimiter || '\n';

        keys = Object.keys(data);
        result = '';
        result += keys.join(columnDelimiter);
        result += lineDelimiter;
        ctr = 0;
        keys.forEach(function (key) {
            if (ctr > 0) result += columnDelimiter;
            result += data[key];
            ctr++;
        });
        result += lineDelimiter;
        return result;
    };

    $.fn.downloadCSV = function () {
        var data, link;
        var filename = 'export.csv';
        var csv = $(this).convertToCSV({
            data: searchQuery
        });
        if (csv == null) return;
        if (!csv.match(/^data:text\/csv/i)) {
            csv = 'data:text/csv;charset=utf-8,' + csv;
        }
        data = encodeURI(csv);
        link = document.createElement('a');
        link.setAttribute('href', data);
        link.setAttribute('download', filename);
        link.click();
    };

    $('#download-cart').on("click", function (e) {
        e.preventDefault();
        searchQuery['description'] = $('#description').val();
        searchQuery['studyName'] = $('#study-name').val();
        searchQuery['design'] = $('#study-design').val();
        searchQuery['disease'] = $('#disease').val();
        searchQuery['hasSpecimens'] = $('#has-specimens').is(':checked');
        searchQuery['hasDatasets'] = $('#has-datasets').is(':checked');
        searchQuery['country'] = $('#specimen-country').val();
        searchQuery['gender'] = $('#participant-sex').val();
        searchQuery['specType'] = $('#specimen-type').val();
        searchQuery['character'] = $('#participant-character').val();
        searchQuery['ethnicity'] = $('#participant-ethnicity').val();
        var ageOp = $('#age-operator').val();
        var ageVal = $('#age-value').val();
        if ( ageOp && ageVal) {
            searchQuery['ageOp'] = ageOp + ' ' + ageVal;
        }
        var bmiOp = $('#bmi-operator').val();
        var bmiVal = $('#bmi-value').val();
        if (bmiOp && bmiVal) {
            searchQuery['bmiOp'] = bmiOp + ' ' + bmiVal;
        }
        $(this).downloadCSV();
    });

    $('#submit_advance').on("click", function (e) {
        $('#description_hidden').val($('#description').val());
    });

});