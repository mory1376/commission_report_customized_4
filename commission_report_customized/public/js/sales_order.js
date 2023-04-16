frappe.ui.form.on("Sales Order", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            hide_sales_team_section(frm);
        }
    }
});

function hide_sales_team_section(frm) {
    frm.toggle_display("sales_team", false);
}