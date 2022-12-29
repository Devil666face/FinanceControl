$(document).ready(function(){
	var date_input=$('input[name="date_month"]'); //our date input has the name "date"
	var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
	var options={
		showButtonPanel: true,
    startView: "months", 
    minViewMode: "months",
    format: 'yyyy-mm',
    container: container,
    todayHighlight: true,
    autoclose: true,
    onClose: function(dateText, inst) { 
        $(this).datepicker('setDate', new Date(inst.selectedYear, inst.selectedMonth, 1));
    }
  };
  date_input.datepicker(options);
})
