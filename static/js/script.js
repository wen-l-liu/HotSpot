const popoverTrigger = document.getElementById('cart-popover');
const popoverContent = document.getElementById('cart-popover-content').innerHTML;

const popover = new bootstrap.Popover(popoverTrigger, {
    html: true,
    content: popoverContent,
    placement: 'bottom'
});



