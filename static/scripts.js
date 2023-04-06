function showValidationMessage(message) {
	const messageContainer = document.getElementById(
		"validation-message-container"
	);
	messageContainer.innerHTML = `<p class="error">${message}</p>`;
}

const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
	const radioButtons = Array.from(form.querySelectorAll('input[type="radio"]'));
	const selected = radioButtons.some((radioButton) => radioButton.checked);

	if (!selected) {
		event.preventDefault();
		showValidationMessage("Please select an option before proceeding.");
	}
});
