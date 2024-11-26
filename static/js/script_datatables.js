let dataTable;

let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        {orderable: false, targets: [5, 6]},
        {searchable: false, targets: [5, 6]}
    ],
    pageLength: 2,
    destroy: true,
}

dataTable = $("#table_posts").DataTable(dataTableOptions)

