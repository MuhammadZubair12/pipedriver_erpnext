// Copyright (c) 2023, zubair and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pipedrive Integration', {
	// refresh: function(frm) {

	// },
	validate: function (frm) {
		// var token = "cdbbce1baa80c959ecc0386a7ff6c98bd73bf090"
		if (frm.doc.api_token) {
			var tok = frm.doc.api_token
			
			fetch(`https://api.pipedrive.com/v1/users/me?api_token=${tok}`, {
				
			})
				.then(r => r.json())
				.then(r => {
					if(r.success == true){
						var value = "ok"
						frappe.call({
							method:"pipedrive_erpnext.pipedrive_erpnext.doctype.pipedrive_integration.pipedrive_integration.create_connect",
							args: {
								name:value
								
							},
							callback:function(r){
								// console.log("Message", r)
							}
						  })
					} else {
						var new_value = "false"
						frappe.call({
							method:"pipedrive_erpnext.pipedrive_erpnext.doctype.pipedrive_integration.pipedrive_integration.create_connect",
							args: {
								name:new_value
								
							},
							callback:function(r){
								// console.log("Message", r)
							}
						  })
						console.log("False");
					}
					
				})
		}else {}

	},
	check: function(frm) {
		frappe.call({
			method:"pipedrive_erpnext.pipedrive_erpnext.doctype.pipedrive_integration.pipedrive_integration.test_pipedrive_token",
			callback:function(r){
				console.log("Message", r)
			}
		  })
	}

});
