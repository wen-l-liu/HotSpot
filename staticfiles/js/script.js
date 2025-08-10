const popoverTrigger = document.getElementById('cart-popover');
const popoverContent = document.getElementById('cart-popover-content').innerHTML;

const popover = new bootstrap.Popover(popoverTrigger, {
    html: true,
    content: popoverContent,
    placement: 'bottom'
});

document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var alert = document.getElementById("msg");
        if (alert) {
            var bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }
    }, 4000); // 5000 milliseconds = 5 seconds
});

