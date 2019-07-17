$(function() {

    "use strict";

    /* --- VARIABLES --- */
    var inputType = "local";
    var rowCount = 0, errorCount = 0, firstError;
    var errorParsing = false;
    
    var header = [
    	"COUNTRY", "UNIQUE SPEC ID", "DE I DENTIFIED PARTICIPANT ID", "STUDY",
    	"NO OF ALIQUOTES", "SPECIMEN TYPE", "DATE OF COLLECTION", "SOURCE SPECIMEN"
    ];
    var notNullColumns = [ "UNIQUE SPEC ID", "DE I DENTIFIED PARTICIPANT ID", "STUDY", "SPECIMEN TYPE" ];
    /* Case for archive data */
    if ($('#parse-csv').hasClass('ROLE_ARCHIVE')) {
    	archiveColumns();
    }
    $("#file-type").change(function() {
    	archiveColumns();
    });
    /* --- MY FUNCTIONS --- */
    
    function archiveColumns () {
    	var fileType = $("#file-type option:selected").val();
    	switch(fileType) {
			case "study":
				header = ["ACRONYM", "TITLE", "STUDY DESIGN", "DESCRIPTION", "TOTAL SPECIMENS", "NO OF CASES",
                          "NO OF CONTROLS", "DESCRIPTION DATASET"];
				notNullColumns = ["ACRONYM", "TITLE"];
				break;
			case "individual":
				header = ["ACRONYM", "UNIQUE SPEC ID", "PARTICIPANT ID", "DATE OF COLLECTION", "AGE", "GENDER",
                          "ETHNICITY", "HEIGHT", "HEIGHT UNIT", "WEIGHT", "BMI", "DISEASE STATUS",
                          "HIV STATUS", "CASE CONTROL"];
				notNullColumns = ["ACRONYM", "UNIQUE SPEC ID", "PARTICIPANT ID"];
				break;
			default:
				break;
		}
    }
    
    function getFileSelected () {
        return $("#file").prop('files')[0];
    }

    function columnFromMultiArray (index, csvArray) {
        var output = [];
        $.map(csvArray, function (arrayVect) {
            output.push(arrayVect[index]);
        });
        return output;
    }

    function appendToTextarea(msg, error) {
        var resultArea = $('#result-parse');
        if (error)
            resultArea.append( '<span style="font-weight: bold; color: red;">' + msg + '</span><br>');
        else
            resultArea.append( '<span style="font-weight: bold;">' + msg + '</span><br>');
    }

    function checkHeader (data) {
        var h = data[0];
        var errHeader = [];

        $.each(header, function (i, v) {
            if ($.inArray(v, h) === -1)
                errHeader.push(v);
        });

        return errHeader;
    }

    function checkColumns(data) {
        $.each(notNullColumns, function (i, v) {
            var index = data[0].indexOf(v);
            var arrayIndex = columnFromMultiArray(index, data);
            if ($.inArray(undefined, arrayIndex) !== -1 ||
                $.inArray("", arrayIndex) !== -1) {
                errorParsing = true;
                var msgCol = "Column " + v + " contains undefined values!";
                appendToTextarea(msgCol, true);
            }else {
                errorParsing = false;
                var msgCol = "Column '" + v + "': <span style=\"color:green;\">OK.</span>";
                appendToTextarea(msgCol, false);
            }
        });
    }

    function otherCheck(data) {
        var errHeader = checkHeader(data);
        if (errHeader.length === 0) {
            errorParsing = false;
            var msgHeader = 'Header columns present: <span style="color:green;">OK.</span>';
            appendToTextarea(msgHeader, false);
            checkColumns(data);
        } else {
            errorParsing = true;
            var msgHeader = 'Columns: ' + errHeader + ' are not present!';
            appendToTextarea(msgHeader, true);
            return;
        }
    }

    function uploadCSV() {
        var fileSelected = getFileSelected();
        var fileName = "<span style='font-weight: bold;'>" + fileSelected.name + "</span>";
        var fileInfo = "File: " + fileName;
        $("#file-selected").html(fileInfo);
        $("#file").clone().appendTo("#file-elem");
        // set the selected file type option to the hidden input
        var typeFile = $("#file-type").val();
        $("#type-file-selected").val(typeFile);
    }

    /* --- PAPA PARSE FUNCTIONS --- */

    function enableButton() {
        $('#parse-csv').prop('disabled', false);
    }

    function printStats(msg) {
        if (msg)
            console.log(msg);
        console.log("  Row count:", rowCount);
        console.log("     Errors:", errorCount);
        if (errorCount)
            console.log("First error:", firstError);
    }

    function completeFn(results) {

        if (results && results.errors) {
            if (results.errors.length !== 0) {
                errorCount = results.errors.length;
                firstError = results.errors[0];
            }
            if (results.data && results.data.length > 0) {
                rowCount = results.data.length;
                otherCheck(results.data)
            }
        }
    }

    function errorFn(err, file) {
        console.log("ERROR:", err, file);
        enableButton();
    }

    function buildConfig() {
        return {
            delimiter: $('#delimiter').val(),
            header: false,
            dynamicTyping: false,
            skipEmptyLines: true,
            preview: parseInt(0),
            step: undefined,
            encoding: $('#encoding').val(),
            worker: true,
            comments: $('#comments').val(),
            complete: completeFn,
            error: errorFn,
            download: inputType == "remote"
        };
    }

    $('#parse-csv').click(function () {

        var fileElem = $('#file');
        if (!fileElem[0].files.length) {
            alert("Please choose your CSV file to parse");
            return enableButton();
        }

        var config = buildConfig();
        var msgStart = "---------------------------------";
        appendToTextarea(msgStart, false);

        fileElem.parse({
            config: config,
            before: function (file, inputElem) {
                var msgFile = "Parsing file " + file.name + ", " +
                        "last modified date " + file.lastModifiedDate;
                appendToTextarea(msgFile, false);
            },
            error: function (err, file) {
                console.log("ERROR:", err, file);
                firstError = firstError || err;
                errorCount++;
            },
            complete: function () {
                if (!errorParsing) {
                    $("ul.tabs > li:nth-child(2)").removeClass("disabled");
                    // uncomment if automatically move to the second tab
                    /*$('ul.tabs').tabs();
                    $('ul.tabs').tabs('select_tab', 'upload-csv');*/
                    uploadCSV();
                }
            }
        })
    });

});
