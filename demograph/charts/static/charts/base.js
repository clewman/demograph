// alert('working')

// hamburger menu
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
});

// navbar hamburger
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
});

// materialize dd
$(".dropdown-trigger").dropdown({hover: true, alignment: 'right', constrainWidth: false});

// checkboxes
$(document).ready(function () {
    $('select').formSelect({constrainWidth: false});
});

