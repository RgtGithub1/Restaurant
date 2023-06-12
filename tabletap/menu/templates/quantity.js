
// Retrieve the quantity input element
const quantityInput = document.querySelector('.quantity-input');

// Retrieve the plus and minus buttons
const plusBtn = document.querySelector('.plus-btn');
const minusBtn = document.querySelector('.minus-btn');

// Add event listener to the plus button
plusBtn.addEventListener('click', function () {
    quantityInput.value = parseInt(quantityInput.value) + 1;
});

// Add event listener to the minus button
minusBtn.addEventListener('click', function () {
    const currentValue = parseInt(quantityInput.value);
    if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
});